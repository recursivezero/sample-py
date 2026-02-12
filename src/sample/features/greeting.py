import streamlit as st

from sample.utils.constants import APP_TITLE, DEFAULT_GREETING
from sample.utils.helper import normalize_name


def greet():
    st.header(APP_TITLE)

    name = st.text_input("Enter your name")

    clean_name = normalize_name(name)

    if clean_name:
        st.success(f"{DEFAULT_GREETING}, {clean_name} 👋")
