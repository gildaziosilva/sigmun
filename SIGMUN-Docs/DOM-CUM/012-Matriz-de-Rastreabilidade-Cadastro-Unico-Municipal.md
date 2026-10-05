# 012 – Matriz-de-Rastreabilidade – Cadastro Único Municipal

#### Matriz-de-Rastreabilidade – Cadastro Único Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CUM-012

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

Este artefato detalha **a matriz de rastreabilidade** do domínio Cadastro Único Municipal (`DOM-CUM`), com base na implementação material identificada em `src/modules/sigmun_cadastro` e no conteúdo de negócio declarado no gerador.

---

# 2. Caso de uso × história × requisito

| Caso de uso | Classe | História | Requisito | Regra |
| --- | --- | --- | --- | --- |
| CU-CUM-001 | RegistrarPessoa | HU-CUM-001 | RF-CUM-001 | RF-CUM-001 |
| CU-CUM-002 | ConsultarPessoa | HU-CUM-002 | RF-CUM-002 | RF-CUM-001 |
| CU-CUM-003 | ListarPessoas | HU-CUM-003 | RF-CUM-003 | RF-CUM-001 |
| CU-CUM-004 | AtualizarPessoaFisica | HU-CUM-004 | RF-CUM-004 | RF-CUM-001 |
| CU-CUM-005 | AtualizarPessoaJuridica | HU-CUM-005 | RF-CUM-005 | RF-CUM-001 |
| CU-CUM-006 | AlterarCategoriaPessoa | HU-CUM-006 | RF-CUM-006 | RF-CUM-001 |
| CU-CUM-007 | ExcluirPessoa | HU-CUM-007 | RF-CUM-007 | RF-CUM-001 |
| CU-CUM-008 | RegistrarUnidade | HU-CUM-001 | RF-CUM-008 | RF-CUM-001 |
| CU-CUM-009 | ConsultarUnidade | HU-CUM-002 | RF-CUM-009 | RF-CUM-001 |
| CU-CUM-010 | ListarUnidades | HU-CUM-003 | RF-CUM-010 | RF-CUM-001 |
| CU-CUM-011 | AtualizarUnidade | HU-CUM-004 | RF-CUM-011 | RF-CUM-001 |
| CU-CUM-012 | ExcluirUnidade | HU-CUM-005 | RF-CUM-012 | RF-CUM-001 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 012-Cadastro-Unico-Municipal-Matriz-de-Rastreabilidade.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
