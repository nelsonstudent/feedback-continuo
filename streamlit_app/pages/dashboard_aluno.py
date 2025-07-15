import streamlit as st
import requests
from utils.pages_utils import inject_css

inject_css("static/dashboard.css")

st.set_page_config(page_title="Dashboard do Aluno - SIAS", page_icon="🎓", layout="wide")

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("Faça login para acessar o dashboard.")
    st.switch_page("main.py")

aluno_nome = st.session_state.get("nome", "Nome do Aluno")
aluno_turma = st.session_state.get("turma", "Turma do Aluno")
grupo = st.session_state.get("grupo", "Grupo do Aluno")

st.markdown("""
<div class="sias-header">
    <span class="sias-logo">SIAS</span> 
    <span class="sias-title">Dashboard do Aluno</span>
</div>
""", unsafe_allow_html=True)

cols = st.columns([1, 4])

with cols[0]:
    st.markdown(f"""
    <div class="sias-sidebar">
        <div class="sias-avatar"></div>
        <a href="#" class="sias-foto-link">Atualizar sua foto</a>
        <div class="sias-username">{aluno_nome}</div>
        <div class="sias-turma">{aluno_turma}</div>
        <div class="sias-section sias-section-grupo">Grupo: {grupo}</div>
        <div class="sias-section sias-section-progresso">PROGRESSO</div>
        <a href="#">Materiais Concluídos</a><br>
        <a href="#">Pré-Teste</a><br>
        <a href="#">Avaliações Realizadas</a>
        <div class="sias-section sias-section-geral">GERAL</div>
        <a href="#">Dados Pessoais</a><br>
        <a href="#">Mensagens</a><br>
        <a href="#">Abrir Chamado</a><br>
        <a href="#">Sistema</a>
    </div>
    """, unsafe_allow_html=True)

with cols[1]:
    st.markdown('<div class="sias-main"></div>', unsafe_allow_html=True)
    st.header("📚 Materiais da Aula")
    st.info("Lista de materiais (textos, vídeos) será exibida aqui.")

    st.header("✅ Marcar Materiais como Concluídos")
    st.info("Funcionalidade para marcar materiais como concluídos.")

    st.header("📝 Pré-Teste")
    st.info("Formulário de pré-teste será exibido aqui.")

    st.header("⭐ Avaliação da Aula")
    st.info("Formulário de avaliação da aula após sua realização.")

    st.header("💬 Meu Feedback")
    st.info("Aqui você verá como seu feedback foi considerado.")
