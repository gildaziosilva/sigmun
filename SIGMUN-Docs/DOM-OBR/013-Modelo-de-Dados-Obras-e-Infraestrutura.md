# 013 – Modelo de Dados – Obras e Infraestrutura

#### Modelo de Dados – Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OBR-013

**Domínio:** Obras e Infraestrutura

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Obras-e-Infraestrutura.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000C-HIERARQUIA-DOCUMENTAL.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `030-Roadmap-de-Implementacao-dos-Dominios.md`
* `Mapa-de-Dominios.md`
* `Modelo-Logico.md`
* `Modelo-Fisico.md`
* `Dicionario-de-dados.md`

---

# 1. Finalidade

Este artefato descreve o modelo de dados do domínio de Obras e Infraestrutura: entidades,
atributos, tipos, restrições e valores admissíveis.

---

# 2. Convenções

* O domínio utiliza banco relacional com schema próprio (`{'codigo': 'DOM-OBR', 'dominio': 'Obras e Infraestrutura', 'modulo': 'sigmun_obras', 'schema': 'obr', 'prefixo': '/api/v1/obr', 'migracao': 'alembic/versions/20260929_04_dom_obr_models.py', 'migracao_id': '20260929_04_dom_obr_models', 'rotulo': 'Obras e Infraestrutura', 'prefixo_regra': 'OBR', 'entidades': [('Obra', 'Obra pública acompanhada quanto ao avanço físico e financeiro.'), ('MedicaoObra', 'Medição físico-financeira de avanço da obra.'), ('EtapaObra', 'Etapa de execução fisicamente verificável da obra.'), ('DespesaObra', 'Desembolso financeiro vinculado à obra.'), ('VistoriaObra', 'Vistoria fiscalizadora com parecer sobre o avanço verificado.')], 'variaveis': (('Tipos de obra', 'pavimentacao, drenagem, construcao, reforma, iluminacao, saneamento, ponte, praca, quadra, outro'), ('Situações da obra', 'planejada, em_licitacao, contratada, em_execucao, suspensa, concluida, cancelada'), ('Tipos de contratação', 'licitacao, dispensa, inexigibilidade, convenio, contrato_direto'), ('Fontes de recurso', 'orcamento_proprio, convenio, convenio_estadual, convenio_federal, transferencia, operacao_credito, outro'), ('Tipos de medição', 'avanco, etapa, final, revisional'), ('Situações da medição', 'registrada, conferida, aprovada, glosada, cancelada'), ('Tipos de despesa', 'medicao, repasse, material, mao_de_obra, tributos, custos, outro'), ('Tipos de etapa', 'projeto, terraplanagem, fundacao, estrutura, acabamento, instalacao, pavimentacao, paisagismo, recepcao'), ('Situações da etapa', 'pendente, em_execucao, concluida, atrasada, cancelada'), ('Tipos de vistoria', 'periodica, parcial, final, recepcao'), ('Pareceres da vistoria', 'aprovado, aprovado_com_ressalvas, reprovado'))}`).
* Chaves primárias são UUID v4 gerados pela aplicação.
* Campos de auditoria (`created_at`, `created_by`, `updated_at`) são comuns às
  entidades submetidas a exclusão lógica.
* **Não há chave estrangeira física entre schemas de domínios**; as referências
  entre domínios são feitas por identificador opaco, conforme o contrato de
  integração.

---

# 3. Entidades

### Obra — Obra pública acompanhada quanto ao avanço físico e financeiro.

**Tabela:** `obr.obras`

| Coluna | Tipo | Padrão |
| --- | | --- | |
| `id` | UUID, PK | — |
| `numero` | TEXT, NOT NULL, UNIQUE | — |
| `nome` | TEXT, NOT NULL | — |
| `descricao` | TEXT | — |
| `tipo` | TEXT, NOT NULL | outro |
| `situacao` | TEXT, NOT NULL | planejada |
| `tipo_contratacao` | TEXT, NOT NULL | licitacao |
| `fonte_recurso` | TEXT, NOT NULL | orcamento_proprio |
| `valor_orcado` | FLOAT, NOT NULL | 0 |
| `valor_contratado` | FLOAT, NOT NULL | 0 |
| `valor_mediado` | FLOAT, NOT NULL | 0 |
| `valor_pago` | FLOAT, NOT NULL | 0 |
| `percentual_fisico` | FLOAT, NOT NULL | 0 |
| `percentual_financeiro` | FLOAT, NOT NULL | 0 |
| `empresa_contratada` | TEXT | — |
| `numero_contrato` | TEXT | — |
| `responsavel_tecnico` | TEXT | — |
| `endereco` | TEXT | — |
| `bairro` | TEXT | — |
| `data_inicio_prevista` | DATE | — |
| `data_fim_prevista` | DATE | — |
| `data_inicio_real` | DATE | — |
| `data_fim_real` | DATE | — |
| `observacao` | TEXT | — |
| `created_at` | DATETIME, NOT NULL | now() |
| `updated_at` | DATETIME | — |
| `created_by` | TEXT | — |
| `is_deleted` | BOOLEAN, NOT NULL | false() |


### MedicaoObra — Medição físico-financeira de avanço da obra.

**Tabela:** `obr.medicoes_obras`

| Coluna | Tipo | Padrão |
| --- | | --- | |
| `id` | UUID, PK | — |
| `obra_id` | TEXT, NOT NULL | — |
| `numero` | TEXT, NOT NULL | — |
| `tipo` | TEXT, NOT NULL | avanco |
| `situacao` | TEXT, NOT NULL | registrada |
| `data` | DATE, NOT NULL | — |
| `percentual_fisico` | FLOAT, NOT NULL | 0 |
| `valor_medido` | FLOAT, NOT NULL | 0 |
| `responsavel_tecnico` | TEXT, NOT NULL | — |
| `observacao` | TEXT | — |
| `created_at` | DATETIME, NOT NULL | now() |
| `updated_at` | DATETIME | — |
| `created_by` | TEXT | — |
| `is_deleted` | BOOLEAN, NOT NULL | false() |


### EtapaObra — Etapa de execução fisicamente verificável da obra.

**Tabela:** `obr.etapas_obras`

| Coluna | Tipo | Padrão |
| --- | | --- | |
| `id` | UUID, PK | — |
| `obra_id` | TEXT, NOT NULL | — |
| `numero` | TEXT, NOT NULL | — |
| `descricao` | TEXT, NOT NULL | — |
| `tipo` | TEXT, NOT NULL | estrutura |
| `situacao` | TEXT, NOT NULL | pendente |
| `percentual_previsto` | FLOAT, NOT NULL | 0 |
| `percentual_realizado` | FLOAT, NOT NULL | 0 |
| `data_inicio_prevista` | DATE | — |
| `data_fim_prevista` | DATE | — |
| `data_conclusao` | DATE | — |
| `responsavel` | TEXT, NOT NULL | — |
| `created_at` | DATETIME, NOT NULL | now() |
| `updated_at` | DATETIME | — |
| `created_by` | TEXT | — |
| `is_deleted` | BOOLEAN, NOT NULL | false() |


### DespesaObra — Desembolso financeiro vinculado à obra.

**Tabela:** `obr.despesas_obras`

| Coluna | Tipo | Padrão |
| --- | | --- | |
| `id` | UUID, PK | — |
| `obra_id` | TEXT, NOT NULL | — |
| `medicao_id` | TEXT | — |
| `descricao` | TEXT, NOT NULL | — |
| `tipo` | TEXT, NOT NULL | medicao |
| `valor` | FLOAT, NOT NULL | 0 |
| `data` | DATE, NOT NULL | — |
| `documento` | TEXT | — |
| `credor` | TEXT | — |
| `observacao` | TEXT | — |
| `created_at` | DATETIME, NOT NULL | now() |
| `created_by` | TEXT | — |
| `is_deleted` | BOOLEAN, NOT NULL | false() |


### VistoriaObra — Vistoria fiscalizadora com parecer sobre o avanço verificado.

**Tabela:** `obr.vistorias_obras`

| Coluna | Tipo | Padrão |
| --- | | --- | |
| `id` | UUID, PK | — |
| `obra_id` | TEXT, NOT NULL | — |
| `data` | DATE, NOT NULL | — |
| `tipo` | TEXT, NOT NULL | periodica |
| `parecer` | TEXT, NOT NULL | aprovado |
| `percentual_fisico_verificado` | FLOAT, NOT NULL | 0 |
| `fiscal` | TEXT, NOT NULL | — |
| `observacao` | TEXT | — |
| `created_at` | DATETIME, NOT NULL | now() |
| `created_by` | TEXT | — |
| `is_deleted` | BOOLEAN, NOT NULL | false() |


---

# 4. Domínios de Valor

* **Tipos de obra:** pavimentacao, drenagem, construcao, reforma, iluminacao, saneamento, ponte, praca, quadra, outro
* **Situações da obra:** planejada, em_licitacao, contratada, em_execucao, suspensa, concluida, cancelada
* **Tipos de contratação:** licitacao, dispensa, inexigibilidade, convenio, contrato_direto
* **Fontes de recurso:** orcamento_proprio, convenio, convenio_estadual, convenio_federal, transferencia, operacao_credito, outro
* **Tipos de medição:** avanco, etapa, final, revisional
* **Situações da medição:** registrada, conferida, aprovada, glosada, cancelada
* **Tipos de despesa:** medicao, repasse, material, mao_de_obra, tributos, custos, outro
* **Tipos de etapa:** projeto, terraplanagem, fundacao, estrutura, acabamento, instalacao, pavimentacao, paisagismo, recepcao
* **Situações da etapa:** pendente, em_execucao, concluida, atrasada, cancelada
* **Tipos de vistoria:** periodica, parcial, final, recepcao
* **Pareceres da vistoria:** aprovado, aprovado_com_ressalvas, reprovado

---

# 5. Índices e Restrições

| Tabela | Restrição | Regra |
| --- | | --- | |
| `obr.obras` | UNIQUE | — |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 013-Modelo-de-Dados-Obras-e-Infraestrutura.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_obras`. Alterações no código devem ser
> refletidas reexecutando o gerador.
