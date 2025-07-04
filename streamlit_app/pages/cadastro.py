import streamlit as st
import time
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

st.set_page_config(page_title="Cadastro - SIAS", page_icon="📝")

st.markdown('<div class="sias-title">Cadastro SIAS</div>', unsafe_allow_html=True)
st.markdown('<div class="sias-subtitle">Crie sua conta de acesso</div>', unsafe_allow_html=True)
st.markdown('<div class="sias-card">', unsafe_allow_html=True)

tipo_usuario = st.selectbox("Sou:", ["Aluno", "Professor"])

nome = st.text_input("Nome completo")
email = st.text_input("E-mail")
senha = st.text_input("Senha", type="password")
confirma_senha = st.text_input("Confirme a senha", type="password")
turma = None
if tipo_usuario == "Aluno":
    turma = st.text_input("Turma")

if st.button("Cadastrar", use_container_width=True):
    # Validação simples
    if not nome or not email or not senha or not confirma_senha or (tipo_usuario == "Aluno" and not turma):
        st.error("Preencha todos os campos obrigatórios.")
    elif senha != confirma_senha:
        st.error("As senhas não coincidem.")
    else:
        payload = {
            "nome": nome,
            "email": email,
            "senha": senha
        }
        if tipo_usuario == "Aluno":
            payload["turma"] = turma
            endpoint = f"{API_URL}/alunos/"
        else:
            endpoint = f"{API_URL}/professores/"
        
        resp = requests.post(endpoint, json=payload, timeout=10)
        if resp.status_code in (200, 201):
            st.success("Cadastro realizado com sucesso! Faça login para acessar.")
            time.sleep(2)
            st.switch_page("main.py")
        else:
            try:
                data = resp.json()
                erro = data.get("erro") or data.get("mensagem") or "Erro ao cadastrar. Tente outro e-mail."
            except Exception:
                erro = f"Erro inesperado: {resp.status_code} - {resp.text[:200]}"
            st.error(erro)

if st.button("Voltar para Login", use_container_width=True):
    st.switch_page("main.py")

st.markdown('</div>', unsafe_allow_html=True)