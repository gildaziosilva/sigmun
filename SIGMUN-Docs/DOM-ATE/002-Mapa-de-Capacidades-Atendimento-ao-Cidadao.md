# 002 – Mapa-de-Capacidades – Atendimento ao Cidadão

#### Mapa-de-Capacidades – Atendimento ao Cidadão

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ATE-002

**Domínio:** Atendimento ao Cidadão

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Atendimento-ao-Cidadao.md`
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

Este artefato detalha **o mapa de capacidades** do domínio Atendimento ao Cidadão (`DOM-ATE`), com base na implementação material identificada em `src/modules/sigmun_ate` e no conteúdo de negócio declarado no gerador.

---

# 2. Capacidades

| Identificador | Capacidade | Descrição | Processo |
| --- | --- | --- | --- |
| CAP-ATE-001 | Triagem do atendimento | Identifica serviço, prioridade e necessidade de encaminhamento. | PRO-ATE-001 |
| CAP-ATE-002 | Gestão de senhas e filas | Emite senha, posiciona na fila e chama o atendimento. | PRO-ATE-002 |
| CAP-ATE-003 | Registro de atendimento | Registra o atendimento realizado e a conclusão. | PRO-ATE-003 |
| CAP-ATE-004 | Avaliação do atendimento | Coleta a nota e o comentário do cidadão. | PRO-ATE-004 |

---

# 3. Processos por capacidade

| Processo | Descrição | Regras |
| --- | --- | --- |
| PRO-ATE-001 | Triar solicitação | Classifica serviço e prioridade na chegada. | RN-ATE-001 |
| PRO-ATE-002 | Emitir e chamar senha | Posiciona na fila e chama o guichê. | RN-ATE-002 |
| PRO-ATE-003 | Registrar atendimento | Executa e registra o atendimento. | RN-ATE-003 |
| PRO-ATE-004 | Avaliar e encaminhar | Avalia satisfação e encaminha quando necessário. | RN-ATE-004 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 002-Atendimento-ao-Cidadao-Mapa-de-Capacidades.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
