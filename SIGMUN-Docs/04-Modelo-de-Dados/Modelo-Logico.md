# Modelo Lógico

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Modelo de Dados

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
- 005-Arquitetura-de-Dados.md
- 006-Cadastro-Unico-Municipal.md
- Modelo-Conceitual.md

---

Este documento corresponde ao **Modelo Lógico Corporativo** do SIGMUN, derivado diretamente do `Modelo-Conceitual.md`. Traduz as entidades e relacionamentos conceituais em tabelas lógicas (esquemas PostgreSQL) com seus atributos e tipos lógicos (`uuid`, `text`, `timestamp`, `date`, `numeric`, `boolean`, `bigint`, `jsonb`), servindo de insumo para o **Modelo Físico** (`Modelo-Fisico.md`).

> **Nota:** campos entre colchetes `[audit fields]` nas tabelas abaixo correspondem a `created_at`, `created_by`, `updated_at`, `updated_by`, `deleted_at`, `deleted_by` (tabelas críticas); ou apenas `created_at`, `created_by` (tabelas de log e junção `N:M`). Aplicam-se as regras de **soft-delete** (`deleted_at`) e **histórico** (`vigencia_inicio`, `vigencia_fim`, `motivo_alteracao`) definidas pela `005-Arquitetura-de-Dados.md` (§ 9).

---

# 1. Objetivo

Definir, a nível lógico, o modelo de dados do SIGMUN expandindo o **Modelo Conceitual** em tabelas, atributos e tipos, mantendo as regras de auditoria, histórico, soft-delete e LGPD. O modelo está particionado em **esquemas PostgreSQL** que refletem os domínios responsáveis descritos no § 2 do documento conceitual.

---

# 2. Esquemas PostgreSQL (mapeamento de domínios)

A seguir, a tradução de domínio → esquema, conforme `Modelo-Conceitual.md` (§ 2). O esquema `core` reúne os grupos conceituais `pessoas`, `usuarios`, `documentos` e `auditoria` (PostgreSQL não admite esquemas aninhados; a nomenclatura `core.<grupo>` é usada aqui apenas como convenção de documentação — todas as tabelas destacam-se no esquema `core`).

| Domínio / Grupo | Esquema | Tabelas (entidades) | Observação |
| --------------- | ------- | ------------------- | ---------- |
| Compartilhado | `core` (grupo `pessoas`) | `pessoas`, `pessoas_fisicas`, `pessoas_juridicas`, `enderecos`, `documentos`, `contatos`, `fornecedores` | Dados mestres de identidade. |
| Compartilhado | `core` (grupo `usuarios`) | `usuarios`, `grupos_usuarios`, `permissoes`, `usuarios_grupos` | Identidade e acesso. |
| Compartilhado | `core` (grupo `documentos`) | `processos_documentais`, `arquivos`, `assinaturas` | documentos. |
| Compartilhado | `core` (grupo `auditoria`) | `auditorias`, `logs_sistema` | auditoria. |
| Compartilhado | `core` | `unidades_administrativas` | Parte responsável de toda transação. |
| Responsável | `rh` | `servidores`, `vinculos`, `cargos`, `funcoes`, `dependencias` | Relações com `core.pessoas`. |
| Responsável | `tributos` | `lancamentos_tributarios`, `quotas`, `debitos`, `creditos` | Para `pessoas`. |
| Responsável | `contabilidade` | `empenhos`, `despesas`, `receitas`, `contas_contabeis`, `rateios` | Para `fornecedores`/`unidades`. |
| Responsável | `compras` | `compras`, `itens_compras`, `contratos`, `licitacaos` | Encapsuladas em PROCESSO_DOCUMENTAL. |
| Responsável | `licitacoes` | `licitacoes_masters`, `objetos`, `lances`, `habilitacoes`, `aditamentos` | Originam CONTRATO. |
| Responsável | `saude` | `agendamentos`, `fichas_atendimento`, `pacientes`, `prescricoes` | Para `pessoas_fisicas`. |
| Responsável | `educacao` | `matriculas`, `turmas`, `alunos`, `disciplinas`, `boletins` | Para `pessoas_fisicas`. |
| Responsável | `assistencia_social` | `fichas_atendimento_as`, `beneficios`, `programas_sociais` | Para `pessoas_fisicas`. |
| Responsável | `almoxarifado` | `itens_estoque`, `movimentos_estoque`, `categorias_itens` | Entre `unidades_administrativas`. |
| Responsável | `patrimonio` | `bens`, `depreciacoes`, `baixas_bens`, `transferencias_bens` | Para `unidades_administrativas`. |
| Responsável | `frotas` | `veiculos`, `abastecimentos`, `manutencoes`, `deslocamentos` | Para `unidades_administrativas`. |
| Responsável | `obras` | `obras`, `plantas`, `servicos_obra`, `inspecoes_obra` | Para `unidades_administrativas`. |
| Responsável | `ouvidoria` | `protocolos`, `atendimentos`, `reclamacoes`, `respostas` | Para `pessoas`/`unidades`. |
| Responsável | `transparencia` | `publicacoes`, `leis`, `colunas_fiscais`, `comprovantes_despesas` | Dados públicos. |
| Responsável | `controladoria` | `indicadores`, `metas`, `avaliacoes`, `perfis_risco` | Para `contas_contabeis`. |
| Responsável | `planejamento` | `planos`, `objetivos_estrategicos`, `atividades_planos`, `cronogramas` | Para `unidades`. |
| Responsável | `procuradoria` | `processos_judiciais`, `autuacoes`, `notificacoes`, `pecas_processuais` | Para `processos_documentais`. |
| Responsável | `gabinete` | `atas`, `distribuicoes`, `posicionamentos` | Para `processos_documentais`. |
| Responsável | `administracao` | `configuracoes`, `parametros`, `tabelas_auxiliares`, `imoveis` | Dados de institucionalização. |
| Responsável | `agricultura` | (entidades específicas) | Seguem o padrão abaixo. |
| Responsável | `financas` | (entidades específicas) | Seguem o padrão abaixo. |

> As demais entidades listadas acima (ex.: `vinculos`, `cargos`, `funcoes`, `dependencias`, `despesas`, `receitas`, `contas_contabeis`, `itens_estoque`, `lances`, `matriculas`, …) **seguem o mesmo padrão** — `id` uuid PK + `[audit fields]` — e estão detalhadas coluna a coluna no `Dicionario-de-dados.md`.

# 3. Metodologia de Mapeamento Conceitual → Lógico

| Conceitual | Lógico (tabela) | Regra de conversão |
| ---------- | --------------- | ------------------ |
| Entidade (`CAIXA_ALTA`) | tabela `snake_case` plural | 1:1 — nome da entidade em minúsculas, pluralizado. |
| Atributo | coluna | tipo lógico (conforme tabela de tipos abaixo). |
| Identificador interno | `id` | `uuid` v4, PK, `NOT NULL`. |
| Identificador externo | coluna(es) | `text`/`numeric`, com `UNIQUE` quando único. |
| Relacionamento 1:1 | coluna FK + `UNIQUE` | `entidade_id` → PK da outra; restrição `UNIQUE` garante 1:1. |
| Relacionamento 1:N | coluna FK | `entidade_id` → PK da outra (sem `UNIQUE`). |
| Relacionamento N:M | tabela de junção | PK composta `(a_id, b_id)` + FKs. |
| Entidade‑mestra | tabela `core.*` | + `[audit fields]` + histórico versionável. |
| Dado sensível (LGPD) | coluna criptografada | `text` armazenado AES-256 + auditoria. |

| Tipo conceitual | Tipo lógico (PostgreSQL) | Uso |
| --------------- | ------------------------ | --- |
| Identificador | `uuid` | PK/ FK genéricas. |
| Texto curto / código | `text` | login, CPF, matrícula, código IBGE. |
| Texto longo / descrição | `text` | assunto, histórico, descrição. |
| Numérico monetário | `numeric(15,2)` | valores, preços, saldos. |
| Quantidade | `numeric(15,2)` | qtde, estoque. |
| Data | `date` | data_nascimento, data_admissao. |
| Data/hora (com timestamp) | `timestamp` | created_at, updated_at, ultimo_login. |
| Booleano | `boolean` | principal, ativo. |
| Inteiro (ano) | `integer` | ano. |
| Inteiro grande (bytes) | `bigint` | tamanho. |
| JSON / estrutura | `jsonb` | valores_antigos, valores_novos, dinâmico. |
| Texto sensível | `text` (criptografado) | CPF, RG, senha, mfa_secret. |

---

# 4. Entidades‑Mestres (Master Data) — Atributos

## 4.1. Pessoa — grupo `core.pessoas`

### `pessoas`  (esquema `core`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| tipo | text | | Não | {FISICA, JURIDICA} |
| categoria | text | | Não | {CIUDADAO, SERVIDOR, FORNECEDOR, AGENTE_EXTERNO} |
| unidade_id | uuid | FK | Sim | → `core.unidades_administrativas` (vinculada a) |
| [audit fields] | | | | |

### `pessoas_fisicas`  (esquema `core`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| pessoa_id | uuid | FK | Não | → `pessoas` (1:1, UNIQUE) |
| data_nascimento | date | | Sim | |
| sexo | text | | Sim | {M, F, OUTRO} |
| estado_civil | text | | Sim | |
| mae | text | | Sim | sensível (LGPD) |
| pai | text | | Sim | sensível (LGPD) |
| [audit fields] | | | | |

### `pessoas_juridicas`  (esquema `core`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| pessoa_id | uuid | FK | Não | → `pessoas` (1:1, UNIQUE) |
| razao_social | text | | Não | |
| nome_fantasia | text | | Sim | |
| cnae_principal | text | | Sim | |
| capital | numeric(15,2) | | Sim | |
| [audit fields] | | | | |

### `enderecos`  (esquema `core`) — histórico
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| pessoa_id | uuid | FK | Não | → `pessoas` (1:N) |
| tipo | text | | Não | {RESIDENCIAL, COMERCIAL, ...} |
| logradouro | text | | Não | |
| numero | text | | Não | |
| complemento | text | | Sim | |
| bairro | text | | Sim | |
| cep | text | | Sim | |
| cidade | text | | Sim | |
| estado | text | | Sim | |
| pais | text | | Sim | |
| principal | boolean | | Não | default `false` |
| vigencia_inicio | timestamp | | Não | histórico |
| vigencia_fim | timestamp | | Sim | histórico (NULL = vigente) |
| motivo_alteracao | text | | Sim | histórico |
| [audit fields] | | | | |

### `documentos`  (esquema `core`) — sensível (LGPD)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| pessoa_id | uuid | FK | Não | → `pessoas` (1:N) |
| tipo | text | | Não | {CPF, RG, CNPJ, CNH, PASSAPORTE...} |
| numero | text | | Não | **criptografado** |
| orgao_emissor | text | | Sim | |
| data_emissao | date | | Sim | |
| data_validade | date | | Sim | |
| principal | boolean | | Não | default `false` |
| [audit fields] | | | | |

### `contatos`  (esquema `core`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| pessoa_id | uuid | FK | Não | → `pessoas` (1:N) |
| tipo | text | | Não | {TEL, EMAIL, REDES, WHATSAPP} |
| valor | text | | Não | |
| principal | boolean | | Não | default `false` |
| [audit fields] | | | | |

### `fornecedores`  (esquema `core`) — perfil de `pessoas_juridicas`
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| pessoa_juridica_id | uuid | FK | Não | → `pessoas_juridicas` (1:1, UNIQUE) |
| situacao_cadastro | text | | Não | {ATIVO, INATIVO, SUSPENSO} |
| macro_categoria | text | | Sim | |
| [audit fields] | | | | |

## 4.2. Unidade, Patrimônio e Mobiliário

### `unidades_administrativas`  (esquema `core`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| unidade_pai_id | uuid | FK | Sim | → `unidades_administrativas` (self, hierarquia) |
| codigo_ibge | text | | Sim | `UNIQUE` |
| codigo_siafen | text | | Sim | `UNIQUE` |
| nome | text | | Não | |
| sigla | text | | Sim | `UNIQUE` |
| [audit fields] | | | | |

### `servidores`  (esquema `rh`) — 1:1 com `pessoas_fisicas`
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| pessoa_fisica_id | uuid | FK | Não | → `pessoas_fisicas` (1:1, UNIQUE) |
| unidade_id | uuid | FK | Não | → `unidades_administrativas` |
| matricula | text | | Não | `UNIQUE` |
| data_admissao | date | | Não | |
| data_desligamento | date | | Sim | |
| [audit fields] | | | | |

### `veiculos`  (esquema `frotas`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| unidade_id | uuid | FK | Não | → `unidades_administrativas` |
| placa | text | | Não | `UNIQUE` |
| chassi | text | | Não | `UNIQUE` |
| marca_modelo | text | | Não | |
| [audit fields] | | | | |

### `imoveis`  (esquema `administracao`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| matricula | text | | Não | `UNIQUE` |
| setor | text | | Sim | |
| tipo | text | | Sim | {TERRITORIAL, PREDIAL, RURAL} |
| unidade_id | uuid | FK | Sim | → `unidades_administrativas` |
| [audit fields] | | | | |

### `bens`  (esquema `patrimonio`) — bem móvel, histórico
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| unidade_id | uuid | FK | Não | → `unidades_administrativas` |
| tombo | text | | Não | `UNIQUE` |
| categoria | text | | Não | |
| marca_modelo | text | | Sim | |
| [audit fields] | | | | |

## 4.3. Identidade e Acesso — grupo `core.usuarios`

### `usuarios`  (esquema `core`) — 1:1 com `pessoas`
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| pessoa_id | uuid | FK | Não | → `pessoas` (1:1, UNIQUE) |
| login | text | | Não | `UNIQUE` |
| senha_hash | text | | Não | **criptografado** (bcrypt/argon2) |
| mfa_secret | text | | Sim | **criptografado** |
| ultimo_login | timestamp | | Sim | |
| [audit fields] | | | | |
> Sensível: `senha_hash`, `mfa_secret`.

### `grupos_usuarios`  (esquema `core`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| nome | text | | Não | `UNIQUE` |
| [audit fields] | | | | |

### `permissoes`  (esquema `core`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| chave_acesso | text | | Não | ex.: `compras.compra.criar` (`UNIQUE`) |
| nome | text | | Não | |
| [audit fields] | | | | |

### `usuarios_grupos`  (esquema `core`) — junção N:M
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| usuario_id | uuid | PK/FK | Não | → `usuarios` |
| grupo_usuario_id | uuid | PK/FK | Não | → `grupos_usuarios` |
| created_at | timestamp | | Não | auditoria |
| created_by | uuid | FK | Sim | → `usuarios` |

## 4.4. Documentos corporativos — grupo `core.documentos`

### `processos_documentais`  (esquema `core`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| unidade_id | uuid | FK | Não | → `unidades_administrativas` (tramita) |
| numero | text | | Não | |
| ano | integer | | Não | |
| assunto | text | | Não | |
| descricao | text | | Sim | |
| [audit fields] | | | | |

### `arquivos`  (esquema `core`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| processo_documental_id | uuid | FK | Não | → `processos_documentais` |
| nome | text | | Não | |
| caminho | text | | Não | storage path |
| hash | text | | Não | integridade |
| tamanho | bigint | | Não | bytes |
| tipo_mime | text | | Sim | |
| [audit fields] | | | | |

### `assinaturas`  (esquema `core`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| processo_documental_id | uuid | FK | Não | → `processos_documentais` |
| pessoa_id | uuid | FK | Não | → `pessoas` (assina) |
| documento_id | uuid | FK | Sim | → `documentos` (valida identidade) |
| hash | text | | Não | |
| data | timestamp | | Não | |
| [audit fields] | | | | |

## 4.5. Auditoria — grupo `core.auditoria`

### `auditorias`  (esquema `core`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| tabela | text | | Não | |
| registro_id | uuid | | Não | PK do registro auditado |
| operacao | text | | Não | {INSERT, UPDATE, DELETE} |
| valores_antigos | jsonb | | Sim | |
| valores_novos | jsonb | | Sim | |
| created_at | timestamp | | Não | auditoria |
| created_by | uuid | FK | Sim | → `usuarios` |

### `logs_sistema`  (esquema `core`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| usuario_id | uuid | FK | Não | → `usuarios` (executa) |
| auditoria_id | uuid | FK | Sim | → `auditorias` |
| nivel | text | | Não | {DEBUG, INFO, WARN, ERROR} |
| mensagem | text | | Não | |
| ip_origem | text | | Sim | |
| created_at | timestamp | | Não | auditoria |

---

# 5. Transações Representativas — Atributos

> Derivadas do § 4 do `Modelo-Conceitual.md`. Todas carregam `unidade_id` NOT NULL (regra de relacionamento nº 1).

### `compras` + `itens_compras`  (esquema `compras`)

#### `compras`
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| processo_documental_id | uuid | FK | Não | → `processos_documentais` (encapsula) |
| fornecedor_id | uuid | FK | Não | → `fornecedores` (fornece para) |
| unidade_id | uuid | FK | Não | → `unidades_administrativas` (responde) |
| numero | text | | Não | |
| data | date | | Não | |
| valor_total | numeric(15,2) | | Sim | |
| situacao | text | | Não | |
| historico | text | | Sim | |
| [audit fields] | | | | |

#### `itens_compras`
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| compra_id | uuid | FK | Não | → `compras` |
| descricao | text | | Não | |
| quantidade | numeric(15,2) | | Não | |
| valor_unitario | numeric(15,2) | | Não | |
| valor_total | numeric(15,2) | | Não | |
| [audit fields] | | | | |

### `contratos`  (esquema `compras`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| processo_documental_id | uuid | FK | Não | → `processos_documentais` (encapsula) |
| fornecedor_id | uuid | FK | Não | → `fornecedores` (arrebatado) |
| unidade_id | uuid | FK | Não | → `unidades_administrativas` (responde) |
| licituacao_master_id | uuid | FK | Sim | → `licitacoes.licitacoes_masters` (origem) |
| numero | text | | Não | |
| data_inicio | date | | Não | |
| data_fim | date | | Sim | |
| valor | numeric(15,2) | | Sim | |
| objeto | text | | Sim | |
| [audit fields] | | | | |

### `empenhos`  (esquema `contabilidade`) — entidade de empenho (§ 4 do conceitual)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| processo_documental_id | uuid | FK | Sim | → `processos_documentais` (de) |
| fornecedor_id | uuid | FK | Não | → `fornecedores` (favorecido) |
| unidade_id | uuid | FK | Não | → `unidades_administrativas` (responde) |
| compra_id | uuid | FK | Sim | → `compras.compras` (origem) |
| numero | text | | Não | |
| data | date | | Não | |
| valor | numeric(15,2) | | Não | |
| [audit fields] | | | | |

### `lancamentos_tributarios`  (esquema `tributos`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| pessoa_id | uuid | FK | Não | → `pessoas` (para) |
| conta_contabil_id | uuid | FK | Não | → `contabilidade.contas_contabeis` (debito/credito em) |
| debito | text | | Não | |
| credito | text | | Não | |
| historico | text | | Não | |
| valor | numeric(15,2) | | Não | |
| data | date | | Não | |
| [audit fields] | | | | |

### `agendamentos`  (esquemas `saude`/`educacao`/`assistencia_social`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| pessoa_fisica_id | uuid | FK | Não | → `pessoas_fisicas` (paciente/aluno/beneficiário) |
| unidade_id | uuid | FK | Não | → `unidades_administrativas` (por) |
| data_hora | timestamp | | Não | |
| status | text | | Não | |
| [audit fields] | | | | |

### `movimentos_estoque`  (esquema `almoxarifado`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| item_estoque_id | uuid | FK | Não | → `almoxarifado.itens_estoque` (de) |
| unidade_origem_id | uuid | FK | Não | → `unidades_administrativas` |
| unidade_destino_id | uuid | FK | Sim | → `unidades_administrativas` |
| tipo | text | | Não | {ENTRADA, SAIDA, AJUSTE} |
| quantidade | numeric(15,2) | | Não | |
| data | date | | Não | |
| [audit fields] | | | | |

### `licitacoes_masters`  (esquema `licitacoes`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| processo_documental_id | uuid | FK | Não | → `processos_documentais` (tramita) |
| unidade_id | uuid | FK | Não | → `unidades_administrativas` (por) |
| objeto_id | uuid | FK | Sim | → `licitacoes.objetos` |
| numero | text | | Não | |
| data | date | | Não | |
| situacao | text | | Não | |
| [audit fields] | | | | |

### `protocolos`  (esquema `ouvidoria`)
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| pessoa_id | uuid | FK | Não | → `pessoas` (do) |
| unidade_id | uuid | FK | Não | → `unidades_administrativas` (por) |
| categoria | text | | Não | |
| status | text | | Não | |
| prioridade | text | | Sim | {BAIXA, MEDIA, ALTA, URGENTE} |
| [audit fields] | | | | |

### `fichas_funcionais`  (esquema `rh`) — histórico de vínculos
| Atributo | Tipo Lógico | Chave | Nulo | Observação |
| -------- | ----------- | ----- | ---- | ---------- |
| id | uuid | PK | Não | UUID v4 |
| servidor_id | uuid | FK | Não | → `servidores` (para) |
| unidade_id | uuid | FK | Não | → `unidades_administrativas` (em) |
| vinculo_tipo | text | | Sim | {PRINCIPAL, SUBCONTRATADO, TERCEIRIZADO} |
| data_inicio | date | | Não | |
| data_fim | date | | Sim | |
| [audit fields] | | | | |

---

# 6. Mapeamento de Chaves e Relacionamentos

> Derivado das § 5 do `Modelo-Conceitual.md`, traduzido para constraints de chave estrangeira.

| Regra conceitual | Tabela lógica | Constraint / observação |
| ---------------- | ------------- | ----------------------- |
| 1. `UNIDADE_ADMINISTRATIVA` é parte responsável de toda transação | todas as transacionais (`compras`, `contratos`, `empenhos`, `protocolos`, `movimentos_estoque`, `agendamentos`, `lancamentos_tributarios`, …) | coluna `unidade_id` (uuid, NOT NULL) → `core.unidades_administrativas` |
| 2. `PESSOA` é parte "on‑screen" das transações | `fornecedores`, `lancamentos_tributarios`, `agendamentos`, `protocolos`, `assinaturas` | FK `pessoa_id`/`fornecedor_id`/`pessoa_fisica_id` → `pessoas`/`fornecedores`/`pessoas_fisicas` |
| 3. `PROCESSO_DOCUMENTAL` encapsula COMPRA, CONTRATO, EMPENHO | `compras`, `contratos`, `empenhos` | `processo_documental_id` → `processos_documentais` |
| 4. `FORNECEDOR` ≈ `PESSOA_JURIDICA` (categoria=FORNECEDOR) | `fornecedores` | `pessoa_juridica_id` UNIQUE → `pessoas_juridicas` |
| 5. `DOCUMENTO` valida identidade de `PESSOA` | `assinaturas` | `documento_id` → `documentos` |
| 6. `USUARIO` atua via `GRUPO_USUARIO`/`PERMISSAO`; `created_by`/`updated_by` → `USUARIO` | todas as críticas + auditoria/log | `created_by`, `updated_by`, `deleted_by` → `usuarios` |
| 6b. `USUARIO` ↔ `GRUPO_USUARIO` (N:M) | `usuarios_grupos` | PK composta (`usuario_id`, `grupo_usuario_id`) + FKs |
| 6c. `GRUPO_USUARIO` ↔ `PERMISSAO` (N:M) | `grupos_permissoes` (tabela de junção) | padrão `core`, PK composta + FKs |
| 1:1 `PESSOA` → `PESSOA_FISICA` / `PESSOA_JURIDICA` | `pessoas_fisicas`, `pessoas_juridicas` | `pessoa_id` UNIQUE NOT NULL → `pessoas` |
| 1:1 `SERVIDOR` → `PESSOA_FISICA` | `servidores` | `pessoa_fisica_id` UNIQUE NOT NULL → `pessoas_fisicas` |
| 1:1 `USUARIO` → `PESSOA` | `usuarios` | `pessoa_id` UNIQUE NOT NULL → `pessoas` |
| 1:1 `FORNECEDOR` → `PESSOA_JURIDICA` | `fornecedores` | `pessoa_juridica_id` UNIQUE NOT NULL → `pessoas_juridicas` |
| `UNIDADE` hierárquica | `unidades_administrativas` | `unidade_pai_id` → `unidades_administrativas` (self-ref) |
| `AUDITORIA` registra `LOG_SISTEMA`; `USUARIO` executa | `auditorias`, `logs_sistema` | `logs_sistema.auditoria_id` → `auditorias`; `logs_sistema.usuario_id` → `usuarios` |
| `ARQUIVO` pertence a `PROCESSO_DOCUMENTAL` | `arquivos` | `processo_documental_id` → `processos_documentais` |
| Soft-delete transversal | todas as críticas | `deleted_at`/`deleted_by`; linhas filhas desvinculadas pela aplicação |

> **Nota:** políticas de exclusão (`soft delete`) e cascata são aplicadas pela camada de aplicação/ORM; em nível lógico mantemos as FKs explícitas e registramos `deleted_at`/`deleted_by`.

---

# 7. Convenções Aplicáveis

| Regra | Aplicação no Modelo Lógico |
| ----- | -------------------------- |
| Identificador interno | `uuid` v4 (`id`) em **toda** entidade. |
| Identificadores externos | `text`/`numeric` (CPF, CNPJ, CNS, NIS, matrícula, códigos IBGE/INEP/CNES). |
| Nomenclatura | tabelas no plural, português, `snake_case`; chaves estrangeiras `*_id`. |
| Tipos lógicos | `uuid`, `text`, `timestamp`, `date`, `numeric(p,s)`, `boolean`, `bigint`, `integer`, `jsonb`. |
| Esquemas | particionamento por domínio responsável (`core`, `rh`, `compras`, …). |
| Auditoria obrigatória | `created_at`, `created_by`, `updated_at`, `updated_by`, `deleted_at`, `deleted_by` em tabelas críticas. |
| Exclusão | **soft delete** (`deleted_at`), nunca físico em dados críticos. |
| Histórico | atributos versionáveis: `vigencia_inicio`, `vigencia_fim`, `motivo_alteracao`. |
| Dados sensíveis | saúde, familiares, documentos, socioassistência → criptografados e auditados (LGPD — Lei 13.709/2018). |

---

# 8. Atributos Sensíveis (LGPD)

| Atributo | Tabela | Motivo | Tratamento |
| -------- | ------ | ------ | ---------- |
| `numero` (CPF/CNPJ/RG/CNH) | `documentos` | identidade | criptografado (AES-256) + auditoria |
| `senha_hash` | `usuarios` | credencial | hash (bcrypt/argon2) + MFA |
| `mfa_secret` | `usuarios` | autenticação | criptografado |
| `mae`, `pai` | `pessoas_fisicas` | genealogia | criptografado |
| `data_nascimento` | `pessoas_fisicas` | identidade | mascarado em relatórios agregados |
| `ip_origem`, `mensagem` | `logs_sistema` | rastreabilidade | retenção conforme política de logs |

---

# 9. Mapeamento para os modelos seguintes

Este documento é insumo direto para:

- **Modelo Físico** (`Modelo-Fisico.md`): DDL PostgreSQL, particionamento por esquema/domínio, índices, políticas de soft-delete e constraints de chave estrangeira.
- **MER / Diagramas ER** (`MER.md` + `Diagramas-ER/`): refinamento visual por esquema (Mermaid / draw.io).
- **Dicionário de Dados** (`Dicionario-de-dados.md`): catálogo completo de colunas, constraints, índices e dicionário.
- **Views** (`Views.md`), **Procedures** (`Procedures.md`), **Seeds** (`Seeds.md`): consumidores diretos deste modelo.
- **Modelos-SQL** (`Modelos-SQL.md`): queries de acesso por domínio.

> O padrão do piloto de Compras — entidade, atributo, chave, histórico e auditoria — foi replicado aqui a nível corporativo.

---

# 10. Versionamento

- 1.0 — 2026-08-19 — Início do modelo lógico corporativo, derivado de `Modelo-Conceitual.md` e `005-Arquitetura-de-Dados.md`.

---

**Documento:**Modelo-Logico.md

**Última atualização:** 2026-08-19

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente