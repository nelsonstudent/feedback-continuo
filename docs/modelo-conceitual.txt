Visão Geral do Fluxo da Plataforma
Pré-Aula (Aula 00):
Professor disponibiliza materiais (textos, vídeos).
Alunos consomem e sinalizam compreensão.
Aula Presencial (Aula 01):
Plataforma divide grupos automaticamente com base no pré-teste ("Sei e posso ensinar", "Não sei", etc.).
Debate guiado entre alunos.
Aula Expositiva (Aula 02):
Professor explica tópicos com base nas lacunas identificadas.
Pós-Aula:
Alunos avaliam a aula (objetivos de aprendizagem).
Professor avalia desempenho dos alunos.
Plataforma gera relatório cruzado (feedback para ambos).

Funcionalidades do MVP (Priorizadas)
1. Para Professores
Upload de Materiais Pré-Aula:
Textos (PDF/HTML) + links de vídeos (YouTube, Vimeo).
Prazo para consumo (ex.: "Disponível até 48h antes da aula").
Formulário de Pré-Teste:
3 opções de resposta:
"Sei e posso ensinar" → Grupo de "mentores".
"Sei, mas não posso ensinar" → Grupo intermediário.
"Não sei" → Grupo de dúvidas.
Auto-agrupamento: Divisão equilibrada dos alunos em grupos.
Dashboard de Métricas:
% de alunos que consumiram materiais.
Mapa de dúvidas (palavras-chave).
Avaliação Pós-Aula:
Formulário para avaliar alunos (ex.: "Participação", "Domínio do tema").
Relatório comparativo: "Desempenho vs. Autoavaliação dos alunos".
2. Para Alunos
Visualização de Materiais:
Interface simples (lista de textos + vídeos).
Marcar como "Concluído".
Pré-Teste:
Responder ao form antes da aula (1 minuto).
Avaliação da Aula:
Escala Likert (ex.: "A aula ajudou a entender o tema? 1-5").
Campo aberto para feedback qualitativo.
3. Funcionalidades Técnicas
Algoritmo de Agrupamento:
Lógica simples (ex.: distribuir 1 "mentor" por grupo).
Relatório Automatizado:
Cruzar dados:
Autoavaliação do aluno (pré-teste) × Avaliação do professor.
Feedback dos alunos × Objetivos da aula.

Ferramentas Sugeridas
Frontend: React.js (simplicidade + componentes reutilizáveis).
Backend: Node.js + Express (para forms e relatórios).
Banco de Dados: PostgreSQL (estrutura relacional para cruzar dados).
Deploy: Vercel (frontend) + Heroku (backend).

Critérios de Aceite (Exemplo)
Pré-Aula:
80% dos alunos consomem materiais antes do prazo.
Autoagrupamento:
Grupos com no máximo 5 alunos e pelo menos 1 "mentor".
Relatório:
Gerado em até 1h após a aula 02.
