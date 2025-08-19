import streamlit as st
import generator, mashup

st.title("📖 AI-Driven Novel Generator (NaNoGenMo Style)")

st.write("Generate algorithmic novels and surreal mashups with a click!")

option = st.selectbox("Choose Generation Mode", ["Novel Generator", "Mashup Generator"])

if option == "Novel Generator":
    if st.button("Generate Novel"):
        generator.generate_novel("novel.txt", word_count=2000)
        st.success("Novel generated successfully!")
        with open("novel.txt", "r", encoding="utf-8") as f:
            st.text_area("Generated Novel", f.read()[:5000], height=300)
elif option == "Mashup Generator":
    if st.button("Generate Mashup"):
        mashup.mashup_text("mashup.txt")
        st.success("Mashup generated successfully!")
        with open("mashup.txt", "r", encoding="utf-8") as f:
            st.text_area("Generated Mashup", f.read()[:5000], height=300)
