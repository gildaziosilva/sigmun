# 005 – Casos-de-Uso – Administração Tributária

#### Casos-de-Uso – Administração Tributária

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TRI-005

**Domínio:** Administração Tributária

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Administracao-Tributaria.md`
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

Este artefato detalha **os casos de uso** do domínio Administração Tributária (`DOM-TRI`), com base na implementação material identificada em `src/modules/sigmun_tributos` e no conteúdo de negócio declarado no gerador.

---

# 2. Casos de uso implementados

| Identificador | Caso de uso | Classe | Resumo |
| --- | --- | --- | --- |
| CU-TRI-001 | CadastrarContribuinte | `CadastrarContribuinteUseCase` | Cadastra um contribuinte (RN-TRI-001/002). |
| CU-TRI-002 | CadastrarImovel | `CadastrarImovelUseCase` | Cadastra um imóvel para IPTU (RN-TRI-010/011). |
| CU-TRI-003 | LancarTributo | `LancarTributoUseCase` | Constitui um crédito tributário (RN-TRI-020/021). |
| CU-TRI-004 | PagarLancamento | `PagarLancamentoUseCase` | Quita integralmente um lançamento (RN-TRI-022). |
| CU-TRI-005 | InscreverDividaAtiva | `InscreverDividaAtivaUseCase` | Inscreve crédito vencido em dívida ativa (RN-TRI-030/031). |
| CU-TRI-006 | BaixarDividaAtiva | `BaixarDividaAtivaUseCase` | Baixa uma inscrição de dívida ativa. |
| CU-TRI-007 | EmitirCertidao | `EmitirCertidaoUseCase` | Emite certidão de regularidade fiscal (RN-TRI-040/041). |

---

# 3. Cobertura

Casos de uso no código: **7**. Operações publicadas: **16**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 005-Administracao-Tributaria-Casos-de-Uso.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
