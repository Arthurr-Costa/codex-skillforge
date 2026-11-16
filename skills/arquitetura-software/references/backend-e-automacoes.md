# Aplicações práticas em backend e automações

Tratar estes exemplos como síntese própria de aplicação dos fundamentos. Não presumir a arquitetura de qualquer projeto real do usuário. Verificar documentação oficial e versões antes de escrever integração específica.

## Django, FastAPI e serviços web

Manter lógica de domínio fora de detalhes de transporte quando sua complexidade e reutilização justificarem. Separar validação de formato, autorização, regra de negócio e persistência. Em CRUD simples, evitar camadas que apenas repassem métodos do ORM.

Em Django, avaliar organização por capacidade/domínio, não apenas por tipo técnico. Apps não garantem isolamento: observar imports, signals, relações entre modelos e transações. Usar serviços de aplicação ou funções de caso de uso onde coordenem regras e operações; não impor repositório genérico sobre todos os QuerySets.

Usar worker para tarefas demoradas quando necessário; definir falha, repetição e visibilidade. Um callback depois do commit pode evitar execução antes da confirmação, mas não equivale a publicação durável: o processo pode cair antes da entrega. Para entrega garantida, examinar persistência de intenção e retomada. [G06]

Em APIs, documentar contrato, evolução, idempotência, paginação, limites, timeout e semântica de erro. Para integrações sujeitas a alteração, traduzir o contrato externo em modelo próprio sem espalhar payloads do fornecedor pelo domínio.

## Bancos SQL

Fazer invariantes relevantes chegarem à camada que controla concorrência: unicidade, integridade referencial e regras transacionais adequadas. Uma checagem Python antes de inserir não impede disputa entre processos.

Não generalizar comportamento de SQLite para servidor concorrente, nem nomes de níveis de isolamento entre engines. Verificar o mecanismo real. Investigar tamanho de transações, índices, locks e retries da transação inteira quando requeridos pelo banco.

Em multitenancy, testar consultas, tarefas, relatórios, exportações e caches. Não depender apenas de filtro da interface. Avaliar chaves e restrições considerando o escopo de cada organização.

## RPA, lotes e arquivos

Representar cada item por estado explícito: pendente, em execução, concluído, falha recuperável, falha definitiva ou resultado desconhecido. A categoria “resultado desconhecido” evita transformar ausência de confirmação em permissão para repetir um efeito.

Definir identidade estável de execução e de item; registrar checkpoints duráveis. Para concorrência, definir claim/lease, expiração e proteção contra worker antigo ainda ativo. Não usar apenas arquivo local de progresso quando várias máquinas disputarem itens.

Em Selenium, tratar interface externa como adaptador instável. Separar navegação da regra de negócio, usar condições observáveis e classificar falhas de sessão, seletor, indisponibilidade e rejeição funcional. Não contornar controles de acesso. Se houver API autorizada, comparar sua estabilidade e custo de integração.

Para SFTP/FTPS e importação, definir convenção de arquivo completo, integridade, duplicatas, quarentena, versão do layout e reconciliação. Não presumir que presença do arquivo implica término da escrita nem que mover/renomear é atômico em qualquer ambiente.

Exemplo original: o robô confirma um acordo e perde a sessão antes de salvar o checkpoint. Na retomada, consultar o sistema de destino pelo identificador do acordo. Repetir automaticamente só se o contrato e a evidência permitirem; caso contrário, encaminhar à reconciliação.

## Entrega enxuta sugerida

Para um serviço pequeno, avaliar primeiro aplicação modular, banco relacional, backups testados, observabilidade essencial e worker quando justificado. Definir condições observáveis de crescimento que levariam a outra opção. Isso é uma hipótese inicial econômica, não uma proibição a sistemas distribuídos.
