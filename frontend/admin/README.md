# SIGMUN Admin — Frontend Administrativo

Aplicação administrativa do **SIGMUN** (Sistema Integrado de Gestão Municipal).
Painel para servidores com **autenticação real** e módulos de negócio conectados à API.

## Fase VI — o que foi implementado

- **VI.1 Auth real (DOM-IDN):** login via `POST /api/v1/idn/auth/login`, token opaco em
  `sessionStorage` + `Authorization: Bearer` em todas as chamadas (`src/lib/api.ts`),
  contexto de sessão (`src/auth/AuthContext.tsx`), logout no backend e guarda de rotas
  por perfil (RBAC client-side: `admin` vê tudo, `servidor` sem acesso a Usuários).
- **VI.2 Módulos:** Compras (lista + detalhe), Fornecedores + Contratos, GDO (lista +
  detalhe, filtro de sigilo na exibição), CUM (pessoas) e IDN (usuários), com estados de
  loading/erro/vazio (`src/components/DataState.tsx`).
- **Limitação conhecida:** o backend ainda não valida o Bearer nas rotas de negócio
  (RBAC server-side pendente); o header já é enviado para compatibilidade futura.

## Tecnologias

- [React 19](https://react.dev/) + [TypeScript](https://www.typescriptlang.org/),
  híbrido do projeto (React/Vue "a definir via ADR", escolhido React pela
  consistência com o ecossistema do app móvel — React Native).
- [Vite 8](https://vitejs.dev/) — build rápido e geração de `dist/`.

## Como executar

Pré-requisitos: Node.js ≥ 20 e npm.

```bash
cd frontend/admin
npm install
npm run dev        # servidor de desenvolvimento (http://localhost:5173)
npx tsc -b         # checagem de tipos (vite build exige binding nativo; ver nota)
npm run lint       # oxlint
npm run preview    # pré-visualiza o build de produção
```

> Nota de ambiente (2026-09-18): `npm run build` (`tsc -b && vite build`) passa no
> `tsc` mas falha no `vite build` neste host por binding nativo ausente do `rolldown`
> (`Cannot find native binding ... @rolldown/binding-linux-x64-gnu`). É problema de
> `node_modules` local (bug conhecido npm/cli#4828), não do código: reinstalar com
> `rm -rf node_modules package-lock.json && npm install` ou construir via Docker
> (`infra/docker/frontend/Dockerfile`) resolve. `npx tsc -b` passa limpo (exit 0).

### Conexão com a API

- Em desenvolvimento, o Vite faz proxy de `/api` e `/health` para
  `http://localhost:8000` (backend local). Ajuste em `vite.config.ts`.
- Em produção (Docker), o `nginx.conf` repassa `/api` e `/health` para o
  serviço `backend` da rede do Docker Compose.
- Opcional: definir `VITE_API_URL` (ex.: `https://api.sigmun.gov.br`) em um
  arquivo `.env.local` para apontar para outra base.

## Estrutura

```
admin/
├── public/            # assets estáticos (favicon)
├── src/
│   ├── auth/AuthContext.tsx  # sessão real (login IDN, token, RBAC client-side)
│   ├── components/DataState.tsx  # hook useApiData + estados loading/erro/vazio
│   ├── lib/api.ts     # cliente HTTP (Bearer, ApiError, endpoints IDN/Compras/GDO/CUM)
│   ├── pages/         # Login, Dashboard + módulos (compras, gdo, cum, idn)
│   ├── App.tsx        # AuthProvider + chaveamento Login/Dashboard
│   ├── main.tsx       # bootstrap do React
│   └── index.css      # estilos globais (tabelas, badges, detalhe)
├── nginx.conf         # config servida no container (SPA + proxy da API)
├── index.html
├── package.json
└── vite.config.ts
```

> Módulos restantes das Ondas 3–4 (Tributos, Orçamento, Patrimônio, Saúde,
> Educação) seguem como próximas iterações. Upload de binários GDO,
> versionamento, tramitação e assinatura digital também evoluem após esta fundação.