# 006 – Historias-de-Usuario – Integração e Interoperabilidade

#### Historias-de-Usuario – Integração e Interoperabilidade

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-INT-006

**Domínio:** Integração e Interoperabilidade

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Integracao-e-Interoperabilidade.md`
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

Este artefato detalha **as histórias de usuário** do domínio Integração e Interoperabilidade (`DOM-INT`), com base na implementação material identificada em `src/modules/sigmun_int` e no conteúdo de negócio declarado no gerador.

---

# 2. Histórias

| Identificador | História | Capacidade | Prioridade |
| --- | --- | --- | --- |
| HU-INT-001 | Como administrador, quero cadastrar uma API externa para integrar o município. | CAP-INT-001 | Alta |
| HU-INT-002 | Como integrador, quero versionar o contrato para evoluir sem quebrar o consumidor. | CAP-INT-002 | Alta |
| HU-INT-003 | Como sistema externo, quero receber webhook para enviar dados ao SIGMUN. | CAP-INT-004 | Alta |
| HU-INT-004 | Como operação, quero reprocessar uma entrega com falha para não perder dados. | CAP-INT-004 | Média |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 006-Integracao-e-Interoperabilidade-Historias-de-Usuario.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
