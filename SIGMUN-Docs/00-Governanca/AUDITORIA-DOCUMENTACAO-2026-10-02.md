# Relatório de Auditoria da Documentação — SIGMUN (2026-10-02)

**Escopo:** `SIGMUN-Docs/` + `docs/` + READMEs + 33 domínios `DOM-*` + `05-Modulos/` + cruzamento com `src/modules/`, `src/main.py`, `frontend/`, `mobile/`, `infra/`, `scripts/`.
**Corpus:** ~1.440 arquivos / ~14 MB em `SIGMUN-Docs/`; 33 dirs `DOM-*` × 28 `.md`; 210 `.puml`; 10 READMEs.
**Modo:** somente leitura + correções P0/P1 aprovadas (sem commit; o tree já possuía ~933 arquivos modificados pré-existentes, não tocados).

## 1. Resumo executivo

| # | Achado | Sev. | Situação após esta sessão |
|---|--------|------|---------------------------|
| F1 | `README.md` raiz com bloco quebrado + só 5/33 domínios | Crítica | ✅ Corrigido (fence fechado, seção reescrita, link 031) |
| F2 | Licença MIT (README) × Apache-2.0 (LICENSE + ADR-0001) | Crítica | ✅ Corrigido (README → Apache-2.0) |
| F3 | Compras: `DOM-COM` × `DOM-COMPRAS-001` × `DOM-CPT` + 3 módulos órfãos | Crítica | 🟡 Parcial (desambiguação + 3 índices criados; falta rename/shim) |
| F4 | Docs citam `src/modules/sigmun_*` inexistentes (10 fantasmas) | Crítica | ❌ Pendente P2 (script detecta; conteúdo não reescrito) |
| F5 | ~192 links `000C` sem versão + `Cadeia-de-Valor.md` sem versão | Alta | ✅ Corrigido via sed (0 restantes) |
| F5b | Typos em nomes: `Arqhiteture`, `Analytcs`, `Governaca-de-Dados` | Alta | ❌ Pendente (requer rename + shim) |
| F6 | `Status` index × 000 divergente (29 domínios) | Alta | ❌ Requer decisão semântica |
| F7 | 18 stubs `05-Modulos` + `docs/api|architecture|diagrams` vazios | Alta | 🟡 Parcial (banner STUB aplicado) |
| F8 | READMEs desatualizados/links quebrados | Alta | 🟡 Parcial (frontend/README corrigido) |
| F9 | 205 `.puml` com fence + 19 PNG em `puml/` + 10 "Captura de tela" | Média | ❌ Pendente P2 |
| F10 | Governança duplicada (GUIA, ADR, TODO×fazer×ROADMAP×Plano) | Média | ❌ Pendente P2 |
| F11 | Matriz 031 congelada (14/28 de 17/09 × real 27/34) | Alta | ❌ Pendente (republicar v1.3) |

## 2. Correções aplicadas nesta sessão

1. `README.md`: removida lista de 5 domínios vazada da árvore; seção reescrita com links para matriz 031 e catálogo 05-Modulos; licença MIT → Apache License 2.0.
2. `frontend/README.md`: stack "React ou Vue (a definir)" → React+Vite+TS real; links relativos corrigidos para `../../SIGMUN-Docs/...`.
3. `sed` em massa: `000C-HIERARQUIA-DOCUMENTAL.md` → `...-v1.0.md` (192 arquivos, 0 restantes); `Cadeia-de-Valor.md` → `Cadeia-de-Valor-v1.1.md` (0 restantes).
4. `DOM-CPT/index.md` + `000-Dominio-Gestao-de-Competencias.md`: banner de desambiguação anti-Compras (DOM-COM × DOM-COMPRAS-001 × DOM-CPT).
5. Criados `05-Modulos/sigmun_con|sigmun_dia|sigmun_orc/index.md` (módulos órfãos; con sem `include_router` direto — registrar ou documentar; dia e orc registrados).
6. Banner `STUB` nos 18 `05-Modulos/*/index.md` mínimos (<2.950 bytes).
7. Criado `scripts/check_docs.sh` (executável, `bash -n` OK) — gate F1–F5 + infos F6/F7/F9/F11.

## 3. Achados pendentes (detalhe)

### F3 — Identidade Compras (restante)
Diretório físico `DOM-COMPRAS-001/` declara identidade lógica `DOM-COM` (ADR-0006); `DOM-CPT` é Gestão de Competências (RH). Falta: renomear para `DOM-COM/` com shim de compatibilidade OU oficializar path físico em ADR e proibir sigla isolada.

### F4 — Módulos fantasma (10)
`sigmun_ana, sigmun_ate, sigmun_cpt, sigmun_dec, sigmun_gov, sigmun_ind, sigmun_inf, sigmun_mam, sigmun_mob, sigmun_pla` citados em `DOM-*/` mas inexistentes em `src/modules/`. Ex.: `DOM-ANA/007` diz "sem módulo implementado" e simultaneamente "combinando a implementação em `src/modules/sigmun_ana`" (RN-ANA-001..004). Correção P2: trocar Fonte para "proposto — sem implementação".

### F5b — Typos em nomes oficiais (pendente)
- `00-Governanca/000F-Registro-de-Decisoes-Arquiteturais-ADRs.md` (5 refs) — "Arqhiteture".
- `01-Arquitetura-Corporativa/017-Arquitetura-de-Governanca-de-Dados.md` (3 refs) — falta "o".
- `01-Arquitetura-Corporativa/018-Arquitetura-de-BI-Analytics-e-Inteligencia-Artificial.md` (3 refs) — "Analytcs".
- 33 refs `000F-Registro-de-Decisoes-Arquiteturais(ADR).md` (nome curto inexistente). Correção: rename com shim + sed nas refs.

### F6 — Status divergente (29 domínios)
Todos os `DOM-*/index.md` = "Em elaboração" x `000-*.md` = "Vigente" (script F6 lista os 29). Decidir semântica: status do índice (navegação) vs status do domínio (negócio), ou unificar. Também: 881x "Vigente" com tabela Versionamento vazia para `Versão 2.0` (801x).

### F8 — READMEs (restante)
- `src/README.md`: tabela com 21 módulos x 34 reais — regenerar de `ls src/modules`.
- `scripts/README.md`: cita `.ps1` Windows inexistentes — reescrever para `make`/scripts reais.
- `mobile/README.md`: descreve 4 apps; só há `*/src/.gitkeep` — banner "não implementado".
- `infra/README.md`: confere `terraform/modules|environments`, `k8s/overlays` — marcar "planejado" se ausente.
- `frontend/admin` (3,6 KB) x portais (~1 KB): nivelar mínimo operacional.

### F9 — PlantUML (pendente P2)
205 `.puml` iniciam com fence `\`\`\`plantuml` (quebra `plantuml *.puml` em lote); 19 PNGs em `puml/` (incl. `DOM-OUV`, `DOM-IDN`, `00-Governanca/puml/`); 10 arquivos "Captura de tela ... .png". Ação: strip do fence nos `.puml`, mover PNGs para `evidencias/` ou `render/`, renomear capturas, pipeline `plantuml -tpng` no CI.

### F10 — Duplicação de governança (pendente P2)
`GUIA-DE-CONTRIBUICAO` (raiz, sem extensão) x `000E`; `DECISOES-ARQUITETURAIS.md` x `ADR/`; `TODO.md` x `fazer.md` x `ROADMAP.md` x `Plano-de-Trabalho.md` (246 KB); `docs/` raiz do workspace (`ai-history/`, `faturas/`, `etapas.odt`) fora do padrão; `_backup_eol/` legado. Ação: hierarquia canônica em `000C` + shims de 5 linhas; mover `faturas/` para fora do repo.

### F11 — Matriz 031 congelada (pendente)
031 §4 (17/09/2026, base 51c82dc): 14 `include_router` / 8 módulos / 28 dirs. Real (02/10/2026): **27** `include_router` em `src/main.py`, **34** `sigmun_*` em `src/modules/`. Republicar 031 v1.3 com recontagem + delta; trocar números absolutos do `05-Modulos/index.md` por link à matriz vigente.

## 4. Como validar

```bash
bash scripts/check_docs.sh   # PASS esperado em F1–F5; F6/F7/F9/F11 são INFO até P2
```

Última execução (02/10/2026): F1 ✅, F2 ✅, F3 🟡 (órfãos OK; DOM-CPT gate ajustado), F4 ❌ (10 fantasmas), F5 ✅ (000C/CV zerados; typos como INFO), F6 INFO (29 divergentes), F7 INFO (3 docs vazios; 16 sem STUB — inclui os 3 novos + portais?), F9 INFO (205/19/10), F11 INFO (27/34).

## 5. Mapa DOM x MOD x código (02/10/2026)

- 33 dirs `DOM-*` x 28 `.md` (estrutura uniforme; conteúdo parcial template).
- `src/modules/`: 34 `sigmun_*` (administracao, agricultura, almoxarifado, assistencia_social, cadastro, cadastro_imobiliario, compras, **con**, contabilidade, controladoria, dad, **dia**, educacao, financas, frotas, gabinete, gdo, geoinformacao, idn, int, licitacoes, met, obras, **orc**, ouvidoria, patrimonio, planejamento, procuradoria, rh, saude, seg, territorial, transparencia, tributos). Negrito = sem espelho antes desta sessão (agora criado).
- Sem implementação mas com docs que citam path: ANA, ATE, CPT, DEC, GOV, IND, INF, MAM, MOB, PLA (F4).
