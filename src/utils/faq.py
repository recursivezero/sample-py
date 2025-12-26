from pathlib import Path
import streamlit as st
from bs4 import BeautifulSoup


def faq_page():
    # Load CSS
    st.title(":blue[❓Threadzip-FAQs]")
    css = Path(r"templates/faq.css").read_text()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

    # Load full HTML
    html = Path(r"templates/faq.html").read_text()

    # Parse and split sections using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    general_faq = str(soup.find(id="general-faq"))
    technical_faq = str(soup.find(id="technical-faq"))

    # Create Streamlit tabs
    tab1, tab2 = st.tabs(["General", "Technical"])

    with tab1:
        st.markdown(general_faq, unsafe_allow_html=True)

    with tab2:
        st.markdown(technical_faq, unsafe_allow_html=True)
