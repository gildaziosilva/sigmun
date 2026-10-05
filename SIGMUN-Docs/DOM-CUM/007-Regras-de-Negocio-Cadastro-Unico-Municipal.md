# 007 – Regras-de-Negocio – Cadastro Único Municipal

#### Regras-de-Negocio – Cadastro Único Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CUM-007

**Domínio:** Cadastro Único Municipal

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Cadastro-Unico-Municipal.md`
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

Este artefato detalha **as regras de negócio** do domínio Cadastro Único Municipal (`DOM-CUM`), com base na implementação material identificada em `src/modules/sigmun_cadastro` e no conteúdo de negócio declarado no gerador.

---

# 2. Regras implementadas

| Identificador | Descrição | Fonte |
| --- | --- | --- |
| RN-CUM-001 | tipo {FISICA, JURIDICA} exige extensão correspondente | `src/modules/sigmun_cadastro` |
| RN-CUM-004 | a unicidade de documento considera apenas registros | `src/modules/sigmun_cadastro` |
| RN-CUM-005 | unicidade de endereço principal vigente por pessoa | `src/modules/sigmun_cadastro` |
| RN-CUM-006 | unicidade de contato principal por tipo por pessoa | `src/modules/sigmun_cadastro` |
| RN-CUM-007 | não operar sobre excluída) | `src/modules/sigmun_cadastro` |
| RN-CUM-008 | o repositório valida ciclos profundos no save | `src/modules/sigmun_cadastro` |
| RN-CUM-009 | unicidade (desconsiderando a própria unidade) | `src/modules/sigmun_cadastro` |

---

# 3. Cobertura

Regras referenciadas no código: **7**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 007-Cadastro-Unico-Municipal-Regras-de-Negocio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
