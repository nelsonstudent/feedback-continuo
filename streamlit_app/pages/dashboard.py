import streamlit as st
import requests
import os
import streamlit as st
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("Faça login para acessar o dashboard.")
    st.switch_page("main.py")

from utils.pages_utils import inject_css
inject_css("static/dashboard.css")



st.set_page_config(page_title="Dashboard - SIAS", page_icon="📊", layout="wide")

# Barra superior
st.markdown("""
<div class="sias-header">
    <span class="sias-logo">SIAS</span> 
    <span class="sias-title">SISTEMA DE AVALIAÇÃO SIMULTÂNEA</span>
</div>
<div class="sias-menu">
    <span>Turmas</span>
    <span>Notícias</span>
    <span>Avaliações</span>
    <span>Cronograma</span>
    <span>Sobre</span>
</div>
""", unsafe_allow_html=True)

cols = st.columns([1, 4])  # Sidebar e área principal

with cols[0]:
    st.markdown("""
    <div class="sias-sidebar">
        <div class="sias-avatar"></div>
        <a href="#" class="sias-foto-link">Atualizar sua foto</a>
        <div class="sias-username">Nome do Aluno</div>
        <div class="sias-turma">Turma do Aluno</div>
        <div class="sias-section sias-section-desempenho">DESEMPENHO</div>
        <a href="#">Consultar Notas</a><br>
        <a href="#">Consultar Comentários</a><br>
        <a href="#">Consultar Faltas</a>
        <div class="sias-section sias-section-geral">GERAL</div>
        <a href="#">Dados Pessoais</a><br>
        <a href="#">Mensagens</a><br>
        <a href="#">Abrir Chamado</a><br>
        <a href="#">Sistema</a>
    </div>
    """, unsafe_allow_html=True)

with cols[1]:
    st.markdown('<div class="sias-main"></div>', unsafe_allow_html=True)