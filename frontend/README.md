# SIGMUN Frontend

Aplicações frontend do SIGMUN, organizadas por portais.

## Estrutura

```
frontend/
├── admin/              # Aplicação administrativa (servidores)
├── portal-cidadao/     # Portal do cidadão (serviços digitais)
└── portal-fornecedor/  # Portal do fornecedor
```

## Tecnologias

- **Framework:** React + Vite + TypeScript (conforme `frontend/admin`, portais do cidadão e do fornecedor)
- **Estilização:** Tailwind CSS ou Bootstrap
- **Acessibilidade:** WCAG 2.1 AA
- **Responsividade:** Mobile-first

## Execução local

Cada aplicação tem seu próprio `package.json` em `frontend/<app>`. O `package.json` na raiz do repositório
expõe atalhos (sem dependências — apenas delegam via `npm --prefix`):

```bash
# Na raiz do repositório (sigmun-v1/sigmun-v1/):
npm run dev:admin        # Vite do admin      → http://localhost:5173 (ou próxima porta livre)
npm run dev:cidadao      # Vite do cidadão    → http://localhost:5173+
npm run dev:fornecedor   # Vite do fornecedor → http://localhost:5173+

npm run test:frontend    # Vitest dos 3 apps
npm run lint:frontend    # oxlint dos 3 apps

# Ou diretamente no app:
cd frontend/portal-cidadao && npm install && npm run dev
```

O dev server do Vite faz proxy de `/api` e `/health` para `http://localhost:8000` (backend).

> As portas **3000/3001/3002** são as portas Docker (nginx). Para desenvolvimento use os Vite acima.

## Padrões

Cada aplicação frontend deve seguir:
- Responsividade
- Acessibilidade (acessibilidade)
- Modularidade
- Orientação a permissões

## Referências

- [Arquitetura de Software - Frontend](../../SIGMUN-Docs/01-Arquitetura-Corporativa/004-Arquitetura-de-Software.md)
- [Arquitetura de Experiência do Usuário](../../SIGMUN-Docs/01-Arquitetura-Corporativa/009-Arquitetura-de-Experiencia-do-Usuario-e-Acessibilidade.md)
