# Estilos, padrões e critérios de escolha

Usar esta matriz como hipótese inicial, nunca como seleção automática. Consultar [B01–B03, B08, G04–G08] na bibliografia. Separar estilo de sistema, organização interna e forma de hospedagem: podem coexistir.

| Opção | Sinal favorável | Custo ou risco | Evidência necessária |
| --- | --- | --- | --- |
| Monólito modular | Equipe pequena; fronteiras em descoberta; transações locais | Limites podem se degradar; implantação conjunta | Dependências controladas; módulos testáveis; carga suportada |
| Camadas | Fluxos previsíveis; separação técnica útil | Camadas vazias; mudanças atravessando toda a estrutura | Responsabilidade real de cada camada |
| Portas e adaptadores | Regras relevantes; entradas/saídas variantes; testes isolados | Contratos e mapeamento adicionais | Uma dependência externa cuja substituição/isolamento traga valor |
| Serviços de granularidade maior | Algumas capacidades precisam de autonomia | Chamadas remotas, contratos e operação adicionais | Limites coerentes e justificativa por capacidade |
| Microsserviços | Autonomia de equipes; escala ou ciclo de implantação distintos | Falhas parciais, dados distribuídos e coordenação | Donos definidos, entrega independente e maturidade operacional |
| Eventos | Consumidores independentes; trabalho assíncrono; propagação de fatos | Consistência atrasada, replay, contratos e diagnóstico | Tolerância a atraso; estratégia para duplicatas e mensagens inválidas |
| Pipeline | Transformações sucessivas; importação e processamento | Estado intermediário, gargalo e retomada | Contratos entre etapas e checkpoints |
| Microkernel/plugins | Núcleo estável com extensões variáveis | Compatibilidade, isolamento e ciclo das extensões | Limite claro entre núcleo e plugin |
| Serverless | Carga intermitente; eventos; gestão reduzida de servidores | Limites de execução, latência, custos e dependência do provedor | Medição representativa e documentação vigente |

Não interpretar monólito como ausência de arquitetura, nem serviço como sinônimo de módulo bem delimitado. Uma aplicação pode usar camadas internamente, eventos em alguns fluxos e uma única implantação. Serverless é uma escolha de execução que não determina o modelo de domínio.

## Antes de distribuir

Identificar o ganho específico: escalar uma capacidade, isolar uma falha, liberar uma equipe, cumprir uma restrição de localização ou reduzir um ciclo de entrega. Comparar com melhorar consultas, modularizar código ou separar um worker.

Estimar o custo do novo limite: autenticação entre serviços, versionamento, observabilidade, ambientes, pipelines, resposta a incidentes, chamadas adicionais e semântica de transações. Se persistir banco compartilhado e implantação coordenada, declarar essa dependência em vez de prometer autonomia.

Tratar a preferência por começar simples como heurística contextual, apoiada em experiência profissional; ela não prova que todo sistema deve começar como monólito. Sistemas com fronteiras maduras, equipes independentes e restrições concretas podem justificar distribuição desde o início. [G08]

## CQRS, event sourcing e mensageria

CQRS separa modelos de atualização e consulta. Não exige serviços, bancos diferentes nem event sourcing. Justificar por necessidades de leitura e escrita diferentes, e declarar como uma projeção ficará atualizada. [G05]

Event sourcing persiste mudanças como fonte de verdade para reconstruir estado. Comparar com auditoria convencional antes de adotá-lo. Considerar evolução de eventos, reconstrução, efeitos externos durante replay, correções e ciclo de vida dos dados. Uma fila de eventos não é, por si, event sourcing.

Distinguir comando (solicitação de ação) de evento (registro de fato). Escolher orquestração quando coordenação explícita e visibilidade do fluxo são importantes; considerar coreografia quando reações independentes e poucos acoplamentos de sequência tornarem o fluxo compreensível. Registrar dono do processo em ambos. [B07, G07]

## Método para decisão

1. Eliminar opções que violem restrições obrigatórias.
2. Comparar as restantes pelos cenários prioritários, incluindo manter a solução atual.
3. Identificar custo incremental, reversibilidade e hipótese mais arriscada.
4. Propor experimento discriminante e registrar o critério antes de executá-lo.
5. Escolher a opção com melhor adequação demonstrável, explicando perdas aceitas.

Exemplo original: extrair notificações de uma API pode reduzir interferência de tarefas demoradas sem separar o domínio inteiro. Um worker compartilhando a base transacional pode ser etapa suficiente. Sua fila exige tratamento de repetição, mesmo que a implantação ainda seja simples.

Não prescrever Kubernetes, Kafka, service mesh ou múltiplas regiões sem requisito correspondente. Preferir serviços gerenciados quando o ganho operacional justificar dependência e custo, comparando alternativas com dados atuais.
