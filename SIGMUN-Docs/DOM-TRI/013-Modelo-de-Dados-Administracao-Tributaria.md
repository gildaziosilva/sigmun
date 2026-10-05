# 013 – Modelo-de-Dados – Administração Tributária

#### Modelo-de-Dados – Administração Tributária

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TRI-013

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

Este artefato detalha **o modelo de dados** do domínio Administração Tributária (`DOM-TRI`), com base na implementação material identificada em `src/modules/sigmun_tributos` e no conteúdo de negócio declarado no gerador.

---

# 2. Tabelas no schema `trib`

### certidoes (`CertidaoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| contribuinte_id : TEXT <<NN>> | NOT NULL |
| tipo : TEXT <<NN>> | NOT NULL |
| numero : TEXT <<UQ, NN>> | NOT NULL |
| data_emissao : DATE | opcional |
| valido_ate : DATE | opcional |
| observacao : TEXT | opcional |
| status : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### contribuintes (`ContribuinteModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| tipo : TEXT <<NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| cpf_cnpj : VARCHAR(14) <<UQ, NN>> | NOT NULL |
| inscricao_municipal : TEXT | opcional |
| email : TEXT | opcional |
| telefone : TEXT | opcional |
| endereco : TEXT | opcional |
| status : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### divida_ativa (`DividaAtivaModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| lancamento_id : TEXT <<UQ, NN>> | NOT NULL |
| numero_inscricao : TEXT <<UQ, NN>> | NOT NULL |
| data_inscricao : DATE | opcional |
| valor_original : FLOAT <<NN>> | NOT NULL |
| valor_atualizado : FLOAT <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### imoveis (`ImovelModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| contribuinte_id : TEXT <<NN>> | NOT NULL |
| inscricao_imobiliaria : TEXT <<UQ, NN>> | NOT NULL |
| logradouro : TEXT | opcional |
| numero : TEXT | opcional |
| bairro : TEXT | opcional |
| cidade : TEXT | opcional |
| uf : VARCHAR(2) | opcional |
| cep : VARCHAR(8) | opcional |
| area_terreno : FLOAT <<NN>> | NOT NULL |
| area_construida : FLOAT <<NN>> | NOT NULL |
| valor_venal : FLOAT <<NN>> | NOT NULL |
| aliquota : FLOAT <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| updated_at : DATETIME | opcional |
| created_by : TEXT | opcional |
| is_deleted : BOOLEAN <<NN>> | NOT NULL |

### lancamentos (`LancamentoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| contribuinte_id : TEXT <<NN>> | NOT NULL |
| imovel_id : TEXT | opcional |
| tipo_tributo : TEXT <<NN>> | NOT NULL |
| exercicio : INTEGER <<NN>> | NOT NULL |
| numero_lancamento : TEXT <<UQ, NN>> | NOT NULL |
| descricao : TEXT | opcional |
| base_calculo : FLOAT <<NN>> | NOT NULL |
| aliquota : FLOAT <<NN>> | NOT NULL |
| valor_tributo : FLOAT <<NN>> | NOT NULL |
| juros : FLOAT <<NN>> | NOT NULL |
| multa : FLOAT <<NN>> | NOT NULL |
| valor_total : FLOAT <<NN>> | NOT NULL |
| data_vencimento : DATE | opcional |
| status : TEXT <<NN>> | NOT NULL |
| data_pagamento : DATE | opcional |
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

**Documento:** 013-Administracao-Tributaria-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
