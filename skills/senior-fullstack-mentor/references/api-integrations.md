# Mentoria de APIs e integrações

## Contrato

Ensine recurso, método, status, schema, erro, paginação, versionamento e compatibilidade. Validação de entrada e autorização devem acontecer no servidor.

## Falhas distribuídas

Toda integração deve considerar timeout, retry limitado, backoff, rate limit, indisponibilidade, resposta inválida, duplicação e estado parcial.

Explique quando usar idempotency key, checkpoint, deduplicação, fila, webhook assinado ou compensação. Não faça retry automático de operações não idempotentes sem estratégia explícita.

## SFTP e arquivos

Considere conexão, host key, autenticação, diretório remoto, arquivos parciais, codificação, atomicidade, confirmação e reprocessamento. Não exponha credenciais ou caminhos sensíveis.

## Evidência

Separe contrato documentado, tráfego observado, hipótese e comportamento validado. Não inferir endpoints de escrita a partir de uma consulta isolada.
