# 005 – Casos-de-Uso – Gestão Patrimonial

#### Casos-de-Uso – Gestão Patrimonial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-PAT-005

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

Este artefato detalha **os casos de uso** do domínio Gestão Patrimonial (`DOM-PAT`), com base na implementação material identificada em `src/modules/sigmun_patrimonio` e no conteúdo de negócio declarado no gerador.

---

# 2. Casos de uso implementados

| Identificador | Caso de uso | Classe | Resumo |
| --- | --- | --- | --- |
| CU-PAT-001 | CadastrarBem | `CadastrarBemUseCase` | Cadastra um bem patrimonial (RN-PAT-001). |
| CU-PAT-002 | DepreciarBem | `DepreciarBemUseCase` | Aplica depreciação linear a um bem (RN-PAT-002). |
| CU-PAT-003 | TransferirBem | `TransferirBemUseCase` | Registra transferência de bem (RN-PAT-010). |
| CU-PAT-004 | ConcluirTransferencia | `ConcluirTransferenciaUseCase` | Consolida uma transferência pendente. |
| CU-PAT-005 | BaixarBem | `BaixarBemUseCase` | Baixa definitiva de um bem (RN-PAT-003). |

---

# 3. Cobertura

Casos de uso no código: **5**. Operações publicadas: **8**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 005-Gestao-Patrimonial-Casos-de-Uso.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
