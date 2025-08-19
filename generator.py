import random

def generate_novel(output_file="novel.txt", word_count=5000):
    with open("data/corpus.txt", "r", encoding="utf-8") as f:
        corpus = f.read().split()
    
    novel = []
    for i in range(word_count):
        word = random.choice(corpus)
        novel.append(word)
        if i % 50 == 0:
            novel.append("\n")
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(" ".join(novel))

if __name__ == "__main__":
    generate_novel()
