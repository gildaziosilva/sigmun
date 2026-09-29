# 012 – Matriz de Rastreabilidade – Geoinformação Municipal

#### Matriz de Rastreabilidade – Geoinformação Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GEO-012

**Domínio:** Geoinformação Municipal

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Geoinformacao-Municipal.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000C-HIERARQUIA-DOCUMENTAL.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `030-Roadmap-de-Implementacao-dos-Dominios.md`
* `Mapa-de-Dominios.md`
* `Modelo-Logico.md`
* `Modelo-Fisico.md`
* `Dicionario-de-dados.md`

---

# 1. Finalidade

Este artefato assegura que toda capacidade, história, requisito e regra do
domínio de Geoinformação Municipal está rastreada ao código e aos testes correspondentes.

---

# 2. Princípio de Rastreabilidade

* Nenhum requisito existe sem capacidade, história e regra associadas.
* Nenhuma regra existe sem teste que a exercite.
* Nenhuma entidade de domínio existe sem operação que a persista.

---

# 3. Rastreabilidade por Capacidade

| Capacidade | Histórias | Requisitos | Regras | Entidades |
| --- | | --- | | --- | | --- | |
| CAP-GEO-001 — Cadastro de camadas cartográficas | HU-GEO-001 | RF-GEO-001, RF-GEO-002 | RN-GEO-001, RN-GEO-006 | — |
| CAP-GEO-002 — Gestão de mapas SIG | HU-GEO-003 | RF-GEO-003, RF-GEO-009 | RN-GEO-002, RN-GEO-004, RN-GEO-005 | — |
| CAP-GEO-003 — Composição de camadas por mapa | HU-GEO-002 | RF-GEO-004 | RN-GEO-004, RN-GEO-008 | — |
| CAP-GEO-004 — Cadastro de elementos geoespaciais | HU-GEO-004 | RF-GEO-005, RF-GEO-006 | RN-GEO-003, RN-GEO-008 | — |
| CAP-GEO-005 — Publicação de serviços geoespaciais | HU-GEO-005 | RF-GEO-007, RF-GEO-008 | RN-GEO-007 | — |
| CAP-GEO-006 — Consulta de mapas e serviços | HU-GEO-006 | — | RN-GEO-003, RN-GEO-004 | — |

---

# 4. Rastreabilidade por História de Usuário

| História | Capacidade | Casos de uso | Critérios | Testes |
| --- | | --- | | --- | | --- | |
| HU-GEO-001 | CAP-GEO-001 | CU-GEO-001, CU-GEO-002, CU-GEO-003, CU-GEO-004, CU-GEO-005 | 4 | 0 teste(s) |
| HU-GEO-002 | CAP-GEO-003 | CU-GEO-008, CU-GEO-009 | 3 | 0 teste(s) |
| HU-GEO-003 | CAP-GEO-002 | CU-GEO-006, CU-GEO-007, CU-GEO-010, CU-GEO-011, CU-GEO-012 | 3 | 0 teste(s) |
| HU-GEO-004 | CAP-GEO-004 | CU-GEO-013, CU-GEO-014 | 3 | 0 teste(s) |
| HU-GEO-005 | CAP-GEO-005 | CU-GEO-015, CU-GEO-016, CU-GEO-017, CU-GEO-018 | 3 | 0 teste(s) |
| HU-GEO-006 | CAP-GEO-006 | CU-GEO-019 | 3 | 0 teste(s) |

---

# 5. Rastreabilidade por Requisito Funcional

| Requisito | Capacidade | Regras | Operações | Testada por |
| --- | | --- | | --- | | --- | |
| RF-GEO-001 | CAP-GEO-001 | RN-GEO-001, RN-GEO-006 | 7 | 0 teste(s) |
| RF-GEO-002 | CAP-GEO-001 | RN-GEO-001 | 1 | 0 teste(s) |
| RF-GEO-003 | CAP-GEO-002 | RN-GEO-002, RN-GEO-004 | 7 | 0 teste(s) |
| RF-GEO-004 | CAP-GEO-003 | RN-GEO-004, RN-GEO-006, RN-GEO-008 | 3 | 0 teste(s) |
| RF-GEO-005 | CAP-GEO-004 | RN-GEO-003, RN-GEO-008 | 4 | 0 teste(s) |
| RF-GEO-006 | CAP-GEO-004 | RN-GEO-008 | 1 | 0 teste(s) |
| RF-GEO-007 | CAP-GEO-005 | RN-GEO-007 | 6 | 0 teste(s) |
| RF-GEO-008 | CAP-GEO-005 | RN-GEO-007 | 1 | 0 teste(s) |
| RF-GEO-009 | CAP-GEO-002 | RN-GEO-004 | 1 | 0 teste(s) |

---

# 6. Cobertura

| Indicador | Quantidade |
| --- | |
| Capacidades | 6 |
| Histórias de usuário | 6 |
| Casos de uso | 19 |
| Requisitos funcionais | 9 |
| Requisitos não funcionais | 8 |
| Regras de negócio | 8 |
| Classes de teste | 10 |
| Testes de unidade | 61 |

---

# 7. Refinamento Futuro

* A matriz é ampliada quando novos artefatos forem detalhados.
* A promoção da correspondência `MOD-*` exige este artefato e a conciliação do
  escopo documental, conforme a matriz DOM ↔ MOD.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 012-Matriz-de-Rastreabilidade-Geoinformacao-Municipal.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_geoinformacao`. Alterações no código devem ser
> refletidas reexecutando o gerador.
