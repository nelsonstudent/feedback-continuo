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

### `test_listar_alunos`
**Objetivo:** Testa a listagem de alunos cadastrados via rota GET /alunos/.

**Critério de aceite:** Deve retornar status 200 e uma lista.

### `test_buscar_aluno`
**Objetivo:** Testa a recuperação de um aluno por ID via rota GET /alunos/<id>.

**Critério de aceite:** Deve retornar status 200 e os dados corretos do aluno.

### `test_criar_aluno`
**Objetivo:** Testa a criação de um novo aluno via POST /alunos/.

**Critério de aceite:** Deve retornar status 201.

### `test_criar_aluno_faltando_campos`
**Objetivo:** Testa o erro ao criar aluno sem campos obrigatórios.

**Critério de aceite:** Deve retornar status 400.

### `test_atualizar_aluno`
**Objetivo:** Testa a atualização do nome de um aluno via PUT /alunos/<id>.

**Critério de aceite:** Deve retornar status 200 e o novo nome.

### `test_deletar_aluno`
**Objetivo:** Testa a exclusão de um aluno via DELETE /alunos/<id>.

**Critério de aceite:** Deve retornar status 200 com mensagem de sucesso.

### `test_listar_aulas`
**Objetivo:** Testa a listagem de aulas via GET /aulas/.

**Critério de aceite:** Deve retornar status 200 e uma lista.

### `test_buscar_aula`
**Objetivo:** Testa a busca de uma aula por ID via GET /aulas/<id>.

**Critério de aceite:** Deve retornar status 200 e o tema correspondente.

### `test_criar_aula`
**Objetivo:** Testa a criação de uma aula via POST /aulas/.

**Critério de aceite:** Deve retornar status 201.

### `test_atualizar_aula`
**Objetivo:** Testa a atualização do tema de uma aula via PUT /aulas/<id>.

**Critério de aceite:** Deve retornar status 200 e novo tema.

### `test_deletar_aula`
**Objetivo:** Testa a exclusão de uma aula via DELETE /aulas/<id>.

**Critério de aceite:** Deve retornar status 200 com mensagem de sucesso.

### `test_login_aluno_com_sucesso`
**Objetivo:** Testa o login com credenciais corretas.

**Critério de aceite:** Deve retornar token de acesso e status 200.

### `test_login_credenciais_invalidas`
**Objetivo:** Testa tentativa de login com dados incorretos.

**Critério de aceite:** Deve retornar status 401 e mensagem de erro.

### `test_listar_avaliacoes`
**Objetivo:** Testa listagem de avaliações via GET /avaliacoes/.

**Critério de aceite:** Deve retornar lista vazia ou avaliações.

### `test_buscar_avaliacao`
**Objetivo:** Testa busca de avaliação por ID.

**Critério de aceite:** Deve retornar os dados da avaliação.

### `test_criar_avaliacao`
**Objetivo:** Testa criação de avaliação via POST /avaliacoes/.

**Critério de aceite:** Deve retornar status 201.

### `test_atualizar_avaliacao`
**Objetivo:** Testa atualização de avaliação via PUT /avaliacoes/<id>.

**Critério de aceite:** Deve retornar nota atualizada.

### `test_deletar_avaliacao`
**Objetivo:** Testa exclusão de avaliação via DELETE /avaliacoes/<id>.

**Critério de aceite:** Deve retornar status 200 e mensagem.