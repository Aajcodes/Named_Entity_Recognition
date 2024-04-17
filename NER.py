import streamlit as st 
from newspaper import Article 
import spacy
from spacy import displacy
import en_core_web_sm

nlp = en_core_web_sm.load()

st.title("Named Entity Recognition")

st.info("This is a streamlit application created for Named Entity Recognition(NER) from user provided paragraphs and online articles ")

check = st.radio("Select",("Enter URL","Enter a Paragraph"))
if check == "Enter URL":
    url = st.text_input("Enter URL")
    button1 = st.button("fetch")
    if button1:
        article = Article(url)
        article.download()
        article.parse()
        doc = nlp(article.text)
        st.markdown(displacy.render(doc,style = 'ent',jupyter = False),unsafe_allow_html = True)
else:
    para_input = st.text_area("Enter the Paragraph")
    button2 = st.button("Done")
    if button2:
        doc = nlp(para_input)
        st.markdown(displacy.render(doc,style = 'ent',jupyter = False), unsafe_allow_html = True)


