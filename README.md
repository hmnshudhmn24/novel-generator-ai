# 📖 AI-Driven Novel Generator (NaNoGenMo Style)

## 🌟 Overview

Inspired by **NaNoGenMo (National Novel Generation Month)** ✍️, this project explores the surreal and creative world of **algorithmically generated novels**.  

This project lets you:  
✨ Generate novels from a text corpus (AI storytelling)  
🔀 Mash up text from multiple sources (tweets, wiki, random text)  
⚡ Create constraint-based “mini-novels” under **256 characters of code**  
🌐 Run everything in a fun **Streamlit web app** demo  

Think of it as a playground for **computational narrative** 🧠📚.



## 🎯 Features

- 📚 **Novel Generator** → Generate thousands of words using a source corpus  
- 🔀 **Mashup Generator** → Blend text from multiple files (tweets/wiki)  
- ✂️ **Constraints Mode** → Tiny <256-char generator, NaNoGenMo-style  
- 🎨 **Interactive App** → Run everything in a Streamlit web UI  



## 🛠️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/novel-generator-ai.git
cd novel-generator-ai
pip install -r requirements.txt
```



## ▶️ Usage

### 1️⃣ Generate a Novel
```bash
python generator.py
```
Outputs a **novel.txt** file with ~2000+ words of surreal storytelling 📖.



### 2️⃣ Generate a Mashup
```bash
python mashup.py
```
Outputs a **mashup.txt** file — blending random tweets/wiki lines into an abstract narrative 🌐.



### 3️⃣ Tiny 256-Character Novel Generator
```bash
python constraints.py
```
Outputs a "micro-novel" using **super-short code** ⚡.



### 4️⃣ Run the Web App
```bash
streamlit run app.py
```
Launches a Streamlit app with interactive buttons 🎛️ to:  
- Generate a novel  
- Generate a mashup  
- View the results directly in the browser  



## 📂 Project Structure

```
novel-generator-ai/
│── generator.py        # Novel generator from corpus
│── mashup.py           # Mashup generator (tweets/wiki/text)
│── constraints.py      # <256 char "NaNoGenMo challenge" generator
│── app.py              # Streamlit web demo
│── requirements.txt    # Dependencies
│── README.md           # Documentation
│── data/
│    └── corpus.txt     # Example corpus for generation
```



## 🚀 Roadmap

- [ ] Add **Markov Chain**-based generator  
- [ ] Add **Transformer / GPT-powered mashups**  
- [ ] Introduce **poetry / rhyme modes** 🎭  
- [ ] Deploy demo app online with **Streamlit Cloud**  

