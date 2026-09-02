# Modelo Físico

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Modelo de Dados

**Versão:** 1.1

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
- 005-Arquitetura-de-Dados.md (01-Arquitetura-Corporativa)
- 006-Cadastro-Unico-Municipal.md
- Modelo-Conceitual.md
- Modelo-Logico.md
- Dicionario-de-dados.md

---

Este documento corresponde ao **Modelo Físico Corporativo** do SIGMUN, derivado diretamente do `Modelo-Logico.md`. Apresenta o DDL PostgreSQL 16, esquemas, extensões, constraints de integridade referencial, índices, políticas de soft-delete, triggers de auditoria e tratamento de dados sensíveis (LGPD), servindo de base para as migrações Alembic e para o `Dicionario-de-dados.md`.

> **Nota:** o DDL abaixo foi pensado para ser executado por scripts de migração (Alembic/PostgreSQL). A aplicação (FastAPI + SQLAlchemy) é responsável por popular os campos de auditoria (`created_by`, `updated_by`, `deleted_by`) e por aplicar a lógica de soft-delete em cascata.

---

# 1. Objetivo

Definir, a nível físico, a estrutura de tabelas, esquemas, índices, constraints e políticas de armazenamento do banco de dados PostgreSQL do SIGMUN, garantindo performance, integridade, rastreabilidade e conformidade com a LGPD (Lei 13.709/2018).

---

# 2. Infraestrutura Física

## 2.1. Extensões PostgreSQL

| Extensão | Motivo |
| -------- | ------ |
| `pgcrypto` | `gen_random_uuid()` (UUID v4) e funções de criptografia AES-256. |
| `pg_trgm` (opcional) | Aceleração de buscas substring em colunas `text`. |

```sql
CREATE EXTENSION IF NOT EXISTS pgcrypto;
CREATE EXTENSION IF NOT EXISTS pg_trgm;
```

## 2.2. Esquemas PostgreSQL

```sql
CREATE SCHEMA IF NOT EXISTS core;
CREATE SCHEMA IF NOT EXISTS rh;
CREATE SCHEMA IF NOT EXISTS tributos;
CREATE SCHEMA IF NOT EXISTS contabilidade;
CREATE SCHEMA IF NOT EXISTS compras;
CREATE SCHEMA IF NOT EXISTS licitacoes;
CREATE SCHEMA IF NOT EXISTS saude;
CREATE SCHEMA IF NOT EXISTS educacao;
CREATE SCHEMA IF NOT EXISTS assistencia_social;
CREATE SCHEMA IF NOT EXISTS almoxarifado;
CREATE SCHEMA IF NOT EXISTS patrimonio;
CREATE SCHEMA IF NOT EXISTS frotas;
CREATE SCHEMA IF NOT EXISTS obras;
CREATE SCHEMA IF NOT EXISTS ouvidoria;
CREATE SCHEMA IF NOT EXISTS transparencia;
CREATE SCHEMA IF NOT EXISTS controladoria;
CREATE SCHEMA IF NOT EXISTS planejamento;
CREATE SCHEMA IF NOT EXISTS procuradoria;
CREATE SCHEMA IF NOT EXISTS gabinete;
CREATE SCHEMA IF NOT EXISTS administracao;
CREATE SCHEMA IF NOT EXISTS agricultura;
CREATE SCHEMA IF NOT EXISTS financas;
```

## 2.3. Mapeamento de Tipos Lógicos → Físicos

| Tipo Lógico | Tipo Físico PostgreSQL |
| ----------- | ----------------------- |
| `uuid` | `UUID` |
| `text` | `TEXT` |
| `timestamp` | `TIMESTAMPTZ` |
| `date` | `DATE` |
| `numeric(15,2)` | `NUMERIC(15,2)` |
| `boolean` | `BOOLEAN` |
| `integer` | `INTEGER` |
| `bigint` | `BIGINT` |
| `jsonb` | `JSONB` |

## 2.4. Configurações de Sessão

```sql
SET timezone TO 'America/Sao_Paulo';
```

---

# 3. Infraestrutura de Auditoria

## 3.1. Convenção de Campos de Auditoria

As **tabelas críticas** recebem os seis campos padrão:

```sql
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by  UUID,
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by  UUID,
    deleted_at  TIMESTAMPTZ,
    deleted_by  UUID,
```

As **tabelas de log e junção N:M** recebem apenas:

```sql
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by  UUID,
```

## 3.2. Função de Atualização Automática de `updated_at`

```sql
CREATE OR REPLACE FUNCTION core.fn_update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

## 3.3. Soft-Delete por Aplicação

> A exclusão lógica é tratada pela camada de aplicação (SQLAlchemy/ORM). Em nível físico, mantemos a coluna `deleted_at TIMESTAMPTZ` e a constraint `CHECK (deleted_at IS NULL OR deleted_at <= NOW())` em tabelas críticas.

## 3.4. Convenção de Histórico (Versionamento)

Atributos versionáveis recebem:

```sql
    versao           INTEGER      NOT NULL DEFAULT 1,
    vigencia_inicio  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    vigencia_fim     TIMESTAMPTZ,            -- NULL = vigente
    motivo_alteracao TEXT,
```

---

# 4. Detalhamento Físico por Domínio

> Todas as tabelas usam `UUID v4` como PK (`DEFAULT gen_random_uuid()`). FKs usam `ON UPDATE CASCADE ON DELETE RESTRICT` (exceto junções N:M, com `CASCADE`).

## 4.1. Grupo `core.pessoas`

### `pessoas`

```sql
CREATE TABLE IF NOT EXISTS core.pessoas (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tipo            TEXT NOT NULL,
    categoria       TEXT NOT NULL,
    unidade_id      UUID,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by      UUID,
    deleted_at      TIMESTAMPTZ,
    deleted_by      UUID,
    CONSTRAINT ck_pessoas_tipo      CHECK (tipo IN ('FISICA', 'JURIDICA')),
    CONSTRAINT ck_pessoas_categoria CHECK (categoria IN ('CIDADAO', 'SERVIDOR', 'FORNECEDOR', 'AGENTE_EXTERNO')),
    CONSTRAINT ck_pessoas_deleted   CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
COMMENT ON TABLE core.pessoas IS 'Entidade-mestra: pessoa física ou jurídica do município.';
COMMENT ON COLUMN core.pessoas.tipo      IS '{FISICA, JURIDICA}';
COMMENT ON COLUMN core.pessoas.categoria IS '{CIDADAO, SERVIDOR, FORNECEDOR, AGENTE_EXTERNO}';
```

### `pessoas_fisicas`

```sql
CREATE TABLE IF NOT EXISTS core.pessoas_fisicas (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pessoa_id       UUID NOT NULL UNIQUE REFERENCES core.pessoas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data_nascimento DATE,
    sexo            TEXT CHECK (sexo IN ('M', 'F', 'OUTRO')),
    estado_civil    TEXT,
    mae             TEXT,
    pai             TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by      UUID,
    deleted_at      TIMESTAMPTZ,
    deleted_by      UUID,
    CONSTRAINT ck_pessoas_fisicas_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
COMMENT ON COLUMN core.pessoas_fisicas.mae IS 'LGPD: criptografado (AES-256)';
COMMENT ON COLUMN core.pessoas_fisicas.pai IS 'LGPD: criptografado (AES-256)';
```

### `pessoas_juridicas`

```sql
CREATE TABLE IF NOT EXISTS core.pessoas_juridicas (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pessoa_id       UUID NOT NULL UNIQUE REFERENCES core.pessoas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    razao_social    TEXT NOT NULL,
    nome_fantasia   TEXT,
    cnae_principal  TEXT,
    capital         NUMERIC(15,2),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by      UUID,
    deleted_at      TIMESTAMPTZ,
    deleted_by      UUID,
    CONSTRAINT ck_pessoas_juridicas_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
```

### `enderecos`

```sql
CREATE TABLE IF NOT EXISTS core.enderecos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pessoa_id       UUID NOT NULL REFERENCES core.pessoas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    tipo            TEXT NOT NULL,
    logradouro      TEXT NOT NULL,
    numero          TEXT NOT NULL,
    complemento     TEXT,
    bairro          TEXT,
    cep             TEXT,
    cidade          TEXT,
    estado          TEXT,
    pais            TEXT,
    principal       BOOLEAN NOT NULL DEFAULT FALSE,
    vigencia_inicio TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    vigencia_fim    TIMESTAMPTZ,
    motivo_alteracao TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by      UUID,
    deleted_at      TIMESTAMPTZ,
    deleted_by      UUID,
    CONSTRAINT ck_enderecos_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
COMMENT ON COLUMN core.enderecos.vigencia_fim IS 'NULL = endereço vigente (histórico).';
```

### `documentos`

```sql
CREATE TABLE IF NOT EXISTS core.documentos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pessoa_id       UUID NOT NULL REFERENCES core.pessoas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    tipo            TEXT NOT NULL,
    numero          TEXT NOT NULL,
    orgao_emissor   TEXT,
    data_emissao    DATE,
    data_validade   DATE,
    principal       BOOLEAN NOT NULL DEFAULT FALSE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by      UUID,
    deleted_at      TIMESTAMPTZ,
    deleted_by      UUID,
    CONSTRAINT ck_documentos_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
COMMENT ON COLUMN core.documentos.numero IS 'LGPD: criptografado (AES-256)';
```

### `contatos`

```sql
CREATE TABLE IF NOT EXISTS core.contatos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pessoa_id       UUID NOT NULL REFERENCES core.pessoas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    tipo            TEXT NOT NULL,
    valor           TEXT NOT NULL,
    principal       BOOLEAN NOT NULL DEFAULT FALSE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by      UUID,
    deleted_at      TIMESTAMPTZ,
    deleted_by      UUID,
    CONSTRAINT ck_contatos_tipo    CHECK (tipo IN ('TEL', 'EMAIL', 'REDES', 'WHATSAPP')),
    CONSTRAINT ck_contatos_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
```

### `fornecedores`

```sql
CREATE TABLE IF NOT EXISTS core.fornecedores (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pessoa_juridica_id  UUID NOT NULL UNIQUE REFERENCES core.pessoas_juridicas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    situacao_cadastro   TEXT NOT NULL,
    macro_categoria     TEXT,
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by          UUID,
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by          UUID,
    deleted_at          TIMESTAMPTZ,
    deleted_by          UUID,
    CONSTRAINT ck_fornecedores_situacao CHECK (situacao_cadastro IN ('ATIVO', 'INATIVO', 'SUSPENSO')),
    CONSTRAINT ck_fornecedores_deleted  CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
COMMENT ON TABLE core.fornecedores IS 'Perfil de fornecedor – pessoa jurídica com categoria FORNECEDOR.';
```

### `unidades_administrativas`

```sql
CREATE TABLE IF NOT EXISTS core.unidades_administrativas (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    unidade_pai_id  UUID REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    codigo_ibge     TEXT UNIQUE,
    codigo_siafi    TEXT UNIQUE,
    nome            TEXT NOT NULL,
    sigla           TEXT UNIQUE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by      UUID,
    deleted_at      TIMESTAMPTZ,
    deleted_by      UUID,
    CONSTRAINT ck_unidades_administrativas_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
COMMENT ON COLUMN core.unidades_administrativas.unidade_pai_id IS 'Auto-referência: unidade superior na hierarquia.';
```

## 4.2. Grupo `core.usuarios`

### `usuarios`

```sql
CREATE TABLE IF NOT EXISTS core.usuarios (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pessoa_id       UUID NOT NULL UNIQUE REFERENCES core.pessoas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    login           TEXT NOT NULL UNIQUE,
    senha_hash      TEXT NOT NULL,
    mfa_secret      TEXT,
    ultimo_login    TIMESTAMPTZ,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by      UUID,
    deleted_at      TIMESTAMPTZ,
    deleted_by      UUID,
    CONSTRAINT ck_usuarios_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
COMMENT ON COLUMN core.usuarios.login      IS 'Login único do usuário.';
COMMENT ON COLUMN core.usuarios.senha_hash IS 'LGPD: bcrypt/argon2 + MFA.';
COMMENT ON COLUMN core.usuarios.mfa_secret IS 'LGPD: criptografado (AES-256).';
```

### `grupos_usuarios`

```sql
CREATE TABLE IF NOT EXISTS core.grupos_usuarios (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    nome            TEXT NOT NULL UNIQUE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by      UUID,
    deleted_at      TIMESTAMPTZ,
    deleted_by      UUID,
    CONSTRAINT ck_grupos_usuarios_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
```

### `permissoes`

```sql
CREATE TABLE IF NOT EXISTS core.permissoes (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    chave_acesso    TEXT NOT NULL UNIQUE,
    nome            TEXT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by      UUID,
    deleted_at      TIMESTAMPTZ,
    deleted_by      UUID,
    CONSTRAINT ck_permissoes_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
```

### `usuarios_grupos` (junção N:M)

```sql
CREATE TABLE IF NOT EXISTS core.usuarios_grupos (
    usuario_id        UUID NOT NULL REFERENCES core.usuarios(id) ON UPDATE CASCADE ON DELETE CASCADE,
    grupo_usuario_id  UUID NOT NULL REFERENCES core.grupos_usuarios(id) ON UPDATE CASCADE ON DELETE CASCADE,
    created_at        TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by        UUID,
    PRIMARY KEY (usuario_id, grupo_usuario_id)
);
COMMENT ON TABLE core.usuarios_grupos IS 'Junção N:M entre USUARIO e GRUPO_USUARIO.';
```

### `grupos_permissoes` (junção N:M)

```sql
CREATE TABLE IF NOT EXISTS core.grupos_permissoes (
    grupo_usuario_id  UUID NOT NULL REFERENCES core.grupos_usuarios(id) ON UPDATE CASCADE ON DELETE CASCADE,
    permissao_id      UUID NOT NULL REFERENCES core.permissoes(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    created_at        TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by        UUID,
    PRIMARY KEY (grupo_usuario_id, permissao_id)
);
COMMENT ON TABLE core.grupos_permissoes IS 'Junção N:M entre GRUPO_USUARIO e PERMISSAO.';
```

## 4.3. Grupo `core.documentos`

### `processos_documentais`

```sql
CREATE TABLE IF NOT EXISTS core.processos_documentais (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    unidade_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    numero          TEXT NOT NULL,
    ano             INTEGER NOT NULL,
    assunto         TEXT NOT NULL,
    descricao       TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by      UUID,
    deleted_at      TIMESTAMPTZ,
    deleted_by      UUID,
    CONSTRAINT uq_processos_documentais_numero_ano UNIQUE (numero, ano),
    CONSTRAINT ck_processos_documentais_deleted   CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
```

### `arquivos`

```sql
CREATE TABLE IF NOT EXISTS core.arquivos (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    processo_documental_id  UUID NOT NULL REFERENCES core.processos_documentais(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    nome                    TEXT NOT NULL,
    caminho                 TEXT NOT NULL,
    hash                    TEXT NOT NULL,
    tamanho                 BIGINT NOT NULL,
    tipo_mime               TEXT,
    created_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by              UUID,
    updated_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by              UUID,
    deleted_at              TIMESTAMPTZ,
    deleted_by              UUID,
    CONSTRAINT ck_arquivos_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
COMMENT ON COLUMN core.arquivos.hash IS 'Hash de integridade do arquivo (SHA-256).';
```

### `assinaturas`

```sql
CREATE TABLE IF NOT EXISTS core.assinaturas (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    processo_documental_id  UUID NOT NULL REFERENCES core.processos_documentais(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    pessoa_id               UUID NOT NULL REFERENCES core.pessoas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    documento_id            UUID REFERENCES core.documentos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    hash                    TEXT NOT NULL,
    data                    TIMESTAMPTZ NOT NULL,
    created_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by              UUID,
    updated_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by              UUID,
    deleted_at              TIMESTAMPTZ,
    deleted_by              UUID,
    CONSTRAINT ck_assinaturas_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
COMMENT ON TABLE core.assinaturas IS 'Assinatura digital de PROCESSO_DOCUMENTAL por PESSOA.';
```

## 4.4. Grupo `core.auditoria`

### `auditorias`

```sql
CREATE TABLE IF NOT EXISTS core.auditorias (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tabela          TEXT NOT NULL,
    registro_id     UUID NOT NULL,
    operacao        TEXT NOT NULL,
    valores_antigos JSONB,
    valores_novos   JSONB,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    CONSTRAINT ck_auditorias_operacao CHECK (operacao IN ('INSERT', 'UPDATE', 'DELETE'))
);
COMMENT ON TABLE core.auditorias IS 'Log de alterações em tabelas críticas (auditoria de dados).';
```

### `logs_sistema`

```sql
CREATE TABLE IF NOT EXISTS core.logs_sistema (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    usuario_id      UUID NOT NULL REFERENCES core.usuarios(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    auditoria_id    UUID REFERENCES core.auditorias(id) ON UPDATE CASCADE ON DELETE SET NULL,
    nivel           TEXT NOT NULL,
    mensagem        TEXT NOT NULL,
    ip_origem       TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT ck_logs_sistema_nivel CHECK (nivel IN ('DEBUG', 'INFO', 'WARN', 'ERROR'))
);
```

## 4.5. Domínio `rh`

### `servidores`

```sql
CREATE TABLE IF NOT EXISTS rh.servidores (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pessoa_fisica_id UUID NOT NULL UNIQUE REFERENCES core.pessoas_fisicas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    matricula       TEXT NOT NULL UNIQUE,
    data_admissao   DATE NOT NULL,
    data_desligamento DATE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by      UUID,
    deleted_at      TIMESTAMPTZ,
    deleted_by      UUID,
    CONSTRAINT ck_servidores_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
```

### `fichas_funcionais`

```sql
CREATE TABLE IF NOT EXISTS rh.fichas_funcionais (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    servidor_id     UUID NOT NULL REFERENCES rh.servidores(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    vinculo_tipo    TEXT,
    data_inicio     DATE NOT NULL,
    data_fim        DATE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by      UUID,
    deleted_at      TIMESTAMPTZ,
    deleted_by      UUID,
    CONSTRAINT ck_fichas_funcionais_vinculo  CHECK (vinculo_tipo IN ('PRINCIPAL', 'SUBCONTRATADO', 'TERCEIRIZADO')),
    CONSTRAINT ck_fichas_funcionais_deleted  CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
```

### `vinculos`, `cargos`, `funcoes`, `dependencias`

```sql
CREATE TABLE IF NOT EXISTS rh.vinculos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    servidor_id     UUID NOT NULL REFERENCES rh.servidores(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data_inicio     DATE NOT NULL,
    data_fim        DATE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_vinculos_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS rh.cargos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    codigo          TEXT NOT NULL UNIQUE,
    nome            TEXT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_cargos_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS rh.funcoes (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    codigo          TEXT NOT NULL UNIQUE,
    nome            TEXT NOT NULL,
    descricao       TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_funcoes_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS rh.dependencias (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pessoa_fisica_id UUID NOT NULL REFERENCES core.pessoas_fisicas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    parentesco      TEXT NOT NULL,
    data_nascimento DATE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_dependencias_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
```

## 4.6. Domínio `tributos`

### `lancamentos_tributarios`

```sql
CREATE TABLE IF NOT EXISTS tributos.lancamentos_tributarios (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pessoa_id       UUID NOT NULL REFERENCES core.pessoas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    conta_contabil_id UUID NOT NULL,
    debito          TEXT NOT NULL,
    credito         TEXT NOT NULL,
    historico       TEXT NOT NULL,
    valor           NUMERIC(15,2) NOT NULL,
    data            DATE NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by      UUID,
    deleted_at      TIMESTAMPTZ,
    deleted_by      UUID,
    CONSTRAINT ck_lancamentos_tributarios_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
```

### `quotas`, `debitos`, `creditos`

```sql
CREATE TABLE IF NOT EXISTS tributos.quotas (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pessoa_id       UUID NOT NULL REFERENCES core.pessoas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    exercicio       INTEGER NOT NULL,
    mes             INTEGER NOT NULL,
    valor           NUMERIC(15,2) NOT NULL,
    situacao        TEXT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_quotas_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS tributos.debitos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    lancamento_id   UUID NOT NULL REFERENCES tributos.lancamentos_tributarios(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    valor           NUMERIC(15,2) NOT NULL,
    data_vencimento DATE NOT NULL,
    situacao        TEXT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by      UUID,
    deleted_at      TIMESTAMPTZ,
    deleted_by      UUID
);

CREATE TABLE IF NOT EXISTS tributos.creditos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    lancamento_id   UUID NOT NULL REFERENCES tributos.lancamentos_tributarios(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    valor           NUMERIC(15,2) NOT NULL,
    data_credito    DATE NOT NULL,
    origem          TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by      UUID,
    deleted_at      TIMESTAMPTZ,
    deleted_by      UUID
);
```

## 4.7. Domínio `contabilidade`

### `contas_contabeis`

```sql
CREATE TABLE IF NOT EXISTS contabilidade.contas_contabeis (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    codigo          TEXT NOT NULL UNIQUE,
    descricao       TEXT NOT NULL,
    tipo            TEXT NOT NULL,
    natureza        TEXT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_contas_contabeis_tipo      CHECK (tipo IN ('DEBITO', 'CREDITO')),
    CONSTRAINT ck_contas_contabeis_natureza  CHECK (natureza IN ('SINTETICA', 'ANALITICA')),
    CONSTRAINT ck_contas_contabeis_deleted   CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
```

### `empenhos`

```sql
CREATE TABLE IF NOT EXISTS contabilidade.empenhos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    processo_documental_id UUID REFERENCES core.processos_documentais(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    fornecedor_id   UUID NOT NULL REFERENCES core.fornecedores(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    compra_id       UUID,
    numero          TEXT NOT NULL,
    data            DATE NOT NULL,
    valor           NUMERIC(15,2) NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by      UUID,
    deleted_at      TIMESTAMPTZ,
    deleted_by      UUID,
    CONSTRAINT ck_empenhos_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
```

### `despesas`, `receitas`, `rateios`

```sql
CREATE TABLE IF NOT EXISTS contabilidade.despesas (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    unidade_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    conta_contabil_id UUID NOT NULL REFERENCES contabilidade.contas_contabeis(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    empenho_id      UUID REFERENCES contabilidade.empenhos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    valor           NUMERIC(15,2) NOT NULL,
    data            DATE NOT NULL,
    historico       TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_despesas_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS contabilidade.receitas (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    unidade_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    conta_contabil_id UUID NOT NULL REFERENCES contabilidade.contas_contabeis(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    fonte           TEXT,
    valor           NUMERIC(15,2) NOT NULL,
    data            DATE NOT NULL,
    historico       TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_receitas_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS contabilidade.rateios (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    empenho_id      UUID NOT NULL REFERENCES contabilidade.empenhos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    conta_contabil_id UUID NOT NULL REFERENCES contabilidade.contas_contabeis(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    percentual      NUMERIC(5,2) NOT NULL,
    valor           NUMERIC(15,2),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);
```

## 4.8. Domínio `compras`

### `compras`

```sql
CREATE TABLE IF NOT EXISTS compras.compras (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    processo_documental_id UUID NOT NULL REFERENCES core.processos_documentais(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    fornecedor_id       UUID NOT NULL REFERENCES core.fornecedores(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_id          UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    numero              TEXT NOT NULL,
    data                DATE NOT NULL,
    valor_total         NUMERIC(15,2),
    situacao            TEXT NOT NULL,
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by          UUID,
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by          UUID,
    deleted_at          TIMESTAMPTZ,
    deleted_by          UUID,
    CONSTRAINT ck_compras_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
```

### `itens_compras`

```sql
CREATE TABLE IF NOT EXISTS compras.itens_compras (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    compra_id       UUID NOT NULL REFERENCES compras.compras(id) ON UPDATE CASCADE ON DELETE CASCADE,
    descricao       TEXT NOT NULL,
    quantidade      NUMERIC(15,2) NOT NULL,
    valor_unitario  NUMERIC(15,2) NOT NULL,
    valor_total     NUMERIC(15,2) NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by      UUID,
    deleted_at      TIMESTAMPTZ,
    deleted_by      UUID,
    CONSTRAINT ck_itens_compras_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
```

### `contratos`

```sql
CREATE TABLE IF NOT EXISTS compras.contratos (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    processo_documental_id  UUID NOT NULL REFERENCES core.processos_documentais(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    fornecedor_id           UUID NOT NULL REFERENCES core.fornecedores(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_id              UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    licitacao_master_id     UUID,
    numero                  TEXT NOT NULL,
    data_inicio             DATE NOT NULL,
    data_fim                DATE,
    valor                   NUMERIC(15,2),
    objeto                  TEXT,
    created_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by              UUID,
    updated_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by              UUID,
    deleted_at              TIMESTAMPTZ,
    deleted_by              UUID,
    CONSTRAINT ck_contratos_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
```

## 4.9. Domínio `licitacoes`

### `licitacoes_masters`

```sql
CREATE TABLE IF NOT EXISTS licitacoes.licitacoes_masters (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    processo_documental_id  UUID NOT NULL REFERENCES core.processos_documentais(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_id              UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    objeto_id               UUID,
    numero                  TEXT NOT NULL,
    data                    DATE NOT NULL,
    status                  TEXT,
    created_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by              UUID,
    updated_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by              UUID,
    deleted_at              TIMESTAMPTZ,
    deleted_by              UUID,
    CONSTRAINT ck_licitacoes_masters_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
```

### `objetos`, `lances`, `habilitacoes`, `aditamentos`

```sql
CREATE TABLE IF NOT EXISTS licitacoes.objetos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    descricao       TEXT NOT NULL,
    categoria       TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_objetos_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS licitacoes.lances (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    licitacao_master_id UUID NOT NULL REFERENCES licitacoes.licitacoes_masters(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    fornecedor_id       UUID NOT NULL REFERENCES core.fornecedores(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    valor               NUMERIC(15,2) NOT NULL,
    data_hora           TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by          UUID,
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by          UUID,
    deleted_at          TIMESTAMPTZ,
    deleted_by          UUID
);

CREATE TABLE IF NOT EXISTS licitacoes.habilitacoes (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    licitacao_master_id UUID NOT NULL REFERENCES licitacoes.licitacoes_masters(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    fornecedor_id       UUID NOT NULL REFERENCES core.fornecedores(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    criterio            TEXT NOT NULL,
    pontuacao           NUMERIC(10,2),
    aprovado            BOOLEAN NOT NULL DEFAULT FALSE,
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by          UUID,
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by          UUID,
    deleted_at          TIMESTAMPTZ,
    deleted_by          UUID
);

CREATE TABLE IF NOT EXISTS licitacoes.aditamentos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    contrato_id     UUID NOT NULL REFERENCES compras.contratos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    numero          TEXT NOT NULL,
    data            DATE NOT NULL,
    valor           NUMERIC(15,2),
    objeto          TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_aditamentos_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
```

## 4.10. Domínios compartilhados — `agendamentos`

> Tabela replicada por esquema (saúde, educação, assistência_social) com a mesma estrutura:

```sql
CREATE TABLE IF NOT EXISTS saude.agendamentos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pessoa_fisica_id UUID NOT NULL REFERENCES core.pessoas_fisicas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data_hora       TIMESTAMPTZ NOT NULL,
    status          TEXT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by      UUID,
    deleted_at      TIMESTAMPTZ,
    deleted_by      UUID,
    CONSTRAINT ck_agendamentos_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
-- Réplica para educacao e assistencia_social:
CREATE TABLE IF NOT EXISTS educacao.agendamentos (LIKE saude.agendamentos INCLUDING ALL);
CREATE TABLE IF NOT EXISTS assistencia_social.agendamentos (LIKE saude.agendamentos INCLUDING ALL);
```

## 4.11. Domínio `almoxarifado`

### `categorias_itens`, `itens_estoque`, `movimentos_estoque`

```sql
CREATE TABLE IF NOT EXISTS almoxarifado.categorias_itens (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    codigo          TEXT NOT NULL UNIQUE,
    nome            TEXT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_categorias_itens_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS almoxarifado.itens_estoque (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    categoria_id        UUID REFERENCES almoxarifado.categorias_itens(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    codigo              TEXT NOT NULL UNIQUE,
    descricao           TEXT NOT NULL,
    unidade_medida      TEXT NOT NULL,
    quantidade_estoque  NUMERIC(15,2) NOT NULL DEFAULT 0,
    valor_unitario      NUMERIC(15,2),
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at          TIMESTAMPTZ,
    CONSTRAINT ck_itens_estoque_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS almoxarifado.movimentos_estoque (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    item_estoque_id     UUID NOT NULL REFERENCES almoxarifado.itens_estoque(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_origem_id   UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_destino_id  UUID REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    tipo                TEXT NOT NULL,
    quantidade          NUMERIC(15,2) NOT NULL,
    data                DATE NOT NULL,
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by          UUID,
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_by          UUID,
    deleted_at          TIMESTAMPTZ,
    deleted_by          UUID,
    CONSTRAINT ck_movimentos_estoque_tipo    CHECK (tipo IN ('ENTRADA', 'SAIDA', 'AJUSTE')),
    CONSTRAINT ck_movimentos_estoque_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
```

## 4.12. Domínio `patrimonio`

### `bens`, `depreciacoes`, `baixas_bens`, `transferencias_bens`

```sql
CREATE TABLE IF NOT EXISTS patrimonio.bens (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    unidade_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    tombo           TEXT NOT NULL UNIQUE,
    categoria       TEXT NOT NULL,
    marca_modelo    TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_bens_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS patrimonio.depreciacoes (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    bem_id          UUID NOT NULL REFERENCES patrimonio.bens(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data            DATE NOT NULL,
    valor           NUMERIC(15,2) NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_depreciacoes_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS patrimonio.baixas_bens (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    bem_id          UUID NOT NULL REFERENCES patrimonio.bens(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data            DATE NOT NULL,
    motivo          TEXT,
    valor_residual  NUMERIC(15,2),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_baixas_bens_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS patrimonio.transferencias_bens (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    bem_id              UUID NOT NULL REFERENCES patrimonio.bens(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_origem_id   UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_destino_id  UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data                DATE NOT NULL,
    motivo              TEXT,
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at          TIMESTAMPTZ,
    CONSTRAINT ck_transferencias_bens_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);
```

## 4.13. Domínio `frotas`

### `veiculos`, `abastecimentos`, `manutencoes`, `deslocamentos`

```sql
CREATE TABLE IF NOT EXISTS frotas.veiculos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    unidade_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    placa           TEXT NOT NULL UNIQUE,
    chassi          TEXT NOT NULL UNIQUE,
    marca_modelo    TEXT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_veiculos_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS frotas.abastecimentos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    veiculo_id      UUID NOT NULL REFERENCES frotas.veiculos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data            DATE NOT NULL,
    litros          NUMERIC(15,2) NOT NULL,
    valor           NUMERIC(15,2) NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS frotas.manutencoes (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    veiculo_id      UUID NOT NULL REFERENCES frotas.veiculos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data            DATE NOT NULL,
    tipo            TEXT NOT NULL,
    descricao       TEXT,
    custo           NUMERIC(15,2),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS frotas.deslocamentos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    veiculo_id      UUID NOT NULL REFERENCES frotas.veiculos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data_hora       TIMESTAMPTZ NOT NULL,
    origem          TEXT,
    destino         TEXT,
    quilometragem   NUMERIC(15,2),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);
```

## 4.14. Domínio `ouvidoria`

### `protocolos`, `atendimentos`, `reclamacoes`, `respostas`

```sql
CREATE TABLE IF NOT EXISTS ouvidoria.protocolos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pessoa_id       UUID NOT NULL REFERENCES core.pessoas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    categoria       TEXT NOT NULL,
    status          TEXT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_protocolos_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS ouvidoria.atendimentos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    protocolo_id    UUID NOT NULL REFERENCES ouvidoria.protocolos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data_hora       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    tipo            TEXT NOT NULL,
    descricao       TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS ouvidoria.reclamacoes (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    atendimento_id  UUID NOT NULL REFERENCES ouvidoria.atendimentos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    descricao       TEXT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS ouvidoria.respostas (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    reclamacao_id   UUID NOT NULL REFERENCES ouvidoria.reclamacoes(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    descricao       TEXT NOT NULL,
    data_resposta    TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);
```

## 4.15. Domínio `obras`

### `obras`, `plantas`, `servicos_obra`, `inspecoes_obra`

```sql
CREATE TABLE IF NOT EXISTS obras.obras (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    unidade_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    codigo          TEXT NOT NULL UNIQUE,
    nome            TEXT NOT NULL,
    descricao       TEXT,
    data_inicio     DATE,
    data_fim        DATE,
    valor           NUMERIC(15,2),
    status          TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_obras_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS obras.plantas (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    obra_id         UUID NOT NULL REFERENCES obras.obras(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    arquivo_id      UUID REFERENCES core.arquivos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    descricao       TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS obras.servicos_obra (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    obra_id         UUID NOT NULL REFERENCES obras.obras(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    descricao       TEXT NOT NULL,
    data_inicio     DATE,
    data_fim        DATE,
    valor           NUMERIC(15,2),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS obras.inspecoes_obra (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    obra_id         UUID NOT NULL REFERENCES obras.obras(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data            DATE NOT NULL,
    tipo            TEXT,
    descricao       TEXT,
    resultado       TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);
```

## 4.16. Domínio `transparencia`

### `publicacoes`, `leis`, `colunas_fiscais`, `comprovantes_despesas`

```sql
CREATE TABLE IF NOT EXISTS transparencia.publicacoes (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    titulo          TEXT NOT NULL,
    descricao       TEXT,
    data_publicacao TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    categoria       TEXT,
    url_arquivo     TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_publicacoes_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS transparencia.leis (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    numero          TEXT NOT NULL,
    ano             INTEGER NOT NULL,
    descricao       TEXT,
    data_leitura    DATE,
    data_sancao     DATE,
    url_documento   TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT uq_leis_numero_ano UNIQUE (numero, ano),
    CONSTRAINT ck_leis_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS transparencia.colunas_fiscais (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    exercicio       INTEGER NOT NULL,
    mes             INTEGER NOT NULL,
    categoria       TEXT NOT NULL,
    valor           NUMERIC(15,2) NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS transparencia.comprovantes_despesas (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    unidade_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    empenho_id      UUID NOT NULL REFERENCES contabilidade.empenhos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data            DATE NOT NULL,
    valor           NUMERIC(15,2) NOT NULL,
    arquivo_id      UUID REFERENCES core.arquivos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);
```

## 4.17. Domínio `controladoria`

### `indicadores`, `metas`, `avaliacoes`, `perfis_risco`

```sql
CREATE TABLE IF NOT EXISTS controladoria.indicadores (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    codigo          TEXT NOT NULL UNIQUE,
    nome            TEXT NOT NULL,
    descricao       TEXT,
    formula         TEXT,
    unidade         TEXT,
    tipo            TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_indicadores_tipo    CHECK (tipo IN ('QUALITATIVO', 'QUANTITATIVO')),
    CONSTRAINT ck_indicadores_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS controladoria.metas (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    indicador_id    UUID NOT NULL REFERENCES controladoria.indicadores(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    exercicio       INTEGER NOT NULL,
    valor_alvo      NUMERIC(15,2) NOT NULL,
    valor_realizado NUMERIC(15,2),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS controladoria.avaliacoes (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    indicador_id    UUID NOT NULL REFERENCES controladoria.indicadores(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data            DATE NOT NULL,
    valor           NUMERIC(15,2),
    observacao      TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS controladoria.perfis_risco (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    processo_documental_id  UUID REFERENCES core.processos_documentais(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    risco                   TEXT,
    probabilidade           TEXT,
    impacto                 TEXT,
    created_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at              TIMESTAMPTZ,
    CONSTRAINT ck_perfis_risco_risco CHECK (risco IN ('BAIXO', 'MEDIO', 'ALTO', 'CRITICO'))
);
```

## 4.18. Domínio `planejamento`

### `planos`, `objetivos_estrategicos`, `atividades_planos`, `cronogramas`

```sql
CREATE TABLE IF NOT EXISTS planejamento.planos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    unidade_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    codigo          TEXT NOT NULL UNIQUE,
    nome            TEXT NOT NULL,
    descricao       TEXT,
    data_inicio     DATE,
    data_fim        DATE,
    status          TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_planos_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS planejamento.objetivos_estrategicos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    plano_id        UUID NOT NULL REFERENCES planejamento.planos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    codigo          TEXT NOT NULL,
    descricao       TEXT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS planejamento.atividades_planos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    objetivo_id     UUID NOT NULL REFERENCES planejamento.objetivos_estrategicos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    descricao       TEXT NOT NULL,
    data_inicio     DATE,
    data_fim        DATE,
    status          TEXT,
    valor           NUMERIC(15,2),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS planejamento.cronogramas (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    atividade_id    UUID NOT NULL REFERENCES planejamento.atividades_planos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data_inicio     DATE NOT NULL,
    data_fim        DATE NOT NULL,
    percentual      NUMERIC(5,2),
    status          TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);
```

## 4.19. Domínio `procuradoria`

### `processos_judiciais`, `autuacoes`, `notificacoes`, `pecas_processuais`

```sql
CREATE TABLE IF NOT EXISTS procuradoria.processos_judiciais (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    processo_documental_id  UUID NOT NULL REFERENCES core.processos_documentais(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_id              UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    numero                  TEXT NOT NULL,
    vara                    TEXT,
    data_distribuicao       DATE,
    status                  TEXT,
    valor                   NUMERIC(15,2),
    created_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at              TIMESTAMPTZ,
    CONSTRAINT ck_processos_judiciais_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS procuradoria.autuacoes (
    id               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    processo_judicial_id UUID NOT NULL REFERENCES procuradoria.processos_judiciais(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data             DATE NOT NULL,
    tipo             TEXT,
    descricao        TEXT,
    created_at       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at       TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS procuradoria.notificacoes (
    id                   UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    processo_judicial_id UUID NOT NULL REFERENCES procuradoria.processos_judiciais(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data                 DATE NOT NULL,
    tipo                 TEXT,
    descricao            TEXT,
    data_resposta        DATE,
    created_at           TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at           TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at           TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS procuradoria.pecas_processuais (
    id                   UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    processo_judicial_id UUID NOT NULL REFERENCES procuradoria.processos_judiciais(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    arquivo_id           UUID NOT NULL REFERENCES core.arquivos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    tipo                 TEXT,
    descricao            TEXT,
    data                 DATE,
    created_at           TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at           TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at           TIMESTAMPTZ
);
```

## 4.20. Domínio `gabinete`

### `atas`, `distribuicoes`, `posicionamentos`

```sql
CREATE TABLE IF NOT EXISTS gabinete.atas (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    processo_documental_id  UUID NOT NULL REFERENCES core.processos_documentais(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_id              UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    numero                  TEXT NOT NULL,
    data_reuniao            DATE NOT NULL,
    descricao               TEXT,
    resultado               TEXT,
    created_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at              TIMESTAMPTZ,
    CONSTRAINT ck_atas_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS gabinete.distribuicoes (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    processo_documental_id  UUID NOT NULL REFERENCES core.processos_documentais(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_destino_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data_distribuicao       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    status                  TEXT,
    created_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at              TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS gabinete.posicionamentos (
    id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    processo_documental_id  UUID NOT NULL REFERENCES core.processos_documentais(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data                    DATE NOT NULL,
    tipo                    TEXT,
    descricao               TEXT,
    created_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at              TIMESTAMPTZ
);
```

## 4.21. Domínio `administracao`

### `imoveis`, `configuracoes`, `parametros`, `tabelas_auxiliares`

```sql
CREATE TABLE IF NOT EXISTS administracao.imoveis (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    matricula       TEXT NOT NULL UNIQUE,
    setor           TEXT,
    tipo            TEXT,
    unidade_id      UUID REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_imoveis_tipo    CHECK (tipo IN ('TERRITORIAL', 'PREDIAL', 'RURAL')),
    CONSTRAINT ck_imoveis_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS administracao.configuracoes (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    chave           TEXT NOT NULL UNIQUE,
    valor           TEXT,
    tipo            TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_configuracoes_tipo CHECK (tipo IN ('STRING', 'INTEGER', 'BOOLEAN', 'JSON'))
);

CREATE TABLE IF NOT EXISTS administracao.parametros (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    chave           TEXT NOT NULL UNIQUE,
    valor           TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS administracao.tabelas_auxiliares (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    codigo          TEXT NOT NULL,
    descricao       TEXT NOT NULL,
    valor           TEXT,
    tabela          TEXT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);
```

## 4.22. Domínio `educacao`

### `turmas`, `alunos`, `matriculas`, `disciplinas`, `boletins`

```sql
CREATE TABLE IF NOT EXISTS educacao.turmas (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    codigo          TEXT NOT NULL UNIQUE,
    nome            TEXT NOT NULL,
    nivel_ensino    TEXT,
    serie           TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS educacao.alunos (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pessoa_fisica_id UUID NOT NULL UNIQUE REFERENCES core.pessoas_fisicas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    matricula       TEXT NOT NULL UNIQUE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS educacao.matriculas (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    aluno_id        UUID NOT NULL REFERENCES educacao.alunos(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    turma_id        UUID NOT NULL REFERENCES educacao.turmas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data_matricula  DATE NOT NULL,
    situacao        TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS educacao.disciplinas (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    codigo          TEXT NOT NULL UNIQUE,
    nome            TEXT NOT NULL,
    carga_horaria   INTEGER,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS educacao.boletins (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    matricula_id    UUID NOT NULL REFERENCES educacao.matriculas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    disciplina_id   UUID NOT NULL REFERENCES educacao.disciplinas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    nota            NUMERIC(5,2),
    data_lancamento DATE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);
```

## 4.23. Domínio `assistencia_social`

### `fichas_atendimento_as`, `beneficios`, `programas_sociais`

```sql
CREATE TABLE IF NOT EXISTS assistencia_social.fichas_atendimento_as (
    id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pessoa_fisica_id   UUID NOT NULL REFERENCES core.pessoas_fisicas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_id         UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data_atendimento   TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    tipo_atendimento   TEXT,
    status             TEXT,
    created_at         TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at         TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at         TIMESTAMPTZ,
    CONSTRAINT ck_fichas_atendimento_as_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS assistencia_social.beneficios (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pessoa_fisica_id UUID NOT NULL REFERENCES core.pessoas_fisicas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    codigo          TEXT NOT NULL UNIQUE,
    nome            TEXT NOT NULL,
    data_inicio     DATE,
    data_fim        DATE,
    valor           NUMERIC(15,2),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS assistencia_social.programas_sociais (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    codigo          TEXT NOT NULL UNIQUE,
    nome            TEXT NOT NULL,
    descricao       TEXT,
    data_inicio     DATE,
    data_fim        DATE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);
```

## 4.24. Domínio `saude` (tabelas complementares)

### `pacientes`, `fichas_atendimento`, `prescricoes`

```sql
CREATE TABLE IF NOT EXISTS saude.pacientes (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pessoa_fisica_id UUID NOT NULL UNIQUE REFERENCES core.pessoas_fisicas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    numero_cns      TEXT UNIQUE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_pacientes_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS saude.fichas_atendimento (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    paciente_id     UUID NOT NULL REFERENCES saude.pacientes(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    unidade_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data_atendimento TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    tipo            TEXT,
    observacao      TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS saude.prescricoes (
    id                    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    ficha_atendimento_id  UUID NOT NULL REFERENCES saude.fichas_atendimento(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    medicamento           TEXT NOT NULL,
    dosagem               TEXT,
    via                   TEXT,
    frequencia            TEXT,
    duracao               TEXT,
    created_at            TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at            TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at            TIMESTAMPTZ
);
```

## 4.25. Domínios `agricultura` e `financas`

> Seguem o padrão genérico (`id UUID PK + [audit fields]`). Colunas específicas serão detalhadas no `Dicionario-de-dados.md`.

### `agricultura.propriedades_rurais`, `agricultura.culturas`, `agricultura.plantios`

```sql
CREATE TABLE IF NOT EXISTS agricultura.propriedades_rurais (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pessoa_id       UUID NOT NULL REFERENCES core.pessoas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    numero_car      TEXT UNIQUE,
    municipio       TEXT,
    area_ha         NUMERIC(15,2),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,
    CONSTRAINT ck_propriedades_rurais_deleted CHECK (deleted_at IS NULL OR deleted_at <= NOW())
);

CREATE TABLE IF NOT EXISTS agricultura.culturas (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    codigo          TEXT NOT NULL UNIQUE,
    nome            TEXT NOT NULL,
    ciclo_meses     INTEGER,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS agricultura.plantios (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    propriedade_id      UUID NOT NULL REFERENCES agricultura.propriedades_rurais(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    cultura_id          UUID NOT NULL REFERENCES agricultura.culturas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    data_plantio        DATE NOT NULL,
    area_ha             NUMERIC(15,2),
    produtividade_estimada NUMERIC(15,2),
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at          TIMESTAMPTZ
);
```

### `financas.concessoes`, `financas.taxas`

```sql
CREATE TABLE IF NOT EXISTS financas.concessoes (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    unidade_id      UUID NOT NULL REFERENCES core.unidades_administrativas(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    numero          TEXT NOT NULL,
    tipo            TEXT,
    data_inicio     DATE,
    data_fim        DATE,
    valor           NUMERIC(15,2),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS financas.taxas (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    concessao_id    UUID NOT NULL REFERENCES financas.concessoes(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    codigo          TEXT NOT NULL,
    descricao       TEXT,
    aliquota        NUMERIC(10,4),
    data_inicio     DATE NOT NULL,
    data_fim        DATE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ
);
```

---

# 5. Ordem de Aplicação e Constraints Adiadas

O DDL deve ser aplicado nesta ordem: extensões, esquemas, função de auditoria, tabelas `core.unidades_administrativas`, demais tabelas `core`, tabelas de domínio e, por último, as constraints abaixo. As constraints são adicionadas após a criação das tabelas referenciadas para permitir execução em uma migração única.

```sql
ALTER TABLE core.pessoas
    ADD CONSTRAINT pessoas_unidade_id_fkey
    FOREIGN KEY (unidade_id) REFERENCES core.unidades_administrativas(id)
    ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE tributos.lancamentos_tributarios
    ADD CONSTRAINT lancamentos_tributarios_conta_contabil_id_fkey
    FOREIGN KEY (conta_contabil_id) REFERENCES contabilidade.contas_contabeis(id)
    ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE contabilidade.empenhos
    ADD CONSTRAINT empenhos_compra_id_fkey
    FOREIGN KEY (compra_id) REFERENCES compras.compras(id)
    ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE compras.contratos
    ADD CONSTRAINT contratos_licitacao_master_id_fkey
    FOREIGN KEY (licitacao_master_id) REFERENCES licitacoes.licitacoes_masters(id)
    ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE licitacoes.licitacoes_masters
    ADD CONSTRAINT licitacoes_masters_objeto_id_fkey
    FOREIGN KEY (objeto_id) REFERENCES licitacoes.objetos(id)
    ON UPDATE CASCADE ON DELETE RESTRICT;
```

> **Nota de migração:** em ambientes já parcialmente criados, as constraints devem ser aplicadas com nomes estáveis e dentro de uma transação. A migração deve falhar se houver dados órfãos, em vez de usar `NOT VALID` silenciosamente.

## 5.1. Índices e Constraints

### 5.1.1. Índices de Desempenho

> O PostgreSQL cria índices automaticamente para `PRIMARY KEY` e `UNIQUE`. Índices adicionais:

```sql
-- core.pessoas
CREATE INDEX IF NOT EXISTS idx_pessoas_tipo       ON core.pessoas(tipo);
CREATE INDEX IF NOT EXISTS idx_pessoas_categoria   ON core.pessoas(categoria);
CREATE INDEX IF NOT EXISTS idx_pessoas_unidade_id  ON core.pessoas(unidade_id);

-- core.pessoas_fisicas / pessoas_juridicas
CREATE INDEX IF NOT EXISTS idx_pessoas_fisicas_pessoa_id   ON core.pessoas_fisicas(pessoa_id);
CREATE INDEX IF NOT EXISTS idx_pessoas_juridicas_pessoa_id ON core.pessoas_juridicas(pessoa_id);

-- core.enderecos
CREATE INDEX IF NOT EXISTS idx_enderecos_pessoa_id  ON core.enderecos(pessoa_id);
CREATE INDEX IF NOT EXISTS idx_enderecos_vigencia   ON core.enderecos(pessoa_id, vigencia_inicio DESC, vigencia_fim);

-- core.documentos
CREATE INDEX IF NOT EXISTS idx_documentos_pessoa_id ON core.documentos(pessoa_id);
CREATE INDEX IF NOT EXISTS idx_documentos_tipo      ON core.documentos(tipo);

-- core.contatos
CREATE INDEX IF NOT EXISTS idx_contatos_pessoa_id ON core.contatos(pessoa_id);
CREATE INDEX IF NOT EXISTS idx_contatos_tipo      ON core.contatos(tipo);

-- core.fornecedores
CREATE INDEX IF NOT EXISTS idx_fornecedores_pessoa_juridica_id ON core.fornecedores(pessoa_juridica_id);
CREATE INDEX IF NOT EXISTS idx_fornecedores_situacao          ON core.fornecedores(situacao_cadastro);

-- core.unidades_administrativas
CREATE INDEX IF NOT EXISTS idx_unidades_pai_id ON core.unidades_administrativas(unidade_pai_id);

-- core.usuarios
CREATE INDEX IF NOT EXISTS idx_usuarios_pessoa_id ON core.usuarios(pessoa_id);

-- core.processos_documentais / arquivos / assinaturas
CREATE INDEX IF NOT EXISTS idx_processos_documentais_unidade_id ON core.processos_documentais(unidade_id);
CREATE INDEX IF NOT EXISTS idx_processos_documentais_numero_ano ON core.processos_documentais(ano, numero);
CREATE INDEX IF NOT EXISTS idx_arquivos_processo_id             ON core.arquivos(processo_documental_id);
CREATE INDEX IF NOT EXISTS idx_assinaturas_processo_id          ON core.assinaturas(processo_documental_id);
CREATE INDEX IF NOT EXISTS idx_assinaturas_pessoa_id            ON core.assinaturas(pessoa_id);

-- core.auditorias / logs_sistema
CREATE INDEX IF NOT EXISTS idx_auditorias_tabela_registro ON core.auditorias(tabela, registro_id);
CREATE INDEX IF NOT EXISTS idx_logs_sistema_usuario_id    ON core.logs_sistema(usuario_id);
CREATE INDEX IF NOT EXISTS idx_logs_sistema_created_at    ON core.logs_sistema(created_at);
CREATE INDEX IF NOT EXISTS idx_logs_sistema_auditoria_id  ON core.logs_sistema(auditoria_id);

-- rh
CREATE INDEX IF NOT EXISTS idx_servidores_pessoa_fisica_id ON rh.servidores(pessoa_fisica_id);
CREATE INDEX IF NOT EXISTS idx_servidores_unidade_id       ON rh.servidores(unidade_id);
CREATE INDEX IF NOT EXISTS idx_fichas_funcionais_servidor_id ON rh.fichas_funcionais(servidor_id);
CREATE INDEX IF NOT EXISTS idx_fichas_funcionais_unidade_id  ON rh.fichas_funcionais(unidade_id);

-- tributos
CREATE INDEX IF NOT EXISTS idx_lancamentos_tributarios_pessoa_id ON tributos.lancamentos_tributarios(pessoa_id);
CREATE INDEX IF NOT EXISTS idx_lancamentos_tributarios_data      ON tributos.lancamentos_tributarios(data);

-- contabilidade / compras
CREATE INDEX IF NOT EXISTS idx_empenhos_fornecedor_id      ON contabilidade.empenhos(fornecedor_id);
CREATE INDEX IF NOT EXISTS idx_empenhos_unidade_id          ON contabilidade.empenhos(unidade_id);
CREATE INDEX IF NOT EXISTS idx_compras_fornecedor_id        ON compras.compras(fornecedor_id);
CREATE INDEX IF NOT EXISTS idx_compras_unidade_id           ON compras.compras(unidade_id);
CREATE INDEX IF NOT EXISTS idx_compras_processo_documental_id ON compras.compras(processo_documental_id);
CREATE INDEX IF NOT EXISTS idx_itens_compras_compra_id      ON compras.itens_compras(compra_id);
CREATE INDEX IF NOT EXISTS idx_contratos_fornecedor_id      ON compras.contratos(fornecedor_id);
CREATE INDEX IF NOT EXISTS idx_contratos_licitacao_id       ON compras.contratos(licitacao_master_id);

-- licitacoes
CREATE INDEX IF NOT EXISTS idx_licitacoes_masters_unidade_id  ON licitacoes.licitacoes_masters(unidade_id);
CREATE INDEX IF NOT EXISTS idx_licitacoes_masters_processo_id ON licitacoes.licitacoes_masters(processo_documental_id);

-- saude / educacao / assistencia_social (agendamentos)
CREATE INDEX IF NOT EXISTS idx_agendamentos_pessoa_fisica_id ON saude.agendamentos(pessoa_fisica_id);
CREATE INDEX IF NOT EXISTS idx_agendamentos_unidade_id       ON saude.agendamentos(unidade_id);
CREATE INDEX IF NOT EXISTS idx_agendamentos_data_hora        ON saude.agendamentos(data_hora);

-- almoxarifado
CREATE INDEX IF NOT EXISTS idx_itens_estoque_categoria_id    ON almoxarifado.itens_estoque(categoria_id);
CREATE INDEX IF NOT EXISTS idx_movimentos_estoque_item_id    ON almoxarifado.movimentos_estoque(item_estoque_id);
CREATE INDEX IF NOT EXISTS idx_movimentos_estoque_origem_id  ON almoxarifado.movimentos_estoque(unidade_origem_id);
CREATE INDEX IF NOT EXISTS idx_movimentos_estoque_destino_id ON almoxarifado.movimentos_estoque(unidade_destino_id);

-- patrimonio / frotas / ouvidoria / transparencia
CREATE INDEX IF NOT EXISTS idx_bens_unidade_id         ON patrimonio.bens(unidade_id);
CREATE INDEX IF NOT EXISTS idx_veiculos_unidade_id     ON frotas.veiculos(unidade_id);
CREATE INDEX IF NOT EXISTS idx_protocolos_pessoa_id    ON ouvidoria.protocolos(pessoa_id);
CREATE INDEX IF NOT EXISTS idx_protocolos_unidade_id   ON ouvidoria.protocolos(unidade_id);
CREATE INDEX IF NOT EXISTS idx_leis_numero_ano          ON transparencia.leis(ano, numero);
CREATE INDEX IF NOT EXISTS idx_colunas_fiscais_exercicio_mes ON transparencia.colunas_fiscais(exercicio, mes);
```

### 5.1.2. Constraints de Integridade Referencial

> Todas as FKs usam `ON UPDATE CASCADE ON DELETE RESTRICT`, exceto tabelas de junção N:M que usam `ON DELETE CASCADE`. Resumo dos nomes:

| Schema | Constraint | Referencia |
| ------ | ---------- | ---------- |
| core | `pessoas_unidade_id_fkey` | `unidades_administrativas` |
| core | `pessoas_fisicas_pessoa_id_fkey` | `pessoas` |
| core | `pessoas_juridicas_pessoa_id_fkey` | `pessoas` |
| core | `enderecos_pessoa_id_fkey` | `pessoas` |
| core | `documentos_pessoa_id_fkey` | `pessoas` |
| core | `contatos_pessoa_id_fkey` | `pessoas` |
| core | `fornecedores_pessoa_juridica_id_fkey` | `pessoas_juridicas` |
| core | `unidades_pai_id_fkey` | `unidades_administrativas` (self) |
| core | `usuarios_pessoa_id_fkey` | `pessoas` |
| core | `usuarios_grupos_*_fkey` | `usuarios`, `grupos_usuarios` |
| core | `grupos_permissoes_*_fkey` | `grupos_usuarios`, `permissoes` |
| core | `processos_documentais_unidade_id_fkey` | `unidades_administrativas` |
| core | `arquivos_processo_documental_id_fkey` | `processos_documentais` |
| core | `assinaturas_*_fkey` | `processos_documentais`, `pessoas`, `documentos` |
| core | `logs_sistema_*_fkey` | `usuarios`, `auditorias` |
| rh | `servidores_*_fkey` | `pessoas_fisicas`, `unidades_administrativas` |
| rh | `fichas_funcionais_*_fkey` | `servidores`, `unidades_administrativas` |
| tributos | `lancamentos_tributarios_*_fkey` | `pessoas`, `contas_contabeis` |
| contabilidade | `empenhos_*_fkey` | `processos_documentais`, `fornecedores`, `unidades_administrativas`, `compras` |
| compras | `compras_*_fkey` | `processos_documentais`, `fornecedores`, `unidades_administrativas` |
| compras | `itens_compras_compra_id_fkey` | `compras` |
| compras | `contratos_*_fkey` | `processos_documentais`, `fornecedores`, `unidades_administrativas`, `licitacoes_masters` |
| licitacoes | `licitacoes_masters_*_fkey` | `processos_documentais`, `unidades_administrativas`, `objetos` |
| saude | `agendamentos_*_fkey` | `pessoas_fisicas`, `unidades_administrativas` |
| almoxarifado | `movimentos_estoque_*_fkey` | `itens_estoque`, `unidades_administrativas` |
| ouvidoria | `protocolos_*_fkey` | `pessoas`, `unidades_administrativas` |
| patrimonio | `bens_unidade_id_fkey` | `unidades_administrativas` |
| frotas | `veiculos_unidade_id_fkey` | `unidades_administrativas` |
| procuradoria | `processos_judiciais_processo_documental_id_fkey` | `processos_documentais` |
| administracao | `imoveis_unidade_id_fkey` | `unidades_administrativas` |

### 5.1.3. Constraints CHECK

| Constraint | Tabela | Coluna | Domínio |
| ---------- | ------ | ------ | ------- |
| `ck_pessoas_tipo` | core.pessoas | tipo | {FISICA, JURIDICA} |
| `ck_pessoas_categoria` | core.pessoas | categoria | {CIDADAO, SERVIDOR, FORNECEDOR, AGENTE_EXTERNO} |
| `ck_contatos_tipo` | core.contatos | tipo | {TEL, EMAIL, REDES, WHATSAPP} |
| `ck_fornecedores_situacao` | core.fornecedores | situacao_cadastro | {ATIVO, INATIVO, SUSPENSO} |
| `ck_auditorias_operacao` | core.auditorias | operacao | {INSERT, UPDATE, DELETE} |
| `ck_logs_sistema_nivel` | core.logs_sistema | nivel | {DEBUG, INFO, WARN, ERROR} |
| `ck_fichas_funcionais_vinculo` | rh.fichas_funcionais | vinculo_tipo | {PRINCIPAL, SUBCONTRATADO, TERCEIRIZADO} |
| `ck_movimentos_estoque_tipo` | almoxarifado.movimentos_estoque | tipo | {ENTRADA, SAIDA, AJUSTE} |
| `ck_imoveis_tipo` | administracao.imoveis | tipo | {TERRITORIAL, PREDIAL, RURAL} |
| `ck_contas_contabeis_tipo` | contabilidade.contas_contabeis | tipo | {DEBITO, CREDITO} |
| `ck_contas_contabeis_natureza` | contabilidade.contas_contabeis | natureza | {SINTETICA, ANALITICA} |
| `ck_indicadores_tipo` | controladoria.indicadores | tipo | {QUALITATIVO, QUANTITATIVO} |
| `ck_perfis_risco_risco` | controladoria.perfis_risco | risco | {BAIXO, MEDIO, ALTO, CRITICO} |
| `ck_configuracoes_tipo` | administracao.configuracoes | tipo | {STRING, INTEGER, BOOLEAN, JSON} |

---

# 6. Triggers de Auditoria (`updated_at`)

> Aplicação da função `core.fn_update_timestamp()` nas tabelas críticas:

```sql
-- core
CREATE TRIGGER trg_pessoas_updated_at          BEFORE UPDATE ON core.pessoas           FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_pessoas_fisicas_updated_at   BEFORE UPDATE ON core.pessoas_fisicas   FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_pessoas_juridicas_updated_at BEFORE UPDATE ON core.pessoas_juridicas FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_enderecos_updated_at         BEFORE UPDATE ON core.enderecos         FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_documentos_updated_at        BEFORE UPDATE ON core.documentos        FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_contatos_updated_at          BEFORE UPDATE ON core.contatos          FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_fornecedores_updated_at      BEFORE UPDATE ON core.fornecedores      FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_unidades_administrativas_updated_at BEFORE UPDATE ON core.unidades_administrativas FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_usuarios_updated_at          BEFORE UPDATE ON core.usuarios          FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_grupos_usuarios_updated_at   BEFORE UPDATE ON core.grupos_usuarios   FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_permissoes_updated_at        BEFORE UPDATE ON core.permissoes        FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_processos_documentais_updated_at BEFORE UPDATE ON core.processos_documentais FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_arquivos_updated_at          BEFORE UPDATE ON core.arquivos          FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_assinaturas_updated_at       BEFORE UPDATE ON core.assinaturas       FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- rh
CREATE TRIGGER trg_servidores_updated_at        BEFORE UPDATE ON rh.servidores          FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_fichas_funcionais_updated_at BEFORE UPDATE ON rh.fichas_funcionais   FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_vinculos_updated_at          BEFORE UPDATE ON rh.vinculos            FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_cargos_updated_at            BEFORE UPDATE ON rh.cargos              FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_funcoes_updated_at           BEFORE UPDATE ON rh.funcoes             FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_dependencias_updated_at      BEFORE UPDATE ON rh.dependencias        FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- tributos
CREATE TRIGGER trg_lancamentos_tributarios_updated_at BEFORE UPDATE ON tributos.lancamentos_tributarios FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_quotas_updated_at            BEFORE UPDATE ON tributos.quotas         FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_debitos_updated_at           BEFORE UPDATE ON tributos.debitos        FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_creditos_updated_at          BEFORE UPDATE ON tributos.creditos       FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- contabilidade
CREATE TRIGGER trg_contas_contabeis_updated_at  BEFORE UPDATE ON contabilidade.contas_contabeis FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_empenhos_updated_at          BEFORE UPDATE ON contabilidade.empenhos  FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_despesas_updated_at          BEFORE UPDATE ON contabilidade.despesas  FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_receitas_updated_at          BEFORE UPDATE ON contabilidade.receitas  FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_rateios_updated_at           BEFORE UPDATE ON contabilidade.rateios   FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- compras
CREATE TRIGGER trg_compras_updated_at           BEFORE UPDATE ON compras.compras         FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_itens_compras_updated_at     BEFORE UPDATE ON compras.itens_compras    FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_contratos_updated_at         BEFORE UPDATE ON compras.contratos       FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- licitacoes
CREATE TRIGGER trg_licitacoes_masters_updated_at BEFORE UPDATE ON licitacoes.licitacoes_masters FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_objetos_updated_at           BEFORE UPDATE ON licitacoes.objetos      FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_lances_updated_at            BEFORE UPDATE ON licitacoes.lances       FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_habilitacoes_updated_at      BEFORE UPDATE ON licitacoes.habilitacoes FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_aditamentos_updated_at       BEFORE UPDATE ON licitacoes.aditamentos  FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- saude / educacao / assistencia_social
CREATE TRIGGER trg_agendamentos_updated_at      BEFORE UPDATE ON saude.agendamentos       FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_pacientes_updated_at         BEFORE UPDATE ON saude.pacientes          FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_fichas_atendimento_updated_at BEFORE UPDATE ON saude.fichas_atendimento FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_prescricoes_updated_at       BEFORE UPDATE ON saude.prescricoes        FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
```
-- almoxarifado
CREATE TRIGGER trg_categorias_itens_updated_at  BEFORE UPDATE ON almoxarifado.categorias_itens  FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_itens_estoque_updated_at     BEFORE UPDATE ON almoxarifado.itens_estoque     FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_movimentos_estoque_updated_at BEFORE UPDATE ON almoxarifado.movimentos_estoque FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- patrimonio
CREATE TRIGGER trg_bens_updated_at              BEFORE UPDATE ON patrimonio.bens              FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_depreciacoes_updated_at      BEFORE UPDATE ON patrimonio.depreciacoes      FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_baixas_bens_updated_at       BEFORE UPDATE ON patrimonio.baixas_bens       FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_transferencias_bens_updated_at BEFORE UPDATE ON patrimonio.transferencias_bens FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- frotas
CREATE TRIGGER trg_veiculos_updated_at          BEFORE UPDATE ON frotas.veiculos             FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_abastecimentos_updated_at    BEFORE UPDATE ON frotas.abastecimentos       FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_manutencoes_updated_at       BEFORE UPDATE ON frotas.manutencoes          FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_deslocamentos_updated_at     BEFORE UPDATE ON frotas.deslocamentos        FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- obras
CREATE TRIGGER trg_obras_updated_at             BEFORE UPDATE ON obras.obras                 FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_plantas_updated_at           BEFORE UPDATE ON obras.plantas               FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_servicos_obra_updated_at     BEFORE UPDATE ON obras.servicos_obra         FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_inspecoes_obra_updated_at    BEFORE UPDATE ON obras.inspecoes_obra        FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- ouvidoria
CREATE TRIGGER trg_protocolos_updated_at        BEFORE UPDATE ON ouvidoria.protocolos        FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_atendimentos_updated_at      BEFORE UPDATE ON ouvidoria.atendimentos      FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_reclamacoes_updated_at       BEFORE UPDATE ON ouvidoria.reclamacoes       FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_respostas_updated_at         BEFORE UPDATE ON ouvidoria.respostas         FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- transparencia
CREATE TRIGGER trg_publicacoes_updated_at       BEFORE UPDATE ON transparencia.publicacoes        FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_leis_updated_at              BEFORE UPDATE ON transparencia.leis               FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_colunas_fiscais_updated_at   BEFORE UPDATE ON transparencia.colunas_fiscais    FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_comprovantes_despesas_updated_at BEFORE UPDATE ON transparencia.comprovantes_despesas FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- controladoria
CREATE TRIGGER trg_indicadores_updated_at       BEFORE UPDATE ON controladoria.indicadores    FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_metas_updated_at             BEFORE UPDATE ON controladoria.metas           FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_avaliacoes_updated_at        BEFORE UPDATE ON controladoria.avaliacoes      FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_perfis_risco_updated_at      BEFORE UPDATE ON controladoria.perfis_risco     FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- planejamento
CREATE TRIGGER trg_planos_updated_at            BEFORE UPDATE ON planejamento.planos           FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_objetivos_estrategicos_updated_at BEFORE UPDATE ON planejamento.objetivos_estrategicos FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_atividades_planos_updated_at BEFORE UPDATE ON planejamento.atividades_planos FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_cronogramas_updated_at       BEFORE UPDATE ON planejamento.cronogramas      FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- procuradoria
CREATE TRIGGER trg_processos_judiciais_updated_at BEFORE UPDATE ON procuradoria.processos_judiciais FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_autuacoes_updated_at         BEFORE UPDATE ON procuradoria.autuacoes        FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_notificacoes_updated_at      BEFORE UPDATE ON procuradoria.notificacoes     FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_pecas_processuais_updated_at BEFORE UPDATE ON procuradoria.pecas_processuais FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- gabinete
CREATE TRIGGER trg_atas_updated_at              BEFORE UPDATE ON gabinete.atas                 FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_distribuicoes_updated_at     BEFORE UPDATE ON gabinete.distribuicoes        FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_posicionamentos_updated_at   BEFORE UPDATE ON gabinete.posicionamentos      FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- administracao
CREATE TRIGGER trg_imoveis_updated_at           BEFORE UPDATE ON administracao.imoveis          FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_configuracoes_updated_at     BEFORE UPDATE ON administracao.configuracoes    FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_parametros_updated_at        BEFORE UPDATE ON administracao.parametros       FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_tabelas_auxiliares_updated_at BEFORE UPDATE ON administracao.tabelas_auxiliares FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- educacao
CREATE TRIGGER trg_turmas_updated_at            BEFORE UPDATE ON educacao.turmas               FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_alunos_updated_at            BEFORE UPDATE ON educacao.alunos               FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_matriculas_updated_at        BEFORE UPDATE ON educacao.matriculas           FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_disciplinas_updated_at       BEFORE UPDATE ON educacao.disciplinas          FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_boletins_updated_at          BEFORE UPDATE ON educacao.boletins             FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- assistencia_social
CREATE TRIGGER trg_fichas_atendimento_as_updated_at BEFORE UPDATE ON assistencia_social.fichas_atendimento_as FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_beneficios_updated_at         BEFORE UPDATE ON assistencia_social.beneficios FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_programas_sociais_updated_at  BEFORE UPDATE ON assistencia_social.programas_sociais FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- agricultura
CREATE TRIGGER trg_propriedades_rurais_updated_at BEFORE UPDATE ON agricultura.propriedades_rurais FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_culturas_updated_at          BEFORE UPDATE ON agricultura.culturas          FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_plantios_updated_at          BEFORE UPDATE ON agricultura.plantios          FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
-- financas
CREATE TRIGGER trg_concessoes_updated_at        BEFORE UPDATE ON financas.concessoes            FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
CREATE TRIGGER trg_taxas_updated_at             BEFORE UPDATE ON financas.taxas                FOR EACH ROW EXECUTE FUNCTION core.fn_update_timestamp();
```

---

# 7. Views de Soft-Delete

> Views que expõem apenas registros ativos (`deleted_at IS NULL`), usadas pela aplicação e relatórios:

```sql
CREATE OR REPLACE VIEW core.vw_pessoas_ativas AS
    SELECT * FROM core.pessoas WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW core.vw_pessoas_fisicas_ativas AS
    SELECT * FROM core.pessoas_fisicas WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW core.vw_pessoas_juridicas_ativas AS
    SELECT * FROM core.pessoas_juridicas WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW core.vw_enderecos_ativos AS
    SELECT * FROM core.enderecos WHERE deleted_at IS NULL AND vigencia_fim IS NULL;
CREATE OR REPLACE VIEW core.vw_documentos_ativos AS
    SELECT * FROM core.documentos WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW core.vw_contatos_ativos AS
    SELECT * FROM core.contatos WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW core.vw_fornecedores_ativos AS
    SELECT * FROM core.fornecedores WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW core.vw_unidades_ativas AS
    SELECT * FROM core.unidades_administrativas WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW core.vw_usuarios_ativos AS
    SELECT * FROM core.usuarios WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW core.vw_grupos_ativos AS
    SELECT * FROM core.grupos_usuarios WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW core.vw_permissoes_ativas AS
    SELECT * FROM core.permissoes WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW core.vw_processos_ativos AS
    SELECT * FROM core.processos_documentais WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW core.vw_arquivos_ativos AS
    SELECT * FROM core.arquivos WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW core.vw_assinaturas_ativas AS
    SELECT * FROM core.assinaturas WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW rh.vw_servidores_ativos AS
    SELECT * FROM rh.servidores WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW rh.vw_fichas_funcionais_ativas AS
    SELECT * FROM rh.fichas_funcionais WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW tributos.vw_lancamentos_tributarios_ativos AS
    SELECT * FROM tributos.lancamentos_tributarios WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW contabilidade.vw_empenhos_ativos AS
    SELECT * FROM contabilidade.empenhos WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW compras.vw_compras_ativas AS
    SELECT * FROM compras.compras WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW compras.vw_itens_compras_ativos AS
    SELECT * FROM compras.itens_compras WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW compras.vw_contratos_ativos AS
    SELECT * FROM compras.contratos WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW licitacoes.vw_licitacoes_masters_ativas AS
    SELECT * FROM licitacoes.licitacoes_masters WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW saude.vw_agendamentos_ativos AS
    SELECT * FROM saude.agendamentos WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW almoxarifado.vw_movimentos_estoque_ativos AS
    SELECT * FROM almoxarifado.movimentos_estoque WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW ouvidoria.vw_protocolos_ativos AS
    SELECT * FROM ouvidoria.protocolos WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW patrimonio.vw_bens_ativos AS
    SELECT * FROM patrimonio.bens WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW frotas.vw_veiculos_ativos AS
    SELECT * FROM frotas.veiculos WHERE deleted_at IS NULL;
CREATE OR REPLACE VIEW administracao.vw_imoveis_ativos AS
    SELECT * FROM administracao.imoveis WHERE deleted_at IS NULL;
```

---

# 8. Criptografia de Dados Sensíveis (LGPD)

> Tratamento conforme Lei 13.709/2018 (LGPD) e `005-Arquitetura-de-Dados.md` (§ 11).

## 8.1. Campos Sensíveis e Tratamento Físico

| Campo | Tabela | Motivo | Tratamento |
| ----- | ------ | ------ | ---------- |
| `numero` | `core.documentos` | Identidade (CPF/RG/CNPJ/CNH) | `TEXT` criptografado AES-256 (`pgp_sym_encrypt`). |
| `senha_hash` | `core.usuarios` | Credencial | Hash bcrypt/argon2 + MFA. |
| `mfa_secret` | `core.usuarios` | Autenticação | `TEXT` criptografado AES-256. |
| `mae` | `core.pessoas_fisicas` | Genealogia | `TEXT` criptografado AES-256. |
| `pai` | `core.pessoas_fisicas` | Genealogia | `TEXT` criptografado AES-256. |
| `data_nascimento` | `core.pessoas_fisicas` | Identidade | Mascarado em relatórios agregados. |
| `ip_origem` | `core.logs_sistema` | Rastreabilidade | Retenção conforme política de logs. |
| `mensagem` | `core.logs_sistema` | Rastreabilidade | Retenção conforme política de logs. |

## 8.2. Uso de `pgcrypto`

```sql
-- Configuração da chave mestra (ex.: via Secrets Manager)
INSERT INTO core.documentos (pessoa_id, tipo, numero, orgao_emissor, data_emissao)
VALUES ('uuid', 'CPF', encode(pgp_sym_encrypt('123.456.789-09', 'chave-mestra'), 'hex'), 'SSP', '2020-01-01');

-- Leitura descriptografada
SELECT convert_from(pgp_sym_decrypt(d.numero::bytea, 'chave-mestra'), 'UTF8') AS numero
FROM core.documentos d WHERE d.id = 'uuid';

-- Hash de senha (bcrypt)
INSERT INTO core.usuarios (pessoa_id, login, senha_hash)
VALUES ('uuid', 'joao.silva', crypt('senha-plana', gen_salt('bf')));

-- Validação de senha
SELECT * FROM core.usuarios u
WHERE u.login = 'joao.silva' AND u.senha_hash = crypt('senha-plana', u.senha_hash);
```

## 8.3. Índice em Colunas Criptografadas

> Índices não podem ser criados diretamente sobre colunas criptografadas. Use coluna derivada (hash determinístico):

```sql
ALTER TABLE core.documentos ADD COLUMN numero_hash TEXT;
UPDATE core.documentos SET numero_hash = digest(
    convert_from(pgp_sym_decrypt(numero::bytea, 'chave-mestra'), 'UTF8'),
    'sha256'
)::text;
CREATE UNIQUE INDEX uk_documentos_numero_hash ON core.documentos(numero_hash);
```

---

# 9. Convenções Físicas Aplicáveis

| Regra | Aplicação no Modelo Físico |
| ----- | -------------------------- |
| Identificador interno | `UUID` v4 (`DEFAULT gen_random_uuid()`), `PRIMARY KEY`. |
| Identificadores externos | `TEXT` (CPF, CNPJ, CNS, NIS, matrícula, códigos IBGE/INEP/CNES). |
| Nomenclatura | Tabelas no plural, português, `snake_case`; FKs `*_id`. |
| Tipos físicos | `UUID`, `TEXT`, `TIMESTAMPTZ`, `DATE`, `NUMERIC(15,2)`, `BOOLEAN`, `INTEGER`, `BIGINT`, `JSONB`. |
| Esquemas | Particionamento por domínio (`core`, `rh`, `compras`, …). |
| Auditoria | Triggers `fn_update_timestamp()` atualizam `updated_at` automaticamente. |
| Exclusão | **Soft delete** (`deleted_at`), `CHECK (deleted_at IS NULL OR deleted_at <= NOW())`. |
| Histórico | `vigencia_inicio`, `vigencia_fim`, `motivo_alteracao`, `versao`. |
| Dados sensíveis | Criptografia AES-256 (`pgcrypto`), hash bcrypt/argon2, mascaramento. |
| FKs | `ON UPDATE CASCADE ON DELETE RESTRICT` (ou `CASCADE` em junção N:M). |

---

# 10. Versionamento

- 1.0 — 2026-08-19 — Início do modelo físico corporativo, derivado de `Modelo-Logico.md` e `005-Arquitetura-de-Dados.md`. Inclui DDL PostgreSQL 16 completo (102 tabelas físicas), esquemas por domínio, índices, triggers de auditoria, views de soft-delete e tratamento de dados sensíveis (LGPD).
- 1.1 — 2026-08-20 — Definição da ordem de aplicação e adiamento de cinco FKs para permitir execução consistente do DDL em migração única.

---

**Documento:** Modelo-Fisico.md
**Última atualização:** 2026-08-20
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
