Lista Consolidada de Requisitos para o SIAS

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
