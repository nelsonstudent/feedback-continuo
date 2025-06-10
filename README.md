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
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Banco de Dados:** SQLite via SQLAlchemy
- **Análise de Texto:** [NLTK](https://www.nltk.org/) (em desenvolvimento para MVP)

### Frontend
- HTML + CSS + JS com [Bootstrap](https://getbootstrap.com/)
- Alternativa: [Vue.js](https://vuejs.org/) para dashboards interativos

### Deploy
- [Vercel](https://vercel.com/) ou GitHub Pages (frontend)
- [Render](https://render.com/) ou [Railway](https://railway.app/) (backend gratuito)

---

## 🧪 Fluxo de Uso

### Aluno
1. Acessa o link da plataforma (enviado pelo professor)
2. Seleciona um emoji: 😊 😐 😞
3. Escreve um comentário opcional:  
   > "Não entendi o exemplo de SQL JOIN..."
4. Envia o feedback

### Professor
1. Acessa seu dashboard com login
2. Visualiza:
   - Satisfação média da aula
   - Comentários mais recorrentes
   - Sugestões de revisão
3. Exporta relatórios em CSV

---

## 📁 Estrutura do Projeto

feedback-continuo/
├── backend/
│ ├── main.py # API FastAPI
│ ├── models.py # ORM com SQLAlchemy
│ ├── database.py # Conexão com SQLite
│ └── requirements.txt # Dependências Python
├── frontend/
│ └── index.html # Interface básica do aluno
├── README.md
└── LICENSE

---




