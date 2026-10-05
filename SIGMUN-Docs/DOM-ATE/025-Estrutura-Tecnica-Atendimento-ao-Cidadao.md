# 025 – Estrutura-Tecnica – Atendimento ao Cidadão

#### Estrutura-Tecnica – Atendimento ao Cidadão

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ATE-025

**Domínio:** Atendimento ao Cidadão

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Atendimento-ao-Cidadao.md`
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

Este artefato detalha **a estrutura técnica** do domínio Atendimento ao Cidadão (`DOM-ATE`), com base na implementação material identificada em `src/modules/sigmun_ate` e no conteúdo de negócio declarado no gerador.

---

# 2. Módulo `sigmun_ate`

| Arquivo | Linhas |
| --- | --- |
| `src/modules/sigmun_ate/application/commands/__init__.py` | 129 |
| `src/modules/sigmun_ate/application/interfaces/__init__.py` | 251 |
| `src/modules/sigmun_ate/application/queries/__init__.py` | 283 |
| `src/modules/sigmun_ate/application/use_cases/__init__.py` | 845 |
| `src/modules/sigmun_ate/domain/entities/__init__.py` | 707 |
| `src/modules/sigmun_ate/domain/events/__init__.py` | 201 |
| `src/modules/sigmun_ate/domain/exceptions/__init__.py` | 199 |
| `src/modules/sigmun_ate/domain/services/__init__.py` | 262 |
| `src/modules/sigmun_ate/domain/value_objects/__init__.py` | 107 |
| `src/modules/sigmun_ate/infrastructure/database/models.py` | 271 |
| `src/modules/sigmun_ate/infrastructure/database/repositories.py` | 527 |
| `src/modules/sigmun_ate/infrastructure/messaging/__init__.py` | 129 |
| `src/modules/sigmun_ate/presentation/api/__init__.py` | 615 |
| `src/modules/sigmun_ate/presentation/schemas/__init__.py` | 341 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 025-Atendimento-ao-Cidadao-Estrutura-Tecnica.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
