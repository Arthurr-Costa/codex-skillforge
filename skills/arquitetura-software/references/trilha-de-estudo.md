# Trilha de aprendizagem orientada a entregas

Adaptar a duração ao usuário; não prometer domínio profissional em prazo fixo. Começar por perguntas e exercícios curtos para calibrar experiência. Usar fontes abertas quando possível; indicar livros como aprofundamento, sem exigir aquisição.

| Etapa | Conteúdo e fontes | Entrega prática | Critério de domínio |
| --- | --- | --- | --- |
| 1. Fundamentos | B01, B02, P01, P02, G14 | Mapa de responsabilidades de uma aplicação conhecida | Explicar arquitetura versus descrição e identificar duas fronteiras justificadas |
| 2. Qualidades | P10, B10 | Três cenários mensuráveis com prioridades | Trocar adjetivos vagos por teste observável e discutir conflito |
| 3. Domínio | B05, B06, G04 | Modelo de domínio e contratos entre módulos | Distinguir entidade, agregado, contexto e unidade de implantação |
| 4. Estilos | B01, B08, G08 | Comparação entre duas arquiteturas para o mesmo problema | Justificar custos, perdas e condição de revisão |
| 5. Dados | B04, P03–P06, G15 | Experimento de concorrência e relatório de falhas | Preservar invariante e explicar limite das garantias |
| 6. Integração | B07, G05–G07, G09 | Fluxo assíncrono com repetição e reconciliação | Demonstrar efeito de duplicata e resposta perdida |
| 7. Documentação | G01–G03, G16 | Vistas suficientes e dois ADRs | Outra pessoa consegue explicar a decisão e localizar evidência |
| 8. Evolução | B03, B09, P09, G10–G13 | Plano incremental e uma verificação arquitetural | Definir corte, compatibilidade, risco e recuperação |

## Ensinar um conceito

Apresentar definição curta, exemplo concreto, contraponto e pergunta de transferência. Distinguir o que a fonte demonstra do que é uma recomendação contextual. Propor exercício pequeno e revisar a justificativa, não apenas o resultado.

Exercícios originais:

- Modularidade: alterar formato de importação sem alterar regra de elegibilidade. Comparar dependências antes e depois.
- Qualidade: explicar por que “escalável” não define aceitação; propor cenário com carga, ambiente e métrica.
- Consistência: reproduzir duas reservas concorrentes; identificar onde proteger a exclusividade.
- Distribuição: simular confirmação perdida e decidir se é seguro repetir.
- Evolução: migrar um contrato de API com consumidores de duas versões coexistindo.
- Avaliação: argumentar a favor da alternativa rejeitada e identificar o que faria a decisão mudar.

## Projeto integrador

Usar um domínio pequeno com regras reais, como reservas, processamento de pedidos ou importação de arquivos. Elaborar contexto, requisitos, decisão inicial, um fluxo crítico, falhas e plano de evolução. Só distribuir componentes se houver uma necessidade demonstrável no exercício.

Avaliar compreensão em quatro dimensões: precisão conceitual, justificativa contextual, evidência e capacidade de explicar consequências. Não aprovar uma proposta apenas porque contém DDD, eventos ou microsserviços.
