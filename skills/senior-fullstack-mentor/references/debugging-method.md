# Método de depuração

## Disciplina

Não comece corrigindo. Primeiro reproduza e localize.

1. Registre comportamento esperado e observado.
2. Obtenha mensagem, stack trace, status, entrada redigida e ambiente.
3. Descubra a primeira camada em que o estado diverge.
4. Liste hipóteses que explicam todos os sintomas.
5. Escolha uma observação que diferencie as hipóteses.
6. Faça o menor teste seguro.
7. Corrija a causa, não apenas o sintoma.
8. Crie um teste de regressão.

## Ensinar durante o diagnóstico

Peça ao usuário que preveja o resultado antes de executar o teste. Depois compare previsão e evidência. Explique o significado da divergência.

Não trate ausência de log como prova de ausência de execução. Considere processo errado, cache, configuração, ambiente, tratamento silencioso e observabilidade incompleta.

## Erros externos

Para banco, rede ou integração, separe DNS, conexão, TLS, autenticação, autorização, contrato, rate limit, timeout, resposta inválida e persistência local. Cada categoria exige uma evidência diferente.
