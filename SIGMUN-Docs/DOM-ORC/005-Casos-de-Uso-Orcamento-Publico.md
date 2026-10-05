# 005 – Casos-de-Uso – Orçamento Público

#### Casos-de-Uso – Orçamento Público

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ORC-005

**Domínio:** Orçamento Público

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Orcamento-Publico.md`
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

Este artefato detalha **os casos de uso** do domínio Orçamento Público (`DOM-ORC`), com base na implementação material identificada em `src/modules/sigmun_orc` e no conteúdo de negócio declarado no gerador.

---

# 2. Casos de uso implementados

| Identificador | Caso de uso | Classe | Resumo |
| --- | --- | --- | --- |
| CU-ORC-001 | CriarDotacao | `CriarDotacaoUseCase` | Cria dotação vinculada à LOA (RN-ORC-030). |
| CU-ORC-002 | SuplementarDotacao | `SuplementarDotacaoUseCase` | Suplementa dotação ativa. |
| CU-ORC-003 | AnularDotacao | `AnularDotacaoUseCase` | Anula parcialmente dotação ativa. |
| CU-ORC-004 | ReservarSaldo | `ReservarSaldoUseCase` | Reserva saldo da dotação (RN-ORC-040). |
| CU-ORC-005 | CancelarReserva | `CancelarReservaUseCase` | Cancela reserva ativa (devolve saldo). |
| CU-ORC-006 | CriarPPA | `CriarPPAUseCase` | Cria PPA do quadriênio (RN-ORC-001). |
| CU-ORC-007 | PublicarPPA | `PublicarPPAUseCase` | Publica PPA em elaboração. |
| CU-ORC-008 | CriarLDO | `CriarLDOUseCase` | Cria LDO vinculada a PPA vigente (RN-ORC-011). |
| CU-ORC-009 | SancionarLDO | `SancionarLDOUseCase` | Aprova e sanciona LDO. |
| CU-ORC-010 | CriarLOA | `CriarLOAUseCase` | Cria LOA vinculada a LDO sancionada (RN-ORC-021). |
| CU-ORC-011 | PublicarLOA | `PublicarLOAUseCase` | Aprova e publica LOA. |

---

# 3. Cobertura

Casos de uso no código: **11**. Operações publicadas: **12**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 005-Orcamento-Publico-Casos-de-Uso.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
