# Dicionário de Dados

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Modelo de Dados

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
- 005-Arquitetura-de-Dados.md (01-Arquitetura-Corporativa)
- Modelo-Conceitual.md
- Modelo-Logico.md
- Modelo-Fisico.md

---

Este documento é o **Dicionário de Dados Corporativo** do SIGMUN, derivado do `Modelo-Fisico.md` (DDL PostgreSQL). Cataloga tabelas, colunas, tipos, constraints, índices, views e políticas de soft-delete de todos os esquemas/domínios do sistema, como referência única para desenvolvedores, administradores de dados e integradores.

> **Nota:** a estrutura física completa (DDL) está no `Modelo-Fisico.md`. Este dicionário documenta entidade por entidade, campo por campo.

---

# 1. Objetivo

Registrar de forma centralizada e normalizada todas as entidades de dados do SIGMUN, seus atributos, tipos físicos, restrições, índices e políticas de dados sensíveis (LGPD), garantizando a "fonte única da verdade" do modelo.

---

# 2. Esquemas do Banco `sigmun`

Relacionados da arquitetura por domínios, todos sob a base `sigmun`:

| Esquema | Responsável | Tabelas |
| ------- | ----------- | ------- |
| `core` | Compartilhado / Cadastro Único | `pessoas`, `pessoas_fisicas`, `pessoas_juridicas`, `enderecos`, `documentos`, `contatos`, `fornecedores`, `unidades_administrativas`, `usuarios`, `grupos_usuarios`, `permissoes`, `usuarios_grupos`, `grupos_permissoes`, `processos_documentais`, `arquivos`, `assinaturas`, `auditorias`, `logs_sistema` |
| `rh` | Recursos Humanos | `servidores`, `fichas_funcionais`, `vinculos`, `cargos`, `funcoes`, `dependencias` |
| `tributos` | Tributação | `lancamentos_tributarios`, `quotas`, `debitos`, `creditos` |
| `contabilidade` | Contabilidade | `contas_contabeis`, `empenhos`, `despesas`, `receitas`, `rateios` |
| `compras` | Compras | `compras`, `itens_compras`, `contratos` |
| `licitacoes` | Licitações | `licitacoes_masters`, `objetos`, `lances`, `habilitacoes`, `aditamentos` |
| `saude` | Saúde | `agendamentos`, `pacientes`, `fichas_atendimento`, `prescricoes` |
| `educacao` | Educação | `agendamentos`, `turmas`, `alunos`, `matriculas`, `disciplinas`, `boletins` |
| `assistencia_social` | Assistência Social | `agendamentos`, `fichas_atendimento_as`, `beneficios`, `programas_sociais` |
| `almoxarifado` | Almoxarifado | `categorias_itens`, `itens_estoque`, `movimentos_estoque` |
| `patrimonio` | Patrimônio | `bens`, `depreciacoes`, `baixas_bens`, `transferencias_bens` |
| `frotas` | Frotas | `veiculos`, `abastecimentos`, `manutencoes`, `deslocamentos` |
| `obras` | Obras | `obras`, `plantas`, `servicos_obra`, `inspecoes_obra` |
| `ouvidoria` | Ouvidoria | `protocolos`, `atendimentos`, `reclamacoes`, `respostas` |
| `transparencia` | Transparencia | `publicacoes`, `leis`, `colunas_fiscais`, `comprovantes_despesas` |
| `controladoria` | Controladoria | `indicadores`, `metas`, `avaliacoes`, `perfis_risco` |
| `planejamento` | Planejamento | `planos`, `objetivos_estrategicos`, `atividades_planos`, `cronogramas` |
| `procuradoria` | Procuradoria | `processos_judiciais`, `autuacoes`, `notificacoes`, `pecas_processuais` |
| `gabinete` | Gabinete | `atas`, `distribuicoes`, `posicionamentos` |
| `administracao` | Administração | `imoveis`, `configuracoes`, `parametros`, `tabelas_auxiliares` |
| `agricultura` | Agricultura | `propriedades_rurais`, `culturas`, `plantios` |
| `financas` | Finanças | `concessoes`, `taxas` |

---

# 3. Convenções de Campos de Auditoria e Histórico

| Campos | Aplicação |
| ------ | ---------- |
| `created_at`, `created_by` | Toda tabela (obrigatório). |
| `updated_at`, `updated_by` | Tabelas críticas. |
| `deleted_at`, `deleted_by` | Tabelas críticas (soft delete). |
| `versao`, `vigencia_inicio`, `vigencia_fim`, `motivo_alteracao` | Atributos versionados (histórico). |

---

# 4. Catálogo de Tabelas

> Convenção de tipos: `UUID` PK/DEFAULT `gen_random_uuid()`; `TEXT` strings; `TIMESTAMPTZ` data/hora com fuso; `DATE` data; `NUMERIC(15,2)` monetario/quantidade; `JSONB` estrutura; `BIGINT` inteiro grande.

## 4.1. Grupo `core.pessoas`

### `core.pessoas`
| Campo | Tipo | Nulo | PK/FK | Obs |
| ----- | ---- | ---- | ----- | --- |
| id | UUID | No | PK | UUID v4 |
| tipo | TEXT | No | | {FISICA, JURIDICA} |
| categoria | TEXT | No | | {CIUDADAO, SERVIDOR, FORNECEDOR, AGENTE_EXTERNO} |
| unidade_id | UUID | Si | FK → `core.unidades_administrativas` | |
| [audit] | | | | created/updated/deleted |

**CHECKS:** `ck_pessoas_tipo`, `ck_pessoas_categoria`, `ck_pessoas_deleted`.
**Índices:** `pk_pessoas`, `idx_pessoas_tipo/categoria/unidade_id`.

### `core.pessoas_fisicas`
| Campo | Tipo | Nulo / Clave | Nota |
| ----- | ---- | ---- | ----- |
| id | UUID | No | PK |
| pessoa_id | UUID | No | FK UNIQUE → `core.pessoas` (1:1) |
| data_nascimento | DATE | Si | |
| sexo | TEXT | Si | {M, F, OUTRO} |
| estado_civil | TEXT | Si | |
| mae | TEXT | Si | LGPD: criptografado |
| pai | TEXT | Si | LGPD: criptografado |
| [audit_fields] | | | |
**CHECK:** `ck_pessoas_fisicas_deleted`.

### `core.pessoas_juridicas`
| Campo | Tipo | Nulo | Clave | Nota |
| ----- | ---- | ---- | ----- | ---- |
| id | UUID | No | PK | |
| pessoa_id | UUID | No | FK UNIQUE → `core.pessoas` | |
| razao_social | TEXT | No | | |
| nome_fantasia | TEXT | Si | | |
| cnae_principal | TEXT | Si | | |
| capital | NUMERIC(15,2) | Si | | |
| [audit_fields] | | | | |
**CHECK:** `ck_pessoas_juridicas_deleted`.

### `core.enderecos`
| Campo | Tipo | Nivo | Clave | Nota |
| ----- | ---- | ----- | ----- | ---- |
| id | UUID | No | PK | |
| pessoa_id | UUID | No | FK → `core.pessoas` | |
| tipo | TEXT | No | | |
| logradouro | TEXT | No | | |
| numero | TEXT | No | | |
| complemento | TEXT | Si | | |
| bairro | TEXT | Si | | |
| cep | TEXT | Si | | |
| cidade | TEXT | Si | | |
| estado | TEXT | Si | | |
| pais | TEXT | Si | | |
| principal | BOOLEAN | No | | DEF FALSE |
| vigencia_inicio | TIMESTAMPTZ | No | | histórico |
| vigencia_fim | TIMESTAMPTZ | Si | | NULL = vigente |
| motivo_alteracao | TEXT | Si | | |
| [audit_fields] | | | | |

Índices: `idx_enderecos_pessoa_id`, `idx_enderecos_vigencia`.

### `core.documentos`
| Campo | Tipo | Nivo | Clave | Nota |
| ----- | ---- | ----- | ----- | ---- |
| id | UUID | No | PK | |
| pessoa_id | UUID | No | FK → `core.pessoas` | |
| tipo | TEXT | No | | CPF, RG, CNPJ... |
| numero | TEXT | No | | LGPD: criptografado |
| orgao_emissor | TEXT | Si | | |
| data_emissao | DATE | Si | | |
| data_validade | DATE | Si | | |
| principal | BOOLEAN | No | | |
| [audit_fields] | | | | |

### `core.contatos`
| Campo | Tipo | Nivo | Clave ||
| id | UUID | No | PK |
| pessoa_id | UUID | No | FK → `core.pessoas` |
| tipo | TEXT | No | {TEL, EMAIL, REDES, WHATSAPP} |
| valor | TEXT | No | |
| principal | BOOLEAN | No | DEF FALSE |
| [audit_fields] | | | |

CHECKS: `ck_contatos_tipo`, `ck_contatos_deleted`.

### `core.fornecedores`
| Campo | Tipo | Nivo | Clave ||
| id | UUID | No | PK |
| pessoa_juridica_id | UUID | No | FK UNIQUE → `core.pessoas_juridicas` |
| situacao_cadastro | TEXT | No | {ATIVO, INATIVO, SUSPENSO} |
| macro_categoria | TEXT | Si | |
| [audit_fields] | | | |

### `core.unidades_administrativas`
| Campo | Tipo | Nivo | Clave ||
| id | UUID | No | PK |
| unidade_pai_id | UUID | Si | FK self-ref |
| codigo_ibge | TEXT | Si | UNIQUE |
| codigo_siafi | TEXT | Si | UNIQUE |
| nome | TEXT | No | |
| sigla | TEXT | Si | UNIQUE |
| [audit_fields] | | | |

## 4.2. Grupo `core.usuarios`

### `core.usuarios`
| Campo | Tipo | Nulo | Clave | Nota |
| ----- | ---- | ---- | ----- | ---- |
| id | UUID | No | PK | |
| pessoa_id | UUID | No | FK UNIQUE → `core.pessoas` | |
| login | TEXT | No | UNIQUE | |
| senha_hash | TEXT | No | | LGPD: bcrypt/argon2 |
| mfa_secret | TEXT | Si | | LGPD: criptografado |
| ultimo_login | TIMESTAMPTZ | Si | | |
| [audit_fields] | | | | |
**CHECK:** `ck_usuarios_deleted`.

### `core.grupos_usuarios`
| Campo | Tipo | Nulo | Clave |
| id | UUID | NO | PK |
| nome | TEXT | NO | UNIQUE |
| [audit_fields] | | | |

### `core.permissoes`
| Campo | Tipo | Nulo | Clave |
| id | UUID | NO | PK |
| chave_acesso | TEXT | NO | UNIQUE |
| nome | TEXT | NO | |
| [audit_fields] | | | |

### `core.usuarios_grupos` (N:M)
| Campo | Tipo | Nulo | Clave |
| usuario_id | UUID | NO | FK → `core.usuarios`; parte de PK |
| grupo_usuario_id | UUID | NO | FK → `core.grupos_usuarios`; parte de PK |
| created_at | TIMESTAMPTZ | NO | |
| created_by | UUID | Si | |

### `core.grupos_permissoes` (N:M)
| Campo | Tipo | Nulo | Clave |
| grupo_usuario_id | UUID | NO | FK; parte de PK |
| permissao_id | UUID | NO | FK → `core.permissoes`; parte de PK |
| created_at | TIMESTAMPTZ | NO | |
| created_by | UUID | Si | |

## 4.3. Grupo `core.documentos`

### `core.processos_documentais`
| Campo | Tipo | Nulo | Clave | Nota |
| id | UUID | NO | PK | |
| unidade_id | UUID | NO | FK → `core.unidades_administrativas` | |
| numero | TEXT | NO | | UNIQUE (numero, ano) |
| ano | INTEGER | NO | | |
| assunto | TEXT | NO | | |
| descricao | TEXT | Si | | |
| [audit_fields] | | | | |
Índices: `idx_processos_documentais_unidade_id`, `idx_processos_documentais_numero_ano`.

### `core.arquivos`
| Campo | Tipo | Nulo | Clave | Nota |
| id | UUID | NO | PK | |
| processo_documental_id | UUID | NO | FK → `core.processos_documentais` | |
| nome | TEXT | NO | | |
| caminho | TEXT | NO | | |
| hash | TEXT | NO | | SHA-256 |
| tamanho | BIGINT | NO | | |
| tipo_mime | TEXT | Si | | |
| [audit_fields] | | | | |

### `core.assinaturas`
| Campo | Tipo | Nulo | Clave | Nota |
| id | UUID | NO | PK | |
| processo_documental_id | UUID | NO | FK → `core.processos_documentais` | |
| pessoa_id | UUID | NO | FK → `core.pessoas` | |
| documento_id | UUID | Si | FK → `core.documentos` | |
| hash | TEXT | NO | | firma digital |
| data | TIMESTAMPTZ | NO | | |

## 4.4. Grupo `core.auditoria`

### `core.auditorias`
| Campo | Tipo | Nulo | Clave | Nota |
| id | UUID | NO | PK | |
| tabela | TEXT | NO | | |
| registro_id | UUID | NO | | PK do registro |
| operacao | TEXT | NO | {INSERT, UPDATE, DELETE} |
| valores_antigos | JSONB | Si | | |
| valores_novos | JSONB | Si | | |
| created_at | TIMESTAMPTZ | NO | | |
| created_by | UUID | Si | | |

### `core.logs_sistema`
| Campo | Tipo | Nulo | Clave | Nota |
| id | UUID | NO | PK | |
| usuario_id | UUID | NO | FK → `core.usuarios` | |
| auditoria_id | UUID | Si | FK → `core.auditorias` | |
| nivel | TEXT | NO | | {DEBUG, INFO, WARN, ERROR} |
| mensagem | TEXT | NO | | |
| ip_origem | TEXT | Si | | |
| created_at | TIMESTAMPTZ | NO | | |

## 4.5. Domínio `rh`

| Tabela | Colunas principais | Chaves / Notas |
| ------ | ---- |
| `rh.servidores` | id PK; pessoa_fisica_id FK UNIQUE→`core.pessoas_fisicas`; unidade_id FK; matricula UNIQUE; data_admissao; data_desligamento; [audit] | |
| `rh.fichas_funcionais` | id PK; servidor_id FK; unidade_id FK; vinculo_tipo {PRINCIPAL, SUBCONTRATADO, TERCEIRIZADO}; data_inicio; data_fim; [audit] | |
| `rh.vinculos` | id PK; servidor_id FK; unidade_id FK; data_inicio; data_fim; [audit] | |
| `rh.cargos` | id PK; codigo UNIQUE; nome; [audit] | |
| `rh.funcoes` | id PK; codigo UNIQUE; nome; descricao; [audit] | |
| `rh.dependencias` | id PK; pessoa_fisica_id FK; parentesco; data_nascimento; [audit] | |

## 4.6. Domínio `tributos`

| Tabela | Colunas | Chaves / Notas |
| ------ | --------|---|---|
| `tributos.lancamentos_tributarios` | id PK; pessoa_id FK→`core.pessoas`; conta_contabil_id FK→`contabilidade.contas_contabeis`; debito TEXT; credito TEXT; historico; valor NUMERIC(15,2); data DATE; [audit] | |
| `tributos.quotas` | id PK; pessoa_id FK; exercicio INT; mes INT; valor NUMERIC; situacao; [audit] | |
| `tributos.debitos` | id PK; lancamento_id FK; valor; data_vencimento; situacao; [audit] | |
| `tributos.creditos` | id PK; lancamento_id FK; valor; data_credito; origem; [audit] | |

## 4.7. Domínio `contabilidade`

| Tabela | Colunas | Chaves / Notas |
| --------- | --------|---|
| `contabilidade.contas_contabeis` | id PK; codigo UNIQUE; descricao; tipo {DEBITO,CREDITO}; natureza {SINTETICA,ANALITICA}; [audit] | |
| `contabilidade.empenhos` | id PK; processo_documental_id FK; fornecedor_id FK; unidade_id FK; compra_id FK; numero; data; valor NUMERIC; [audit] | |
| `contabilidade.despesas` | id PK; unidade_id FK; conta_contabil_id FK; empenho_id FK; valor; data; historico; [audit] | |
| `contabilidade.receitas` | id PK; unidade_id FK; conta_contabil_id FK; fonte; valor; data; historico; [audit] | |
| `contabilidade.rateios` | id PK; empenho_id FK; conta_contabil_id FK; percentual NUMERIC(5,2); valor; [audit] | |

## 4.8. Domínio `compras`

| Tabela | Colunas | Chaves / Notas |
| --------- | --------|---|
| `compras.compras` | id PK; processo_documental_id FK; fornecedor_id FK; unidade_id FK; numero; data; valor_total; situacao; [audit] | |
| `compras.itens_compras` | id PK; compra_id FK; descricao; quantidade; valor_unitario; valor_total; [audit] | |
| `compras.contratos` | id PK; processo FK; fornecedor FK; unidade FK; licitacao_master_id FK→`licitacoes.licitacoes_masters`; numero; data_inicio; data_fim; valor; objeto; [audit] | |

## 4.9. Domínio `licitacoes`

| Tabela | Colunas | Chaves |
|----------|----------|--------|
| `licitacoes.licitacoes_masters` | id PK; processo FK; unidade FK; objeto_id FK; numero; data; status; [audit] | |
| `licitacoes.objetos` | id PK; descricao; categoria; [audit] | |
| `licitacoes.lances` | id PK; licitacao FK; fornecedor FK; valor; data_hora; [audit] | |
| `licitacoes.habilitacoes` | id PK; licitacao FK; fornecedor FK; criterio; pontuacao; aprovado BOOL; [audit] | |
| `licitacoes.aditamentos` | id PK; contrato FK; numero; data; valor; objeto; [audit] | |

## 4.10. Domínio `saude`

| Tabela | Colunas |
|------|----------|
| `saude.agendamentos` | id PK; pessoa_fisica_id FK; unidade_id FK; data_hora; status; [audit] |
| `saude.pacientes` | id PK; pessoa_fisica_id FK UNIQUE; numero_cns; [audit] |
| `saude.fichas_atendimento` | id PK; paciente_id FK; unidade FK; data_atendimento; tipo; observacao; [audit] |
| `saude.prescricoes` | id PK; ficha FK; medicamento; dosagem; via; frequencia; duracao; [audit] |

## 4.11. Domínio `educacao`

| Tabela | Colunas |
|---------|--------|
| `educacao.agendamentos` | replicada (LIKE saude.agendamentos) |
| `educacao.turmas` | id PK; codigo UNIQUE; nome; nivel; serie; [audit] |
| `educacao.alunos` | id PK; pessoa_fisica_id FK UNIQUE; matricula UNIQUE; [audit] |
| `educacao.matriculas` | id PK; aluno FK; turma FK; data; situacion; [audit] |
| `educacao.disciplinas` | id PK; codigo UNIQUE; nome; carga_horaria; [audit] |
| `educacao.boletins` | id PK; matricula FK; disciplina FK; nota NUMERIC(5,2); data_lancamento; [audit] |

## 4.12. Domínio `assistencia_social`

| Tabela | Colunas |
|-----|----|
| `assistencia_social.agendamentos` | replicada |
| `assistencia_social.fichas_atendimento_as` | id PK; pessoa_fisica FK; unidade FK; data; tipo_atendimento; status; [audit] |
| `assistencia_social.beneficios` | id PK; pessoa_fisica FK; codigo UNIQUE; nome; inicio; fim; valor; [audit] |
| `assistencia_social.programas_sociais` | id PK; codigo UNIQUE; nome; descricao; inicio; fim; [audit] |

## 4.13. Domínio `almoxarifado`

| Tabela | Colunas |
|-----------|------|
| `almoxarifado.categorias_itens` | id PK; codigo UNIQUE; nome; [audit] |
| `almoxarifado.itens_estoque` | id PK; categoria FK; codigo UNIQUE; descricao; unidade_medida; quantidade; valor_unitario; [audit] |
| `almoxarifado.movimentos_estoque` | id PK; item FK; unid. origem FK; unid. destino FK; tipo {ENTRADA,SAIDA,AJUSTE}; quantidade; data; [audit] |

## 4.14. Domínio `patrimonio`

| Tabela | Colunas |
|-----|-----|
| `patrimonio.bens` | id PK; unidade FK; tombo UNIQUE; categoria; marca_modelo; [audit] |
| `patrimonio.depreciacoes` | id PK; bem FK; data; valor; [audit] |
| `patrimonio.baixas_bens` | id PK; bem FK; data; motivo; valor_residual; [audit] |
| `patrimonio.transferencias_bens` | id PK; bem FK; unid. origem FK; unid. destino FK; data; motivo; [audit] |

## 4.15. Domínio `frotas`

| Tabela | Colunas |
|-----|----|
| `frotas.veiculos` | id; unidade_id FK; placa UNIQUE; chassi UNIQUE; marca_modelo; [audit] |
| `frotas.abastecimentos` | id; veiculo FK; data; litros; valor; [audit] |
| `frotas.manutencoes` | id; veiculo FK; data; tipo; descricao; custo; [audit] |
| `frotas.deslocamentos` | id; veiculo FK; unidade FK; data_hora; origem; destino; quilometragem; [audit] |

## 4.16. Domínio `obras`

| Tabela | Colunas |
|-----|----|
| `obras.obras` | id; unidade FK; codigo UNIQUE; nome; descricao; inicio; fim; valor; status; [audit] |
| `obras.plantas` | id; obra FK; arquivo FK; descricao; [audit] |
| `obras.servicos_obra` | id; obra FK; descricao; inicio; fim; valor; [audit] |
| `obras.inspecoes_obra` | id; obra FK; data; tipo; descricao; resultado; [audit] |

## 4.17. Domínio `ouvidoria`

| Tabela | Colunas |
|-----|------|
| `ouvidoria.protocolos` | id; pessoa FK; unidade FK; categoria; status; [audit] |
| `ouvidoria.atendimentos` | id; protocolo FK; unidade FK; data_hora; tipo; descricao; [audit] |
| `ouvidoria.reclamacoes` | id; atendimento FK; descricao; [audit] |
| `ouvidoria.respostas` | id; reclamacao FK; descricao; data_resposta; [audit] |

## 4.18. Domínio `transparencia`

| Tabela | Colunas |
|-----|-----|
| `transparencia.publicacoes` | id; titulo; descricao; data_publicacao; categoria; url_arquivo; [audit] |
| `transparencia.leis` | id; numero; ano UNIQUE(numero,ano); descricao; data_leitura; data_sancao; url_documento; [audit] |
| `transparencia.colunas_fiscais` | id; exercicio; mes; categoria; valor; [audit] |
| `transparencia.comprovantes_despesas` | id; unidade FK; empenho FK; data; valor; arquivo FK; [audit] |

## 4.19. Domínio `controladoria`

| Tabela | Colunas |
|-----|-----|
| `controladoria.indicadores` | id; codigo UNIQUE; nome; descricao; formula; unidade; tipo {QUALITATIVO,QUANTITATIVO}; [audit] |
| `controladoria.metas` | id; indicador FK; exercicio; valor_alvo; valor_realizado; [audit] |
| `controladoria.avaliacoes` | id; indicador FK; data; valor; observacao; [audit] |
| `controladoria.perfis_risco` | id; processo FK; risco {BAIXO,MEDIO,ALTO,CRITICO}; probabilidade; impacto; [audit] |

## 4.20. Domínio `planejamento`

| Tabela | Colunas |
|-----|-----|
| `planejamento.planos` | id; unidade FK; codigo UNIQUE; nome; descricao; inicio; fim; status; [audit] |
| `planejamento.objetivos_estrategicos` | id; plano FK; codigo; descricao; [audit] |
| `planejamento.atividades_planos` | id; objetivo FK; unidade FK; descricao; inicio; fim; status; valor; [audit] |
| `planejamento.cronogramas` | id; atividade FK; inicio; fim; percentual; status; [audit] |

## 4.21. Domínio `procuradoria`

| Tabela | Colunas |
|--------|---------|
| `procuradoria.processos_judiciais` | id; processo_documental FK; unidade FK; numero; vara; data; status; valor; [audit] |
| `procuradoria.autuacoes` | id; processo FK; data; tipo; descricao; [audit] |
| `procuradoria.notificacoes` | id; processo FK; data; tipo; descricao; data_resposta; [audit] |
| `procuradoria.pecas_processuais` | id; processo FK; arquivo FK; tipo; descricao; data; [audit] |

## 4.22. Domínio `gabinete`

| Tabela | Colunas |
|--------|---------|
| `gabinete.atas` | id; processo_documental FK; unidade FK; numero; data_reuniao; descricao; resultado; [audit] |
| `gabinete.distribuicoes` | id; processo FK; unidade_destino FK; data; status; [audit] |
| `gabinete.posicionamentos` | id; processo FK; data; tipo; descricao; [audit] |

## 4.23. Domínio `administracao`

| Tabela | Colunas |
|--------|---------|
| `administracao.imoveis` | id; matricula UNIQUE; setor; tipo {TERRITORIAL,PREDIAL,RURAL}; unidade FK; [audit] |
| `administracao.configuracoes` | id; chave UNIQUE; valor; tipo {STRING,INTEGER,BOOLEAN,JSON}; [audit] |
| `administracao.parametros` | id; chave UNIQUE; valor; [audit] |
| `administracao.tabelas_auxiliares` | id; codigo; descricao; valor; tabela; [audit] |

## 4.24. Domínio `agricultura`

| Tabela | Colunas |
|--------|---------|
| `agricultura.propriedades_rurais` | id; pessoa FK; numero_car UNIQUE; municipio; area_ha; [audit] |
| `agricultura.culturas` | id; codigo UNIQUE; nome; ciclo_meses; [audit] |
| `agricultura.plantios` | id; propriedad FK; cultura FK; data_plantio; area_ha; produtividade; [audit] |

## 4.25. Domínio `financas`

| Tabela | Colunas |
|--------|---------|
| `financas.concessoes` | id; unidade FK; numero; tipo; inicio; fim; valor; [audit] |
| `financas.taxas` | id; concessao FK; codigo; descricao; aliquota NUMERIC(10,4); inicio; fim; [audit] |

---

# 5. Índices Relevantes (resumo)

> Índices automáticos de PK/UNIQUE + índices de desempenho mais relevantes (lista completa no `Modelo-Fisico.md § 5`):

| Índice | Tabela | Motivo |
| ------ | ------ | ------ |
| `idx_pessoas_unidade_id` | `core.pessoas` | Filtro por unidade |
| `idx_enderecos_pessoa_id` | `core.enderecos` | Histórico de endereços |
| `idx_documentos_pessoa_id` | `core.documentos` | Documentos de pessoa |
| `idx_contatos_pessoa_id` | `core.contatos` | Contatos por pessoa |
| `idx_fornecedores_pessoa_juridica_id` | `core.fornecedores` | Fornecedor por jurídica |
| `idx_unidades_pai_id` | `core.unidades_administrativas` | Hierarquia |
| `idx_usuarios_pessoa_id` | `core.usuarios` | Usuário por pessoa |
| `idx_processos_documentais_unidade_id` | `core.processos_documentais` | Processos por unidade |
| `idx_arquivos_processo_id` | `core.arquivos` | Arquivos por processo |
| `idx_assinaturas_processo_id` | `core.assinaturas` | Assinaturas por processo |
| `idx_auditorias_tabela_registro` | `core.auditorias` | Auditoria por entidade |
| `idx_logs_sistema_created_at` | `core.logs_sistema` | Logs por data |
| `idx_servidores_unidade_id` | `rh.servidores` | Servidores por unidade |
| `idx_lancamentos_trib_tributarios_data` | `tributos.lancamentos_tributarios` | Lançamento por data |
| `idx_empenhos_fornecedor_id` | `contabilidade.empenhos` | Empenhos por fornecedor |
| `idx_compras_processo_documental_id` | `compras.compras` | Compras por processo |
| `idx_contratos_licitacao_id` | `compras.contratos` | Contrato por licitação |
| `idx_movimentos_estoque_item_id` | `almoxarifado.movimentos_estoque` | Movimentos por item |
| `idx_veiculos_unidade_id` | `frotas.veiculos` | Veículos por unidade |
| `idx_bens_unidade_id` | `patrimonio.bens` | Bens por unidade |
| `idx_protocolos_pessoa_id` | `ouvidoria.protocolos` | Protocolos por pessoa |
| `idx_agendamentos_pessoa_fisica_id` | `saude.agendamentos` | Agenda por pessoa |

---

# 6. Dados Sensíveis (LGPD)

| Campo | Tabela | Tratamento |
| ----- | ------ | ----------- |
| `numero` | `core.documentos` | Criptografia AES-256 (`pgcrypto`) |
| `senha_hash` | `core.usuarios` | Hash bcrypt/argon2 + MFA |
| `mfa_secret` | `core.usuarios` | Criptografia AES-256 |
| `mae`, `pai` | `core.pessoas_fisicas` | Criptografia AES-256 |
| `data_nascimento` | `core.pessoas_fisicas` | Mascaramento |
| `ip_origem`, `mensagem` | `core.logs_sistema` | Retenção política de logs |

---

# 7. Versionamento

- 2.0 — 2026-08-19 — Dicionário atualizado a partir do `Modelo-Fisico.md` v1.0. Catalogação de toda a estrutura corporativa: esquemas, ~58 tabelas, índices, constraints e dados sensíveis (LGPD).
- 1.0 — 2026-08-03 — Esqueleto inicial (em elaboração).

---

**Documento:** Dicionario-de-dados.md
**Última atualização:** 2026-08-19
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
