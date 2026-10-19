# Matriz RBAC por domínio — SIGMUN

- **Documento:** `matriz-rbac.md` · **Tarefa:** TODO2 T-2.4
- **Data:** 2026-10-06 · **Status:** Vigente · **Classificação:** Pública
- **Relacionados:** ADR-0007 (auth cadastro), ADR-0008 (autorização DOM-OUV),
  ADR-0009 (fim do header legado), ADR-0010 (endpoints públicos),
  `src/shared/presentation/dependencies.py` (contrato único T-2.1).

## Regras gerais (T-2.2)

| Operação | Dependência exigida |
| --- | --- |
| `GET` / `HEAD` / `OPTIONS` | `UsuarioOpcional` (identidade capturada se houver token) — ou rota pública listada no ADR-0010 |
| `POST` / `PUT` / `PATCH` | `UsuarioObrigatorio` + `exigir_papeis("gestor", "admin", "<papel>")` |
| `DELETE` e atos destrutivos (revogar, baixar, excluir) | `UsuarioObrigatorio` + `exigir_papeis("admin", "<papel>")` (aplicado onde sinalizado) |

- **Papéis do sistema:** `admin`, `gestor` + um papel por domínio
  (ex.: `seguranca`, `cadastro`, `orcamento`). O banco grava `ROLE_<NOME>` e
  `_normaliza_papel()` reconcilia `admin` ≡ `ROLE_ADMIN` (C18).
- **Fallback legado:** `X-Usuario-Id`/`X-Usuario-Papel` **nunca** confere
  identidade/papel (ADR-0009; `ALLOW_LEGACY_HEADERS=False`).

## Matriz por domínio (24 módulos com rotas)

| Módulo | Prefixo | Rotas | Escrita: papéis | Restritos a `admin` (destrutivos) |
| --- | --- | --- | --- | --- |
| `sigmun_seg` | `/api/v1/seg` | 32 | `gestor`, `admin`, `seguranca` | `admin`, `seguranca` (4) |
| `sigmun_cadastro_imobiliario` | `/api/v1/imo` | 25 | `gestor`, `admin`, `cadastro` | `admin`, `cadastro` (2) |
| `sigmun_rh` | `/api/v1/pes` | 19 | `gestor`, `admin`, `rh` | — |
| `sigmun_saude` | `/api/v1/sau` | 18 | `gestor`, `admin`, `saude` | — |
| `sigmun_orc` | `/api/v1/orc` | 12 | `gestor`, `admin`, `orcamento` | — |
| `sigmun_tributos` | `/api/v1/tri` | 16 | `gestor`, `admin`, `tributos` | — |
| `sigmun_con` | `/api/v1/con` | 7 | `gestor`, `admin`, `contabilidade` | — |
| `sigmun_patrimonio` | `/api/v1/pat` | 8 | `gestor`, `admin`, `patrimonio` | — |
| `sigmun_frotas` | `/api/v1/fro` | 13 | `gestor`, `admin`, `frotas` | — |
| `sigmun_met` | `/api/v1/met` | 30 | `gestor`, `admin`, `metas` | `admin`, `metas` (5) |
| `sigmun_dad` | `/api/v1/dad` | 29 | `gestor`, `admin`, `dados` | `admin`, `dados` (5) |
| `sigmun_gdo` | `/api/v1/gdo` | 20 | `gestor`, `admin`, `gdo` | — |
| `sigmun_int` | `/api/v1/int` | 31 | `gestor`, `admin`, `integracao` | `admin`, `integracao` (4) |
| `sigmun_geoinformacao` | `/api/v1/geo` | 28 | `gestor`, `admin`, `geo` | `admin`, `geo` (5) |
| `sigmun_territorial` | `/api/v1/tel` | 25 | `gestor`, `admin`, `territorial` | `admin`, `territorial` (3) |
| `sigmun_educacao` | `/api/v1/edu` | 25 | `gestor`, `admin`, `educacao` | — |
| `sigmun_assistencia_social` | `/api/v1/ass` | 31 | `gestor`, `admin`, `assistencia` | `admin`, `assistencia` (3) |
| `sigmun_ate` | `/api/v1/ate` | 19 | `gestor`, `admin`, `atendimento` | — |
| `sigmun_obras` | `/api/v1/obr` | 24 | `gestor`, `admin`, `obras` | `admin`, `obras` (2) |
| `sigmun_dia` | `/api/v1/dia` | 20 | `gestor`, `admin`, `dia` | — |
| `sigmun_cadastro` | `/api/v1/cadastro` | 12 | `gestor`, `admin`, `cadastro` | `admin`, `cadastro` (1) |
| `sigmun_compras` | `/api/v1/{compras,contratos,fornecedores,processos-documentais,itens-compras,auditoria}` | 30 | `gestor`, `admin`, `compras` | `admin`, `compras` (5) |
| `sigmun_idn` | `/api/v1/idn` | 12 | `admin` (somente — gestão de usuários) | todas as `/usuarios*` (6) |
| `sigmun_ouvidoria` | `/api/v1/ouv` | 16 | consulta: `ouvidor`, `corregedor`, `auditor`, `admin` · tratamento: `ouvidor`, `corregedor` | atos de tratamento restritos (ADR-0008) |

**Contagem de decorators:** 20 módulos da Fase 2 = **432 rotas**; os 4
pré-existentes (`cadastro` 12 + `compras` 30 + `idn` 12 + `ouvidoria` 16) =
**70 rotas**.

## Exceções públicas (por decisão, não por acidente)

- **18 rotas anônimas** inventariadas no
  [ADR-0010](../00-Governanca/ADR/ADR-0010-endpoints-publicos.md)
  (compras/cadastro leitura de transparência, `/auth/*` do idn, `/health`, `/`).
- **Criação anônima na ouvidoria** (`POST /ouv/denuncias`,
  `POST /ouv/manifestacoes`, `POST /ouv/pedidos-lai`, recurso) — exigência da
  LAI, validada pelo ADR-0008 §2.2. Usam `UsuarioOpcional`.

## Verificação

```bash
# Trio 401/403/autorizado nos 24 módulos (72 casos):
.venv/bin/python -m pytest tests/integration/test_rbac_por_dominio.py -q

# Inventário de rotas públicas deve bater exatamente com o ADR-0010:
.venv/bin/python scripts/verificar_rotas_publicas.py

# Regressão do código das roles (C18):
.venv/bin/python -m pytest tests/integration/test_rbac_roles_reais.py -q
```

- **Última execução (2026-10-06):** `test_rbac_por_dominio.py` **72 passed**;
  `verificar_rotas_publicas.py` **OK — 18 rotas**.
