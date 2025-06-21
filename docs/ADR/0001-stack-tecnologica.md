# ADR-001: Stack Tecnológica para MVP da Plataforma Educacional

## Contexto

O objetivo deste documento é registrar as decisões técnicas para o desenvolvimento do MVP da Plataforma Educacional, conforme requisitos coletados. A decisão visa garantir simplicidade, aprendizado rápido e aderência às necessidades do projeto.

## Problema

Precisamos definir uma stack tecnológica que permita:

- Desenvolvimento rápido do MVP
- Facilidade de aprendizado e implementação pelos membros da equipe
- Atender aos requisitos funcionais e técnicos levantados
- Permitir evolução futura da plataforma

## Decisão

### Linguagem Principal

- **Python**

### Frontend

- **Streamlit**
  - Justificativa: Permite construção rápida de interfaces web, dashboards e formulários em Python puro, sem necessidade de aprender JavaScript/HTML/CSS. Ótimo para prototipação e MVPs.
- **Alternativa:** Gradio (em caso de necessidade de protótipos de formulários ainda mais rápidos, mas Streamlit é preferível).

### Backend

- **Flask**
  - Justificativa: Framework web minimalista, fácil de aprender, com ampla documentação e comunidade ativa. Ideal para APIs, autenticação simples, uploads e integração com banco de dados.

### Banco de Dados

- **SQLite**
  - Justificativa: Simples, integrado ao Python, não requer instalação adicional. Ideal para MVPs e ambientes de teste.

### ORM

- **SQLAlchemy**
  - Justificativa: Facilita o acesso e manipulação de dados relacionais no Python, reduzindo a necessidade de SQL puro e evitando erros comuns de manipulação manual.

### Upload de Arquivos

- **Local (diretório do projeto)**
  - Justificativa: Simplicidade para MVP, baixo custo e fácil de implementar.
- **Alternativa:** Cloudinary (para arquivos maiores ou produção, integração gratuita e fácil via API).

### Geração de Relatórios

- **Pandas**
  - Justificativa: Biblioteca poderosa para manipulação e exportação de dados (ex: CSV), facilitando a geração de relatórios customizados.

### Deploy

- **Heroku**
  - Justificativa: Plataforma gratuita para MVPs, fácil integração com projetos Python, ampla documentação.
- **Alternativa:** Railway (também simples e didático para deploys rápidos).

### Organização do Projeto

- **GitHub** (controle de versão)
- **Trello ou GitHub Projects** (gestão de tarefas)

### Bibliotecas Auxiliares

- **Jinja2** (se necessário customizar templates HTML no Flask)
- **Chart.js/Plotly** (se quiser adicionar gráficos customizados, embora Streamlit já ofereça visualizações nativas)

---

## Consequências

- **Vantagens:**
  - Curva de aprendizado baixa, especialmente para equipe iniciante em Python
  - Rapidez no desenvolvimento e iteração do MVP
  - Facilidade de manutenção e posterior evolução da stack
  - Amplo material de apoio e exemplos na internet

- **Desvantagens:**
  - Menos customização visual do frontend com Streamlit (em relação a frameworks JS modernos)
  - SQLite não é recomendado para produção em larga escala
  - Para produção, será necessário migrar uploads locais para serviço de armazenamento externo e migrar o banco para PostgreSQL

---

## Resumo da Stack

| Camada        | Ferramenta             | Motivo                                                     |
|---------------|------------------------|------------------------------------------------------------|
| Frontend      | Streamlit              | Python, rápido, fácil, ideal para MVP                      |
| Backend       | Flask                  | Python, minimalista, fácil de aprender                     |
| Banco de Dados| SQLite                 | Simples, integrado, ideal para MVP                         |
| ORM           | SQLAlchemy             | Abstração do banco, reduz erros, integração Python         |
| Relatórios    | Pandas                 | Manipulação/exportação de dados fácil                      |
| Deploy        | Heroku                 | Deploy gratuito e fácil para Python                        |
| Uploads       | Local/Cloudinary       | Simplicidade e/ou escalabilidade futura                    |

---

## Referências

- [Flask Mega-Tutorial (em português)](https://blog.miguelgrinberg.com/post/o-flask-mega-tutorial-parte-i-ol-mundo)
- [Streamlit Docs](https://docs.streamlit.io/)
- [Deploy Flask no Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)

---

*Documento ADR elaborado em 20/06/2025 por decisão coletiva da equipe.*