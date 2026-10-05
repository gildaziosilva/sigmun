# 002 – Mapa-de-Capacidades – Assistência Social

#### Mapa-de-Capacidades – Assistência Social

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ASS-002

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

Este artefato detalha **o mapa de capacidades** do domínio Assistência Social (`DOM-ASS`), com base na implementação material identificada em `src/modules/sigmun_assistencia_social` e no conteúdo de negócio declarado no gerador.

---

# 2. Capacidades

| Identificador | Capacidade | Descrição | Processo |
| --- | --- | --- | --- |
| CAP-ASS-001 | Cadastro de família | Registra a família CadÚnico e seu NIS. | PRO-ASS-001 |
| CAP-ASS-002 | Atendimento social | Registra atendimento e encaminhamento. | PRO-ASS-002 |
| CAP-ASS-003 | Benefício eventual | Solicita, autoriza, nega e entrega o benefício. | PRO-ASS-003 |
| CAP-ASS-004 | Unidades de atendimento | Mantém CRAS, CREAS e demais unidades. | PRO-ASS-004 |

---

# 3. Processos por capacidade

| Processo | Descrição | Regras |
| --- | --- | --- |
| PRO-ASS-001 | Cadastrar família | Registra família e pessoas vinculadas. | RN-ASS-001, RN-ASS-002 |
| PRO-ASS-002 | Atender e encaminhar | Registra atendimento e encaminhamento. | RN-ASS-004 |
| PRO-ASS-003 | Conceder benefício eventual | Solicita, autoriza, nega, entrega ou cancela. | RN-ASS-003 |
| PRO-ASS-004 | Manter unidade de atendimento | Cadastra e mantém CRAS/CREAS. | — |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 002-Assistencia-Social-Mapa-de-Capacidades.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
