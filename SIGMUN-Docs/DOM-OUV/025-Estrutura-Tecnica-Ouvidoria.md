# 025 – Estrutura-Tecnica – Ouvidoria

#### Estrutura-Tecnica – Ouvidoria

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OUV-025

**Domínio:** Ouvidoria

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Ouvidoria.md`
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

Este artefato detalha **a estrutura técnica** do domínio Ouvidoria (`DOM-OUV`), com base na implementação material identificada em `src/modules/sigmun_ouvidoria` e no conteúdo de negócio declarado no gerador.

---

# 2. Módulo `sigmun_ouvidoria`

| Arquivo | Linhas |
| --- | --- |
| `src/modules/sigmun_ouvidoria/__init__.py` | 1 |
| `src/modules/sigmun_ouvidoria/application/commands/__init__.py` | 1 |
| `src/modules/sigmun_ouvidoria/application/interfaces.py` | 212 |
| `src/modules/sigmun_ouvidoria/application/queries/__init__.py` | 1 |
| `src/modules/sigmun_ouvidoria/application/use_cases/__init__.py` | 732 |
| `src/modules/sigmun_ouvidoria/domain/entities/__init__.py` | 367 |
| `src/modules/sigmun_ouvidoria/domain/events/__init__.py` | 147 |
| `src/modules/sigmun_ouvidoria/domain/exceptions.py` | 52 |
| `src/modules/sigmun_ouvidoria/domain/services/__init__.py` | 264 |
| `src/modules/sigmun_ouvidoria/domain/value_objects/__init__.py` | 319 |
| `src/modules/sigmun_ouvidoria/infrastructure/database/__init__.py` | 304 |
| `src/modules/sigmun_ouvidoria/infrastructure/integrations/__init__.py` | 1 |
| `src/modules/sigmun_ouvidoria/infrastructure/repositories/__init__.py` | 1172 |
| `src/modules/sigmun_ouvidoria/presentation/api/__init__.py` | 856 |
| `src/modules/sigmun_ouvidoria/presentation/schemas/__init__.py` | 357 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 025-Ouvidoria-Estrutura-Tecnica.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
