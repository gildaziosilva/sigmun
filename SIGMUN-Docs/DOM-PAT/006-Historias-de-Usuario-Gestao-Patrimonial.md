# 006 – Historias-de-Usuario – Gestão Patrimonial

#### Historias-de-Usuario – Gestão Patrimonial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PAT-006

**Domínio:** Gestão Patrimonial

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Patrimonial.md`
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

Este artefato detalha **as histórias de usuário** do domínio Gestão Patrimonial (`DOM-PAT`), com base na implementação material identificada em `src/modules/sigmun_patrimonio` e no conteúdo de negócio declarado no gerador.

---

# 2. Histórias

| Identificador | História | Capacidade | Prioridade |
| --- | --- | --- | --- |
| HU-PAT-001 | Como servidor, quero cadastrar o bem com valor para compor o patrimônio. | CAP-PAT-001 | Alta |
| HU-PAT-002 | Como servidor, quero lançar a depreciação para atualizar o valor contábil. | CAP-PAT-002 | Média |
| HU-PAT-003 | Como gestor, quero transferir o bem para outra unidade. | CAP-PAT-003 | Média |
| HU-PAT-004 | Como contabilidade, quero ver o bem com valor atualizado na baixa. | CAP-PAT-004 | Média |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 006-Gestao-Patrimonial-Historias-de-Usuario.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
