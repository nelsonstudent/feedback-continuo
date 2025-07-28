# Documentação dos testes automatizados

---

## Testes de Integração com o Banco de Dados

Este documento descreve os **objetivos** e **critérios de aceite** de cada um dos casos de teste presentes no arquivo `test_database.py`, que valida a integração entre os modelos da aplicação e o banco de dados utilizando SQLAlchemy.

---

### `test_insert_aluno`

* **Objetivo:** Verificar se um objeto `Aluno` é inserido corretamente no banco de dados.
* **Critérios de Aceite:** O atributo `id` do aluno é preenchido após o commit, confirmando a inserção.

### `test_verificar_aluno`

* **Objetivo:** Validar a persistência e consulta de um `Aluno` com filtro por email.
* **Critérios de Aceite:** A consulta retorna um objeto não nulo com o nome correspondente ao esperado.

### `test_insert_aula`

* **Objetivo:** Garantir que uma `Aula` pode ser criada com sucesso.
* **Critérios de Aceite:** O campo `id` da aula é definido após a inserção.

### `test_verificar_aula`

* **Objetivo:** Validar a consulta de uma `Aula` pelo tema.
* **Critérios de Aceite:** A aula retornada possui o tema esperado.

### `test_insert_aula_material`

* **Objetivo:** Testar a inserção de relação entre `Aula` e `Material` na tabela intermediária `aula_material`.
* **Critérios de Aceite:** Nenhuma exceção é levantada e o insert ocorre com sucesso.

### `test_verificar_aula_material`

* **Objetivo:** Validar a persistência da associação entre `Aula` e `Material`.
* **Critérios de Aceite:** O registro na tabela `aula_material` é recuperado com os `ids` corretos.

### `test_insert_avaliacao`

* **Objetivo:** Verificar a criação de uma `Avaliacao` relacionando `Aluno` e `Aula`.
* **Critérios de Aceite:** O `id` da avaliação é gerado com sucesso após o commit.

### `test_verificar_avaliacao`

* **Objetivo:** Verificar a persistência e consulta de uma `Avaliacao` por aluno e aula.
* **Critérios de Aceite:** O tipo de avaliação recuperado é igual ao esperado.

### `test_insert_grupo_aula`

* **Objetivo:** Testar a inserção de um `GrupoAula`.
* **Critérios de Aceite:** O `id` é preenchido corretamente.

### `test_insert_material`

* **Objetivo:** Validar a inserção de um `Material` no banco de dados.
* **Critérios de Aceite:** O material possui um `id` após commit.

### `test_insert_material_visualizado`

* **Objetivo:** Verificar se a relação entre `Aluno` e `MaterialVisualizado` é persistida.
* **Critérios de Aceite:** Um objeto de `MaterialVisualizado` é salvo com sucesso.

### `test_insert_pre_teste`

* **Objetivo:** Testar a criação de uma pergunta de `PreTeste`.
* **Critérios de Aceite:** O `id` da instância é definido corretamente.

### `test_insert_professor`

* **Objetivo:** Garantir que um `Professor` pode ser inserido no banco.
* **Critérios de Aceite:** O `id` é definido após commit.

### `test_insert_relatorio`

* **Objetivo:** Verificar a inserção de um objeto `Relatorio`.
* **Critérios de Aceite:** A instância é salva com um `id` válido.

### `test_insert_resposta_pre_teste`

* **Objetivo:** Testar a persistência de uma `RespostaPreTeste`.
* **Critérios de Aceite:** O `id` da resposta é gerado corretamente.

---

Esses testes garantem que os modelos da aplicação estão corretamente configurados e integrados ao esquema do banco de dados.


---
## Testes de rotas com do BackEnd com Flask