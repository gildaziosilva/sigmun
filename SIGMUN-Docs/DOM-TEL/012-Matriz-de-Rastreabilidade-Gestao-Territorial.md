# 012 – Matriz de Rastreabilidade – Gestão Territorial

#### Matriz de Rastreabilidade – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-012

**Domínio:** Gestão Territorial

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Territorial.md`
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
domínio de Gestão Territorial está rastreada ao código e aos testes correspondentes.

---

# 2. Princípio de Rastreabilidade

* Nenhum requisito existe sem capacidade, história e regra associadas.
* Nenhuma regra existe sem teste que a exercite.
* Nenhuma entidade de domínio existe sem operação que a persista.

---

# 3. Rastreabilidade por Capacidade

| Capacidade | Histórias | Requisitos | Regras | Entidades |
| --- | | --- | | --- | | --- | |
| CAP-TEL-001 — Cadastro de divisões territoriais | HU-TEL-001 | RF-TEL-001, RF-TEL-002 | RN-TEL-001, RN-TEL-006 | Bairro |
| CAP-TEL-002 — Cadastro de logradouros públicos | HU-TEL-002 | RF-TEL-003, RF-TEL-004 | RN-TEL-002, RN-TEL-006 | Logradouro |
| CAP-TEL-003 — Gestão da planta genérica de valores | HU-TEL-003 | RF-TEL-005, RF-TEL-006, RF-TEL-007, RF-TEL-009 | RN-TEL-003, RN-TEL-004 | PlantaGenericaValores |
| CAP-TEL-004 — Consulta de valores vigentes | HU-TEL-004 | RF-TEL-008 | RN-TEL-003 | PlantaGenericaValores |
| CAP-TEL-005 — Georreferenciamento territorial | HU-TEL-005 | RF-TEL-010, RF-TEL-011 | RN-TEL-005 | Georreferencia |

---

# 4. Rastreabilidade por História de Usuário

| História | Capacidade | Casos de uso | Critérios | Testes |
| --- | | --- | | --- | | --- | |
| HU-TEL-001 | CAP-TEL-001 | CU-TEL-001, CU-TEL-002, CU-TEL-003 | 3 | 0 teste(s) |
| HU-TEL-002 | CAP-TEL-002 | CU-TEL-004 | 3 | 0 teste(s) |
| HU-TEL-003 | CAP-TEL-003 | CU-TEL-005, CU-TEL-006, CU-TEL-007 | 5 | 0 teste(s) |
| HU-TEL-004 | CAP-TEL-004 | CU-TEL-008 | 2 | 0 teste(s) |
| HU-TEL-005 | CAP-TEL-005 | CU-TEL-009 | 4 | 0 teste(s) |

---

# 5. Rastreabilidade por Requisito Funcional

| Requisito | Capacidade | Regras | Operações | Testada por |
| --- | | --- | | --- | | --- | |
| RF-TEL-001 | CAP-TEL-001 | RN-TEL-001, RN-TEL-006 | 5 | 0 teste(s) |
| RF-TEL-002 | CAP-TEL-001 | RN-TEL-001 | 1 | 0 teste(s) |
| RF-TEL-003 | CAP-TEL-002 | RN-TEL-002, RN-TEL-006 | 5 | 0 teste(s) |
| RF-TEL-004 | CAP-TEL-002 | RN-TEL-002 | 1 | 0 teste(s) |
| RF-TEL-005 | CAP-TEL-003 | RN-TEL-003, RN-TEL-004 | 1 | 0 teste(s) |
| RF-TEL-006 | CAP-TEL-003 | RN-TEL-004 | 2 | 0 teste(s) |
| RF-TEL-007 | CAP-TEL-003 | RN-TEL-004 | 1 | 0 teste(s) |
| RF-TEL-008 | CAP-TEL-004 | RN-TEL-003 | 1 | 0 teste(s) |
| RF-TEL-009 | CAP-TEL-003 | — | 2 | — |
| RF-TEL-010 | CAP-TEL-005 | RN-TEL-005 | 4 | 0 teste(s) |
| RF-TEL-011 | CAP-TEL-005 | RN-TEL-005 | 1 | 0 teste(s) |

---

# 6. Cobertura

| Indicador | Quantidade |
| --- | |
| Capacidades | 5 |
| Histórias de usuário | 5 |
| Casos de uso | 9 |
| Requisitos funcionais | 11 |
| Requisitos não funcionais | 7 |
| Regras de negócio | 6 |
| Classes de teste | 4 |
| Testes de unidade | 62 |

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

**Documento:** 012-Matriz-de-Rastreabilidade-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
