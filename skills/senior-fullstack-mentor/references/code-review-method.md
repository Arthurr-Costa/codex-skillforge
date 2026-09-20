# Revisão de código como mentoria

## Ordem da revisão

1. intenção e contrato;
2. correção funcional;
3. integridade de dados;
4. segurança;
5. concorrência e falhas;
6. testes;
7. legibilidade e manutenção;
8. performance comprovável;
9. operação e rollback.

## Severidade

- **Bloqueador:** perda de dados, vulnerabilidade explorável, contrato quebrado ou falha provável em produção.
- **Importante:** defeito, cobertura insuficiente de risco ou manutenção seriamente prejudicada.
- **Melhoria:** simplificação ou clareza sem impedir a entrega.

Cada apontamento deve indicar localização, cenário, consequência e forma de comprovar a correção.

## Pedagogia

Reconheça decisões corretas. Para um problema relevante, primeiro pergunte como o usuário espera que o código se comporte no cenário de falha. Dê uma pista antes da solução completa. Ao final, peça que ele resuma a regra aprendida.

Não reescreva o estilo pessoal quando o código já é claro e consistente com o projeto.
