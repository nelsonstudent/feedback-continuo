# ADR-003: Decisão sobre a Arquitetura do Projeto

## Contexto

O projeto visa entregar um MVP educacional utilizando Python e tecnologias correlatas, com uma equipe de perfil iniciante. Era necessário adotar uma arquitetura que facilitasse o desenvolvimento incremental, a separação de responsabilidades e a futura evolução do sistema.

## Decisão

Foi escolhida a arquitetura **MVC Simples (Model-View-Controller)** com adaptações para projetos Python modernos:

- **Model:** Responsável pelas entidades, validação e interação com o banco de dados (ORM SQLAlchemy).
- **View:** Responsável pela apresentação (Streamlit para dashboards/formulários; templates Jinja2 para possíveis telas Flask).
- **Controller/API:** Responsável pelo fluxo de dados, endpoints e orquestração das regras de negócio.
- **Repository e Service:** Camadas intermediárias para reforçar a separação entre persistência e lógica de negócio.

A estrutura do projeto seguirá a separação clara entre backend (Flask), frontend (Streamlit) e documentação, conforme detalhado em ADR anterior.

## Consequências

- **Vantagens:**
  - Organização do código e facilidade de onboarding para novos membros.
  - Permite evolução para sistemas mais robustos no futuro.
  - Reduz riscos de acoplamento e facilita testes.

- **Desvantagens:**
  - Leve aumento da complexidade inicial para projetos muito pequenos.
  - Exige disciplina na separação de responsabilidades desde o início.

## Referências

- [MVC com Flask](https://medium.com/@leandro.campos.m/mvc-com-flask-python-8b0c8c0b8f9a)
- [Padrões Arquiteturais para Python](https://realpython.com/architecture-patterns-python/)
- [Documentação oficial do Flask](https://flask.palletsprojects.com/)

---

*ADR elaborada em 20/06/2025 para registrar a decisão arquitetural do projeto.*
