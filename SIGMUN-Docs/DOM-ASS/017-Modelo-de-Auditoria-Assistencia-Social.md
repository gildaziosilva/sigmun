# 017 – Modelo-de-Auditoria – Assistência Social

#### Modelo-de-Auditoria – Assistência Social

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ASS-017

**Domínio:** Assistência Social

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Assistencia-Social.md`
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

Este artefato detalha **o modelo de auditoria** do domínio Assistência Social (`DOM-ASS`), com base na implementação material identificada em `src/modules/sigmun_assistencia_social` e no conteúdo de negócio declarado no gerador.

---

# 2. Colunas de auditoria

| Coluna | Presente em |
| --- | --- |
| created_at | 5 tabelas |
| created_by | 5 tabelas |
| updated_at | 5 tabelas |

---

# 3. Princípio

Toda alteração registra autor e data; a exclusão é lógica e auditável.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 017-Assistencia-Social-Modelo-de-Auditoria.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
