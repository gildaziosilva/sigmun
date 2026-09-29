# 012 – Matriz de Rastreabilidade – Cadastro Imobiliário

#### Matriz de Rastreabilidade – Cadastro Imobiliário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IMO-012

**Domínio:** Cadastro Imobiliário

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Cadastro-Imobiliario.md`
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
domínio de Cadastro Imobiliário está rastreada ao código e aos testes correspondentes.

---

# 2. Princípio de Rastreabilidade

* Nenhum requisito existe sem capacidade, história e regra associadas.
* Nenhuma regra existe sem teste que a exercite.
* Nenhuma entidade de domínio existe sem operação que a persista.

---

# 3. Rastreabilidade por Capacidade

| Capacidade | Histórias | Requisitos | Regras | Entidades |
| --- | | --- | | --- | | --- | |
| CAP-IMO-001 — Cadastro de lotes | HU-IMO-001 | RF-IMO-001, RF-IMO-002, RF-IMO-007 | RN-IMO-001, RN-IMO-002, RN-IMO-003 | Imovel, CaracteristicaImovel |
| CAP-IMO-002 — Titularidade do imóvel | HU-IMO-002 | RF-IMO-004 | RN-IMO-006 | ProprietarioImovel |
| CAP-IMO-003 — Ciclo de vida do imóvel | HU-IMO-003 | RF-IMO-003 | RN-IMO-004 | Imovel |
| CAP-IMO-004 — Avaliação do valor venal | HU-IMO-004 | RF-IMO-005, RF-IMO-006 | RN-IMO-005 | AvaliacaoImovel |
| CAP-IMO-005 — Consulta e contestação cadastral | — | — | RN-IMO-001, RN-IMO-005 | Imovel, AvaliacaoImovel |
| CAP-IMO-006 — Georreferenciamento do lote | HU-IMO-005 | RF-IMO-008 | RN-IMO-007 | GeometriaImovel |

---

# 4. Rastreabilidade por História de Usuário

| História | Capacidade | Casos de uso | Critérios | Testes |
| --- | | --- | | --- | | --- | |
| HU-IMO-001 | CAP-IMO-001 | CU-IMO-001 | 3 | 0 teste(s) |
| HU-IMO-002 | CAP-IMO-002 | CU-IMO-002 | 4 | 0 teste(s) |
| HU-IMO-003 | CAP-IMO-003 | CU-IMO-003 | 3 | 0 teste(s) |
| HU-IMO-004 | CAP-IMO-004 | CU-IMO-004 | 3 | 0 teste(s) |
| HU-IMO-005 | CAP-IMO-006 | CU-IMO-006 | 3 | 0 teste(s) |

---

# 5. Rastreabilidade por Requisito Funcional

| Requisito | Capacidade | Regras | Operações | Testada por |
| --- | | --- | | --- | | --- | |
| RF-IMO-001 | CAP-IMO-001 | RN-IMO-001, RN-IMO-002, RN-IMO-003 | 5 | 0 teste(s) |
| RF-IMO-002 | CAP-IMO-001 | RN-IMO-001 | 3 | 0 teste(s) |
| RF-IMO-003 | CAP-IMO-003 | RN-IMO-004 | 1 | 0 teste(s) |
| RF-IMO-004 | CAP-IMO-002 | RN-IMO-006 | 4 | 0 teste(s) |
| RF-IMO-005 | CAP-IMO-004 | RN-IMO-005 | 2 | 0 teste(s) |
| RF-IMO-006 | CAP-IMO-004 | RN-IMO-005 | 4 | 0 teste(s) |
| RF-IMO-007 | CAP-IMO-001 | RN-IMO-003 | 3 | 0 teste(s) |
| RF-IMO-008 | CAP-IMO-006 | RN-IMO-007 | 3 | 0 teste(s) |

---

# 6. Cobertura

| Indicador | Quantidade |
| --- | |
| Capacidades | 6 |
| Histórias de usuário | 5 |
| Casos de uso | 6 |
| Requisitos funcionais | 8 |
| Requisitos não funcionais | 7 |
| Regras de negócio | 7 |
| Classes de teste | 6 |
| Testes de unidade | 58 |

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

**Documento:** 012-Matriz-de-Rastreabilidade-Cadastro-Imobiliario.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_cadastro_imobiliario`. Alterações no código devem ser
> refletidas reexecutando o gerador.
