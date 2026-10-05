# 002 – Mapa-de-Capacidades – Gestão de Diárias, Viagens e Deslocamentos

#### Mapa-de-Capacidades – Gestão de Diárias, Viagens e Deslocamentos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DIA-002

**Domínio:** Gestão de Diárias, Viagens e Deslocamentos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-de-Diarias-Viagens-e-Deslocamentos.md`
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

Este artefato detalha **o mapa de capacidades** do domínio Gestão de Diárias, Viagens e Deslocamentos (`DOM-DIA`), com base na implementação material identificada em `src/modules/sigmun_dia` e no conteúdo de negócio declarado no gerador.

---

# 2. Capacidades

| Identificador | Capacidade | Descrição | Processo |
| --- | --- | --- | --- |
| CAP-DIA-001 | Viagens e deslocamentos | Registra e tramita viagens entre unidades. | PRO-DIA-001 |
| CAP-DIA-002 | Diárias | Solicita, autoriza, calcula, concede e paga a diária. | PRO-DIA-002 |
| CAP-DIA-003 | Prestação de contas | Abre, confere, aprova, glosa e restitui. | PRO-DIA-003 |
| CAP-DIA-004 | Rastreabilidade | Grava os eventos de situação da diária. | PRO-DIA-004 |

---

# 3. Processos por capacidade

| Processo | Descrição | Regras |
| --- | --- | --- |
| PRO-DIA-001 | Viagem | Cria a viagem e tramita entre unidades. | — |
| PRO-DIA-002 | Concessão da diária | Solicita, autoriza, calcula e concede. | RN-DIA-001 a 008 |
| PRO-DIA-003 | Prestação de contas | Abre, confere, aprova, glosa e restitui. | RN-DIA-009, 011 a 017 |
| PRO-DIA-004 | Auditoria do ciclo | Registra a transição de situação em eventos_diarias. | — |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 002-Gestao-de-Diarias-Viagens-e-Deslocamentos-Mapa-de-Capacidades.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
