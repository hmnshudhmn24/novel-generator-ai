import gradio as gr, os, tempfile
from src.datasets.ingest import load_corpus
from src.generators.markov import MarkovWriter
from src.generators.grammar import Grammar
from src.generators.constraint_256 import micro_novel
from src.mixins.editing import lipogram, acrostic_chapters, sprinkle_alliteration

DEFAULT_GRAMMAR = {
    "origin": "#opening#\n\n#chapter#\n\n#chapter#\n\n#ending#",
    "opening": [
        "Once upon a sluggish socket, a story negotiated with silence.",
        "At midnight, the server farm yawned; somewhere a cursor blinked like a lighthouse."
    ],
    "chapter": [
        "#scene# #beat# #scene# #beat#",
        "#scene# #scene# #twist#",
    ],
    "scene": [
        "The #hero# drifted across #place#.",
        "A #thing# learned a new verb in #place#.",
    ],
    "beat": [
        "Footnotes multiplied like rabbits.",
        "A rumor took the elevator and pressed 'infinite'."
    ],
    "hero": ["pilgrim", "synthetic poet", "astronaut", "archivist", "errant API"],
    "thing": ["clock", "mirror", "drone", "network", "promise"],
    "place": ["a neon field", "the quiet RAM", "a hallway of keys", "the wet city"],
    "twist": ["Then the sun compiled.", "The river undid its encryption."],
    "ending": [
        "Morning arrived wearing yesterday's rain. The page refused to end.",
        "Finally, the book closed itself, softly, like a tab you meant to keep."
    ]
}

def run_gen(files, mode, words, chapters, order, lip, acro, allit):
    corpus = ""
    if files and len(files):
        # Gradio gives temp file paths
        paths = ",".join(f.name for f in files)
        corpus = load_corpus(paths)

    if mode == "markov":
        m = MarkovWriter(order=order)
        m.fit(corpus or "The seed is a whisper across a keyboard.")
        txt = m.generate_text(words)
    elif mode == "grammar":
        g = Grammar(DEFAULT_GRAMMAR)
        txt = "\n\n".join(g.expand() for _ in range(chapters))
    elif mode == "mashup":
        if not corpus.strip():
            corpus = "A seed is enough if the wind cooperates."
        m = MarkovWriter(order=2)
        m.fit(corpus)
        a = m.generate_text(max(1, words//2))
        b = micro_novel(corpus, words=max(1, words - words//2))
        txt = a + "\n\n" + b
    else:
        txt = micro_novel(corpus if corpus else "A seed of wind", words=words)

    if lip:
        txt = lipogram(txt, lip)
    if allit:
        txt = sprinkle_alliteration(txt, letter=allit, chance=0.06)
    if acro:
        txt = acrostic_chapters(txt, acro)

    return txt

with gr.Blocks(title="AI-Driven Novel Generator") as demo:
    gr.Markdown("# 📚 AI-Driven Novel Generator (NaNoGenMo style)\nUpload some text, pick a mode, sprinkle constraints, and conjure a novel ✨")
    with gr.Row():
        files = gr.Files(label="Upload corpus files (.txt/.md/.jsonl)", file_count="multiple", type="file")
    with gr.Row():
        mode = gr.Radio(["markov","grammar","mashup","micro"], value="markov", label="Mode")
        words = gr.Slider(100, 50000, 2000, step=100, label="Target words (for markov/mashup/micro)")
        chapters = gr.Slider(1, 50, 12, step=1, label="Chapters (grammar mode)")
        order = gr.Slider(1, 4, 2, step=1, label="Markov order")
    with gr.Row():
        lip = gr.Textbox(label="Lipogram ban letter (e.g., e)", value="")
        acro = gr.Textbox(label="Acrostic (chapter initials, e.g., NANOGENMO)", value="")
        allit = gr.Textbox(label="Alliteration focus letter (optional)", value="")
    btn = gr.Button("🖋️ Generate")
    out = gr.Textbox(label="Novel", lines=28)

    btn.click(run_gen, inputs=[files, mode, words, chapters, order, lip, acro, allit], outputs=[out])

if __name__ == "__main__":
    demo.launch()
