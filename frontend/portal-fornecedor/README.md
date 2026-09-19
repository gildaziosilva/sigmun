# SIGMUN — Portal do Fornecedor

Aplicação frontend com área logada para fornecedores municipais de Camacan-BA
acompanharem licitações, empenhos e contratos.

> **Status Fase VI (2026-09-18):** fundação implementada — acompanhamento público
> de licitações (GET /api/v1/compras) e contratos (GET /api/v1/contratos);
> empenhos como placeholder até DOM-ORC/Onda 3. Tipos validados via tsc.

## Stack

- React 19 + Vite 8 + TypeScript (mesma stack do `frontend/admin`)
- Linting com oxlint
- `nginx.conf` para a imagem de produção (proxy `/api` e `/health` → `backend:8000`)

## Comandos

```bash
npm install
npm run dev      # desenvolvimento (proxy /api e /health para localhost:8000)
npx tsc -b       # checagem de tipos (usa o tsc do admin se este pacote sem node_modules)
npm run lint     # oxlint
```

## Docker

O serviço `frontend-portal-fornecedor` do `docker-compose.yml` constrói esta
imagem com `infra/docker/frontend/Dockerfile` e a expõe na porta **3002**.
