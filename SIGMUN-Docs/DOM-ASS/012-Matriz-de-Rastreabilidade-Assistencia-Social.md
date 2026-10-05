# 012 – Matriz-de-Rastreabilidade – Assistência Social

#### Matriz-de-Rastreabilidade – Assistência Social

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ASS-012

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

Este artefato detalha **a matriz de rastreabilidade** do domínio Assistência Social (`DOM-ASS`), com base na implementação material identificada em `src/modules/sigmun_assistencia_social` e no conteúdo de negócio declarado no gerador.

---

# 2. Caso de uso × história × requisito

| Caso de uso | Classe | História | Requisito | Regra |
| --- | --- | --- | --- | --- |
| CU-ASS-001 | CadastrarFamilia | HU-ASS-001 | RF-ASS-001 | RF-CUM-001 |
| CU-ASS-002 | CadastrarPessoa | HU-ASS-002 | RF-ASS-002 | RF-CUM-001 |
| CU-ASS-003 | CadastrarUnidade | HU-ASS-003 | RF-ASS-003 | RF-CUM-001 |
| CU-ASS-004 | AtualizarFamilia | HU-ASS-004 | RF-ASS-004 | RF-CUM-001 |
| CU-ASS-005 | ExcluirFamilia | HU-ASS-001 | RF-ASS-005 | RF-CUM-001 |
| CU-ASS-006 | AtualizarPessoa | HU-ASS-002 | RF-ASS-006 | RF-CUM-001 |
| CU-ASS-007 | ExcluirPessoa | HU-ASS-003 | RF-ASS-007 | RF-CUM-001 |
| CU-ASS-008 | AtualizarUnidade | HU-ASS-004 | RF-ASS-008 | RF-CUM-001 |
| CU-ASS-009 | ExcluirUnidade | HU-ASS-001 | RF-ASS-009 | RF-CUM-001 |
| CU-ASS-010 | SolicitarBeneficio | HU-ASS-002 | RF-ASS-010 | RF-CUM-001 |
| CU-ASS-011 | AprovarBeneficio | HU-ASS-003 | RF-ASS-011 | RF-CUM-001 |
| CU-ASS-012 | NegarBeneficio | HU-ASS-004 | RF-ASS-012 | RF-CUM-001 |
| CU-ASS-013 | EntregarBeneficio | HU-ASS-001 | RF-ASS-013 | RF-CUM-001 |
| CU-ASS-014 | CancelarBeneficio | HU-ASS-002 | RF-ASS-014 | RF-CUM-001 |
| CU-ASS-015 | RegistrarAtendimento | HU-ASS-003 | RF-ASS-015 | RF-CUM-001 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 012-Assistencia-Social-Matriz-de-Rastreabilidade.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
