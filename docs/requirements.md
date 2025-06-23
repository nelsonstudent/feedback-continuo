# Lista Consolidada de Requisitos para o SIAS

Requisitos Funcionais (RF)

📚 Para Professores

RF01: Permitir upload de materiais (PDF/HTML + links de vídeo) com definição de prazo de disponibilidade
RF02: Configurar pré-testes com 3 alternativas por questão ("Sei e posso ensinar", "Sei mas não posso ensinar", "Não sei")
RF03: Visualizar dashboard com % acesso a materiais, satisfação média (1-5) e mapa de dúvidas
RF04: Avaliar desempenho dos alunos (participação, domínio do tema) com integração a dados de pré-teste
RF05: Exportar relatórios CSV com dados de alunos, feedbacks, sentimentos e notas

👨‍🎓 Para Alunos

RF06: Acessar materiais de aula (textos/vídeos) até 48h antes da aula
RF07: Marcar materiais como "concluídos" com sincronização imediata
RF08: Realizar pré-testes com temporizador de 1 minuto e 3 alternativas por questão
RF09: Enviar feedbacks com emoji + comentário opcional (≤500 palavras) e opção de anonimato
RF10: Avaliar aulas com nota 1-5 e formulário Likert integrado

⚙ Técnicos / Sistema

RF11: Agrupar alunos automaticamente (1 mentor/grupo, máximo 5 alunos) baseado em pré-testes
RF12: Processar sentimentos e extrair keywords de comentários usando NLP
RF13: Calcular métricas de satisfação (média, mediana, desvio) em tempo real
RF14: Gerar relatórios cruzados (autoavaliação × avaliação professor) em ≤1h pós-aula

Requisitos Não Funcionais (RNF)

🚫 Segurança e Conformidade

RNF01: Autenticação JWT com validação de permissões (aluno/professor) e expiração em 24h
RNF02: Criptografia AES-256 para dados em trânsito e repouso (conformidade LGPD/GDPR)
RNF03: Anonimização opcional de dados sensíveis e exclusão automática após 6 meses

⚡ Performance e Disponibilidade

RNF04: Tempo resposta API <200ms, dashboards <3s sob carga de 500 usuários concorrentes
RNF05: Disponibilidade ≥99.9% em horário letivo (7h-22h) com monitoramento ativo
RNF06: Escalabilidade horizontal com microsserviços e balanceamento automático de carga

📱 Experiência do Usuário

RNF07: Responsividade em dispositivos móveis (≥320px) e navegadores modernos (Chrome, Firefox, Safari)
RNF08: Interface intuitiva com feedback visual imediato para ações críticas (upload, avaliações)
=======

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
