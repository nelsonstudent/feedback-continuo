import streamlit as st
import os

def inject_css(file_path="static/style.css"):
    base_path = os.path.dirname(os.path.abspath(__file__))
    css_path = os.path.join(base_path, "..", file_path)
    css_path = os.path.normpath(css_path)
    with open(css_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)