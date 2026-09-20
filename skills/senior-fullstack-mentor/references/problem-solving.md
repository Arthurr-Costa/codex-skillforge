# Resolução de problemas

## Enquadramento

Antes do código, defina:

- estado atual;
- estado desejado;
- diferença observável;
- entradas e saídas;
- restrições;
- responsáveis pelo comportamento;
- evidência de conclusão.

## Decomposição

Trace o caminho principal e depois as bordas:

```text
entrada -> validação -> regra -> estado -> saída -> registro operacional
```

Para cada etapa, pergunte:

- quem é responsável;
- o que pode falhar;
- como a falha aparece;
- como distinguir causas concorrentes;
- como testar sem afetar dados reais.

## Estratégia

Prefira o menor experimento que elimina uma hipótese relevante. Não altere várias camadas antes de descobrir onde o comportamento diverge.

Quando houver alternativas, compare adequação ao projeto, complexidade, custo de operação, reversibilidade e capacidade da equipe. Recomende uma, sem esconder a principal desvantagem.
