import streamlit as st
import requests
import os

from utils.pages_utils import inject_css
inject_css("static/style.css")

try:
    from dotenv import load_dotenv
    load_dotenv()
    API_URL = os.getenv("API_URL", "http://localhost:5000")
except ImportError:
    API_URL = os.getenv("API_URL", "http://localhost:5000")

st.set_page_config(
    page_title="SIAS - Sistema de Avaliação Simultânea",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="collapsed"
)

with st.container():
    st.markdown('<div class="sias-container">', unsafe_allow_html=True)
    st.markdown('<div class="sias-title">SIAS</div>', unsafe_allow_html=True)
    st.markdown('<div class="sias-subtitle">SISTEMA DE AVALIAÇÃO SIMULTÂNEA</div>', unsafe_allow_html=True)
    st.markdown("<hr style='margin: 1.5rem 0; border-color: #f0ffb5;'>", unsafe_allow_html=True)

    st.markdown('<div style="margin-bottom: 1rem; font-weight: bold; color: #2c6e00;">Login</div>', unsafe_allow_html=True)
    email = st.text_input("", placeholder="Seu e-mail", label_visibility="collapsed", key="login_email")
    senha = st.text_input("", placeholder="Sua senha", type="password", label_visibility="collapsed", key="login_pass")

    col1, col2 = st.columns([2, 1])
    with col1:
        if st.button("Fazer cadastro", use_container_width=True):
            st.switch_page("pages/cadastro.py")
    with col2:
        st.markdown('<span style="color: #79a149; font-style: italic;">Esqueceu sua senha?</span>', unsafe_allow_html=True)

    if st.button("LOGIN", use_container_width=True):
        if not email or not senha:
            st.error("Preencha e-mail e senha.")
        else:
            try:
                resp = requests.post(f"{API_URL}/login", json={"email": email, "senha": senha}, timeout=10)
                if resp.status_code == 200:
                    user_data = resp.json()
                    st.session_state["logged_in"] = True
                    st.session_state["user_role"] = user_data.get("role", "aluno")
                    st.session_state["user_name"] = user_data.get("nome", email)
                    st.switch_page("pages/dashboard.py")
                else:
                    st.error("Usuário ou senha inválidos.")
            except Exception as e:
                st.error(f"Erro ao conectar ao servidor: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
