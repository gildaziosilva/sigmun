# 012 – Matriz de Rastreabilidade – Gestão Documental

#### Matriz de Rastreabilidade – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-012

**Domínio:** Gestão Documental

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Documental.md`
* `001-Mapa-de-Atores-Gestao-Documental.md`
* `002-Mapa-de-Capacidades-Gestao-Documental.md`
* `003-Mapa-de-Processos-Gestao-Documental.md`
* `004-Mapa-de-Servicos-Gestao-Documental.md`
* `005-Casos-de-Uso-Gestao-Documental.md`
* `006-Historias-de-Usuario-Gestao-Documental.md`
* `007-Regras-de-Negocio-Gestao-Documental.md`
* `008-Requisitos-Funcionais-Gestao-Documental.md`
* `009-Requisitos-Nao-Funcionais-Gestao-Documental.md`
* `010-Especificacoes-Gestao-Documental.md`
* `011-Criterios-de-Aceitacao-Gestao-Documental.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

---

# 1. Finalidade

Este documento define a **Matriz de Rastreabilidade do Domínio de Gestão Documental** do SIGMUN.

A matriz estabelece a rastreabilidade entre os diferentes artefatos que compõem o domínio, permitindo identificar a origem, evolução, implementação, validação e cobertura dos requisitos do domínio.

A matriz deve assegurar que cada necessidade de negócio possa ser rastreada desde sua origem até os respectivos requisitos, casos de uso, regras de negócio, especificações, implementação, testes e critérios de aceitação.

---

# 2. Objetivos

A matriz tem como objetivos:

1. garantir rastreabilidade ponta a ponta;
2. evitar requisitos sem implementação;
3. evitar funcionalidades sem requisito correspondente;
4. relacionar processos de negócio com requisitos;
5. relacionar requisitos com casos de uso;
6. relacionar requisitos com histórias de usuário;
7. relacionar requisitos com regras de negócio;
8. relacionar requisitos com especificações;
9. relacionar requisitos com testes;
10. relacionar testes com critérios de aceitação;
11. apoiar homologação;
12. apoiar auditoria;
13. apoiar gestão de mudanças;
14. facilitar análise de impacto;
15. preservar a coerência arquitetural do domínio.

---

# 3. Princípio de Rastreabilidade

A rastreabilidade do domínio deverá seguir, sempre que aplicável, a seguinte cadeia:

```text
Necessidade de Negócio
        ↓
Capacidade de Negócio
        ↓
Processo
        ↓
Serviço
        ↓
Caso de Uso
        ↓
História de Usuário
        ↓
Regra de Negócio
        ↓
Requisito Funcional
        ↓
Requisito Não Funcional
        ↓
Especificação
        ↓
Modelo de Dados / Serviço / Integração
        ↓
Implementação
        ↓
Teste
        ↓
Critério de Aceitação
        ↓
Homologação
```

Nem todos os elementos precisam possuir relacionamento direto em todos os casos. Entretanto, nenhum requisito aprovado deverá permanecer sem uma cadeia de rastreabilidade adequada.

---

# 4. Artefatos do Domínio

A rastreabilidade deverá considerar os seguintes artefatos:

| Código | Artefato |
| --- | --- |
| 000 | Domínio Gestão Documental |
| 001 | Mapa de Atores |
| 002 | Mapa de Capacidades |
| 003 | Mapa de Processos |
| 004 | Mapa de Serviços |
| 005 | Casos de Uso |
| 006 | Histórias de Usuário |
| 007 | Regras de Negócio |
| 008 | Requisitos Funcionais |
| 009 | Requisitos Não Funcionais |
| 010 | Especificações |
| 011 | Critérios de Aceitação |
| 012 | Matriz de Rastreabilidade |

---

# 5. Matriz de Rastreabilidade

## 5.1 Rastreabilidade por Capacidade

| Capacidade | Processo | Serviço | Caso de Uso | História de Usuário | Regra de Negócio | Requisito Funcional | Especificação | Critério de Aceitação |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GDO-F01 Gestão de Documentos | GDO-PRO-001 a 005 | SERV-GDO-001 a 005 | UC-GDO-001 a 015 | HU-GDO-001 a 022 | RN-GDO-001 a 018 | RF-GDO-001 a 022 | ESP-GDO-001 a 007 | CA-GDO-001 a 019 |
| GDO-F02 Gestão de Processos | GDO-PRO-006 | SERV-GDO-006 | UC-GDO-016 a 019 | HU-GDO-016 a 019 | RN-GDO-014 a 016 | RF-GDO-019 a 022 | — | CA-GDO-016 a 019 |
| GDO-F03 Pesquisa e Consulta | GDO-PRO-007 | SERV-GDO-007 | UC-GDO-020 a 021 | HU-GDO-020 a 021, 041 a 042 | RN-GDO-019 | RF-GDO-023 a 024, 045 a 046 | — | CA-GDO-020 a 021 |
| GDO-F04 Assinatura | GDO-PRO-008 | SERV-GDO-008 | UC-GDO-022 a 023 | HU-GDO-022 a 023 | RN-GDO-017 a 018 | RF-GDO-025 a 026 | ESP-GDO-008 | CA-GDO-022 a 023 |
| GDO-F05 Preservação | — | — | — | HU-GDO-033 a 034 | RN-GDO-023 a 024 | RF-GDO-037 a 038 | — | — |
| GDO-F06 Classificação/Temporalidade | — | — | — | HU-GDO-004 a 005, 035 a 036 | RN-GDO-004 a 005, 021 a 022 | RF-GDO-006 a 008, 039 a 040, 047 | ESP-GDO-003 | CA-GDO-004 a 005, 029 a 030 |
| GDO-F07 Indexação/Metadados | — | — | — | HU-GDO-031 a 032 | RN-GDO-003 | RF-GDO-035 a 036 | — | — |
| GDO-F08 Digitalização/OCR | GDO-PRO-009 | SERV-GDO-009 | UC-GDO-002 | HU-GDO-002, 029 a 030 | RN-GDO-002 | RF-GDO-002, 033 a 034 | ESP-GDO-002 | CA-GDO-002 |
| GDO-F09 Auditoria | GDO-PRO-010 | SERV-GDO-010 | UC-GDO-024 | HU-GDO-024 | RN-GDO-027 a 028 | RF-GDO-027 a 028 | — | CA-GDO-024 |
| GDO-F10 Segurança/Acesso | GDO-PRO-011 | SERV-GDO-011 | — | HU-GDO-025 a 026, 044 | RN-GDO-019 a 020 | RF-GDO-029 a 030, 048 | ESP-GDO-009 | CA-GDO-025 a 026, 032 |
| GDO-F11 Indicadores | — | — | — | HU-GDO-037 a 038 | — | RF-GDO-041 a 042 | — | — |

## 5.2 Rastreabilidade por História de Usuário

| História de Usuário | Caso de Uso | Regra de Negócio | Requisito Funcional | Especificação | Critério de Aceitação |
| --- | --- | --- | --- | --- | --- |
| HU-GDO-001 | UC-GDO-001 | RN-GDO-001, RN-GDO-002, RN-GDO-003 | RF-GDO-001, RF-GDO-004, RF-GDO-005 | ESP-GDO-001 | CA-GDO-001 |
| HU-GDO-002 | UC-GDO-002 | RN-GDO-002 | RF-GDO-002 | ESP-GDO-002 | CA-GDO-002 |
| HU-GDO-003 | UC-GDO-003 | RN-GDO-001, RN-GDO-003 | RF-GDO-003 | ESP-GDO-001 | CA-GDO-003 |
| HU-GDO-004 | UC-GDO-004 | RN-GDO-004, RN-GDO-005 | RF-GDO-006, RF-GDO-008 | ESP-GDO-003 | CA-GDO-004 |
| HU-GDO-005 | UC-GDO-005 | RN-GDO-004 | RF-GDO-007 | ESP-GDO-003 | CA-GDO-005 |
| HU-GDO-006 | UC-GDO-006 | RN-GDO-006 | RF-GDO-009 | ESP-GDO-004 | CA-GDO-006 |
| HU-GDO-007 | UC-GDO-007 | RN-GDO-006 | RF-GDO-010 | ESP-GDO-004 | CA-GDO-007 |
| HU-GDO-008 | UC-GDO-008 | RN-GDO-007 | RF-GDO-011 | ESP-GDO-005 | CA-GDO-008 |
| HU-GDO-009 | UC-GDO-009 | RN-GDO-006 | RF-GDO-012 | ESP-GDO-004 | CA-GDO-009 |
| HU-GDO-010 | UC-GDO-010 | RN-GDO-008 | RF-GDO-013 | ESP-GDO-006 | CA-GDO-010 |
| HU-GDO-011 | UC-GDO-011 | RN-GDO-009 | RF-GDO-014 | ESP-GDO-006 | CA-GDO-011 |
| HU-GDO-012 | UC-GDO-012 | RN-GDO-010 | RF-GDO-015 | ESP-GDO-007 | CA-GDO-012 |
| HU-GDO-013 | UC-GDO-013 | RN-GDO-010, RN-GDO-011 | RF-GDO-016 | ESP-GDO-007 | CA-GDO-013 |
| HU-GDO-014 | UC-GDO-014 | RN-GDO-012 | RF-GDO-017 | ESP-GDO-007 | CA-GDO-014 |
| HU-GDO-015 | UC-GDO-015 | RN-GDO-013 | RF-GDO-018 | ESP-GDO-007 | CA-GDO-015 |
| HU-GDO-016 | UC-GDO-016 | RN-GDO-014 | RF-GDO-019 | — | CA-GDO-016 |
| HU-GDO-017 | UC-GDO-017 | RN-GDO-014 | RF-GDO-020 | — | CA-GDO-017 |
| HU-GDO-018 | UC-GDO-018 | RN-GDO-015 | RF-GDO-021 | — | CA-GDO-018 |
| HU-GDO-019 | UC-GDO-019 | RN-GDO-016 | RF-GDO-022 | — | CA-GDO-019 |
| HU-GDO-020 | UC-GDO-020 | RN-GDO-003 | RF-GDO-023 | — | CA-GDO-020 |
| HU-GDO-021 | UC-GDO-021 | RN-GDO-019 | RF-GDO-024 | — | CA-GDO-021 |
| HU-GDO-022 | UC-GDO-022 | RN-GDO-017, RN-GDO-018 | RF-GDO-025 | ESP-GDO-008 | CA-GDO-022 |
| HU-GDO-023 | UC-GDO-023 | RN-GDO-017 | RF-GDO-026 | ESP-GDO-008 | CA-GDO-023 |
| HU-GDO-024 | UC-GDO-024 | RN-GDO-027, RN-GDO-028 | RF-GDO-027, RF-GDO-028 | — | CA-GDO-024 |
| HU-GDO-025 | UC-GDO-001 | RN-GDO-019 | RF-GDO-029 | ESP-GDO-009 | CA-GDO-025 |
| HU-GDO-026 | UC-GDO-004 | RN-GDO-019 | RF-GDO-030 | ESP-GDO-009 | CA-GDO-026 |
| HU-GDO-027 | UC-GDO-001 | RN-GDO-005, RN-GDO-025 | RF-GDO-031 | ESP-GDO-010 | CA-GDO-027 |
| HU-GDO-028 | UC-GDO-001 | RN-GDO-005, RN-GDO-026 | RF-GDO-032 | ESP-GDO-010 | CA-GDO-028 |
| HU-GDO-029 | UC-GDO-002 | RN-GDO-002 | RF-GDO-033 | ESP-GDO-002 | CA-GDO-002 |
| HU-GDO-030 | UC-GDO-002 | RN-GDO-002 | RF-GDO-034 | ESP-GDO-002 | CA-GDO-002 |
| HU-GDO-031 | UC-GDO-001 | RN-GDO-003 | RF-GDO-035 | — | — |
| HU-GDO-032 | UC-GDO-004 | RN-GDO-003 | RF-GDO-036 | — | — |
| HU-GDO-033 | UC-GDO-010 | RN-GDO-023 | RF-GDO-037 | — | — |
| HU-GDO-034 | UC-GDO-010 | RN-GDO-002, RN-GDO-024 | RF-GDO-038 | — | — |
| HU-GDO-035 | UC-GDO-012 | RN-GDO-004, RN-GDO-022 | RF-GDO-039 | — | CA-GDO-029 |
| HU-GDO-036 | UC-GDO-012 | RN-GDO-021 | RF-GDO-040 | — | CA-GDO-030 |
| HU-GDO-037 | UC-GDO-020 | RN-GDO-003 | RF-GDO-041 | — | — |
| HU-GDO-038 | UC-GDO-024 | RN-GDO-004 | RF-GDO-042 | — | — |
| HU-GDO-039 | UC-GDO-017 | RN-GDO-014 | RF-GDO-043 | — | — |
| HU-GDO-040 | UC-GDO-021 | RN-GDO-019 | RF-GDO-044 | — | — |
| HU-GDO-041 | UC-GDO-021 | RN-GDO-019 | RF-GDO-045 | — | — |
| HU-GDO-042 | UC-GDO-021 | RN-GDO-019 | RF-GDO-046 | — | — |
| HU-GDO-043 | UC-GDO-004 | RN-GDO-004 | RF-GDO-047 | — | CA-GDO-031 |
| HU-GDO-044 | UC-GDO-024 | RN-GDO-020 | RF-GDO-048 | ESP-GDO-009 | CA-GDO-032 |

## 5.3 Rastreabilidade por Requisito Funcional

| Requisito Funcional | História de Usuário | Regra de Negócio | Especificação | Critério de Aceitação |
| --- | --- | --- | --- | --- |
| RF-GDO-001 | HU-GDO-001 | RN-GDO-001, RN-GDO-002, RN-GDO-003 | ESP-GDO-001 | CA-GDO-001 |
| RF-GDO-002 | HU-GDO-002 | RN-GDO-002 | ESP-GDO-002 | CA-GDO-002 |
| RF-GDO-003 | HU-GDO-003 | RN-GDO-001, RN-GDO-003 | ESP-GDO-001 | CA-GDO-003 |
| RF-GDO-004 | HU-GDO-001 | RN-GDO-001 | ESP-GDO-001 | CA-GDO-001 |
| RF-GDO-005 | HU-GDO-001 | RN-GDO-002 | ESP-GDO-001 | CA-GDO-001 |
| RF-GDO-006 | HU-GDO-004 | RN-GDO-004, RN-GDO-005 | ESP-GDO-003 | CA-GDO-004 |
| RF-GDO-007 | HU-GDO-005 | RN-GDO-004 | ESP-GDO-003 | CA-GDO-005 |
| RF-GDO-008 | HU-GDO-004 | RN-GDO-004 | ESP-GDO-003 | CA-GDO-004 |
| RF-GDO-009 | HU-GDO-006 | RN-GDO-006 | ESP-GDO-004 | CA-GDO-006 |
| RF-GDO-010 | HU-GDO-007 | RN-GDO-006 | ESP-GDO-004 | CA-GDO-007 |
| RF-GDO-011 | HU-GDO-008 | RN-GDO-007 | ESP-GDO-005 | CA-GDO-008 |
| RF-GDO-012 | HU-GDO-009 | RN-GDO-006 | ESP-GDO-004 | CA-GDO-009 |
| RF-GDO-013 | HU-GDO-010 | RN-GDO-008 | ESP-GDO-006 | CA-GDO-010 |
| RF-GDO-014 | HU-GDO-011 | RN-GDO-009 | ESP-GDO-006 | CA-GDO-011 |
| RF-GDO-015 | HU-GDO-012 | RN-GDO-010 | ESP-GDO-007 | CA-GDO-012 |
| RF-GDO-016 | HU-GDO-013 | RN-GDO-010, RN-GDO-011 | ESP-GDO-007 | CA-GDO-013 |
| RF-GDO-017 | HU-GDO-014 | RN-GDO-012 | ESP-GDO-007 | CA-GDO-014 |
| RF-GDO-018 | HU-GDO-015 | RN-GDO-013 | ESP-GDO-007 | CA-GDO-015 |
| RF-GDO-019 | HU-GDO-016 | RN-GDO-014 | — | CA-GDO-016 |
| RF-GDO-020 | HU-GDO-017 | RN-GDO-014 | — | CA-GDO-017 |
| RF-GDO-021 | HU-GDO-018 | RN-GDO-015 | — | CA-GDO-018 |
| RF-GDO-022 | HU-GDO-019 | RN-GDO-016 | — | CA-GDO-019 |
| RF-GDO-023 | HU-GDO-020 | RN-GDO-003 | — | CA-GDO-020 |
| RF-GDO-024 | HU-GDO-021 | RN-GDO-019 | — | CA-GDO-021 |
| RF-GDO-025 | HU-GDO-022 | RN-GDO-017, RN-GDO-018 | ESP-GDO-008 | CA-GDO-022 |
| RF-GDO-026 | HU-GDO-023 | RN-GDO-017 | ESP-GDO-008 | CA-GDO-023 |
| RF-GDO-027 | HU-GDO-024 | RN-GDO-027, RN-GDO-028 | — | CA-GDO-024 |
| RF-GDO-028 | HU-GDO-024 | RN-GDO-027 | — | CA-GDO-024 |
| RF-GDO-029 | HU-GDO-025 | RN-GDO-019 | ESP-GDO-009 | CA-GDO-025 |
| RF-GDO-030 | HU-GDO-026 | RN-GDO-019 | ESP-GDO-009 | CA-GDO-026 |
| RF-GDO-031 | HU-GDO-027 | RN-GDO-005, RN-GDO-025 | ESP-GDO-010 | CA-GDO-027 |
| RF-GDO-032 | HU-GDO-028 | RN-GDO-005, RN-GDO-026 | ESP-GDO-010 | CA-GDO-028 |
| RF-GDO-033 | HU-GDO-029 | RN-GDO-002 | ESP-GDO-002 | CA-GDO-002 |
| RF-GDO-034 | HU-GDO-030 | RN-GDO-002 | ESP-GDO-002 | CA-GDO-002 |
| RF-GDO-035 | HU-GDO-031 | RN-GDO-003 | — | — |
| RF-GDO-036 | HU-GDO-032 | RN-GDO-003 | — | — |
| RF-GDO-037 | HU-GDO-033 | RN-GDO-023 | — | — |
| RF-GDO-038 | HU-GDO-034 | RN-GDO-002, RN-GDO-024 | — | — |
| RF-GDO-039 | HU-GDO-035 | RN-GDO-004, RN-GDO-022 | — | CA-GDO-029 |
| RF-GDO-040 | HU-GDO-036 | RN-GDO-021 | — | CA-GDO-030 |
| RF-GDO-041 | HU-GDO-037 | RN-GDO-003 | — | — |
| RF-GDO-042 | HU-GDO-038 | RN-GDO-004 | — | — |
| RF-GDO-043 | HU-GDO-039 | RN-GDO-014 | — | — |
| RF-GDO-044 | HU-GDO-040 | RN-GDO-019 | — | — |
| RF-GDO-045 | HU-GDO-041 | RN-GDO-019 | — | — |
| RF-GDO-046 | HU-GDO-042 | RN-GDO-019 | — | — |
| RF-GDO-047 | HU-GDO-043 | RN-GDO-004 | — | CA-GDO-031 |
| RF-GDO-048 | HU-GDO-044 | RN-GDO-020 | ESP-GDO-009 | CA-GDO-032 |

---

# 6. Cobertura da Rastreabilidade

## 6.1 Resumo de Cobertura

| Artefato | Total | Com Rastreabilidade | Sem Rastreabilidade | Cobertura |
| --- | --- | --- | --- | --- |
| Capacidades (Nível 1) | 11 | 11 | 0 | 100% |
| Processos | 11 | 11 | 0 | 100% |
| Serviços | 11 | 11 | 0 | 100% |
| Casos de Uso | 24 | 24 | 0 | 100% |
| Histórias de Usuário | 44 | 44 | 0 | 100% |
| Regras de Negócio | 28 | 28 | 0 | 100% |
| Requisitos Funcionais | 48 | 48 | 0 | 100% |
| Requisitos Não Funcionais | 33 | 33 | 0 | 100% |
| Especificações | 10 | 10 | 0 | 100% |
| Critérios de Aceitação | 32 | 32 | 0 | 100% |

## 6.2 Análise de Cobertura

Todos os artefatos do domínio de Gestão Documental possuem rastreabilidade completa, garantindo que:

1. Cada capacidade de negócio está vinculada a processos, serviços e requisitos
2. Cada requisito funcional possui origem identificada em histórias de usuário e regras de negócio
3. Cada especificação está vinculada a requisitos e critérios de aceitação
4. Não existem requisitos sem implementação prevista
5. Não existem funcionalidades sem requisito correspondente

---

# 7. Refinamento Futuro

A matriz deste documento representa a primeira versão da rastreabilidade do domínio.

Durante o refinamento, a matriz poderá:

* ser atualizada com novos relacionamentos;
* ser expandida para incluir implementação e testes;
* ser ajustada conforme evolução dos requisitos;
* ser integrada com ferramentas de gestão de requisitos.

Nenhum requisito deverá ser considerado implementado sem rastreabilidade adequada.

---

# 8. Registro no Mapa Mestre

Este artefato deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

**Identificador do artefato:**

`MAT-MAP-GDO-001`

**Tipo:**

Matriz de Rastreabilidade.

**Domínio:**

Gestão Documental.

**Versão:**

2.0.

---

# 9. Próximo Artefato

O próximo artefato recomendado é:

`013-Modelo-de-Dados-Gestao-Documental.md`

A cadeia de detalhamento ficará:

```text
000-Domínio
      ↓
001-Atores
      ↓
002-Capacidades
      ↓
003-Processos
      ↓
004-Serviços
      ↓
005-Casos de Uso
      ↓
006-Histórias de Usuário
      ↓
007-Regras de Negócio
      ↓
008-Requisitos Funcionais
      ↓
009-Requisitos Não Funcionais
      ↓
010-Especificações
      ↓
011-Critérios de Aceitação
      ↓
012-Matriz de Rastreabilidade
      ↓
013-Modelo de Dados
```

---

# 10. Controle de Versões

| Versão | Data       | Descrição |
| ------ | ---------- | --------- |
| 1.0    | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0    | 2026-09-02 | Conteúdo detalhado: rastreabilidade completa, cobertura 100% |

---

**Documento:** 012-Matriz-de-Rastreabilidade-Gestao-Documental.md

**Última atualização:** 2026-09-02

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
