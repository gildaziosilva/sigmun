# 012 – Matriz de Rastreabilidade – Obras e Infraestrutura

#### Matriz de Rastreabilidade – Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OBR-012

**Domínio:** Obras e Infraestrutura

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Obras-e-Infraestrutura.md`
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
domínio de Obras e Infraestrutura está rastreada ao código e aos testes correspondentes.

---

# 2. Princípio de Rastreabilidade

* Nenhum requisito existe sem capacidade, história e regra associadas.
* Nenhuma regra existe sem teste que a exercite.
* Nenhuma entidade de domínio existe sem operação que a persista.

---

# 3. Rastreabilidade por Capacidade

| Capacidade | Histórias | Requisitos | Regras | Entidades |
| --- | | --- | | --- | | --- | |
| CAP-OBR-001 — Cadastro e ciclo de vida das obras | HU-OBR-001, HU-OBR-002 | RF-OBR-001, RF-OBR-002, RF-OBR-003 | RN-OBR-001, RN-OBR-002, RN-OBR-003, RN-OBR-004 | — |
| CAP-OBR-002 — Medição físico-financeira | HU-OBR-003 | RF-OBR-004 | RN-OBR-005 | — |
| CAP-OBR-003 — Execução financeira da obra | HU-OBR-005 | RF-OBR-005 | RN-OBR-004, RN-OBR-006 | — |
| CAP-OBR-004 — Acompanhamento de etapas e vistorias | HU-OBR-004 | RF-OBR-006, RF-OBR-007 | RN-OBR-007, RN-OBR-008 | — |
| CAP-OBR-005 — Consulta do andamento das obras | HU-OBR-006, HU-OBR-007 | RF-OBR-008, RF-OBR-009 | RN-OBR-004, RN-OBR-005, RN-OBR-006 | — |

---

# 4. Rastreabilidade por História de Usuário

| História | Capacidade | Casos de uso | Critérios | Testes |
| --- | | --- | | --- | | --- | |
| HU-OBR-001 | CAP-OBR-001 | CU-OBR-001, CU-OBR-002, CU-OBR-003, CU-OBR-004, CU-OBR-005, CU-OBR-006, CU-OBR-007 | 4 | 0 teste(s) |
| HU-OBR-002 | CAP-OBR-001 | CU-OBR-001, CU-OBR-002, CU-OBR-003, CU-OBR-004, CU-OBR-005, CU-OBR-006, CU-OBR-007 | 3 | 0 teste(s) |
| HU-OBR-003 | CAP-OBR-002 | CU-OBR-008, CU-OBR-009, CU-OBR-010, CU-OBR-011 | 4 | 0 teste(s) |
| HU-OBR-004 | CAP-OBR-004 | CU-OBR-014, CU-OBR-015, CU-OBR-016, CU-OBR-017 | 4 | 0 teste(s) |
| HU-OBR-005 | CAP-OBR-003 | CU-OBR-012, CU-OBR-013 | 3 | 0 teste(s) |
| HU-OBR-006 | CAP-OBR-005 | CU-OBR-018 | 3 | 0 teste(s) |
| HU-OBR-007 | CAP-OBR-005 | CU-OBR-018 | 2 | 0 teste(s) |

---

# 5. Rastreabilidade por Requisito Funcional

| Requisito | Capacidade | Regras | Operações | Testada por |
| --- | | --- | | --- | | --- | |
| RF-OBR-001 | CAP-OBR-001 | RN-OBR-001, RN-OBR-002, RN-OBR-004 | 5 | 0 teste(s) |
| RF-OBR-002 | CAP-OBR-001 | RN-OBR-002, RN-OBR-003, RN-OBR-005 | 4 | 0 teste(s) |
| RF-OBR-003 | CAP-OBR-001 | RN-OBR-002 | 1 | 0 teste(s) |
| RF-OBR-004 | CAP-OBR-002 | RN-OBR-004, RN-OBR-005 | 4 | 0 teste(s) |
| RF-OBR-005 | CAP-OBR-003 | RN-OBR-004, RN-OBR-006 | 2 | 0 teste(s) |
| RF-OBR-006 | CAP-OBR-004 | RN-OBR-007 | 3 | 0 teste(s) |
| RF-OBR-007 | CAP-OBR-004 | RN-OBR-008 | 1 | 0 teste(s) |
| RF-OBR-008 | CAP-OBR-005 | RN-OBR-004, RN-OBR-005, RN-OBR-006 | 1 | 0 teste(s) |
| RF-OBR-009 | CAP-OBR-005 | RN-OBR-005, RN-OBR-006, RN-OBR-007, RN-OBR-008 | 4 | 0 teste(s) |

---

# 6. Cobertura

| Indicador | Quantidade |
| --- | |
| Capacidades | 5 |
| Histórias de usuário | 7 |
| Casos de uso | 18 |
| Requisitos funcionais | 9 |
| Requisitos não funcionais | 8 |
| Regras de negócio | 8 |
| Classes de teste | 8 |
| Testes de unidade | 55 |

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

**Documento:** 012-Matriz-de-Rastreabilidade-Obras-e-Infraestrutura.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_obras`. Alterações no código devem ser
> refletidas reexecutando o gerador.
