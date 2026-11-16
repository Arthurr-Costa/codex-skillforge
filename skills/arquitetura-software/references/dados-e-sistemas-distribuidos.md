# Dados e sistemas distribuídos

## Definir garantias antes de mecanismos

Nomear a unidade de atomicidade, o dono das escritas, o isolamento exigido e o modelo de falhas. Distinguir consistência de réplicas, integridade de negócio e o C de ACID. Uma transação local não engloba automaticamente uma chamada HTTP. [B04]

| Conceito | Interpretação útil | Erro a evitar |
| --- | --- | --- |
| Linearizabilidade | Operações parecem instantâneas e respeitam a ordem real de operações não sobrepostas | Confundir com qualquer uso de transação |
| Serializabilidade | Resultado de transações equivale a alguma execução serial | Supor automaticamente ordem de tempo real |
| Consistência eventual | Réplicas podem convergir sob condições do protocolo e sem novas alterações | Prometer um prazo de atualização não especificado |
| Replicação | Manter cópias coordenadas dos dados | Tratar réplica como backup contra erro lógico |
| Particionamento de dados | Distribuir subconjuntos por chave ou faixa | Ignorar hotspots, resharding e consultas cruzadas |

## CAP, FLP, tempo e consenso

CAP: no modelo do teorema, uma partição impede garantir simultaneamente consistência linearizável e resposta a toda requisição em nó não falho. “Disponibilidade” nessa definição não equivale ao SLO comercial. Discutir comportamento por operação durante partições; não escolher “CA” e declarar rede infalível. [P03]

FLP: consenso determinístico em sistema completamente assíncrono, com possibilidade de uma falha por parada, não tem garantia universal de término. Não concluir que consenso prático é impossível: declarar hipóteses adicionais, mecanismos de detecção, aleatoriedade ou condições de progresso quando aplicáveis. [P05]

Relógios físicos não estabelecem causalidade de modo confiável. Em relógios de Lamport, causalidade implica aumento do valor lógico, mas o aumento não prova causalidade. Identificar se o requisito é ordem por entidade, por partição ou global. [P04]

Raft organiza consenso de log replicado por liderança, replicação e condições de segurança. Não inferir que três nós em uma única zona resistem à perda dessa zona. Não implementar consenso artesanal para uma aplicação comum; usar sistemas consolidados e verificar suas configurações e garantias. [P06]

## Corrida entre operações

Exemplo original: duas requisições leem “horário livre” e ambas inserem uma reserva. Uma validação antes da inserção é insuficiente. Procurar uma restrição no banco, escrita condicional, bloqueio ou isolamento que preserve a regra, de acordo com o banco e o modelo de horário. Testar a concorrência real e o tratamento de conflito. Não prometer equivalência de mecanismos entre SQLite, MySQL e PostgreSQL.

Para decisões sobre réplica de leitura, declarar atraso tolerável e necessidade de leitura após escrita. Para cache, definir fonte de verdade, invalidação, TTL, falha, aquecimento e risco de dados de outro usuário. Medir antes de acrescentar cache.

## Mensagens, atomicidade e repetição

Uma escrita no banco seguida de publicação pode falhar entre as duas etapas. Outbox registra estado e intenção de publicação na mesma transação; um relay publica depois. O relay ainda pode repetir mensagens. Confirmar durabilidade, retomada e monitoramento antes de afirmar entrega. [G06]

Projetar o consumidor com chave de operação estável e escopo definido. Quando possível, persistir deduplicação e efeito na mesma transação. Um conjunto em memória ou marcar “processado” antes do efeito deixa janelas de falha. Se o efeito for externo, usar idempotência do provedor ou reconciliação; uma transação local não fecha essa fronteira.

Especificar janela de deduplicação, retenção e destino de mensagens inválidas. Definir intervenção e reprocessamento para dead-letter queue; ela não resolve incidentes sozinha. Limitar concorrência e crescimento da fila, medir idade da mensagem mais antiga e proteger dependências. [B07]

Para idempotência, não reutilizar a chave para intenção ou payload diferente. Tratar concorrência entre tentativas e expiração de registros. Distinguir “mesmo resultado” de “nenhum novo efeito”. Usar os contratos reais do provedor.

## Transações entre serviços

Comparar transação local, protocolo distribuído suportado, reserva, saga e revisão da fronteira. Não declarar 2PC proibido universalmente; avaliar suporte, coordenação e comportamento sob falha.

Saga coordena transações locais e ações compensatórias. Compensação é uma nova operação de negócio, pode falhar e pode não apagar efeitos observados. Identificar estados intermediários, concorrência, etapas irreversíveis e intervenção humana. Não prometer isolamento serializável por usar saga. [G07]

Exemplo original: após autorização de cobrança, a resposta se perde. O estado é desconhecido, não necessariamente “falhou”. Consultar pelo identificador de operação e reconciliar antes de repetir uma ação que possa cobrar novamente.

## Ensaios mínimos para fluxos críticos

Planejar duplicação, mensagem fora de ordem, falha antes/depois do commit, perda de confirmação, timeout externo, queda do worker, reexecução e sobrecarga. Para cada ensaio registrar invariante, estado final esperado e como verificar efeitos externos. Executar apenas em ambiente autorizado e seguro.
