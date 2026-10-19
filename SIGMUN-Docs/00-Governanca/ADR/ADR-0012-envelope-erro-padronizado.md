# ADR-0012 — Envelope de erro padronizado com correlation_id

- **Status:** Aceito
- **Data:** 2026-10-08
- **Próxima revisão:** 2027-01-08 (trimestral)

## Contexto

A API possuía múltiplos formatos de resposta de erro diferentes entre módulos, sem padronização:
- Alguns módulos usavam `ErrorResponse` com apenas `detail: str`
- Outros não tinham schema de erro definido
- Não havia correlation_id nas respostas de erro, dificultando rastreabilidade distribuída

## Decisão

**Padronizar o formato de resposta de erro em toda a API** com:

1. **Schema unificado** em `src/shared/presentation/erros.py`:
   - `ErrorEnvelope` — envelope principal com `code`, `message`, `details`, `correlation_id`, `timestamp`
   - `ErrorResponse` — wrapper `{ "error": ErrorEnvelope }`
   - `ErrorDetail` — detalhes por campo (`field`, `issue`, `code`)
   - `ErrorCodes` — códigos categorizados (VALIDATION_ERROR, NOT_FOUND, UNAUTHORIZED, etc.)

2. **Exception handlers globais** em `src/main.py`:
   - `RequestValidationError` (422) → VALIDATION_ERROR com detalhes por campo
   - `ValidationError` (Pydantic) → VALIDATION_ERROR
   - `StarletteHTTPException` (401, 403, 404, 409) → códigos mapeados
   - `IntegrityError` (SQLAlchemy) → ALREADY_EXISTS / CONFLICT
   - `OperationalError` (SQLAlchemy) → DATABASE_ERROR (503)
   - `Exception` genérico → INTERNAL_ERROR (500) com log completo

3. **Correlation ID automático** via middleware existente (`CorrelationIDMiddleware`):
   - Header `X-Correlation-ID` propagado na resposta
   - Incluído no envelope de erro para rastreabilidade

## Exemplo de resposta

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dados de entrada inválidos",
    "details": [
      {"field": "email", "issue": "formato inválido", "code": "value_error.email"}
    ],
    "correlation_id": "550e8400-e29b-41d4-a716-446655440000",
    "timestamp": "2026-10-08T15:30:00.123456Z"
  }
}
```

## Verificação

```bash
# Testes de RBAC (incluem verificação de 401/403/404 padronizados)
.venv/bin/python -m pytest tests/integration/test_rbac_por_dominio.py -q

# Testes de contrato OpenAPI
.venv/bin/python -m pytest tests/integration/test_openapi.py -q
```

## Consequências

- **Quebra de contrato** para clientes que esperavam formatos antigos
- Todos os erros agora incluem `correlation_id` para debugging distribuído
- Códigos de erro categorizados facilitam tratamento programático no frontend

## Referências

- TODO2 T-3.2
- `src/shared/presentation/erros.py`
- `src/shared/middleware/correlation_id_middleware.py`