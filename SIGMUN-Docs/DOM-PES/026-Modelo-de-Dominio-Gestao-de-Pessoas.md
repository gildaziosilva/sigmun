# 026 – Modelo de Domínio – Gestão de Pessoas

**Versão:** 2.0 — **Status:** Implementado (2026-09-19)

## 1. Agregados implementados (`src/modules/sigmun_rh/`)

| Agregado | Entidade | Regras |
|---|---|---|
| Cargos | `Cargo` | RN-PES-001 código único; RN-PES-002 salário-base > 0 |
| Servidores | `Servidor` + `StatusServidor` + `TipoVinculo` | RN-PES-010 matrícula única; RN-PES-011 CPF único 11 dígitos; RN-PES-012 cargo válido; RN-PES-013 datas admissão/desligamento; transições ATIVO↔AFASTADO→EXONERADO/DEMITIDO |
| Lotações | `Lotacao` | RN-PES-020 sem sobreposição vigente; RN-PES-021 unidade + início obrigatórios; RN-PES-022 remoção encerra vigência |
| Folha | `FolhaPagamento` + `StatusFolha` | RN-PES-030 competência única; RN-PES-031 só ABERTA recebe lançamentos; RN-PES-032 fechamento exige lançamentos; RN-PES-033 HOMOLOGADA/PAGA terminal; máquina ABERTA→FECHADA→HOMOLOGADA→PAGA (+CANCELADA/REABERTA) |
| Férias | `Ferias` + `StatusFerias` | RN-PES-040/041 mín 10 dias, máx 3 parcelas; máquina PLANEJADA→APROVADA→EM_GOZO→CONCLUIDA (+CANCELADA) |
| Frequência | `Frequencia` + `TipoFrequencia` | RN-PES-050 unicidade servidor/dia; RN-PES-051 atraso > 60min = meio período; RN-PES-052 falta injustificada → desconto em folha |

## 2. Portas e adaptadores

- Ports: `application/interfaces.py` (`RepositorioCargo/Servidor/Lotacao/Folha/Ferias/Frequencia`).
- Use cases (22): `use_cases_cargos_servidores.py`, `use_cases_lotacao.py`, `use_cases_folha.py`, `use_cases_ferias.py`, `use_cases_frequencia.py`.
- Adaptadores SQLAlchemy (schema `rh`): `infrastructure/database/models.py` + `models_folha.py`; repositórios `sqlalchemy_*_repository.py`.
- API: 19 endpoints `/api/v1/pes/*` (`presentation/api/*_endpoints.py`), registrados em `src/main.py` + tag OpenAPI `Gestão de Pessoas`.
- Migrações: `20260919_01_dom_pes_models.py` (cargos/servidores/lotações) → `20260919_02_dom_pes_folha.py` (folhas/ferias/frequencias).

## 3. Integrações

- Fornece `servidor_id` para DOM-DIA (viagens/diárias) e futuros DOM-ORC/DOM-GDO.
- Consome `unidade_id` do DOM-CUM (unidades administrativas).

