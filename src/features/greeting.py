import streamlit as st

from utils.constants import (
    APP_TITLE,
    DEFAULT_GREETING,
    FAQ_TITLE,
)
from utils.helper import normalize_name
from utils.faq import faq_page


def greet():
    st.header(APP_TITLE)

    name = st.text_input("Enter your name")

    clean_name = normalize_name(name)

    if clean_name:
        st.success(f"{DEFAULT_GREETING}, {clean_name} 👋")

    with st.expander(FAQ_TITLE):
        faq_page()
