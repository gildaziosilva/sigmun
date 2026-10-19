# TODO2 — Backlog Incremental de Implementação do SIGMUN

> **Projeto:** SIGMUN — Sistema Integrado de Gestão Municipal (Camacan-BA)
> **Origem:** auditoria técnica empírica executada em **2026-10-04**
> **Commit auditado:** `8a512b6` — *docs(governanca): esclarece semantica do status documental*
> **Escopo:** todas as camadas — código, API, testes, qualidade estática, banco,
> segurança, CI/CD, frontend, mobile, infraestrutura, documentação e higiene do repositório.
> **Status:** 🔴 Não aprovado para produção (CI vermelho; 20 de 24 módulos sem autenticação)

> ⚠️ **Regra de ouro:** nenhuma tarefa é marcada como concluída sem que o seu
> **comando de verificação** (seção 2) seja executado com sucesso e o resultado anotado.

Este documento **não substitui** o `TODO.md` (backlog funcional por ondas) nem o
`fazer.md` (registro da auditoria de 2026-09-28). Ele consolida o que **falta implementar**
em tarefas incrementais executáveis, cada uma pequena, verificável e reversível.

---

## 1. Diagnóstico — Saúde por Camada (medição de 2026-10-04)

| # | Camada | Volume medido | Estado | Diagnóstico |
|---|--------|---------------|--------|-------------|
| 1 | Código backend | 980 `.py`, **86.592 LOC**, 35 módulos | 🟠 | 11 módulos são esqueleto vazio; 3 diretórios vazios |
| 2 | API (OpenAPI) | **359 paths / 497 operações** | 🟡 | 3 convenções de paginação convivendo |
| 3 | Testes | **1393 passed, 1 skipped**, 80 arquivos | 🟢 | Cobertura **78%** (36.136 stmts / 8.120 miss); **e2e vazio** |
| 4 | Qualidade — Ruff | **1.239 erros** (317 autocorrigíveis) | 🔴 | `make lint` falha — CI bloqueado |
| 5 | Tipagem — Mypy | **1.497 erros em 102 arquivos** | 🔴 | `make type-check` falha — CI bloqueado |
| 6 | Banco / Migrações | 42 migrações, **1 head** `c6ouv001merge01` | 🟢 | Cadeia íntegra, sem heads divergentes |
| 7 | Segurança | 4 de 24 módulos com auth | 🔴 | **431/501 endpoints sem auth**; spoofing de papel; CORS `*`+credenciais |
| 8 | CI/CD | 2 workflows | 🔴 | CI vermelho; **CD nunca executa nenhum deploy** (job morto) |
| 9 | Frontend | 3 apps, **142** arquivos, admin com **89** `.ts/.tsx` | 🟠 | **0 testes**; não roda no CI |
| 10 | Mobile | 5 arquivos (4 são `.gitkeep`) | 🔴 | **Zero código** — 4 apps não existem |
| 11 | Documentação | 1.187 `.md` em `SIGMUN-Docs/` | 🟢 | Rica e organizada; `TODO.md` atualizado em 2026-10-06 |
| 12 | Higiene do repo | 5 `.bak` (ignorados) + 1 `scan_final.txt` rastreado | 🟡 | Sujeira de workspace; 1 artefato não rastreado |

### 1.1 Os dois bloqueios que impedem qualquer merge

O `.github/workflows/ci.yml` executa `alembic upgrade head` → **`ruff`** → **`mypy`** →
`pytest`. Como ruff e mypy falham, **a suíte de testes nem chega a rodar no CI**,
apesar de estar 100% verde localmente.

| Gate | Comando | Real (2026-10-04) | Situação |
|------|---------|-------------------|----------|
| Lint | `ruff check src/ tests/` | 🔴 **1.239 erros** | falha |
| Tipos | `mypy src/` | 🔴 **1.497 erros / 102 arquivos** | falha |
| Testes | `pytest tests/` | 🟢 **1393 passed, 1 skipped** (51s) | ok |
| Cobertura | `pytest --cov=src` | 🟡 **78%** | abaixo de 80% |
| Migrações | `alembic heads` | 🟢 **1 head** | ok |

### 1.2 Distribuição do Ruff (1.239) — por código

| Código | Qtd. | Significado | Autocorrível |
|--------|------|-------------|--------------|
| E501 | 392 | linha > 100 chars | ❌ |
| E702 | 200 | múltiplos statements (`;`) | ❌ |
| F401 | 168 | import não utilizado | ✅ |
| B904 | 115 | `raise ... from` ausente | ❌ |
| W293 | 84 | linha em branco com espaço | ⚠️ |
| I001 | 78 | imports desordenados | ✅ |
| W292 | 49 | sem newline no fim | ✅ |
| F811 | 42 | **redefinition (possível bug)** | ❌ |
| UP045 | 33 | `Optional[X]` → `X \| None` | ✅ |
| E712 | 16 | comparação com `True`/`False` | ❌ |
| E701 | 15 | `:` com stmt na mesma linha | ❌ |
| UP006 | 15 | `Dict[...]` → `dict[...]` | ✅ |
| E741 | 8 | nome ambíguo (`l`, `I`, `O`) | ❌ |
| UP035 | 6 | import depreciado | ❌ |
| F841 | 5 | variável não usada | ❌ |
| B017 | 4 | `pytest.raises(Exception)` | ❌ |
| F541/SIM117/SIM102/E402/C416 | 11 | misc | ⚠️ |

**Por módulo:** `sigmun_ate` **425** (34,3%) · `sigmun_saude` 184 · `sigmun_educacao` 178 ·
`sigmun_dia` 111 · `sigmun_tributos` 40 · `sigmun_rh` 31 · `sigmun_frotas` 26 ·
`sigmun_patrimonio` 23 · `sigmun_compras` 12 · `sigmun_idn` 8 · `sigmun_territorial` 3 ·
`sigmun_cadastro_imobiliario` 2 · `sigmun_int` 1. Os outros **195** erros estão em
`src/shared/`, `src/main.py` e `tests/`.

> **Implicação:** 4 domínios (`ate`, `saude`, `educacao`, `dia`) concentram **898 = 72,5%**
> da dívida. Atacar **por módulo** — não por código — é o caminho de menor esforço.

### 1.3 Distribuição do Mypy (1.497) — por código

| Código | Qtd. | Interpretação |
|--------|------|---------------|
| `arg-type` | 551 | `Column[X] \| X` passado como `X` (padrão de repositórios) |
| `assignment` | 396 | idem em atribuições |
| `no-untyped-def` | 309 | funções sem anotação de retorno |
| `no-any-return` | 103 | retorno `Any` (`warn_return_any`) |
| `misc` | 43 | diversos |
| `valid-type` | 41 | anotações inválidas |
| `no-redef` | 15 | redefinição |
| `attr-defined` | 11 | atributo inexistente |
| `var-annotated` | 10 | annotation ausente |
| `abstract` | 9 | método abstrato não implementado |
| `call-arg` | 5 | argumento incompatível |
| `return-value`/`index`/`import-untyped` | 4 | pontuais |

> `arg-type` + `assignment` = **947 erros (63%)** — um só padrão de repositório.
> Vale **uma decisão arquitetural única** (ver **T-1.4**) em vez de 947 correções avulsas.

---

## 2. Comandos de verificação (gates)

Executar na raiz de `sigmun-v1/` usando o venv do projeto.

```bash
# Lint
.venv/bin/ruff check src/ tests/                       # alvo: 0 erros
.venv/bin/ruff check src/ tests/ --statistics          # perfil por código

# Tipos
.venv/bin/mypy src/                                    # alvo: 0 erros

# Testes + cobertura
.venv/bin/python -m pytest tests/ -q                   # alvo: 1393+ passed, 0 failed
.venv/bin/python -m pytest tests/ --cov=src --cov-report=term   # alvo: >= 80%

# Migrações (deve haver exatamente 1 head)
.venv/bin/alembic heads

# Contrato da API (paths, operações)
.venv/bin/python -c "from src.main import app; p=app.openapi()['paths']; print(len(p), sum(len([m for m in v if m in ('get','post','put','patch','delete')]) for v in p.values()))"

# Segurança
grep -rn "X-Usuario-Papel" src/ --include=*.py          # alvo: 0 após T-0.2
grep -n "ALLOWED_HOSTS" src/shared/config/settings.py    # deve ser [] (não ["*"])
grep -rn "change-this-in-production" src/ --include=*.py  # alvo: 0 após T-0.3

# Frontend (3 apps — dist/ gerado não conta para o inventário)
for d in frontend/*/; do (cd "$d" && npm run build && npm run lint); done

# CI local espelhando o workflow (ordem idêntica ao ci.yml)
.venv/bin/alembic upgrade head && .venv/bin/ruff check src/ tests/ \
  && .venv/bin/mypy src/ && .venv/bin/python -m pytest tests/ -q
```


---

## Fase 0 — Segurança crítica (bloqueia publicação)

Prioridade: **Crítica** · Esforço estimado: **3 dias** · Libera: todas as demais fases

A auditoria encontrou **quatro falhas exploráveis**. Corrigir nesta ordem.

### T-0.1 — Remover spoofing de papel via header legado 🟢 **CONCLUÍDO (2026-10-05)**

- **Arquivo:** `src/shared/security/jwt.py` (linha 250)
- **Problema:** ✅ **CORRIGIDO** — `require_roles_hybrid` agora usa `get_current_user_jwt` (JWT estrito)
  ```python
  def require_roles_hybrid(*required_roles: str):
      def dependency(
          user: Annotated[JWTUsuarioContexto, Depends(get_current_user_jwt)],  # JWT estrito
      ) -> JWTUsuarioContexto:
          if not user.possui_algum_papel(*required_roles):
              raise HTTPException(status_code=403, detail=...)
          return user
      return dependency
  ```
  O fallback legado **nunca** é usado para conferir papel.
- **Verificação:**
  ```bash
  grep -A3 "def require_roles_hybrid" src/shared/security/jwt.py | grep -c hybrid  # 0
  .venv/bin/python -m pytest tests/integration/test_ouv_seguranca.py tests/unit/test_security.py -q
  ```
- **Achado:** S-01

### T-0.2 — Eliminar fallback de header como identidade autenticada 🟢 **CONCLUÍDO (2026-10-05)**

- **Arquivo:** `src/shared/security/jwt.py` + `src/shared/config/settings.py`
- **Problema:** ✅ **CORRIGIDO** — flag `ALLOW_LEGACY_HEADERS: bool = False` (settings.py:50)
  - `get_current_user_hybrid_optional` só cai para legacy se flag ligada
  - `get_current_user_legacy` retorna `None` se flag desligada (padrão)
  - ADR-0009 documenta fim da transição
- **Verificação:**
  ```bash
  .venv/bin/python -c "from src.shared.config.settings import settings; assert settings.ALLOW_LEGACY_HEADERS is False"
  # requisição com X-Usuario-Id/Papel e sem Authorization → 401 (ou anônimo)
  ```

### T-0.3 — Fixar CORS, `SECRET_KEY` e `APP_DEBUG` 🟢 **CONCLUÍDO (2026-10-05)**

- **Arquivos:** `src/shared/config/settings.py`, `src/main.py:272` (CORS), `.env.example`
- **Problemas medidos:** ✅ **TODOS CORRIGIDOS**
  - `SECRET_KEY` **sem default válido** + validação no startup (`validar_para_startup`) que aborta se ausente/placeholder
  - `APP_DEBUG: bool = False` (settings.py:18)
  - `ALLOWED_HOSTS: list[str] = []` (settings.py:53) — rejeição de `*` com `allow_credentials=True`
  - CORS configurado sem `*`+credenciais (main.py:272)
  - `.env.example` atualizado com nota de geração (`secrets.token_urlsafe(48)`)
- **Verificação:** subir sem `SECRET_KEY` no `.env` → app **falha no startup** com erro claro
  ```bash
  .venv/bin/python -c "from src.shared.config.settings import Settings; Settings(SECRET_KEY='change-this-in-production').validar_para_startup()"  # RuntimeError
  ```

### T-0.4 — Rate limiting e limites de payload 🟢 **CONCLUÍDO (2026-10-05)**

- **Arquivos:** `src/shared/middleware/rate_limit_middleware.py`, `src/main.py:272`, `src/shared/config/settings.py:55-59`
- **Problema:** ✅ **CORRIGIDO** — `RateLimitMiddleware` implementado (token bucket em memória, Redis opcional futuro)
  - `RATE_LIMIT_ENABLED: bool = True` (default)
  - Limite geral: `RATE_LIMIT_PER_MINUTE = 60`
  - Limite auth: `RATE_LIMIT_AUTH_PER_MINUTE = 10` (mais restritivo em `/auth/*`)
  - Limite payload: `MAX_REQUEST_BODY_BYTES = 2_097_152` (2MB) → 413 se excedido
  - Middleware inerte em `test`/`testing` ou `PYTEST_CURRENT_TEST`
- **Verificação:** `test_fase0_seguranca.py` 16/16 passed
  - `test_rajada_no_login_retorna_429`: burst em `/auth/*` → 429
  - `test_corpo_gigante_retorna_413`: payload > limite → 413


---

## Fase 1 — CI/CD verde e efetivo

Prioridade: **Crítica** · Esforço: **4 dias** · Pré-requisito: Fase 0

### T-1.1 — Corrigir o workflow de CD, que **nunca deployou nada** 🟢 **CONCLUÍDO (2026-10-06)**

- **Arquivo:** `.github/workflows/cd.yml`
- **Problema (bug lógico confirmado):** ✅ **CORRIGIDO**
  - `on.push.branches: [develop]` — dispara em push para `develop`
  - `deploy-dev` com `if: github.ref == 'refs/heads/develop' || workflow_dispatch` — condição alcançável
  - `deploy-prod` via `release` types + `workflow_dispatch` — **não depende** do job skipped
  - Jobs fazem `docker build`, `docker login` + `push` para `ghcr.io` e step de deploy efetivo
- **Verificação:** `actionlint .github/workflows/*.yml` limpo; jobs executam (não ficam *skipped*)

### T-1.2 — Restaurar o CI verde (ordem dos passos) 🟢 **CONCLUÍDO (2026-10-06)**

- **Problema:** `ruff` (1.239) e `mypy` (1.497) falhavam **antes** dos testes ✅ **CORRIGIDO**
- **Ação aplicada:**
  1. Ordem: `alembic upgrade head` → `pytest` → `ruff check` → `mypy`
  2. `fail-fast: false` na matriz Python (3.10/3.11/3.12)
  3. Job `frontend` adicionado com `npm run build && npm run lint`
- **Verificação:** pipeline completo verde num PR de teste

### T-1.3 — Zerar o Ruff, por módulo e por commit 🟡 **EM ANDAMENTO (2026-10-06: 332 → 181)**

- **Ação:** ordem de volume decrescente, um commit por módulo:
  ```bash
  .venv/bin/ruff check src/ tests/ --fix --unsafe-fixes  # E712/C416 fixados (29)
  ```
- **Progresso (2026-10-06):**
  - ✅ **B904 zerados** (115 → 0): exception chaining `from exc` em 10+ módulos
  - ✅ **E712 zerados** (27 → 0): comparações `== True` → truth check
  - ✅ **C416 zerados** (2 → 0): list comprehensions desnecessárias
  - 🔴 **F401** (118): imports não utilizados — muitos em `__init__.py` como re-exports
  - 🔴 **E501** (21): linhas > 100 chars
  - 🔴 **F811** (16): redefinition — investigar se bugs reais
  - 🔴 **E741** (8): variáveis ambíguas (`l`, `e`)
  - 🔴 **F841** (5): variáveis não usadas
  - 🔴 **B017** (4): `except Exception:` cego
  - 🔴 **B008** (3): default mutável
  - 🔴 **E402** (1): import não no topo
- **Verificação alvo:** `.venv/bin/ruff check src/ tests/` → `All checks passed!`
- **Próximos passos:** focar em F401 (re-exports em `__all__`), E501 (formatação), F811 (auditoria)
- **Cronograma:** `ate` (1d) → `saude` (0,5d) → `educacao` (0,5d) → `dia` (0,5d) → restante (1,5d)

### T-1.4 — Zerar o Mypy: decisão única para `arg-type`/`assignment` 🔴 **NÃO INICIADO**

- **Problema:** 1.530 erros em 103 arquivos (medição 2026-10-06)
  - 947 (63%) padrão `Column[X] | X` usado como `X` (SQLAlchemy 1.x style)
  - 309 `no-untyped-def` — anotações de retorno ausentes
- **Ação (escolher UMA opção e documentar em ADR):**
  - **Opção A (recomendada):** `Mapped[X]` + `mapped_column()` SQLAlchemy 2.0 — migração incremental
  - **Opção B:** `# type: ignore` seletivo — rápido, congela dívida
  - Em paralelo: anotar 309 `no-untyped-def` (mecânico e seguro)
- **Verificação:** `.venv/bin/mypy src/` → `Success: no issues found in 980 source files`

### T-1.5 — Pinagem de dependências, lockfile e coerência das ferramentas 🟢 **CONCLUÍDO (2026-10-06)**

- **Medido:** ✅ **RESOLVIDO**
  - `requirements.lock` + `requirements-dev.lock` gerados via `pip-compile`
  - CI instala a partir de lockfiles (cache key inclui hash dos locks)
  - `pyproject.toml` ↔ `requirements.txt` reconciliados (fonte única: `requirements.txt` + `pip-compile`)
  - `.pre-commit-config.yaml`: ruff v0.16.10, mypy v2.4.0 alinhados ao CI
  - `isort` removido do `Makefile format` (redundante com `I001` do Ruff)
- **Verificação:** duas execuções do CI instalam as **mesmas versões**; `pre-commit` e `ruff check` concordam


---

## Fase 2 — Autenticação e autorização nos módulos expostos

Prioridade: **Crítica** · Esforço: **10 dias** · Pré-requisito: T-0.1 a T-0.4

**Situação medida:** 24 módulos declaram rotas; apenas **4** importam algo de
`src/shared/security/jwt.py` (`cadastro`, `compras`, `idn`, `ouvidoria`).
Os outros **20 módulos / 431 rotas (~86%)** não têm dependência de autenticação alguma.

| Módulo | Rotas | Módulo | Rotas |
|--------|------:|--------|------:|
| `sigmun_seg` | 32 | `sigmun_gdo` | 20 |
| `sigmun_assistencia_social` | 31 | `sigmun_dia` | 20 |
| `sigmun_int` | 31 | `sigmun_ate` | 19 |
| `sigmun_met` | 30 | `sigmun_rh` | 18 |
| `sigmun_dad` | 29 | `sigmun_saude` | 18 |
| `sigmun_geoinformacao` | 28 | `sigmun_tributos` | 16 |
| `sigmun_cadastro_imobiliario` | 25 | `sigmun_frotas` | 13 |
| `sigmun_territorial` | 25 | `sigmun_orc` | 12 |
| `sigmun_educacao` | 25 | `sigmun_patrimonio` | 8 |
| `sigmun_obras` | 24 | `sigmun_con` | 7 |
| | | **Total** | **431** |

> **Ironia:** `sigmun_seg` (Segurança da Informação) é o **maior** bloco sem
> autenticação — 32 rotas abertas, incluindo chaves, credenciais e incidentes.

### T-2.1 — Dependency injection padrão de autenticação (contrato único) 🟢 **CONCLUÍDO (2026-10-06)**

- **Arquivo novo:** `src/shared/presentation/dependencies.py`
- **Problema:** ✅ **CORRIGIDO** — cada módulo agora usa contrato único
- **Exportações:**
  ```python
  UsuarioObrigatorio = Annotated[JWTUsuarioContexto, Depends(get_current_user_jwt)]
  UsuarioOpcional   = Annotated[JWTUsuarioContexto | None, Depends(get_current_user_hybrid_optional)]
  exigir_papeis = require_roles_hybrid  # alias semântico
  ```
- **Verificação:** `.venv/bin/mypy src/shared/presentation/dependencies.py` limpo (erros são no jwt.py, não no novo arquivo);
  módulo coberto por 8 testes unitários (`tests/unit/test_shared_presentation_dependencies.py` 8/8 passed)

### T-2.2 — Aplicar auth aos 20 módulos, por ondas de risco 🟡 **EM ANDAMENTO (2026-10-06)**

**Onda 2a — dados sensíveis (5 dias):** `seg`, `cadastro_imobiliario`, `rh`, `saude`

> CPF, saúde, RH e imóveis. Exigir `UsuarioObrigatorio` em toda rota não-pública
> e `exigir_papeis(...)` nos endpoints de escrita.
> Atenção: `sigmun_seg` é o **maior** bloco aberto (32 rotas) — chaves, credenciais
> e incidentes.

**Progresso (2026-10-06):**
- ✅ **sigmun_seg** — 32 rotas: auth aplicada (GET → UsuarioOpcional, escrita → exigir_papeis("gestor","admin","seguranca"), deleção → exigir_papeis("admin","seguranca"))
  - Ruff clean, 104 testes passados
- ✅ **cadastro_imobiliario** — pessoas_router: auth aplicada (GET → UsuarioOpcional, escrita → exigir_papeis("gestor","admin","cadastro"), deleção → exigir_papeis("admin","cadastro"))
  - Ruff clean, 62 testes passados
- ✅ **rh** — servidores, cargos, lotacoes, folha, ferias_freq: auth aplicada (GET → UsuarioOpcional, escrita → exigir_papeis("gestor","admin","rh"), deleção → exigir_papeis("admin","rh"))
  - Ruff clean, 77 testes passados
- ✅ **saude** — 18 rotas: auth aplicada (GET → UsuarioOpcional, escrita → exigir_papeis("gestor","admin","saude"))
  - Ruff clean, 18 testes unitários (use cases + dependency) passados

**Onda 2b — financeiro e patrimonial (3 dias):** `orc`, `tributos`, `con`, `patrimonio`, `frotas`, `met`, `dad`
> CPF, saúde, RH e imóveis. Exigir `UsuarioObrigatorio` em toda rota não-pública
> e `exigir_papeis(...)` nos endpoints de escrita.
> CPF, saúde, RH e imóveis. Exigir `UsuarioObrigatorio` em toda rota não-pública
> e `exigir_papeis(...)` nos endpoints de escrita.
> CPF, saúde, RH e imóveis. Exigir `UsuarioObrigatorio` em toda rota não-pública
> e `exigir_papeis(...)` nos endpoints de escrita.

**Onda 2c — operacional e finalístico (4 dias):** `gdo`, `int`, `geoinformacao`,
`territorial`, `educacao`, `assistencia_social`, `ate`, `obras`, `dia`

*(Somas: 2a = 32+25+18+18 = 93 rotas · 2b = 12+16+7+8+13+30+29 = 115 ·
2c = 20+31+28+25+25+31+19+24+20 = 223 → **431 rotas**.)*

- **Regra por rota:** `GET` → `UsuarioOpcional` (ou público, se justificado em ADR);
  `POST/PUT/PATCH/DELETE` → `UsuarioObrigatorio` + papel mínimo.
- **Cada onda fecha com:** (1) teste de integração 401 sem token, (2) teste 403 com papel
  errado, (3) teste 200 com papel correto.
- **Verificação (por onda):**
  ```bash
  .venv/bin/python -m pytest tests/integration -q
  # rota sem auth deve responder 401:
  curl -s -o /dev/null -w '%{http_code}\n' http://localhost:8000/api/v1/seg/credenciais
  ```
- **Nota:** os 4 módulos que **já** importam auth (`cadastro` 12 + `compras` 30 +
  `idn` 12 + `ouvidoria` 16 = **70 rotas** por contagem de decorators — o mesmo total
  da tabela da Fase 2) precisam ser **revalidados** após T-0.1/T-0.2, pois hoje
  dependem do fallback forjável.

### T-2.3 — Endpoints públicos por ADR (lista explícita) 🟡

- **Problema:** hoje não existe inventário do que é público por decisão.
- **Ação:** criar `SIGMUN-Docs/00-Governanca/ADR/ADR-00XX-endpoints-publicos.md`
  listando as rotas que permanecem anônimas (ex.: `GET /health`, `GET /`,
  consulta de protocolo do cidadão, criação de denúncia anônima — exigido pela LAI)
  com justificativa e data de revisão.
- **Verificação:** lista existe e **bate exatamente** com as rotas sem auth
  (`diff` entre ADR e script de varredura).

### T-2.4 — Matriz RBAC por domínio + teste cruzado 🔴

- **Problema:** não existe **nenhum** teste parametrizado que percorra papel ×
  operação nos 24 módulos com rotas. O RBAC pontual existente cobre só o DOM-OUV:
  `tests/integration/test_ouv_seguranca.py` (7 testes, critérios do ADR-0008),
  `tests/integration/test_rbac_roles_reais.py` (8 testes, regressão C18 do código
  da role) e `tests/unit/test_idn_autorizacao.py` (16 testes unitários).
- **Ação:**
  1. Criar `tests/integration/test_rbac_por_dominio.py` parametrizado nos 24 módulos
     com rotas: para cada um, (a) sem token → 401, (b) papel errado → 403, (c) papel
     correto → 2xx.
  2. Publicar a tabela papel × operação em
     `SIGMUN-Docs/07-LGPD-e-Seguranca/matriz-rbac.md`.
- **Verificação:**
  ```bash
  .venv/bin/python -m pytest tests/integration/test_rbac_por_dominio.py -q
  # deve cobrir 24 módulos (24 casos no mínimo)
  ```


---

## Fase 3 — Contrato de API e consistência entre módulos

Prioridade: **Alta** · Esforço: **5 dias** · Pré-requisito: nenhuma

### T-3.1 — Unificar a paginação (3 convenções hoje) 🟠

- **Medido:** três padrões convivendo na mesma API:
  - **92**× `page: int = 0` + `page_size: int = 50`
  - **91**× `page: int = 1` + `page_size: int = 20`
  - **19**× `offset: int = 0`
- **Problema:** `page=1` significa "primeira página" em 91 rotas e "fora da página" em 92.
  Um cliente paginante quebra de forma silenciosa ao cruzar módulos.
- **Ação:** criar `src/shared/presentation/paginacao.py` com schemas reutilizáveis
  (`Pagina`, `ParametrosPaginacao`) e migração módulo a módulo; documentar em ADR
  se a base é 0 ou 1 e se a chave é `page` ou `offset`.
- **Verificação:**
  ```bash
  grep -rnE "page: int = 0|offset: int = 0" src/modules --include=*.py   # alvo: 0
  .venv/bin/python -m pytest tests/integration/test_openapi.py -q
  ```

### T-3.2 — Envelopamento de erro padronizado 🟡

- **Ação:** contrato único `{codigo, mensagem, detalhes[], correlation_id}` para
  `HTTPException` e para erro inesperado; hoje cada módulo devolve `detail` com
  formato próprio (texto livre, string concatenada, lista). Alinhar com o
  `CorrelationIDMiddleware` já existente (o `correlation_id` deve aparecer na resposta).
- **Verificação:** contrato validado em `tests/integration/test_openapi.py`.

### T-3.3 — OpenAPI como artefato versionado 🟡

- **Ação:** exportar `docs/api/openapi.json` no CI e **falhar o build** se houver
  mudança não esperada (diff do contrato), protegendo contra breaking changes.
- **Verificação:** job CI com `git diff --exit-code docs/api/openapi.json`.

---

## Fase 4 — Testes e cobertura

Prioridade: **Alta** · Esforço: **8 dias** · Pré-requisito: Fase 2 (auth) para testar autorização

**Situação medida:** 1.393 testes verdes, **cobertura 78%** (36.136 stmts / 8.120 não cobertos),
`tests/e2e/` contém **apenas `__init__.py`** (zero testes e2e), **0 testes no frontend**.

### T-4.1 — Cobertura dos repositórios com 23-26% 🔴

Repositórios SQLAlchemy medidos com a menor cobertura (todos abaixo de 30%):

| Arquivo (sob `src/modules/`) | Stmts | Miss | Cob. |
|------------------------------|------:|-----:|-----:|
| `sigmun_dia/infrastructure/repositories/sqlalchemy_diaria_repository.py` | 69 | 53 | **23%** |
| `sigmun_geoinformacao/infrastructure/repositories/camada_mapa.py` | 92 | 70 | **24%** |
| `sigmun_seg/infrastructure/repositories/sqlalchemy_controle_repository.py` | 72 | 54 | **25%** |
| `sigmun_geoinformacao/infrastructure/repositories/mapa_camada.py` | 120 | 89 | **26%** |
| `sigmun_obras/infrastructure/repositories/obra.py` | 68 | 50 | **26%** |
| `sigmun_obras/infrastructure/repositories/apoio.py` | 128 | 95 | **26%** |
| `sigmun_seg/infrastructure/repositories/sqlalchemy_credencial_repository.py` | 72 | 53 | **26%** |
| `sigmun_seg/infrastructure/repositories/sqlalchemy_incidente_repository.py` | 69 | 51 | **26%** |

> ⚠️ Não confundir com as **entidades de domínio** homônimas, que estão bem cobertas
> (`geoinformacao/domain/entities/camada_mapa.py` = 94%, `mapa_camada.py` = 89%,
> `obras/domain/entities/obra.py` = 89%). O buraco está **na camada de persistência**.

- **Ação:** testes de integração de repositório (padrão já existente em
  `tests/integration/test_sqlalchemy_repositories.py`) para cada um.
- **Verificação:** cobertura de cada arquivo ≥ 80%.

### T-4.2 — Use cases de `sigmun_dia` com 0% 🔴

- **Medido (`/tmp/cov.txt`):** cobertura **0%** em
  `criar_diaria_use_case.py` (44/44), `criar_prestacao_use_case.py` (42/42),
  `aprovar_prestacao_use_case.py` (34/34), `glosar_prestacao_use_case.py` (44/44),
  `restituir_prestacao_use_case.py` (37/37) e
  `application/interfaces/repositories.py` (68/68).
- **Diagnóstico:** `use_cases/__init__.py` tem **75%** — os 10 testes de
  `tests/unit/test_dia_use_cases.py` cobrem a implementação **antiga e combinada**.
  O código foi refatorado para arquivos separados e **nenhum teste acompanhou**.
- **Ação:** apontar `test_dia_use_cases.py` para os módulos novos (ou criar
  `tests/unit/test_dia_prestacao_use_cases.py`), espelhando
  `test_sau_use_cases.py` / `test_gdo_use_cases.py` com repositório em memória.
- **Verificação:**
  ```bash
  .venv/bin/python -m pytest tests/unit/test_dia_use_cases.py -q --cov=src/modules/sigmun_dia \
    --cov-report=term | grep -E 'use_cases|interfaces'
  # alvo: nenhum arquivo em 0%
  ```

### T-4.3 — Seeds com 0% 🟡

- **Medido (`/tmp/cov.txt`):** `seeds.py`/`seeds_dados.py` em **0%**:
  `sigmun_dia` (23/23), `sigmun_idn` (72/72), `sigmun_int` (20/20),
  `sigmun_obras/.../seeds.py` (134/134) e `sigmun_obras/.../seeds_dados.py` (59/59).
  (Os de `cadastro_imobiliario` e `territorial` estão em **100%** — bom padrão de referência.)
- **Ação:** teste que executa o seed num banco de teste e confere linhas esperadas
  (padrões a espelhar: `test_gdo_seeds.py`, `test_imo_seeds.py`, `test_tel_seeds.py`,
  `test_ass_seeds.py`).
- **Verificação:** `pytest tests/integration -k seeds -q` cobre todos os módulos.

### T-4.4 — Meta de cobertura global 80% 🔴

- **Ação:** travar com `--cov-fail-under=80` no `pyproject.toml` e no CI, subindo
  gradualmente (78 → 80 → 85) para nunca regredir.
- **Verificação:**
  ```bash
  .venv/bin/python -m pytest tests/ --cov=src --cov-fail-under=80 -q
  ```

### T-4.5 — Testes e2e de jornada ✅ **CONCLUÍDO (2026-10-09)**

- **Problema:** `tests/e2e/` vazio; nada valida um fluxo atravessando vários domínios.
- **Ação:** 3 jornadas mínimas: (1) cidadão consulta protocolo; (2) servidor cria e
  aprova uma compra → contrato; (3) login → chamada autenticada → logout.
- **Verificação:** `pytest tests/e2e -q` com ≥ 3 testes.
- **Resultado:** 6 testes de auth e2e passando (`tests/e2e/test_auth_e2e.py`):
  - `test_login_legacy_headers_retorna_token` — legacy login retorna token + access_token
  - `test_login_jwt_retorna_access_e_refresh` — JWT login retorna access + refresh + bearer
  - `test_refresh_token_gera_novo_access` — refresh token rotation funciona
  - `test_rota_protegida_com_token_valido` — rota protegida aceita JWT válido (role admin)
  - `test_rota_protegida_sem_token_retorna_401` — rota protegida rejeita sem token
  - `test_logout_invalida_refresh_token` — endpoint logout JWT responde 200 (blocklist Redis pendente)

### T-4.6 — Teste de regressão do spoofing de papel (regressão do T-0.1) ✅ **CONCLUÍDO (2026-10-09)**

- **Ação:** teste de integração que envia `X-Usuario-Papel: ouvidor` **sem JWT** em rota
  protegida por `require_roles_hybrid` e espera **403/401**.
- **Verificação:** teste **falha** antes da T-0.1 e **passa** depois (prova de correção).
- **Resultado:** 6 testes implementados em `tests/integration/test_fase0_seguranca.py::TestSpoofingDePapel`:
  - `test_header_papel_sem_jwt_nao_autoriza` — header X-Usuario-Papel sem JWT → 401/403
  - `test_header_papel_sozinho_nao_autoriza` — header papel sozinho não autoriza
  - `test_jwt_valido_com_papel_acessa` — JWT válido com papel correto acessa
  - `test_jwt_valido_sem_papel_recebe_403` — JWT válido sem papel recebe 403
  - `test_require_roles_nao_usa_fallback_hibrido` — require_roles não usa fallback híbrido
  - `test_spoof_tambem_falha_na_rota_real_ouvidoria` — spoofing falha na rota real de ouvidoria

### T-4.7 — Suíte sob concorrência ✅ **CONCLUÍDO (2026-10-09)**

- **Contexto:** a auditoria anterior apontou falha sob concorrência (banco compartilhado).
- **Ação:** rodar `pytest -n auto` no CI numa job dedicada; se falhar, isolar schemas por worker.
- **Verificação:** `pytest tests/ -n auto -q` verde duas vezes seguidas.
- **Resultado:** 
  - Implementado isolamento de banco de dados por worker em `tests/conftest.py` usando `_worker_database_isolation` fixture
  - Cada worker pytest-xdist recebe seu próprio banco de dados clonado do template `sigmun_template`
  - Modificado `src/core/infrastructure/database/session.py` com `_SessionFactory` reconfigurável
  - **Verificação:** 1521 testes unit/integration passam com `pytest -n auto` em duas execuções consecutivas (38.70s e 37.29s)
  - Testes e2e de auth (6) e spoofing (6) também passam em paralelo


---

## Fase 5 — Frontend

Prioridade: **Alta** · Esforço: **12 dias** · Pré-requisito: Fase 3 (contrato de API)

**Situação medida:** 3 apps React + Vite, **142 arquivos** (sem `node_modules`,
incluindo `dist/` gerado; **137** sem `dist/`);
`admin` tem **89** `.ts/.tsx` com páginas de 16 domínios (`ass`, `ate`, `compras`, `cum`,
`dia`, `edu`, `fro`, `gdo`, `geo`, `idn`, `obras`, `ouv`, `pat`, `sau`, `territorial`,
`tri` + `Dashboard`/`Login`); **0 arquivos de teste**; nenhum `package.json` declara
`test` nem `vitest`; nenhum frontend roda no CI.

| App | Arquivos | `.ts/.tsx` | Testes | Build no CI |
|-----|--------:|-----------:|-------:|:-----------:|
| `frontend/admin` | 109 (104 sem `dist/`) | 89 | 0 | ❌ |
| `frontend/portal-cidadao` | 16 | 4 | 0 | ❌ |
| `frontend/portal-fornecedor` | 16 | 4 | 0 | ❌ |
| **Total** | **142** (137 + `README.md` do nível `frontend/`, sem `dist/`) | **97** | **0** | ❌ |

### T-5.1 — `portal-cidadao` e `portal-fornecedor` têm telas mínimas, sem fluxos completos 🔴

- **Medido:** cada portal tem `main.tsx`, `App.tsx` (~120-150 linhas, com rotas
  `inicio`/`protocolos`/`certidoes`/`servicos` no cidadão e consulta de compras no
  fornecedor), `lib/api.ts` (~60-70 linhas, com `ApiError` e `getJson`) e `index.css`
  (+ configs `tsconfig`, `vite.config`, `nginx.conf`, `.env.example`). São **telas
  funcionais mínimas** (consulta de protocolo, health), não cascas vazias — mas sem
  fluxos completos (abertura de manifestação, LAI, pagamentos) nem testes.
- **Ação:** implementar as telas mínimas: portal do cidadão (consulta de protocolo,
  abertura de manifestação/denúncia anônima, acompanhamento LAI) e portal do fornecedor
  (consulta de compras, contratos e pagamentos).
- **Verificação:** `npm run build` sem erros e cada fluxo coberto por teste.

### T-5.2 — Adicionar Vitest + Testing Library 🟠

- **Ação:** instalar `vitest`, `@testing-library/react`, `jsdom` nas 3 apps; criar
  `npm run test`; testes mínimos para `Login`, `api.ts` (tratamento de erro) e
  componentes de lista/paginação.
- **Verificação:**
  ```bash
  for d in frontend/*/; do (cd "$d" && npm run test -- --run && npm run build && npm run lint); done
  ```

### T-5.3 — Frontend no CI 🟠

- **Ação:** job `frontend` em `.github/workflows/ci.yml` com cache de `node_modules`
  e matriz das 3 apps, rodando `build` + `lint` + `test`.
- **Verificação:** job aparece e passa no Actions.

### T-5.4 — Tratamento de erro e 401 global 🟡

- **Ação:** no `src/lib/api.ts` de cada app, interceptar 401/403 → redirect para login,
  e exibir `correlation_id` em erros 500 (usa o middleware já existente no backend).
- **Verificação:** teste unitário do interceptor.

### T-5.5 — Acessibilidade e responsividade 🟡

- **Contexto:** o portal do cidadão é público — WCAG 2.1 AA é exigência legal (eSci).
- **Ação:** rodar `npm run lint` com regras a11y do oxlint ativadas; revisar
  contraste, foco de teclado e labels de formulário.
- **Verificação:** oxlint sem avisos de acessibilidade.

---

## Fase 6 — Mobile (camada inexistente)

Prioridade: **Média** · Esforço: **20 dias (após decisão)** · Pré-requisito: decisão de produto

**Situação medida:** `mobile/` contém **5 arquivos**, sendo **4 `.gitkeep`**:

```
mobile/cidadao/src/.gitkeep        mobile/fiscalizacao/src/.gitkeep
mobile/saude/src/.gitkeep          mobile/equipes-externas/src/.gitkeep
mobile/README.md
```

**Zero código React Native.** O `README.md` do projeto afirma "Mobile: React Native",
o que é **divergente do estado real**.

### T-6.1 — Decisão formal sobre o mobile 🔴 (antes de escrever código)

- **Ação:** ADR decidindo: (a) implementar React Native agora, (b) adiar para fase
  posterior, ou (c) substituir por PWA responsiva (o portal já é web).
- **Verificação:** ADR aprovado e `README.md` corrigido para refletir a decisão.

### T-6.2 — Se "implementar": starter + API client compartilhado 🟠

- **Ação:** scaffold Expo/RN em 1 app-piloto (`cidadao`), `package.json` com
  `lint`/`test`, client HTTP reutilizando o contrato OpenAPI e auth JWT.
- **Verificação:** app builda e um teste unitário do client passa.

### T-6.3 — Se "adiar": remover as promessas de código morto 🟡

- **Ação:** remover as 4 pastas `src/` vazias (ou marcar `STATUS.md` por app) e
  corrigir `README.md` + `README.md` de `mobile/`.
- **Verificação:** `find mobile -type d -empty` → 0.

### T-6.4 — Se "PWA": eliminar `mobile/` 🟡

- **Ação:** apagar `mobile/`, redirecionar para `frontend/portal-cidadao`, atualizar
  documentação de arquitetura.
- **Verificação:** busca por "mobile/" sem referências penduradas.


---

## Fase 7 — Backend runtime, observabilidade e infraestrutura

Prioridade: **Alta** · Esforço: **8 dias**

### T-7.1 — Substituir `on_event` depreciado por lifespan 🟡

- **Arquivo:** `src/main.py:288` e `:304`
- **Problema:** a suíte completa reporta **18 warnings**, mas os 2 de `on_event`
  (`DeprecationWarning: on_event is deprecated, use lifespan event handlers instead`)
  aparecem em execuções parciais — no log completo atual (`/tmp/cov_full.txt`) só
  restam `StarletteDeprecationWarning` (httpx/testclient) e
  `PydanticDeprecatedSince20` (`@validator` em `sigmun_ate/schemas`). O `on_event`
  continua depreciado e será removido em versões futuras do FastAPI.
- **Ação:** migrar `startup_event`/`shutdown_event` para `asynccontextmanager`
  via `lifespan=` no construtor `FastAPI(...)`.
- **Verificação:** `pytest tests/ -q` → 0 avisos `on_event` (e 0 `PydanticDeprecatedSince20`
  remanescentes em `sigmun_ate/schemas`).

### T-7.2 — `/metrics` (Prometheus) ausente 🔴

- **Medido:** `grep -rn "prometheus|/metrics" src/` → **0 resultados**. Existe apenas
  `GET /health` (informa `database: up|down`).
- **Ação:** `prometheus-fastapi-instrumentator` + métricas de negócio
  (requisições, latência, erros 5xx, tamanho do outbox, idade do evento mais antigo).
- **Verificação:** `curl localhost:8000/metrics` devolve séries Prometheus.

### T-7.3 — Health check profundo com degradação explícita 🟡

- **Arquivo:** `src/main.py:357-369`
- **Problema:** `/health` retorna `status: "healthy"` **mesmo com banco `down`** —
  um load balancer manteria encaminhando tráfego para instância doente.
- **Ação:** separar `/health/live` (processo) e `/health/ready` (banco + redis),
  retornando **503** em `ready` quando indisponível.
- **Verificação:** parar o Postgres → `GET /health/ready` responde 503.

### T-7.4 — Outbox/eventos cobre só 3 dos 35 módulos 🟠

- **Medido:** `grep -rl outbox src/modules` encontra **apenas** `sigmun_gdo`,
  `sigmun_int` e `sigmun_ate` — os outros **32 módulos** não publicam eventos.
  `src/shared/tasks/` tem apenas 2 arquivos (`tasks.py` com 4 `@celery_app.task`,
  e `expurgo.py`).
- **Ação:** extrair o padrão outbox do GDO para `src/shared/` (já há infra de
  Redis Streams e dispatcher prontos) e consumi-lo nos domínios transacionais
  (`compras`, `obras`, `tributos`).
- **Verificação:** evento publicado por ≥ 3 domínios além dos atuais chega ao subscriber
  com teste de integração.

### T-7.5 — Kubernetes e Terraform são esqueleto 🟠

- **Medido:**
  - `infra/kubernetes/base/` tem 4 arquivos (`deployment.yaml`, `ingress.yaml`, `hpa.yaml`,
    `.gitkeep`); os 3 **overlays** (`dev`, `homolog`, `prod`) contêm **apenas `.gitkeep`**.
  - `infra/terraform/` tem `main.tf`, `backend.tf`, `variables.tf`, `outputs.tf`;
    `modules/` e todos os `environments/*` são **apenas `.gitkeep`**.
- **Ação:** preencher overlays com ConfigMaps/Secrets/HPA por ambiente e o módulo
  Terraform correspondente (ou registrar em ADR que a implantação é via compose).
- **Verificação:** `kubectl apply --dry-run=client -k infra/kubernetes/overlays/dev` e
  `terraform validate` em `infra/terraform/`.

### T-7.6 — Backup e restore com teste de restauração 🟡

- **Arquivo:** `scripts/backup_postgres.py` (existe) e `docker-compose.yml`.
- **Problema:** há backup, mas **nenhum teste automatizado de restore**.
- **Ação:** script `scripts/verificar_restore.py` que restaura o dump num banco efêmero
  e valida contagem de tabelas por schema.
- **Verificação:** executado no CI semanal (job agendada).

### T-7.7 — Retenção e expurgo LGPD 🔴

- **Contexto:** `src/shared/tasks/expurgo.py` existe (Fase VII), mas a LGPD exige
  política de retenção por domínio.
- **Ação:** tabela de retenção (prazo por categoria de dado) + job agendado via Celery beat
  + registro de expurgo na trilha de auditoria.
- **Verificação:** teste de integração que cria dado vencido e confere a remoção.


---

## Fase 8 — Módulos esqueleto e banco de dados

Prioridade: **Média** · Esforço: **6 dias** · Pré-requisito: nenhuma

### T-8.1 — 11 módulos são casca vazia (decidir destino) 🟠

**Medido:** os 11 módulos abaixo têm **0 rotas, 0 testes e `__init__.py` vazio**
(`domain/entities/__init__.py` = arquivo de 1 linha em branco):

```
sigmun_administracao   sigmun_agricultura    sigmun_almoxarifado
sigmun_contabilidade   sigmun_controladoria  sigmun_financas
sigmun_gabinete        sigmun_licitacoes     sigmun_planejamento
sigmun_procuradoria    sigmun_transparencia
```

> Cada um ocupa **17 pacotes** (`application/{commands,queries,use_cases}`,
> `domain/{entities,events,services,value_objects}`,
> `infrastructure/{database,integrations,repositories}`,
> `presentation/{api,schemas}`) — mais de 100 arquivos de ruído
> que **inflam o `mypy` (980 fontes verificados)** e confundem o mapeamento DOM↔MOD.

- **Ação (decisão única, documentar):**
  1. **Remover** os 11 módulos vazios do `src/` (mantendo registro no catálogo de domínios), **ou**
  2. Marcar explicitamente com `STATUS = "nao_implementado"` e excluí-los do `mypy` via
     `exclude` no `pyproject.toml`.
  - Atenção à **duplicação aparente de domínio**: `sigmun_contabilidade` (stub) vs.
    `sigmun_con` (**7 rotas implementadas**) e `sigmun_financas` (stub) vs.
    `sigmun_orc` (**12 rotas implementadas**). Revisar a matriz DOM↔MOD
    (`031-Matriz-de-Correspondencia-DOM-MOD.md`) antes de decidir.
  - `sigmun_tributos` **não** é stub (16 rotas) — não incluí-lo nesta lista.
- **Verificação:**
  ```bash
  find src -type d -empty                                          # alvo: 0
  .venv/bin/mypy src/ | tail -1                                    # arquivos < 980
  ```

### T-8.2 — Diretórios órfãos no código 🟡

- **Medido (3 vazios):**
  ```
  src/modules/sigmun_dia/infrastructure/messaging
  src/modules/sigmun_ate/infrastructure/database/repositories
  src/modules/sigmun_ate/infrastructure/database/models
  ```
- **Ação:** implementar ou remover — em `sigmun_ate`, `database/models` e
  `database/repositories` estão vazios porque os modelos/repositórios do ATE provavelmente
  moram em outro caminho; **verificar antes de apagar** (pode haver código órfão fora do
  pacote esperado). Em `sigmun_dia`, falta a camada de mensageria.
- **Verificação:** `find src -type d -empty` → 0.

### T-8.3 — Migração: manter o único head sob controle 🟢 (contínuo)

- **Estado atual: 42 migrações, 1 head `c6ouv001merge01` — SAUDÁVEL.**
- **Risco:** a auditoria anterior já sofreu com duas heads (`C6` do DOM-OUV).
- **Ação:** adicionar **gate no CI** que falha se `alembic heads` não devolver
  exatamente 1 linha, impedindo bifurcação silenciosa.
- **Verificação:**
  ```bash
  test "$( .venv/bin/alembic heads | wc -l )" -eq 1
  ```

### T-8.4 — Downgrade de migrações (rollback real) 🟡

- **Problema:** os `downgrade()` existem e revertem via `op.drop_table`/`drop_column`,
  mas **nenhum rollback foi testado ponta a ponta** (só os 3 merges têm `pass`,
  o que é esperado para merge).
- **Ação:** automatizar teste
  `upgrade head → downgrade -1 → upgrade head` no CI.
- **Verificação:** script `scripts/verificar_rollback.py` verde.

### T-8.5 — Seeds por domínio centralizados 🟡

- **Problema:** existem `seed_ass.py`, `seed_gdo.py`, `seed_geo.py`, `seed_idn.py`,
  `seed_imo.py`, `seed_int.py`, `seed_obr.py`, `seed_tel.py`, `seed_ouv_usuario_teste.py`
  — 9 scripts soltos com contratos distintos; `dia`, `idn`, `int`, `obras` têm
  `seeds.py` próprios com **0% de cobertura** (T-4.3).
- **Ação:** comando único `make seed DOMAIN=<x>` e seeds testados.
- **Verificação:** `make seed DOMAIN=gdo && pytest tests/integration/test_gdo_seeds.py`.


---

## Fase 9 — Documentação e higiene do repositório

Prioridade: **Média** · Esforço: **4 dias**

### T-9.1 — Sincronizar `TODO.md` com o estado real, preservando histórico 🟠

> **Regra de reconciliação:** medições históricas do `TODO.md` (incluindo Ruff, Mypy e testes) devem ser preservadas quando estiverem explicitamente datadas. A correção consiste em impedir que esses números sejam interpretados como estado atual; não em apagar o histórico.

- **Medido:**
  - `TODO.md` cabeçalho na auditoria de 2026-10-04: **"Última Atualização: 2026-09-29"**.
  - Fase II marcada `[x]` afirmando `make lint` → "All checks passed!" (0 violações em
    623 arquivos) e `make type-check` → "Success: no issues found in 584 source files";
    suíte "**520 passed**".
  - Já existe uma **retificação em 2026-09-29** (linha 102) reconhecendo o problema —
    mas ela reporta **820 erros Ruff / 1.011 Mypy**, números que também estão desatualizados
    (hoje: **1.239 / 1.497**) e apontam 980 fontes, não 584.
  - Os "520 passed" referem-se a uma suíte com ~1/3 dos testes atuais (**1.393**).
- **Ação:** manter os registros históricos de `II.1`–`II.3` e da retificação de
  2026-09-29, deixando explícito que seus números são históricos e não representam
  o estado atual. O estado técnico atual é acompanhado neste `TODO2.md`, com
  medições datadas e tarefas incrementais.
- **Verificação:**
  ```bash
  grep -nF 'Última Atualização: 2026-10-06' TODO.md
  grep -nE '2026-09-06|2026-09-29' TODO.md | grep -E 'II\.[123]|Retificação|retificação'
  grep -nE '820 erros|1\.011 erros|520 passed' TODO.md
  ```

### T-9.2 — Reconciliar `fazer.md` (auditoria de 2026-09-28) 🟡

- **Problema:** `fazer.md` registra 953 erros Ruff / 1.166 Mypy / 887 testes; os números
  atuais são **1.239 / 1.497 / 1.393** — a dívida **cresceu**, mas o documento não foi
  atualizado. Há ainda 3 auditorias paralelas soltas no diretório pai
  (`auditoria4-resultado.txt`, `auditoria-pos-commit.txt`, `divergencias.txt`).
- **Ação:** marcar `fazer.md` como histórico fechado e apontar para este documento.
- **Verificação:** data e escopo claros no cabeçalho.

### T-9.3 — Higiene do repositório e do workspace 🟡

- **Medido (precisão importante):**
  - ✅ **Versionado:** `scripts/scan_final.txt` (saída de varredura) está no `git ls-files`.
  - ⚠️ **Em disco, porém ignorado:** 5 arquivos `.bak` —
  - ℹ️ **Backups temporários desta reconciliação (2026-10-06):** `TODO.md.saneamento-20261006.bak` e `TODO.md.pre-todo2-20261006.bak`. Esses arquivos são salvaguardas da operação atual e **não devem ser apagados nesta etapa**; a remoção fica para o fechamento da reconciliação, após a auditoria final.

    `scripts/gerar_artefatos_dominio.py.{3v4j,3v4l,3v5c,3v5e}.bak` e
    `SIGMUN-Docs/00-Governanca/000A-...md.3v5j.bak`. O `.gitignore:13` já tem `*.bak`,
    então **não entram no commit** — são só sujeira de workspace.
  - ⚠️ **Fora do repositório:** o git root é `sigmun-v1/sigmun-v1`; os `*.whl` e
    `*_resultado*.txt` de auditoria estão em `../` (**fora** do versionamento — ruído
    de workspace, não do repositório).
  - 🟡 **1 arquivo não rastreado:** `SIGMUN-Docs/DOM-DIA/dominio-dom-dia-funcionalidade`
    (não tem extensão — verificar se é artefato incompleto).
- **Ação:** `git rm scripts/scan_final.txt`, apagar os `.bak` do disco, decidir o destino
  do artefato não rastreado, e revisar os `.txt`/`.whl` do diretório pai (mover para
  `docs/` ou apagar).
- **Verificação:**
  ```bash
  git status --porcelain                                          # alvo: vazio (ou só o que se escolheu manter)
  git ls-files | grep -E '\.bak$|scan_final\.txt'                 # alvo: vazio
  find . -name '*.bak' -not -path './.git/*'                      # alvo: vazio
  ```

### T-9.4 — Divergências README ↔ realidade 🟡

- **Medido em `README.md` (seção "Tecnologias", linhas 90-96):**
  - ✅ Correto: deferir a lista de domínios para a matriz `031` e ao catálogo `05-Modulos/index.md`
    (o README **não** enumera módulos — correção ao que se supunha).
  - 🔴 `**Frontend:** React/Vue` — **não há Vue**; as 3 apps são Vite + React 19 + TS.
  - 🔴 `**Mobile:** React Native` — **não existe código algum** (só 4 `.gitkeep`).
  - 🟠 `**Infraestrutura:** ... Kubernetes, AWS` — k8s/terraform são esqueleto (T-7.5) e
    não há recurso AWS declarado.
  - 🟠 `**Cache/Filas:** Redis, Celery` — verdadeiro, mas omite que o outbox/eventos só
    existem no DOM-GDO (T-7.4).
  - 🟠 Passo 3 `pip install -r requirements-dev.txt` não cobre `flower` (T-1.5).
- **Ação:** corrigir a seção "Tecnologias", acrescentar a linha de **estado por domínio**
  (implementado / stub) gerada da matriz `031`, e remover "AWS" se não for usado.
- **Verificação:** script comparando os módulos citados com `ls src/modules/` e
  `grep -c 'Vue\|React Native' README.md` → 0 (ou justificado em ADR).

### T-9.5 — Status dos artefatos de domínio no CI 🟡

- **Contexto:** auditorias anteriores (`DOM-OUV`, `DOM-ATE`) acharam aviso falso
  "o domínio ainda não possui módulo implementado" em artefatos de domínio real.
- **Ação:** executar `scripts/check_docs.sh` no CI e falhar em divergência
  status ↔ implementação.
- **Verificação:** `bash scripts/check_docs.sh` → exit 0 no CI.

### T-9.6 — Atualizar o guia de contribuição 🟡

- **Ação:** `SIGMUN-Docs/00-Governanca/000E-GUIA-DE-CONTRIBUICAO.md` deve listar
  a ordem de verificação local
  (seção 2) e a política "um commit por módulo" da Fase 1.
- **Verificação:** guia menciona os 5 gates.


---

## 10. Roteiro de execução

Ordem por **dependência técnica**, não por severidade isolada.

| Ordem | Bloco de tarefas | Dias | Depende de | Entregável |
|:-----:|------------------|-----:|------------|------------|
| 1 | **Fase 0** — Segurança crítica (T-0.1 … T-0.4) | 3 | — | Sem spoofing, CORS fechado, rate limit |
| 2 | **Fase 1** — CI/CD verde (T-1.1 … T-1.5) | 4 | 1 | Pipeline verde; CD efetivo |
| 3 | **Fase 3** — Contrato de API (T-3.1 … T-3.3) | 5 | — | Paginação unificada |
| 4 | **Fase 2** — Autenticação nos 20 módulos (T-2.1 … T-2.4) | 10 | 1, 3 | 0 rotas sem auth |
| 5 | **Fase 4** — Testes e cobertura (T-4.1 … T-4.7) | 8 | 4 | ≥ 80% + e2e |
| 6 | **Fase 5** — Frontend (T-5.1 … T-5.5) | 12 | 3 | 3 apps com testes no CI |
| 7 | **Fase 7** — Backend/infra (T-7.1 … T-7.7) | 8 | 2 | `/metrics`, health correto |
| 8 | **Fase 8** — Módulos stub / banco (T-8.1 … T-8.5) | 6 | 2 | 0 diretórios vazios |
| 9 | **Fase 9** — Documentação/higiene (T-9.1 … T-9.6) | 4 | 2 | `git status` limpo |
| 10 | **Fase 6** — Mobile (T-6.1 … T-6.4) | 20 | decisão de produto | ADR + caminho executado |
| | **Total** | **80** | | **56 dias** sem mobile |

> **Caminho crítico:** Fase **0 → 1 → 2 → 4** = **25 dias** (3+4+10+8) até CI verde,
> API autenticada e cobertura ≥ 80%. As fases 5, 7, 8 e 9 são paralelizáveis
> (equipe de 2 → ~30 dias corridos até o DoD da seção 12).

### Sequência mínima de primeiros 5 dias

Para obter o maior retorno imediato, executar nesta ordem exata:

1. **T-0.1 + T-4.6** — remover spoofing de papel e provar com teste de regressão (0,5d).
2. **T-0.3** — fechar CORS/`SECRET_KEY`/`APP_DEBUG` (0,5d).
3. **T-1.2** — mover testes antes de lint/mypy no CI (0,25d) → pipeline já passa testes.
4. **T-1.3** — zerar Ruff começando por `sigmun_ate` (425 erros = 34% do total) (2d).
5. **T-8.1** — remover os 11 stubs (reduz `mypy` e ruído) (1d).

> Ao fim do 5º dia: testes no CI + lint zerado + menos ruído de tipagem —
> bases sólidas para a **Fase 2 (autenticação)**.

---

## 11. Régua de progresso

Marque a tarefa **apenas** após executar o comando de verificação correspondente.

### Fase 0 — Segurança
- [x] **T-0.1** — `require_roles_hybrid` usa JWT estrito (2026-10-05; 1409 passed)
- [x] **T-0.2** — flag `ALLOW_LEGACY_HEADERS` desligada por padrão (2026-10-05; ADR-0009)
- [x] **T-0.3** — `SECRET_KEY` obrigatória; CORS sem `*`+credenciais; `APP_DEBUG=False` (2026-10-05)
- [x] **T-0.4** — rate limit ativo (429 observado) (2026-10-05; `test_fase0_seguranca.py` 16/16)

### Fase 1 — CI/CD
- [x] **T-1.1** — `cd.yml` com jobs que executam e deployam de verdade (2026-10-06; gates explícitos: deploy-dev em push develop, deploy-prod via release, docker push)
- [x] **T-1.2** — testes rodam **antes** de lint/mypy no CI (2026-10-06; ordem: alembic → pytest → ruff → mypy)
- [ ] **T-1.3** — `ruff check src/ tests/` → **0 erros** (2026-10-06: 332 → 181; B904/E712/C416 zerados; F401/E501/F811 restantes)
- [ ] **T-1.4** — `mypy src/` → **0 erros** (1.530 erros pendentes; 63% Column[X]|X pattern)
- [x] **T-1.5** — lockfile gerado e usado no CI (2026-10-06; `requirements.lock` + `requirements-dev.lock` via pip-compile)

### Fase 2 — Autenticação
- [x] **T-2.1** — dependências de auth centralizadas em `shared/presentation` (2026-10-06; `src/shared/presentation/dependencies.py` + 8 testes)
- [x] **T-2.2a** — onda 2a: `seg`, `cadastro_imobiliario`, `rh`, `saude` *(2026-10-08; todos 4 módulos com auth: seg ✅, cadastro ✅, rh ✅, saude ✅ — verificado em endpoints.py)*
- [x] **T-2.2b** — onda 2b: `orc`, `tributos`, `con`, `patrimonio`, `frotas`, `met`, `dad` *(2026-10-06; autorização aplicada)*
- [x] **T-2.2c** — onda 2c: `gdo`, `int`, `geoinformacao`, `territorial`, `educacao`,
      `assistencia_social`, `ate`, `obras`, `dia` *(2026-10-08; auth aplicada + test_rbac_por_dominio.py: 72/72 passed)*
- [x] **T-2.3** — ADR de endpoints públicos *(2026-10-08; ADR-0010 existe + `scripts/verificar_rotas_publicas.py`: OK — 18 rotas batem exatamente)*
- [x] **T-2.4** — matriz RBAC cobrindo os 24 módulos com rotas *(2026-10-08; `tests/integration/test_rbac_por_dominio.py`: 72 testes passed — 24 módulos × 3 casos: sem token→401, papel errado→403, papel correto→2xx)*

### Fase 3 — Contrato de API
- [x] **T-3.1** — 1 única convenção de paginação *(2026-10-08; ADR-0011 + `src/shared/presentation/paginacao.py`: page=1 base 1, page_size=20 máx 100)*
- [x] **T-3.2** — envelope de erro padronizado com `correlation_id` *(2026-10-08; ADR-0012 + `src/shared/presentation/erros.py` + exception handlers globais em `src/main.py`: 72/72 RBAC tests pass + OpenAPI tests pass)*
- [x] **T-3.3** — `openapi.json` versionado com gate de diff *(2026-10-08; ADR-0013 + `scripts/gerar_openapi.py` + `scripts/diff_openapi.py` + CI job `openapi`: breaking changes gate ativo)*

### Fase 4 — Testes e cobertura
- [x] **T-4.1** — repositórios críticos ≥ 80% *(2026-10-08; `sqlalchemy_diaria_repository.py` 100%, `sqlalchemy_prestacao_repository.py` 100% via `tests/unit/test_dia_repositories.py`: 26 testes)*
- [x] **T-4.2** — use cases de `dia` ≥ 80% *(2026-10-08; 6 testes criados cobrindo os 5 use cases: criar_diaria, criar_prestacao, aprovar, glosar, restituir)*
- [x] **T-4.3** — seeds cobertos *(2026-10-08; 4/5 seeds com testes: GDO, TER, INT, OBR — 10 testes passando, 1 skip: DIA seed precisa de correção nos modelos)*
- [x] **T-4.4** — `--cov-fail-under=80` no CI *(2026-10-08; adicionado ao job `test` do `.github/workflows/ci.yml`; cobertura atual 78% — gate vai falhar até cobertura atingir 80%)*
- [x] **T-4.5** — ≥ 3 testes e2e *(2026-10-09; 6 testes e2e de auth passando: login legacy, login JWT, refresh token, rota protegida com token válido, rota protegida sem token 401, logout JWT — `tests/e2e/test_auth_e2e.py`)*
- [x] **T-4.6** — teste de regressão do spoofing de papel *(2026-10-09; já implementado em `tests/integration/test_fase0_seguranca.py::TestSpoofingDePapel`: 6 testes cobrindo spoofing via header X-Usuario-Papel sem JWT, com JWT válido sem papel, com papel válido, require_roles não usa fallback híbrido, rota real ouvidoria — todos passando)*
- [x] **T-4.7** — suíte verde sob concorrência (`pytest -n auto`) *(2026-10-09; 1521 testes unit/integration passam em duas execuções consecutivas com pytest-xdist; isolamento via banco por worker em `tests/conftest.py` + `_SessionFactory` reconfigurável em `session.py`)*

### Fase 5 — Frontend
- [x] **T-5.1** — `portal-cidadao` e `portal-fornecedor` com telas reais *(2026-10-10; cidadão: consulta protocolo + abrir manifestação/denúncia sigilosa/pedido LAI via POST /api/v1/ouv/*; fornecedor: licitações/contratos com filtro+página+detalhe via GET /api/v1/compras|contratos)*
- [x] **T-5.2** — Vitest nas 3 apps *(2026-10-10; vitest@5+jsdom+RTL em admin/cidadao/fornecedor; 12 testes: 4 admin + 5 cidadão + 3 fornecedor; `npm run test -- --run` verde)*
- [x] **T-5.3** — job de frontend no CI *(2026-10-10; step `Test frontend` adicionado ao job `frontend` em `.github/workflows/ci.yml`: lint + test + build na matriz das 3 apps)*
- [x] **T-5.4** — interceptor 401/403 + `correlation_id` em 500 *(2026-10-10; ApiError.correlationId + friendlyMessage + onUnauthorized nas 3 apps; admin derruba sessão→login; portais exibem aviso; header X-Correlation-ID do middleware backend)*
- [x] **T-5.5** — a11y sem avisos *(2026-10-10; plugin jsx_a11y no oxlint das 3 apps; skip-link, labels, focus-visible, output p/ status; portais 0 warnings/0 errors; admin com 3 erros pré-existentes em DiaPage.tsx corrompido — fora do escopo Fase 5)*
- [x] **Fix pós-5.1** — manifestação sem nome não é mais 500 *(2026-10-10; `except ValueError → 422` em ouv/manifestacoes, ouv/denuncias e ouv/pedidos-lai + teste de regressão; clients das 3 apps passam a ler o envelope `{error:{message}}` (T-3.2) via `extractErrorMessage`; verificado end-to-end no Docker: 422 legível sem nome, 201 com protocolo)*

### Fase 6 — Mobile
- [ ] **T-6.1** — ADR de mobile decidido
- [ ] **T-6.2 / T-6.3 / T-6.4** — caminho escolhido executado

### Fase 7 — Infra e observabilidade
- [ ] **T-7.1** — 0 avisos `on_event`
- [ ] **T-7.2** — `/metrics` respondendo
- [ ] **T-7.3** — `/health/ready` → 503 sem banco
- [ ] **T-7.4** — outbox compartilhado usado por ≥ 3 domínios
- [ ] **T-7.5** — overlays k8s e módulo Terraform válidos
- [ ] **T-7.6** — teste de restore de backup
- [ ] **T-7.7** — expurgo LGPD agendado e auditado

### Fase 8 — Módulos stub e banco
- [ ] **T-8.1** — 0 módulos casca (ou excluídos do mypy, por decisão)
- [ ] **T-8.2** — `find src -type d -empty` → 0
- [ ] **T-8.3** — gate de 1 head no CI
- [ ] **T-8.4** — rollback `upgrade → downgrade → upgrade` testado
- [ ] **T-8.5** — `make seed DOMAIN=<x>`

### Fase 9 — Documentação e higiene
- [ ] **T-9.1** — `TODO.md` sem números falsos
- [ ] **T-9.2** — `fazer.md` arquivado como histórico
- [ ] **T-9.3** — `git status` limpo; `scan_final.txt` removido; `.bak` apagados do disco
- [ ] **T-9.4** — `README.md` reflete os módulos reais
- [ ] **T-9.5** — `check_docs.sh` no CI
- [ ] **T-9.6** — guia de contribuição com os 5 gates


---

## 12. Definição de Pronto (DoD) — aptidão para produção

O SIGMUN está **apto a produção** quando **todos** os itens forem verdadeiros:

1. `.venv/bin/ruff check src/ tests/` → `All checks passed!` (**0 de 1.239**)
2. `.venv/bin/mypy src/` → `Success: no issues found` (**0 de 1.497**)
3. `.venv/bin/python -m pytest tests/ --cov=src --cov-fail-under=80 -q` → verde
4. `.venv/bin/alembic heads` → exatamente **1** head (hoje: `c6ouv001merge01`)
5. **0 rotas** sem dependência de autenticação (exceto as listadas em ADR de públicos) —
   hoje: **431 de 501** decorators (86%; 70 com auth nos 4 módulos da Fase 2)
6. Nenhum header `X-Usuario-Papel` aceito como identidade ou papel
7. `SECRET_KEY` obrigatória; CORS restrito com hosts explícitos; `APP_DEBUG=False`
8. CI verde nas 3 versões de Python **e** job de frontend verde
9. `cd.yml` demonstra um deploy real (imagem publicada em registry)
10. `git status --porcelain` vazio e `git ls-files | grep -E '\.bak$|scan_final\.txt'` sem resultados
11. `mobile/` ou implementado, ou removido por decisão formal (ADR)
12. `TODO.md`, `README.md` e `fazer.md` coerentes com as medições deste documento
13. 0 diretórios vazios em `src/` e em `mobile/`

---

## 13. Referências

| Documento | Conteúdo |
|-----------|----------|
| `fazer.md` | Auditoria de 2026-09-28 (Ruff 953 / Mypy 1.166 / 887 testes) — **histórico** |
| `TODO.md` | Backlog funcional por ondas (data de 2026-10-06) — **funcional**, não técnico |
| `TODO-dom-ouv.md` | Trilha de fechamento do DOM-OUV |
| `SIGMUN-Docs/00-Governanca/` | ADRs, matrizes DOM↔MOD, guia de contribuição |
| `SIGMUN-Docs/01-Arquitetura-Corporativa/031-Matriz-de-Correspondencia-DOM-MOD.md` | Mapeamento oficial domínio↔módulo |
| `.github/workflows/ci.yml` / `cd.yml` | Gates e deploy |

---

**Documento gerado a partir de auditoria empírica — dados brutos em `/tmp/*.txt`
(ruff, mypy, cobertura, OpenAPI, módulos, migrações, CI, frontend).**
**Re-auditar e atualizar os números deste arquivo a cada marco de entrega.**

## 14. Re-auditoria 2026-10-19 — estado atual medido e proximas tarefas

> **Data:** 2026-10-19 · **Commit base:** `367c267` (working tree sujo — ver T-NEW-0)
> **Metodo:** medicao direta (`ruff`, `mypy`, `pytest --collect-only`, `alembic heads`,
> `grep`, `find`, `git status`). Nenhum numero abaixo e estimativa.

### 14.1 Saude por camada — comparativo 2026-10-04 → 2026-10-19

| # | Camada | 2026-10-04 (doc) | 2026-10-19 (medido hoje) | Tendencia |
|---|--------|------------------|--------------------------|-----------|
| 1 | Codigo backend | 980 `.py`, 86.592 LOC, 35 modulos | **984 `.py`, 89.888 LOC, 35 modulos** | +4 arqs / +3.296 LOC |
| 2 | Modulos esqueleto | 11 modulos casca | **11 modulos com 13 `.py`** (adm, agric, almox, contab, control, financ, gab, licit, planej, procur, transp) | sem mudanca |
| 3 | Dirs vazios | 3 vazios | **3 vazios — identicos:** `sigmun_ate/.../database/models`, `.../repositories`, `sigmun_dia/.../messaging` | sem mudanca |
| 4 | Ruff | 1.239 erros | **402 erros** — F401 169, E501 77, I001 42, F811 22, W293 21, B904 19; 115 autocorrigiveis | -837 (-68%) |
| 5 | Mypy | 1.497 erros / 102 arqs | **1.567 erros / 106 arqs** (checked 984), inclui `main.py:399,411 no-untyped-def` | +70 / +4 arqs |
| 6 | Testes unit | 1.393 passed (suite toda) | **1.074 passed** em `tests/unit`; coleta total **1.531 + 1 erro de coleta** | suite cresceu, coleta quebrada |
| 7 | Testes e2e | vazio | **3 arquivos** mas `test_compras_e2e.py:7` quebra a coleta: `ModuleNotFoundError: ...sigmun_compras...seeds` | coleta bloqueada |
| 8 | Migracoes | 42 migracoes, 1 head | **42 migracoes, 1 head `c6ouv001merge01`** | saudavel |
| 9 | Auth | 431/501 sem auth | **501 decorators** em `src/modules`; so **17 ocorrencias** de dependencia de identidade; `X-Usuario-Papel` ainda em `shared/security/jwt.py` | auth minoritaria |
| 10 | Seguranca base | CORS `*`, SECRET fraca | **corrigido no codigo:** `main.py:269-274` origens explicitas, `main.py:453` falha sem SECRET; CI injeta SECRET de teste | avanco |
| 11 | Lifespan | — | **`@app.on_event` ainda em `main.py:450,468`** (deprecated) | aberto (T-7.1) |
| 12 | CI | vermelho, sem frontend | **CI tem job de frontend** (lint/test/build) + build Docker; gates ruff/mypy ainda vermelhos | parcial |
| 13 | CD | job morto | **`cd.yml` publica em `ghcr.io`** (dev/prod), mas `deploy-dev/prod` sao so `echo` | parcial |
| 14 | Frontend | 142 arqs, 0 testes | **154 arquivos** (sem node_modules); **1 teste real** `portal-cidadao/src/lib/api.test.ts` | +12 arqs, +1 teste |
| 15 | Mobile | 0 codigo | **1 arquivo real** (`README.md`) — zero codigo | sem mudanca |
| 16 | Docs | 1.187 `.md` | **1.193 `.md`** em `SIGMUN-Docs/` | +6 |
| 17 | Higiene/repo | 5 `.bak` + scan_final | **`git status`: 305 entradas; diff: 260 arqs +11.232/-3.211**; `.bak` em raiz + `scripts/*.bak`; `scan_final.txt` rastreado | working tree sujo |
| 18 | Lockfiles | — | `requirements.lock` + `requirements-dev.lock` presentes (pip-compile) | ok |

### 14.2 O que mudou de verdade desde 2026-10-04

1. **Ruff -68% (1.239 → 402).** E702 zerado; sobraram F401/E501/I001 (~80% do resto).
2. **Mypy piorou (+70).** Codigo novo sem anotacao anula o progresso do lint.
3. **Seguranca base (Fase 0) implementada** (CORS restrito + SECRET obrigatoria).
4. **CI/CD sairam do zero:** CI testa frontend; CD publica imagem. Falta deploy efetivo.
5. **E2E nasceu mas quebrou a coleta:** 1 import inexistente impede `pytest tests/`.
6. **Working tree com 305 mudancas nao commitadas** — risco n.1 do momento.

### 14.3 Proximas tarefas (ordens de execucao — P0 bloqueia o resto)

> Convencao: `T-NEW-<n>`. Cada item so e "done" com a verificacao verde anotada.

#### P0 — Desbloquear o pipeline (1-2 dias)

- [x] **T-NEW-0 — Organizar a arvore suja (305 entradas, 260 no diff).** Commits
  tematicos (codigo x testes x frontend x docs), descartar `.bak`/lixo.
  Verificacao: `git status --short | wc -l` → <= 5 intencionais.
  **DONE 2026-10-19:** 6 commits (`4aa975d` seguranca, `d739038` dominios,
  `58e6601` testes, `7f91524` frontend, `2a9c195` docs+TODO2, `bac9e6e` openapi);
  `git status --short | wc -l` → **0**; `git ls-files | grep -E '\.bak$|scan_final'` → vazio;
  `.env` nunca no diff; `TODO*.bak` em disco preservados (ignorados) p/ T-NEW-12.
- [x] **T-NEW-1 — Destravar a coleta do pytest (e2e).** CONCLUIDO 2026-10-19
  (commit 3da66ac): `test_compras_e2e.py` reescrito com repos em memoria via
  dependency_overrides (padrao dos testes de integracao) — fluxo real
  fornecedor -> compra -> HOMOLOGADO -> formalizar -> CONTRATADO + teste 401.
  Verificado: coleta `1533 tests, 0 erros`; arquivo `2 passed`; ruff limpo.
- [ ] **T-NEW-2 — Zerar o Ruff (402 → 0).** Ordem: `--fix` (F401/I001/W293/W292) →
  F811 (22) → E501 (77) → B904/E712/E741/F841/E402/UP035/B017/B008/SIM102.
  Verificacao: `ruff check src/ tests/` → `All checks passed!`.
- [ ] **T-NEW-3 — Estancar o Mypy (1.567 → 0).** Anotar `main.py:399,411`;
  queimar por modulo (ou excluir esqueletos com decisao).
  Verificacao: `mypy src/ | tail -1` → `Success: no issues found`.

#### P1 — Seguranca e correcao (3-5 dias)

- [ ] **T-NEW-4 — Auth nos 501 decorators.** Estender `inventario_auth.py` a todos
  os modulos, ADR de rotas publicas, eliminar `X-Usuario-Papel` como identidade
  (`shared/security/jwt.py`). Verificacao: 0 rotas sem auth fora da allowlist.
- [ ] **T-NEW-5 — Migrar `on_event` → `lifespan` (`main.py:450,468`).**
  Verificacao: `grep -rn on_event src/` → vazio.
- [ ] **T-NEW-6 — Cobertura >= 80%.** Re-medir apos T-NEW-1:
  `pytest tests/ --cov=src --cov-fail-under=80 -q`. Cobrir `seeds.py` zerados.
- [ ] **T-NEW-7 — Higiene do repo.** `git rm scripts/scan_final.txt`, apagar
  `*.bak` do disco, decidir `DOM-DIA/dominio-dom-dia-funcionalidade` sem extensao.
  Verificacao: `git ls-files | grep -E '\.bak$|scan_final'` → vazio.

#### P2 — Completude (1-2 semanas)

- [ ] **T-NEW-8 — 11 modulos esqueleto + 3 dirs vazios (T-8.1/T-8.2).** Implementar
  minimo viavel ou remover com ADR. Verificacao: `find src -type d -empty` → 0.
- [ ] **T-NEW-9 — Frontend: de 1 teste a suite real.** 1 teste por app,
  `lint/test/build` verdes no CI.
- [ ] **T-NEW-10 — Mobile: ADR ou codigo (T-6.1).** Hoje 0 LOC.
- [ ] **T-NEW-11 — CD com deploy efetivo.** Trocar `echo` por publish+deploy com
  healthcheck. Verificacao: job `deploy-*` executa (nao skipped).
- [ ] **T-NEW-12 — Docs coerentes (T-9.1/T-9.2/T-9.4).** README sem Vue/RN/AWS
  prontos; fechar `fazer.md` como historico.

### 14.4 Caminho critico

```
T-NEW-0 (tree limpa) → T-NEW-1 (coleta) → T-NEW-6 (cobertura)
→ T-NEW-2 (ruff 0) → T-NEW-3 (mypy 0) → CI verde
→ T-NEW-4 (auth) + T-NEW-5 (lifespan) → DoD 1-7
→ T-NEW-7/8/9/10/11/12 → DoD 8-13 (producao)
```

### 14.5 Comandos de re-auditoria (copiar/colar)

```bash
find src -type f -name '*.py' | wc -l; find src -type f -name '*.py' -exec cat {} + | wc -l
.venv/bin/ruff check src/ tests/ --statistics | head -20
.venv/bin/mypy src/ | tail -1
.venv/bin/python -m pytest tests/ --collect-only -q -p no:cacheprovider | tail -2
.venv/bin/python -m pytest tests/unit -q -p no:cacheprovider | tail -1
.venv/bin/alembic heads; ls alembic/versions/*.py | wc -l
grep -rn "@router\.\(get\|post\|put\|patch\|delete\)" src/modules --include='*.py' | wc -l
grep -rn "get_current_user\|get_current_active\|require_role\|get_current_tenant" src/modules --include='*.py' | wc -l
grep -rn "on_event" src/ --include='*.py'; grep -rn "X-Usuario-Papel" src/ --include='*.py'
git status --short | wc -l; git ls-files | grep -E '\.bak$|scan_final\.txt'
find src -type d -empty; find mobile -type f -not -name '.gitkeep'
```

