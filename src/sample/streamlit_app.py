import sys
from pathlib import Path
import streamlit as st

# --- Path setup ---
package_root = str(Path(__file__).parent)
if package_root not in sys.path:
    sys.path.append(package_root)

# --- Imports ---
from utils.constants import COMPANY_LOGO, FAQ_TITLE
from utils.faq import faq_page
from utils.load_messages import get_msg
from features.greeting import greet

MSG = get_msg("MAIN_APP")


def main():
    st.set_page_config(
        page_title=MSG.title.page,
    )

    # Apply global sidebar CSS
    st.markdown(MSG.html.sidebar_style, unsafe_allow_html=True)
    st.markdown(
        """
    <style>
    section[data-testid="stSidebar"] li:has(button[data-test-id*="view_records"]) {
        display: none !important;
    }
    </style>
""",
        unsafe_allow_html=True,
    )

    # Define navigation pages from config
    pages = [
        st.Page(greet, title="Greeting Page", icon="🖌️", url_path="/greet"),
        st.Page(
            faq_page,
            title=FAQ_TITLE,
            icon="❓",
            url_path="/faq",
        ),
    ]

    # Sidebar with logo on top
    with st.sidebar:
        st.image(COMPANY_LOGO, width="stretch")
        nav = st.navigation(pages)

    nav.run()

    # Footer
    st.markdown(MSG.html.footer, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
