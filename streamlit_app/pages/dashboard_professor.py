import streamlit as st
import requests
from utils.pages_utils import inject_css

inject_css("static/dashboard.css")

st.set_page_config(page_title="Dashboard do Professor - SIAS", page_icon="🧑‍🏫", layout="wide")

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("Faça login para acessar o dashboard.")
    st.switch_page("main.py")

prof_nome = st.session_state.get("nome", "Nome do Professor")
prof_area = st.session_state.get("area", "Área do Professor")

st.markdown("""
<div class="sias-header">
    <span class="sias-logo">SIAS</span> 
    <span class="sias-title">Dashboard do Professor</span>
</div>
""", unsafe_allow_html=True)

cols = st.columns([1, 4])

with cols[0]:
    st.markdown(f"""
    <div class="sias-sidebar">
        <div class="sias-avatar"></div>
        <a href="#" class="sias-foto-link">Atualizar sua foto</a>
        <div class="sias-username">{prof_nome}</div>
        <div class="sias-area">{prof_area}</div>
        <div class="sias-section sias-section-turmas">TURMAS</div>
        <a href="#">Visualizar Turmas</a><br>
        <a href="#">Agrupamento de Alunos</a>
        <div class="sias-section sias-section-materiais">MATERIAIS</div>
        <a href="#">Upload de Materiais</a><br>
        <a href="#">Pré-Teste</a>
        <div class="sias-section sias-section-avaliacao">AVALIAÇÃO</div>
        <a href="#">Avaliar Alunos</a><br>
        <a href="#">Relatórios</a>
        <div class="sias-section sias-section-geral">GERAL</div>
        <a href="#">Dados Pessoais</a><br>
        <a href="#">Mensagens</a><br>
        <a href="#">Abrir Chamado</a><br>
        <a href="#">Sistema</a>
    </div>
    """, unsafe_allow_html=True)

with cols[1]:
    st.markdown('<div class="sias-main"></div>', unsafe_allow_html=True)
    st.header("📂 Upload de Materiais Pré-Aula")
    st.info("Funcionalidade para fazer upload de textos e vídeos.")

    st.header("📝 Configuração de Pré-Teste")
    st.info("Configuração e acompanhamento do pré-teste.")

    st.header("📊 Métricas de Acesso e Compreensão")
    st.info("Painel com KPIs: % alunos que consumiram materiais, mapa de dúvidas, etc.")

    st.header("👥 Visualização de Turmas e Grupos")
    st.info("Listagem das turmas e agrupamento automático dos alunos.")

    st.header("🔎 Avaliação e Relatórios")
    st.info("Formulário para avaliar alunos e acessar relatórios cruzados.")
