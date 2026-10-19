# ADR-0011 — Convenção única de paginação (page base 1, page_size=20)

- **Status:** Aceito
- **Data:** 2026-10-08
- **Próxima revisão:** 2027-01-08 (trimestral)

## Contexto

A auditoria de 2026-10-04 (TODO2 T-3.1) identificou **três convenções** convivendo na mesma API:

| Padrão | Ocorrências | Problema |
|--------|-------------|----------|
| `page: int = 0` + `page_size: int = 50` | 92 | Base 0 confunde clientes humanos; `page=1` retorna "fora da página" |
| `page: int = 1` + `page_size: int = 20` | 91 | **Já é a convenção desejada** |
| `offset: int = 0` | 19 | Baixo nível; vaza detalhe de implementação SQL |

Um cliente paginante quebra silenciosamente ao cruzar módulos: `page=1` significa "primeira página" em 91 rotas e "fora da página" em 92.

## Decisão

**Padronizar em `page: int = 1` (base 1) + `page_size: int = 20` (máx 100).**

- `page=1` → primeira página (intuitivo para humanos e clientes REST)
- `page_size` padrão 20, limite superior 100 (protege contra DoS acidental)
- Offset 0-based (`(page-1)*page_size`) fica **interno** ao repository/SQL, não exposto na API

## Implementação

Criado módulo compartilhado: `src/shared/presentation/paginacao.py`

Exports:
- `ParametrosPaginacao` — query params de entrada (`page`, `page_size`)
- `Pagina[T]` — response padronizada (`items`, `page`, `page_size`, `total`, `total_pages`, `has_next`, `has_prev`)
- `criar_pagina(items, params, total)` — factory helper
- `PaginaRequest` — alias semântico para `Depends()` em endpoints

## Migração (pode ser incremental, módulo a módulo)

1. Importar: `from src.shared.presentation.paginacao import ParametrosPaginacao, Pagina, criar_pagina`
2. Substituir parâmetros soltos por `params: ParametrosPaginacao = Depends()`
3. No use case/repository: usar `params.offset()` e `params.limit()` para SQL
4. Retornar `criar_pagina(items, params, total)`

## Verificação

```bash
# Não deve haver mais ocorrências dos padrões antigos
grep -rnE "page: int = 0|offset: int = 0" src/modules --include=*.py   # alvo: 0
# Testes de contrato OpenAPI passam
.venv/bin/python -m pytest tests/integration/test_openapi.py -q
```

## Consequências

- **Quebra de contrato** para clientes que usavam `page=0` nas 92 rotas antigas. Comunicar via changelog e versão da API.
- Endpoints com `offset` (19 rotas) migram para `page`/`page_size` — mais semântico.
- `page_size` máximo 100 evita consultas pesadas acidentais.

## Referências

- TODO2 T-3.1
- `src/shared/presentation/paginacao.py`