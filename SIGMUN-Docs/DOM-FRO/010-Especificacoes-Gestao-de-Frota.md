# 010 – Especificacoes – Gestão de Frota

#### Especificacoes – Gestão de Frota

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-FRO-010

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

Este artefato detalha **as especificações** do domínio Gestão de Frota (`DOM-FRO`), com base na implementação material identificada em `src/modules/sigmun_frotas` e no conteúdo de negócio declarado no gerador.

---

# 2. Contratos publicados

| Método | Caminho | Recurso | Corpo |
| --- | --- | --- | --- |
| GET | `/api/v1/fro/abastecimentos` | abastecimentos | JSON (payload do domínio) |
| GET | `/api/v1/fro/manutencoes` | manutencoes | JSON (payload do domínio) |
| POST | `/api/v1/fro/manutencoes/{manutencao_id}/concluir` | manutencoes | JSON (payload do domínio) |
| GET | `/api/v1/fro/rotas` | rotas | JSON (payload do domínio) |
| POST | `/api/v1/fro/rotas/{rota_id}/concluir` | rotas | JSON (payload do domínio) |
| GET | `/api/v1/fro/veiculos` | veiculos | JSON (payload do domínio) |
| POST | `/api/v1/fro/veiculos` | veiculos | JSON (payload do domínio) |
| GET | `/api/v1/fro/veiculos/{veiculo_id}` | veiculos | JSON (payload do domínio) |
| GET | `/api/v1/fro/veiculos/{veiculo_id}/abastecimentos` | veiculos | JSON (payload do domínio) |
| POST | `/api/v1/fro/veiculos/{veiculo_id}/abastecimentos` | veiculos | JSON (payload do domínio) |
| POST | `/api/v1/fro/veiculos/{veiculo_id}/baixar` | veiculos | JSON (payload do domínio) |
| POST | `/api/v1/fro/veiculos/{veiculo_id}/manutencoes` | veiculos | JSON (payload do domínio) |
| POST | `/api/v1/fro/veiculos/{veiculo_id}/rotas` | veiculos | JSON (payload do domínio) |

---

# 3. Validações aplicadas

| Regra | Validação |
| --- | --- |
| RN-FRO-001 | a placa do veículo é única no cadastro |
| RN-FRO-002 | veículos em manutenção têm status ``manutencao``; concluída a |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 010-Gestao-de-Frota-Especificacoes.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
