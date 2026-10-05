# 013 – Modelo-de-Dados – Gestão de Frota

#### Modelo-de-Dados – Gestão de Frota

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-FRO-013

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

Este artefato detalha **o modelo de dados** do domínio Gestão de Frota (`DOM-FRO`), com base na implementação material identificada em `src/modules/sigmun_frotas` e no conteúdo de negócio declarado no gerador.

---

# 2. Tabelas no schema `fro`

### abastecimentos (`AbastecimentoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| veiculo_id : TEXT <<NN>> | NOT NULL |
| data : DATE | opcional |
| quantidade_litros : FLOAT <<NN>> | NOT NULL |
| valor_unitario : FLOAT <<NN>> | NOT NULL |
| valor_total : FLOAT <<NN>> | NOT NULL |
| odometro : FLOAT <<NN>> | NOT NULL |
| posto : TEXT | opcional |
| tipo_combustivel : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |

### manutencoes (`ManutencaoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| veiculo_id : TEXT <<NN>> | NOT NULL |
| data_entrada : DATE | opcional |
| data_saida : DATE | opcional |
| tipo : TEXT <<NN>> | NOT NULL |
| descricao : TEXT <<NN>> | NOT NULL |
| oficina : TEXT | opcional |
| valor : FLOAT <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |

### rotas (`RotaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| veiculo_id : TEXT <<NN>> | NOT NULL |
| data : DATE | opcional |
| origem : TEXT <<NN>> | NOT NULL |
| destino : TEXT <<NN>> | NOT NULL |
| km_inicio : FLOAT <<NN>> | NOT NULL |
| km_fim : FLOAT <<NN>> | NOT NULL |
| distancia_km : FLOAT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| status : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : TEXT | opcional |

### veiculos (`VeiculoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| placa : TEXT <<UQ, NN>> | NOT NULL |
| chassi : TEXT | opcional |
| renavam : TEXT | opcional |
| marca : TEXT <<NN>> | NOT NULL |
| modelo : TEXT <<NN>> | NOT NULL |
| ano_fabricacao : INTEGER <<NN>> | NOT NULL |
| ano_modelo : INTEGER <<NN>> | NOT NULL |
| tipo : TEXT <<NN>> | NOT NULL |
| combustivel : TEXT <<NN>> | NOT NULL |
| capacidade : FLOAT <<NN>> | NOT NULL |
| odometro_atual : FLOAT <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| unidade_id : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 013-Gestao-de-Frota-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
