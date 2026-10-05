# 002 – Mapa-de-Capacidades – Educação Pública

#### Mapa-de-Capacidades – Educação Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-EDU-002

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

Este artefato detalha **o mapa de capacidades** do domínio Educação Pública (`DOM-EDU`), com base na implementação material identificada em `src/modules/sigmun_educacao` e no conteúdo de negócio declarado no gerador.

---

# 2. Capacidades

| Identificador | Capacidade | Descrição | Processo |
| --- | --- | --- | --- |
| CAP-EDU-001 | Cadastro de aluno | Registra aluno e sua identidade. | PRO-EDU-001 |
| CAP-EDU-002 | Matrícula | Matrícula, transfere, cancela e conclui. | PRO-EDU-002 |
| CAP-EDU-003 | Diário escolar | Registra presença e lançamento. | PRO-EDU-003 |
| CAP-EDU-004 | Merenda e transporte | Itens de merenda, distribuição e rotas. | PRO-EDU-004 |

---

# 3. Processos por capacidade

| Processo | Descrição | Regras |
| --- | --- | --- |
| PRO-EDU-001 | Cadastrar aluno | Registra aluno com documento e escola. | RN-EDU-001 |
| PRO-EDU-002 | Movimentar matrícula | Matrícula, transfere, cancela e conclui. | RN-EDU-010, RN-EDU-020 |
| PRO-EDU-003 | Lançar no diário | Registra presença e conteúdo. | RN-EDU-030 |
| PRO-EDU-004 | Atender merenda e transporte | Distribui merenda e passagem de transporte. | RN-EDU-040 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 002-Educacao-Publica-Mapa-de-Capacidades.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
