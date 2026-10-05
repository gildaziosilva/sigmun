# 005 – Casos-de-Uso – Atendimento ao Cidadão

#### Casos-de-Uso – Atendimento ao Cidadão

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ATE-005

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

Este artefato detalha **os casos de uso** do domínio Atendimento ao Cidadão (`DOM-ATE`), com base na implementação material identificada em `src/modules/sigmun_ate` e no conteúdo de negócio declarado no gerador.

---

# 2. Casos de uso implementados

| Identificador | Caso de uso | Classe | Resumo |
| --- | --- | --- | --- |
| CU-ATE-001 | RealizarTriagem | `RealizarTriagemUseCase` | Caso de uso: Realizar triagem de atendimento. |
| CU-ATE-002 | AbrirFila | `AbrirFilaUseCase` | Caso de uso: Abrir fila de atendimento. |
| CU-ATE-003 | FecharFila | `FecharFilaUseCase` | Caso de uso: Fechar fila de atendimento. |
| CU-ATE-004 | EmitirSenha | `EmitirSenhaUseCase` | Caso de uso: Emitir senha de atendimento. |
| CU-ATE-005 | ChamarSenha | `ChamarSenhaUseCase` | Caso de uso: Chamar senha para atendimento. |
| CU-ATE-006 | RechamarSenha | `RechamarSenhaUseCase` | Caso de uso: Rechamar senha. |
| CU-ATE-007 | MarcarSenhaAtendida | `MarcarSenhaAtendidaUseCase` | Caso de uso: Marcar senha como atendida. |
| CU-ATE-008 | IniciarAtendimento | `IniciarAtendimentoUseCase` | Caso de uso: Iniciar atendimento. |
| CU-ATE-009 | ConcluirAtendimento | `ConcluirAtendimentoUseCase` | Caso de uso: Concluir atendimento. |
| CU-ATE-010 | CancelarAtendimento | `CancelarAtendimentoUseCase` | Caso de uso: Cancelar atendimento. |
| CU-ATE-011 | RegistrarAvaliacao | `RegistrarAvaliacaoUseCase` | Caso de uso: Registrar avaliação de atendimento. |
| CU-ATE-012 | CriarEncaminhamento | `CriarEncaminhamentoUseCase` | Caso de uso: Criar encaminhamento. |
| CU-ATE-013 | ConcluirEncaminhamento | `ConcluirEncaminhamentoUseCase` | Caso de uso: Concluir encaminhamento. |

---

# 3. Cobertura

Casos de uso no código: **13**. Operações publicadas: **19**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 005-Atendimento-ao-Cidadao-Casos-de-Uso.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
