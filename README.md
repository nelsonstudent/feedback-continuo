# 📊 Plataforma de Feedback Contínuo para Professores e Alunos

Uma solução simples e funcional para **avaliação e feedback contínuo no ambiente educacional**. Permite que **alunos enviem feedbacks anônimos ou identificados** e que **professores acompanhem os dados consolidados** em um dashboard, promovendo melhorias em tempo real na didática e nos conteúdos apresentados.

---

## 🎯 Objetivo

Criar um MVP funcional para resolver a dificuldade em medir o desempenho de alunos e professores, usando **técnicas de engenharia de software** e ferramentas de **analytics educacional**.

---

## 🧩 Funcionalidades

### Para Alunos
- ✅ Enviar feedback anônimo ou identificado (ex.: *"A aula foi muito rápida"*)
- ✅ Selecionar nota para aula (escala de 1 a 5 com emojis)
- ✅ Escrever comentários livres sobre dúvidas ou sugestões
- ✅ Sugerir tópicos para revisão

### Para Professores
- 📊 Visualizar um **dashboard simplificado** com:
  - Gráfico de satisfação média por aula
  - Palavras-chave mais citadas (com análise básica de sentimentos)
  - Tópicos com maior número de dúvidas
- 📁 Exportar relatórios em CSV

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Linguagem:** Python
- **Framework:** [Flask](https://flask.palletsprojects.com/)
- **Banco de Dados:** SQLite via [SQLAlchemy](https://www.sqlalchemy.org/)
- **Manipulação de Dados:** [Pandas](https://pandas.pydata.org/)
- **Análise de Texto:** (futuro) Ferramentas Python (ex: NLTK, spaCy) – *não prioritário para o MVP*

### Frontend
- **Framework:** [Streamlit](https://streamlit.io/) (dashboard e interação para alunos e professores)
- Alternativa futura: HTML + CSS + JS com [Bootstrap](https://getbootstrap.com/) para páginas administrativas simples

### Deploy
- [Render](https://render.com/) ou [Railway](https://railway.app/) (backend Flask)
- [Streamlit Community Cloud](https://streamlit.io/cloud) (frontend)  
  > *Obs: O Streamlit pode ser executado localmente ou hospedado separadamente, conforme necessidade do MVP.*

---

## 🧪 Fluxo de Uso

### Aluno
1. Acessa o link da plataforma (enviado pelo professor)
2. Seleciona um emoji: 😊 😐 😞
3. Escreve um comentário opcional:  
   > "Não entendi o exemplo de SQL JOIN..."
4. Envia o feedback

### Professor
1. Acessa seu dashboard (via Streamlit) com login
2. Visualiza:
   - Satisfação média da aula
   - Comentários mais recorrentes
   - Sugestões de revisão
3. Exporta relatórios em CSV ou Excel

---

## 📁 Estrutura do Projeto

```
feedback-continuo/
├── app/
│   ├── __init__.py         # Inicialização do Flask
│   ├── config.py           # Configurações
│   ├── models/             # ORM com SQLAlchemy
│   ├── repositories/       # Padrão Repository
│   ├── services/           # Lógica de negócio
│   ├── api/                # Rotas Flask (Controllers)
│   ├── templates/          # (Opcional) HTML para admin ou forms
│   └── static/             # Arquivos estáticos (uploads, css, imgs)
├── streamlit_app/
│   ├── main.py             # Dashboard principal (Streamlit)
│   └── pages/              # Páginas adicionais para alunos/professores
├── tests/                  # Testes automatizados
├── docs/                   # Documentação e diagramas
├── requirements.txt        # Dependências Python
├── README.md
└── LICENSE
```

---




