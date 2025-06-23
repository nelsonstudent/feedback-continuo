# ADR-002: Decisão sobre o Padrão de Projeto

## Contexto

Durante a concepção do MVP da plataforma educacional, foi identificada a necessidade de adotar padrões de projeto para garantir a organização, manutenibilidade e escalabilidade do código, mesmo em um cenário inicial com equipe iniciante em Python.

## Decisão

Serão adotados os seguintes padrões de projeto:

- **Repository Pattern**: Cria uma camada intermediária entre o domínio e a persistência, isolando regras de acesso a dados e facilitando futuras trocas de banco.
- **Service Layer Pattern**: Centraliza a lógica de negócio, mantendo os controllers (rotas Flask) e os repositórios focados em suas responsabilidades.
- **Factory Pattern (Simples)**: Utilizado para criação flexível de objetos específicos, como relatórios, agrupamentos ou outros recursos configuráveis.
- **Singleton Pattern (opcional)**: Aplicado para garantir uma única instância de recursos compartilhados, como a conexão com o banco de dados, quando necessário.

Esses padrões serão aplicados de forma pragmática, adaptando-se à simplicidade do MVP e ao aprendizado da equipe.

## Consequências

- **Vantagens:**
  - Facilita manutenção, testes e evolução do sistema.
  - Permite separar claramente responsabilidades no código.
  - Torna o código mais didático e alinhado com boas práticas do mercado.

- **Desvantagens:**
  - Pode adicionar algum overhead inicial para equipes muito iniciantes, mas o ganho em organização compensa a curva de aprendizado.

## Referências

- [Repository Pattern em Python](https://www.treinaweb.com.br/blog/implementando-o-pattern-repository-no-python)
- [Service Layer Pattern (Martin Fowler)](https://martinfowler.com/eaaCatalog/serviceLayer.html)
- [Factory Pattern em Python (Real Python)](https://realpython.com/factory-method-python/)
- [Singleton Pattern em Python](https://refactoring.guru/pt-br/design-patterns/singleton/python/example)

---

*ADR elaborada em 20/06/2025 para orientar decisões de design do projeto.*

