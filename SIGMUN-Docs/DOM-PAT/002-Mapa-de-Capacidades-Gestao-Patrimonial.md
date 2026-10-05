# 002 – Mapa-de-Capacidades – Gestão Patrimonial

#### Mapa-de-Capacidades – Gestão Patrimonial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PAT-002

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

Este artefato detalha **o mapa de capacidades** do domínio Gestão Patrimonial (`DOM-PAT`), com base na implementação material identificada em `src/modules/sigmun_patrimonio` e no conteúdo de negócio declarado no gerador.

---

# 2. Capacidades

| Identificador | Capacidade | Descrição | Processo |
| --- | --- | --- | --- |
| CAP-PAT-001 | Cadastro de bens | Registra o bem, seu tipo, valor e responsável. | PRO-PAT-001 |
| CAP-PAT-002 | Depreciação | Lança depreciação e valor contábil atualizado. | PRO-PAT-002 |
| CAP-PAT-003 | Transferência | Transfere o bem entre unidades e conclui a carga. | PRO-PAT-003 |
| CAP-PAT-004 | Baixa | Baixa o bem com motivo e registro. | PRO-PAT-004 |

---

# 3. Processos por capacidade

| Processo | Descrição | Regras |
| --- | --- | --- |
| PRO-PAT-001 | Cadastrar bem | Registra o bem com tipo e valor de aquisição. | RN-PAT-001 |
| PRO-PAT-002 | Depreciar bem | Lança a depreciação do período. | RN-PAT-002 |
| PRO-PAT-003 | Transferir bem | Abre e conclui a transferência entre unidades. | RN-PAT-003, RN-PAT-010 |
| PRO-PAT-004 | Baixar bem | Baixa o bem com justificativa. | — |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 002-Gestao-Patrimonial-Mapa-de-Capacidades.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
