# 025 – Estrutura-Tecnica – Planejamento Governamental

#### Estrutura-Tecnica – Planejamento Governamental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PLA-025

**Domínio:** Planejamento Governamental

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Planejamento-Governamental.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `030-Roadmap-de-Implementacao-dos-Dominios.md`
* `Mapa-de-Dominios.md`

---


# 1. Finalidade

Este artefato descreve **a estrutura técnica** do domínio Planejamento Governamental (`DOM-PLA`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Módulo `sigmun_planejamento`

| Arquivo | Linhas |
| --- | --- |
| `src/modules/sigmun_planejamento/__init__.py` | 1 |
| `src/modules/sigmun_planejamento/application/commands/__init__.py` | 1 |
| `src/modules/sigmun_planejamento/application/queries/__init__.py` | 1 |
| `src/modules/sigmun_planejamento/application/use_cases/__init__.py` | 1 |
| `src/modules/sigmun_planejamento/domain/entities/__init__.py` | 1 |
| `src/modules/sigmun_planejamento/domain/events/__init__.py` | 1 |
| `src/modules/sigmun_planejamento/domain/services/__init__.py` | 1 |
| `src/modules/sigmun_planejamento/domain/value_objects/__init__.py` | 1 |
| `src/modules/sigmun_planejamento/infrastructure/database/__init__.py` | 1 |
| `src/modules/sigmun_planejamento/infrastructure/integrations/__init__.py` | 1 |
| `src/modules/sigmun_planejamento/infrastructure/repositories/__init__.py` | 1 |
| `src/modules/sigmun_planejamento/presentation/api/__init__.py` | 1 |
| `src/modules/sigmun_planejamento/presentation/schemas/__init__.py` | 1 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 025-Planejamento-Governamental-Estrutura-Tecnica.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
