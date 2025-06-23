# Documento de Requisitos

Este documento descreve os requisitos funcionais e não funcionais do sistema de apoio ao ensino baseado em feedback contínuo.

---

## ✅ Requisitos Funcionais (RF)

### 📚 Para Professores

- **RF01**: O sistema deve permitir o upload de materiais (textos e vídeos) para cada aula.
- **RF02**: O sistema deve permitir que o professor configure um pré-teste com três alternativas por questão.
- **RF03**: O sistema deve exibir um dashboard com métricas de acesso e compreensão dos alunos.
- **RF04**: O sistema deve permitir que o professor avalie a participação e desempenho dos alunos.
- **RF05**: O sistema deve gerar relatórios com cruzamento entre desempenho dos alunos e suas autoavaliações.

### 👨‍🎓 Para Alunos

- **RF06**: O sistema deve permitir que o aluno acesse materiais das aulas (textos e vídeos).
- **RF07**: O sistema deve permitir que o aluno marque os materiais como "concluídos".
- **RF08**: O sistema deve apresentar um pré-teste ao aluno antes da aula.
- **RF09**: O sistema deve permitir que o aluno avalie a aula após sua realização.
- **RF10**: O sistema deve mostrar aos alunos como seu feedback foi considerado nas aulas seguintes.

### ⚙️ Técnicos / Sistema

- **RF11**: O sistema deve agrupar automaticamente os alunos com base no resultado do pré-teste, garantindo pelo menos um aluno com alto desempenho por grupo.
- **RF12**: O sistema deve gerar relatórios comparando a autoavaliação dos alunos com a avaliação do professor.
- **RF13**: O sistema deve disponibilizar os relatórios em até 1 hora após o término da aula 02.

---

## 🚫 Requisitos Não Funcionais (RNF)

- **RNF01**: O sistema deve estar disponível 99% do tempo em horário letivo.
- **RNF02**: O tempo de resposta das páginas de dashboard e relatórios deve ser inferior a 3 segundos.
- **RNF03**: O sistema deve ser acessível por dispositivos móveis e navegadores modernos.
- **RNF04**: Os dados dos alunos e professores devem estar protegidos conforme a LGPD.
- **RNF05**: O sistema deve possuir autenticação com diferentes níveis de permissão (professor, aluno e administrador).
- **RNF06**: O sistema deve armazenar os dados dos relatórios e interações por no mínimo 6 meses.

---

**Versão**: 1.0  
**Data**: Junho/2025  
**Autor**: Documento gerado automaticamente com base nas User Stories do projeto.
