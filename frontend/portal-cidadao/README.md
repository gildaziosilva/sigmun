# SIGMUN — Portal do Cidadão

Aplicação frontend de serviços digitais ao cidadão (consulta de protocolos,
emissão de certidões e serviços públicos) do município de Camacan-BA.

> **Status Fase VI (2026-09-18):** fundação implementada — consulta pública de
> protocolos (não sigilosos) via GET /api/v1/gdo/documentos, páginas de certidões
> (placeholder até DOM-TRI/Onda 3) e serviços. Tipos validados via tsc
> (vite build com mesma limitação de binding nativo do admin neste host).

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

O serviço `frontend-portal-cidadao` do `docker-compose.yml` constrói esta
imagem com `infra/docker/frontend/Dockerfile` e a expõe na porta **3001**.
