# SIGMUN Admin — Frontend Administrativo

Aplicação administrativa do **SIGMUN** (Sistema Integrado de Gestão Municipal).
Painel mínimo para servidores: **login** e **dashboard** com verificação de
conectividade com a API.

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
npm run build      # build de produção (dist/)
npm run preview    # pré-visualiza o build de produção
```

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
│   ├── lib/api.ts     # cliente HTTP mínimo para a API
│   ├── pages/         # páginas (Login, Dashboard)
│   ├── App.tsx        # controle de sessão e navegação entre telas
│   ├── main.tsx       # bootstrap do React
│   └── index.css      # estilos globais
├── nginx.conf         # config servida no container (SPA + proxy da API)
├── index.html
├── package.json
└── vite.config.ts
```

> Os módulos de negócio (Compras, Tributos, Orçamento, etc.) aparecem como
> placeholders. A autenticação real será ligada ao endpoint de login da API
> quando disponível (`POST /api/v1/auth/login`).