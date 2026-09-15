# SIGMUN — Portal do Cidadão

Aplicação frontend de serviços digitais ao cidadão (consulta de protocolos,
emissão de certidões e serviços públicos) do município de Camacan-BA.

> **Status:** scaffolding inicial. O desenvolvimento real está planejado na
> Fase VI do `TODO.md` (tarefa VI.3 — "Inicializar Scaffolding Real dos
> Portais Externos").

## Stack

- React 19 + Vite 8 + TypeScript (mesma stack do `frontend/admin`)
- Linting com oxlint
- `nginx.conf` para a imagem de produção (proxy `/api` e `/health` → `backend:8000`)

## Comandos

```bash
npm install
npm run dev      # desenvolvimento (proxy /api e /health para localhost:8000)
npm run build    # build de produção (dist/)
npm run lint     # oxlint
```

## Docker

O serviço `frontend-portal-cidadao` do `docker-compose.yml` constrói esta
imagem com `infra/docker/frontend/Dockerfile` e a expõe na porta **3001**.
