# ADR-0013 — openapi.json versionado com gate de diff (breaking changes)

- **Status:** Aceito
- **Data:** 2026-10-08
- **Próxima revisão:** 2027-01-08 (trimestral)

## Contexto

A API não tinha versionamento formal do contrato OpenAPI. Mudanças breaking eram descobertas apenas em produção quando clientes quebravam.

## Decisão

**Versionar o openapi.json a cada release e impor gate de diff no CI:**

1. **Geração versionada** (`scripts/gerar_openapi.py`):
   - Gera `openapi/v{VERSION}/openapi.json` com metadados (timestamp, versão)
   - Mantém `openapi/latest/` como symlink/cópia da versão mais recente
   - Versão derivada de tag git (`git describe --tags`) ou timestamp

2. **Diff gate** (`scripts/diff_openapi.py`):
   - Compara versão nova com `latest` (versão anterior)
   - Detecta breaking changes:
     - Path/operação removida
     - Parâmetro removido
     - Request body removido ou tornado obrigatório
     - Response removida
     - Schema removido ou propriedade/required removida
     - Valores de enum removidos
     - Requisitos de segurança aumentados
   - Non-breaking (apenas aviso):
     - Path/operação/schema/parâmetro adicionado
     - Propriedade adicionada
     - Response adicionada
     - Versão alterada

3. **CI Integration** (`.github/workflows/ci.yml`):
   - Job `openapi` roda após `test` passar
   - Gera versão, faz diff contra `latest`, falha se breaking changes
   - Upload do artefato `openapi/` como artifact (retention 30 dias)

## Verificação

```bash
# Local: gerar versão e testar diff
python scripts/gerar_openapi.py --version 1.0.0
python scripts/diff_openapi.py --base openapi/latest/openapi.json --head openapi/v1.0.0/openapi.json

# CI: job 'openapi' executa automaticamente
```

## Consequências

- **Breaking changes bloqueiam merge** — exige versionamento semântico consciente
- Histórico completo de contratos preservado em `openapi/v*/`
- Clientes podem consumir versão específica via `openapi/v1.0.0/openapi.json`

## Referências

- TODO2 T-3.3
- `scripts/gerar_openapi.py`
- `scripts/diff_openapi.py`
- `.github/workflows/ci.yml` (job `openapi`)