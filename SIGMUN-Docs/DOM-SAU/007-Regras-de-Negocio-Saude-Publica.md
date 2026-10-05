# 007 – Regras-de-Negocio – Saúde Pública

#### Regras-de-Negocio – Saúde Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-SAU-007

**Domínio:** Saúde Pública

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Saude-Publica.md`
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

Este artefato detalha **as regras de negócio** do domínio Saúde Pública (`DOM-SAU`), com base na implementação material identificada em `src/modules/sigmun_saude` e no conteúdo de negócio declarado no gerador.

---

# 2. Regras implementadas

| Identificador | Descrição | Fonte |
| --- | --- | --- |
| RN-SAU-001 | o CNS do paciente é único no cadastro municipal | `src/modules/sigmun_saude` |
| RN-SAU-002 | prontuário reúne atendimentos em ordem cronológica | `src/modules/sigmun_saude` |
| RN-SAU-003 | a regulação é autorizada conforme a prioridade registrada. | `src/modules/sigmun_saude` |
| RN-SAU-004 | a dispensação referencia o paciente e o medicamento administered. | `src/modules/sigmun_saude` |
| RN-SAU-010 | atendimento exige paciente e profissional/estabelecimento | `src/modules/sigmun_saude` |
| RN-SAU-020 | agendamento nasce ``agendado`` e só transita para | `src/modules/sigmun_saude` |
| RN-SAU-030 | regulação nasce ``solicitada`` e transita para | `src/modules/sigmun_saude` |
| RN-SAU-040 | dispensação exige estoque suficiente; baixa é atômica no | `src/modules/sigmun_saude` |

---

# 3. Cobertura

Regras referenciadas no código: **8**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 007-Saude-Publica-Regras-de-Negocio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
