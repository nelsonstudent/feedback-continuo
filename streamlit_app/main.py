import streamlit as st

st.sidebar.title("Navegação")
pagina = st.sidebar.selectbox("Ir para:", ["Alunos", "Professores", "Materiais Concluídos"])

if pagina =="Alunos":
   st.write("Página de Alunos")
elif pagina == "Professores":
   st.write("Página de Professores")
elif pagina == "Materiais Concluídos":
    st.write("Página de Materiais Concluídos")
    st.success("✅ Já concluído")
else:
    st.error("Página não encontrada")
    st.error("Erro ao carregar materiais")
    