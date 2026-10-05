# 012 – Matriz-de-Rastreabilidade – Educação Pública

#### Matriz-de-Rastreabilidade – Educação Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-EDU-012

**Domínio:** Educação Pública

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Educacao-Publica.md`
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

Este artefato detalha **a matriz de rastreabilidade** do domínio Educação Pública (`DOM-EDU`), com base na implementação material identificada em `src/modules/sigmun_educacao` e no conteúdo de negócio declarado no gerador.

---

# 2. Caso de uso × história × requisito

| Caso de uso | Classe | História | Requisito | Regra |
| --- | --- | --- | --- | --- |
| CU-EDU-001 | CadastrarAluno | HU-EDU-001 | RF-EDU-001 | RF-CUM-001 |
| CU-EDU-002 | RealizarMatricula | HU-EDU-002 | RF-EDU-002 | RF-CUM-001 |
| CU-EDU-003 | TransferirMatricula | HU-EDU-003 | RF-EDU-003 | RF-CUM-001 |
| CU-EDU-004 | CancelarMatricula | HU-EDU-004 | RF-EDU-004 | RF-CUM-001 |
| CU-EDU-005 | ConcluirMatricula | HU-EDU-001 | RF-EDU-005 | RF-CUM-001 |
| CU-EDU-006 | RegistrarLancamentoDiario | HU-EDU-002 | RF-EDU-006 | RF-CUM-001 |
| CU-EDU-007 | CadastrarRotaTransporte | HU-EDU-003 | RF-EDU-007 | RF-CUM-001 |
| CU-EDU-008 | InativarRotaTransporte | HU-EDU-004 | RF-EDU-008 | RF-CUM-001 |
| CU-EDU-009 | AtivarRotaTransporte | HU-EDU-001 | RF-EDU-009 | RF-CUM-001 |
| CU-EDU-010 | RegistrarPassagem | HU-EDU-002 | RF-EDU-010 | RF-CUM-001 |
| CU-EDU-011 | CadastrarItemMerenda | HU-EDU-003 | RF-EDU-011 | RF-CUM-001 |
| CU-EDU-012 | ReporEstoqueMerenda | HU-EDU-004 | RF-EDU-012 | RF-CUM-001 |
| CU-EDU-013 | DistribuirMerenda | HU-EDU-001 | RF-EDU-013 | RF-CUM-001 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 012-Educacao-Publica-Matriz-de-Rastreabilidade.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
