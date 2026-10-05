# 002 – Mapa-de-Capacidades – Ouvidoria

#### Mapa-de-Capacidades – Ouvidoria

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OUV-002

**Domínio:** Ouvidoria

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Ouvidoria.md`
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

Este artefato detalha **o mapa de capacidades** do domínio Ouvidoria (`DOM-OUV`), com base na implementação material identificada em `src/modules/sigmun_ouvidoria` e no conteúdo de negócio declarado no gerador.

---

# 2. Capacidades

| Identificador | Capacidade | Descrição | Processo |
| --- | --- | --- | --- |
| CAP-OU-001 | Recepção de manifestação | Registra a manifestação e gera protocolo. | PRO-OU-001 |
| CAP-OU-002 | Triagem e classificação | Classifica a matéria e define o fluxo. | PRO-OU-002 |
| CAP-OU-003 | Encaminhamento | Encaminha a órgão responsável com prazo. | PRO-OU-003 |
| CAP-OU-004 | Resposta e LAI | Produz resposta e trata pedido de informação. | PRO-OU-004 |
| CAP-OU-005 | Prazos e avaliação | Controla prazo e mede satisfação do cidadão. | PRO-OU-005 |

---

# 3. Processos por capacidade

| Processo | Descrição | Regras |
| --- | --- | --- |
| PRO-OU-001 | Receber manifestação | Registra a manifestação e abre protocolo. | RN-OU-001 |
| PRO-OU-002 | Triar e classificar | Define tipo, prioridade e sigilo. | RN-OU-002 |
| PRO-OU-003 | Encaminhar e tratar | Encaminha ao órgão e registra o tratamento. | RN-OU-003 |
| PRO-OU-004 | Responder e avaliar | Responde e registra a satisfação do cidadão. | RN-OU-004 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 002-Ouvidoria-Mapa-de-Capacidades.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
