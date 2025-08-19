import random

def mashup_text(output_file="mashup.txt", sources=["data/corpus.txt", "data/wiki.txt", "data/tweets.txt"]):
    all_text = []
    for src in sources:
        try:
            with open(src, "r", encoding="utf-8") as f:
                all_text.extend(f.readlines())
        except FileNotFoundError:
            print(f"Source not found: {src}")
    
    mashup = []
    for i in range(1000):
        line = random.choice(all_text).strip()
        mashup.append(line)
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(mashup))

if __name__ == "__main__":
    mashup_text()
