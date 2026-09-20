# Autorrevisão do desenvolvedor

## Intenção

- Consigo explicar o problema sem depender da implementação?
- Minha mudança permanece dentro do escopo?
- O fluxo principal está claro?

## Correção

- Validei entradas e casos de borda relevantes?
- Preservei contratos e dados existentes?
- Tratei falhas na camada responsável?
- Considerei estado parcial, repetição e concorrência quando aplicável?

## Segurança

- Autorização ocorre no servidor?
- Entradas não confiáveis são tratadas com segurança?
- Queries e comandos evitam concatenação insegura?
- Logs e respostas não expõem segredos ou dados pessoais?

## Testes

- Existe teste que falharia sem a mudança?
- Testei o caminho principal e a falha mais importante?
- Sei dizer exatamente quais comandos foram executados?

## Operação

- A mudança pode ser observada e diagnosticada?
- Existe rollback ou recuperação proporcional ao risco?
- Configuração, migrations e dependências estão explícitas?

## Aprendizado

- Consigo justificar a abordagem escolhida?
- Qual alternativa descartei e por quê?
- O que eu faria se volume, contrato ou ambiente mudasse?
