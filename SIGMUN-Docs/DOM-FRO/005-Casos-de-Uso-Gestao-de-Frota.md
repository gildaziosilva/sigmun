# 005 – Casos-de-Uso – Gestão de Frota

#### Casos-de-Uso – Gestão de Frota

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-FRO-005

**Domínio:** Gestão de Frota

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-de-Frota.md`
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

Este artefato detalha **os casos de uso** do domínio Gestão de Frota (`DOM-FRO`), com base na implementação material identificada em `src/modules/sigmun_frotas` e no conteúdo de negócio declarado no gerador.

---

# 2. Casos de uso implementados

| Identificador | Caso de uso | Classe | Resumo |
| --- | --- | --- | --- |
| CU-FRO-001 | CadastrarVeiculo | `CadastrarVeiculoUseCase` | Cadastra um veículo (RN-FRO-001). |
| CU-FRO-002 | RegistrarAbastecimento | `RegistrarAbastecimentoUseCase` | Registra um abastecimento e atualiza o odômetro do veículo. |
| CU-FRO-003 | AbrirManutencao | `AbrirManutencaoUseCase` | Abre manutenção e marca o veículo como em manutenção (RN-FRO-002). |
| CU-FRO-004 | ConcluirManutencao | `ConcluirManutencaoUseCase` | Conclui manutenção e reativa o veículo (RN-FRO-002). |
| CU-FRO-005 | RegistrarRota | `RegistrarRotaUseCase` | Registra uma rota e calcula a distância percorrida. |
| CU-FRO-006 | ConcluirRota | `ConcluirRotaUseCase` | Conclui uma rota e atualiza o odômetro do veículo. |
| CU-FRO-007 | BaixarVeiculo | `BaixarVeiculoUseCase` | Baixa definitiva de um veículo. |

---

# 3. Cobertura

Casos de uso no código: **7**. Operações publicadas: **13**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 005-Gestao-de-Frota-Casos-de-Uso.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
