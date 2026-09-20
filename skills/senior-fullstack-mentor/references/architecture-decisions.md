# Decisões de arquitetura

Arquitetura é gestão de consequências, não seleção de padrões populares.

## Perguntas essenciais

- Qual capacidade precisa mudar?
- Que volume, sensibilidade e disponibilidade são reais?
- Quem manterá a solução?
- Que contratos não podem quebrar?
- Qual falha é aceitável?
- Como observar, recuperar e reverter?

## Comparação

Avalie alternativas por simplicidade, acoplamento, consistência, latência, custo operacional, segurança, testabilidade, reversibilidade e aderência à equipe.

Comece com a solução mais simples que satisfaz requisitos conhecidos. Extraia serviço, fila, cache ou abstração somente quando houver uma pressão concreta.

Registre decisões relevantes no modelo `assets/technical-decision-template.md`. Inclua contexto, opções, escolha, consequências e gatilhos para revisão futura.
