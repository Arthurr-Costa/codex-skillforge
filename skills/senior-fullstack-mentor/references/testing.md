# Mentoria de testes

Teste é uma hipótese executável sobre comportamento.

## Escolha

- unidade para regras puras e casos de borda;
- integração para banco, framework e serviços;
- contrato para fronteiras externas;
- ponta a ponta para jornadas críticas;
- regressão para reproduzir um defeito corrigido.

## Estrutura

Ensine contexto, ação e resultado. Prefira nomes que descrevem comportamento. Controle tempo, aleatoriedade, rede e estado compartilhado.

Peça ao usuário que preveja qual teste falhará antes da correção. Um teste útil deve falhar pelo motivo esperado e passar depois da mudança.

Não use apenas quantidade ou cobertura como qualidade. Avalie cenários, assertivas, isolamento e capacidade de detectar regressão. Não afirme sucesso sem comando, exit code e saída relevante.
