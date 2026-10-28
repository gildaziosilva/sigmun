# ADR-0010 — Endpoints públicos por decisão (inventário explícito)

- **Status:** Aceito
- **Data:** 2026-10-06
- **Próxima revisão:** 2027-01-06 (trimestral) — ou antes, se qualquer rota
  desta lista passar a expor dado pessoal ou dado sigiloso.
- **Contexto:** A Fase 2 (T-2.2a/2b/2c) aplicou autenticação às 431 rotas dos
  20 módulos-alvo, mas não existia inventário do que permanece anônimo **por
  decisão** (TODO2 T-2.3). Sem esse inventário, uma rota nova sem auth entra
  em produção sem passar por revisão de segurança.
- **Decisão:** apenas as rotas listadas abaixo podem responder sem
  autenticação. Qualquer outra rota sem dependência de auth é **regressão** e
  falha o verificador (`scripts/verificar_rotas_publicas.py`, exit 1).
- **Verificação (deve bater exatamente — diff ADR x varredura):**
  ```bash
  .venv/bin/python scripts/verificar_rotas_publicas.py
  # OK — 7 rotas publicas batem exatamente com o ADR-0010.
  ```

## Inventário (7 rotas)

| # | Método | Caminho | Domínio | Justificativa |
|---|--------|---------|---------|---------------|
| 1 | POST | `/api/v1/idn/auth/login` | DOM-IDN | Login legacy: impossível exigir token antes de emitir token. |
| 2 | POST | `/api/v1/idn/auth/login/jwt` | DOM-IDN | Login JWT: mesma razão (porta de entrada da autenticação). |
| 3 | POST | `/api/v1/idn/auth/refresh` | DOM-IDN | Renovação valida o refresh token do corpo — não há sessão prévia. |
| 4 | POST | `/api/v1/idn/auth/logout` | DOM-IDN | Logout é idempotente e seguro sem sessão (invalida o próprio token). |
| 5 | POST | `/api/v1/idn/auth/logout/jwt` | DOM-IDN | Idem — variante JWT. |
| 6 | GET | `/health` | Infra | Healthcheck do orquestrador (liveness), sem dado de negócio. |
| 7 | GET | `/` | Infra | Raiz do serviço (redirect/informativo), sem dado de negócio. |

## Fora do alcance desta lista

- **`/docs`, `/redoc`, `/openapi.json`** — rotas de framework do FastAPI,
  não são handlers do domínio; a superfície de exposição do OpenAPI é
  controle de ambiente (T-3.3).
- **`POST /api/v1/ouvidoria/denuncias`** — permite anônimo, mas **tem**
  dependência (`UsuarioOpcional`/hybrid_optional) com validação de anonimato
  por RN-OUV-002; portanto não aparece na varredura "sem auth".
- **Rotas `GET` com `UsuarioOpcional`** — identidade é capturada quando há
  token; anonimato permitido por padrão de leitura (regra T-2.2) e coberto
  pelo contrato do ADR-0009.

## Consequências

1. Escritas administrativas do DOM-IDN (`/api/v1/idn/usuarios*`) deixaram de
   ser anônimas e agora exigem papel `admin` (`exigir_papeis("admin")`,
   T-2.2/regra de escrita). O usuário inicial vem do seed
   (`src/modules/sigmun_idn/infrastructure/database/seeds.py`).
2. Toda rota pública nova exige (a) entrada nesta tabela e (b) atualização de
   `ESPERADAS` em `scripts/verificar_rotas_publicas.py` — revisão de segurança
   obrigatória.
3. Se a revisão trimestral identificar dado pessoal em rota 1–11, a rota
   migra para `UsuarioOpcional`/`UsuarioObrigatorio` e sai desta lista.

- **Referências:** TODO2 T-2.2 (regra por rota), T-2.3; ADR-0007; ADR-0009.

> **Nota de revisão (2026-10-27):** As 11 rotas GET anteriormente listadas como
públicas (itens 1–11 da versão anterior) foram removidas desta lista porque
  o código atual as protege com `exigir_papeis("gestor", "admin", "compras")`
  ou `exigir_papeis("gestor", "admin", "cadastro")`, exigindo autenticação e
  autorização por papel. A correção é factual: alinha o inventário ao
  comportamento atual do código. A decisão de torná-las públicas no futuro
  exige análise funcional, de dados e de segurança específica.
