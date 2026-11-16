# Qualidade, desempenho e operação

## Cenários verificáveis

Substituir adjetivos como “rápido”, “seguro” ou “escalável” por critérios observáveis. Especificar fonte, estímulo, ambiente, elemento, resposta e medida; priorizar com stakeholders. Usar QAW para elicitação de cenários, sem chamar uma conversa individual de workshop formal. [B02, P10]

Exemplos originais, sempre sujeitos a validação do usuário:

| Qualidade | Cenário ilustrativo | Verificação |
| --- | --- | --- |
| Desempenho | Na carga de referência acordada, 95% das consultas respondem em até 400 ms | Teste representativo e medição ponta a ponta |
| Recuperação | Após perda do banco primário, restaurar com RPO de 15 min e RTO de 2 h | Ensaio de restauração cronometrado |
| Modificabilidade | Alterar regra de elegibilidade sem modificar o adaptador de integração | Revisão do diff e testes de regra/contrato |
| Isolamento | Usuário de uma empresa não acessa registros de outra | Casos positivos e negativos em API, jobs e exportações |

RPO limita a perda de dados tolerada; RTO define o tempo de recuperação almejado. Backup existente não demonstra restauração possível. Não adotar esses números sem confirmação.

## SLI, SLO e capacidade

Definir indicador (SLI), meta e janela (SLO), população medida e exclusões. Separar compromisso contratual (SLA). O orçamento de erros é a fração permitida pelo objetivo; sua política precisa ser acordada, não inferida apenas do número. Percentual por requisições e disponibilidade por tempo são medidas diferentes. [B10]

Investigar latências de cauda, além de médias: fan-out e recursos saturados podem ampliar atrasos raros. Não somar percentis de etapas como se fossem latência total. Medir o caminho crítico com carga e distribuição plausíveis. [P08]

Para estimativas, escrever unidade, fórmula, premissas e intervalo. Exemplo original: 120 requisições/s com permanência média de 0,25 s implicam aproximadamente 30 requisições simultaneamente no sistema, se o fluxo for estável, pela relação de Little. Isso não determina quantidade de workers: incluir CPU, I/O, pool de conexões, fila e contenção. Não confundir média com pico nem estimativa com benchmark. [P07]

Verificar plano de consulta, volume, índices, seletividade, N+1, contenção e payload antes de propor sharding. Distinguir escala vertical, horizontal e capacidade útil. Réplicas não tornam escrita ilimitada.

## Tolerância a falhas e sobrecarga

Definir deadlines e timeouts por caminho; limitar tentativas, adicionar backoff e jitter e evitar repetição amplificada por várias camadas. Repetir somente operações cuja semântica permita; timeout não confirma ausência de efeito. Escolher valores com a distribuição de latência e a tolerância a falsos timeouts. [G09]

Decidir onde aplicar isolamento de recursos, limite de concorrência, backpressure, descarte de carga e circuit breaker. Uma fila desacopla chegada e processamento, mas não cria capacidade. Estabelecer prioridade e tratamento de backlog. Verificar se fallback entrega resultado válido ou encobre erro de negócio.

## Segurança e privacidade como propriedades

Mapear ativos, identidades e limites de confiança; especificar autenticação, autorização por ação/recurso, separação entre organizações, gestão de segredos e exposição de dados. Escolher requisitos pertinentes do ASVS e fixar versão ao referenciá-los; a versão consultada nesta pesquisa é 5.0.0. [G11]

Incluir logs, mensagens, backups e exportações na análise de dados sensíveis. Não reduzir segurança a HTTPS/JWT. Uma revisão arquitetural identifica riscos e necessidades de verificação, mas não certifica segurança nem conformidade legal. Quando for necessária auditoria especializada, encaminhar para o fluxo apropriado e manter a análise arquitetural proporcional.

## Observabilidade e responsabilidade

Definir sinais de sucesso do negócio, erros, latência e saturação. Relacionar IDs de correlação a logs/traces sem registrar segredos. Controlar cardinalidade e retenção. Toda política de recuperação precisa de dono e procedimento executável.

Testar inicialização, graceful shutdown, jobs em andamento e dependências indisponíveis. Distinguir endpoint de saúde do processo de prontidão para receber tráfego. Validar configuração no ambiente real sem presumir equivalência com desenvolvimento.

## Economia e operação sustentável

Comparar custo de computação, banco, rede, observabilidade, redundância e trabalho humano. Incluir aprendizado, plantão, manutenção, migração e saída do fornecedor. Consultar preços e quotas oficiais no momento da decisão, informando região, moeda e data.

Usar AWS e Azure Well-Architected como lentes de revisão contextualizadas, sem tornar o catálogo do provedor uma obrigação. Relacionar confiabilidade, segurança, desempenho, custo e operação; reduzir desperdício e retenção desnecessária quando compatível com requisitos. [G12, G13]
