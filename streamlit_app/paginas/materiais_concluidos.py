import streamlit as st
import requests

API_URL = "https://api.example.com/materiais_concluidos/completos"

st.title("Materiais Disponíveis")

# Buscar todos os materiais
resp = requests.get(f"{API_URL}")
if resp.ok:
    materiais = resp.json()
else:
    st.error("Erro ao carregar materiais")
    materiais = []

for m in materiais:
    st.subheader(m["titulo"])
    # Botão para concluir
    if not m.get("concluido", False):
        if st.button(f"Concluir {m['titulo']}", key=f"complete-{m['id']}"):
            post = requests.post(f"{API_URL}/{m['id']}/materiais_concluidos")
            if post.ok:
                st.success("✅ Marcado como concluído!")
                st.experimental_rerun()
            else:
                st.error("❌ Falha ao concluir")
    else:
        st.info("✅ Já concluído")