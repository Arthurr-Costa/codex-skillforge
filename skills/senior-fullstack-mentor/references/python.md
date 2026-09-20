# Mentoria Python

Ensine Python por modelos: valores, referências, mutabilidade, escopo, exceções, iteradores, contexto, tipos e fronteiras de I/O.

## Decisões de qualidade

- funções pequenas com responsabilidade observável;
- nomes de domínio em vez de nomes mecânicos;
- tipos nas fronteiras e em contratos relevantes;
- exceções específicas e tratadas na camada apropriada;
- `Decimal` para valores monetários;
- timezone explícito para datas operacionais;
- context managers para recursos;
- configuração fora do código;
- logs úteis sem dados sensíveis;
- idempotência e checkpoints em lotes recuperáveis.

Explique quando uma classe representa estado e comportamento real; não transforme toda função em classe. Diferencie concorrência por threads, processos e async segundo a carga e as bibliotecas utilizadas.

Valide com as ferramentas já configuradas no projeto, como `pytest`, `ruff`, `mypy`, `bandit` e `pip-audit`. Não instale ferramentas automaticamente.
