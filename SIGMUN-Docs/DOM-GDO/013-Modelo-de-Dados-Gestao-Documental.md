# 013 – Modelo de Dados – Gestão Documental

#### Modelo de Dados – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-013

**Domínio:** Gestão Documental

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Documental.md`
* `001-Mapa-de-Atores-Gestao-Documental.md`
* `002-Mapa-de-Capacidades-Gestao-Documental.md`
* `003-Mapa-de-Processos-Gestao-Documental.md`
* `004-Mapa-de-Servicos-Gestao-Documental.md`
* `005-Casos-de-Uso-Gestao-Documental.md`
* `006-Historias-de-Usuario-Gestao-Documental.md`
* `007-Regras-de-Negocio-Gestao-Documental.md`
* `008-Requisitos-Funcionais-Gestao-Documental.md`
* `009-Requisitos-Nao-Funcionais-Gestao-Documental.md`
* `010-Especificacoes-Gestao-Documental.md`
* `011-Criterios-de-Aceitacao-Gestao-Documental.md`
* `012-Matriz-de-Rastreabilidade-Gestao-Documental.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

---

# 1. Finalidade

Este documento define o **Modelo de Dados conceitual e lógico do Domínio de Gestão Documental do SIGMUN**.

O modelo estabelece as principais entidades, relacionamentos, atributos, identificadores, estados e regras de integridade necessários para representar o ciclo de vida documental na Administração Pública Municipal.

O modelo deverá servir como referência para:

* arquitetura de dados;
* modelagem lógica;
* modelagem física;
* desenvolvimento de serviços;
* desenvolvimento de APIs;
* persistência de dados;
* relatórios;
* indicadores;
* auditoria;
* integração com outros domínios;
* migração de dados;
* testes;
* rastreabilidade.

---

# 2. Objetivos

São objetivos deste modelo:

1. estabelecer uma visão corporativa dos dados do domínio;
2. identificar as principais entidades de negócio;
3. estabelecer relacionamentos entre entidades;
4. definir identificadores e chaves;
5. preservar integridade referencial;
6. evitar duplicidade de informações;
7. garantir rastreabilidade do ciclo de vida documental;
8. permitir auditoria dos eventos;
9. permitir integração com outros domínios;
10. preparar o domínio para implementação tecnológica.

---

# 3. Princípios de Modelagem

O modelo deverá observar os princípios corporativos do SIGMUN.

## 3.1 Fonte Única da Verdade

Cada informação deverá possuir uma fonte de autoridade claramente definida.

## 3.2 Não Duplicação Desnecessária

Informações corporativas existentes em outros domínios não deverão ser replicadas sem justificativa arquitetural.

Exemplos:
* pessoas (DOM-CUM);
* unidades administrativas (DOM-CUM);
* usuários (DOM-IDN);
* metadados corporativos (DOM-MET).

Quando apropriado, o domínio deverá utilizar referências às entidades corporativas.

## 3.3 Rastreabilidade

Todo documento deverá permitir reconstruir sua trajetória:

```text
Criação
    ↓
Classificação
    ↓
Tramitação
    ↓
Arquivamento
    ↓
Destinação
```

## 3.4 Auditoria

Eventos relevantes deverão ser rastreáveis por:
* usuário;
* data e hora;
* operação;
* entidade;
* registro afetado;
* origem;
* resultado.

---

# 4. Entidades do Domínio

## 4.1 Entidades Principais

| Entidade | Descrição | Tipo |
| --- | --- | --- |
| documento | Representa um documento municipal | Principal |
| versao_documento | Versões de um documento | Secundária |
| tramitacao | Movimentações de documentos entre unidades | Secundária |
| processo_documental | Processos administrativos | Principal |
| classificacao | Classificação arquivística | Configuração |
| temporalidade | Prazos de retenção e destinação | Configuração |
| assinatura | Assinaturas digitais de documentos | Secundária |
| permissao_documento | Permissões de acesso a documentos | Configuração |
| metadado_documento | Metadados associados a documentos | Secundária |
| auditoria | Registros de auditoria | Histórico |

## 4.2 Entidades de Configuração

| Entidade | Descrição | Tipo |
| --- | --- | --- |
| tipo_documental | Tipos de documentos | Configuração |
| plano_classificação | Plano de classificação hierárquico | Configuração |
| tabela_temporalidade | Tabela de temporalidade documental | Configuração |
| taxaonomia | Taxonomias para indexação | Configuração |

## 4.3 Entidades de Referência (Outros Domínios)

| Entidade | Domínio | Descrição |
| --- | --- | --- |
| unidade_administrativa | DOM-CUM | Unidades organizacionais |
| pessoa | DOM-CUM | Pessoas físicas e jurídicas |
| usuario | DOM-IDN | Usuários do sistema |
| metadado_corporativo | DOM-MET | Metadados corporativos |

---

# 5. Modelo Conceitual

## 5.1 Diagrama Entidade-Relacionamento (Conceitual)

```text
┌─────────────────┐       ┌─────────────────────┐       ┌─────────────────┐
│   CLASSIFICACAO │       │      DOCUMENTO      │       │ TIPO_DOCUMENTAL │├─────────────────┤       ├─────────────────────┤       ├─────────────────┤
│ id (PK)         │       │ id (PK)             │       │ id (PK)         │
│ codigo          │◄──────│ classificacao_id(FK) │       │ codigo          │
│ nome            │       │ tipo_documental_id  │──────►│ nome            │
│ nivel           │       │ codigo_unico        │       │ descricao       │
│ classe          │       │ titulo              │       └─────────────────┘
│ subclasse       │       │ conteudo            │
│ serie           │       │ hash_sha256         │       ┌─────────────────┐
│ temporalidade_id│──────►│ data_criacao        │       │  TEMPORALIDADE  │
└─────────────────┘       │ status              │       ├─────────────────┤
                          │ nivel_sigilo        │       │ id (PK)         │
┌─────────────────┐       │ unidade_id (FK)     │       │ prazo_retencao  │
│   PROCESSO_     │       │ autor_id (FK)       │       │ destinacao      │
│   DOCUMENTAL    │       └──────────┬──────────┘       └─────────────────┘
├─────────────────┤                  │
│ id (PK)         │                  │
│ numero          │       ┌──────────┴──────────┐       ┌─────────────────┐
│ assunto         │       │  VERSAO_DOCUMENTO    │       │   ASSINATURA    │
│ data_abertura   │       ├─────────────────────┤       ├─────────────────┤
│ data_encerramento       │ id (PK)             │       │ id (PK)         │
│ status          │       │ documento_id (FK)   │       │ documento_id(FK)│
│ unidade_id (FK) │       │ numero_versao       │       │ usuario_id (FK) │
└────────┬────────┘       │ conteudo            │       │ certificado     │
         │                │ hash_sha256         │       │ data_assinatura │
         │                │ data_criacao        │       │ valida          │
         │                │ usuario_id (FK)     │       └─────────────────┘
         │                └─────────────────────┘
         │
         │         ┌─────────────────────┐       ┌─────────────────┐
         │         │    TRAMITACAO       │       │ PERMISSAO_      │
         │         ├─────────────────────┤       │ DOCUMENTO       │
         └────────►│ id (PK)             │       ├─────────────────┤
                   │ documento_id (FK)   │       │ id (PK)         │
                   │ processo_id (FK)    │       │ documento_id(FK)│
                   │ unidade_origem_id(FK)│       │ usuario_id (FK) │
                   │ unidade_destino_id(FK)      │ nivel_acesso    │
                   │ data_envio          │       └─────────────────┘
                   │ data_recebimento    │
                   │ observacao          │       ┌─────────────────┐
                   │ status              │       │ METADADO_       │
                   └─────────────────────┘       │ DOCUMENTO       │
                                                 ├─────────────────┤
┌─────────────────┐       ┌─────────────────────┐│ id (PK)         │
│  AUDITORIA      │       │  PLANO_CLASSIFICACAO││ documento_id(FK)│
├─────────────────┤       ├─────────────────────┤│ chave           │
│ id (PK)         │       │ id (PK)             ││ valor           │
│ entidade        │       │ classe              │└─────────────────┘
│ entidade_id     │       │ subclasse           │
│ operacao        │       │ serie               │
│ usuario_id (FK) │       │ descricao           │
│ data_hora       │       └─────────────────────┘
│ ip_origem       │
│ dados           │
└─────────────────┘
```

---

# 6. Modelo Lógico

## 6.1 Tabela: documento

| Campo | Tipo | Restrição | Descrição |
| --- | --- | --- | --- |
| id | UUID | PK | Identificador único |
| codigo_unico | VARCHAR(50) | UNIQUE, NOT NULL | Código único do documento (RN-GDO-001) |
| tipo_documental_id | UUID | FK → tipo_documental | Tipo do documento |
| classificacao_id | UUID | FK → plano_classificacao | Classificação arquivística |
| titulo | VARCHAR(500) | NOT NULL | Título do documento |
| conteudo | TEXT/BLOB | NULL | Conteúdo ou referência ao arquivo |
| hash_sha256 | VARCHAR(64) | NOT NULL | Hash SHA-256 do conteúdo (RN-GDO-002) |
| data_criacao | TIMESTAMP | NOT NULL | Data de criação |
| data_atualizacao | TIMESTAMP | NULL | Data da última atualização |
| status | ENUM | NOT NULL | Status: rascunho, registrado, em_tramitacao, arquivado, eliminado, guarda_permanente |
| nivel_sigilo | ENUM | NOT NULL | Nível de sigilo: publico, reservado, secreto |
| unidade_id | UUID | FK → unidade_administrativa | Unidade responsável |
| autor_id | UUID | FK → usuario | Autor do documento |
| assinado | BOOLEAN | DEFAULT FALSE | Indica se está assinado |

## 6.2 Tabela: versao_documento

| Campo | Tipo | Restrição | Descrição |
| --- | --- | --- | --- |
| id | UUID | PK | Identificador único |
| documento_id | UUID | FK → documento, NOT NULL | Documento relacionado |
| numero_versao | INTEGER | NOT NULL | Número da versão |
| conteudo | TEXT/BLOB | NULL | Conteúdo ou referência ao arquivo |
| hash_sha256 | VARCHAR(64) | NOT NULL | Hash SHA-256 da versão |
| data_criacao | TIMESTAMP | NOT NULL | Data de criação da versão |
| usuario_id | UUID | FK → usuário | Usuário que criou a versão |
| justificativa | VARCHAR(500) | NULL | Justificativa da nova versão |

**Restrição UNIQUE:** (documento_id, numero_versao)

## 6.3 Tabela: tramitacao

| Campo | Tipo | Restrição | Descrição |
| --- | --- | --- | --- |
| id | UUID | PK | Identificador único |
| documento_id | UUID | FK → documento, NOT NULL | Documento tramitado |
| processo_id | UUID | FK → processo_documental, NULL | Processo relacionado |
| unidade_origem_id | UUID | FK → unidade_administrativa | Unidade de origem |
| unidade_destino_id | UUID | FK → unidade_administrativa | Unidade de destino |
| data_envio | TIMESTAMP | NOT NULL | Data do envio |
| data_recebimento | TIMESTAMP | NULL | Data do recebimento |
| observacao | TEXT | NULL | Observações/despacho |
| status | ENUM | NOT NULL | Status: pendente, recebido, devolvido |
| usuario_envio_id | UUID | FK → usuário | Usuário que enviou |
| usuario_recebimento_id | UUID | FK → usuário | Usuário que recebeu |

## 6.4 Tabela: processo_documental

| Campo | Tipo | Restrição | Descrição |
| --- | --- | --- | --- |
| id | UUID | PK | Identificador único |
| numero | VARCHAR(50) | UNIQUE, NOT NULL | Número do processo |
| assunto | VARCHAR(500) | NOT NULL | Assunto do processo |
| data_abertura | TIMESTAMP | NOT NULL | Data de abertura |
| data_encerramento | TIMESTAMP | NULL | Data de encerramento |
| status | ENUM | NOT NULL | Status: aberto, encerrado, reaberto |
| unidade_id | UUID | FK → unidade_administrativa | Unidade responsável |
| usuario_abertura_id | UUID | FK → usuário | Usuário que abriu |
| usuario_encerramento_id | UUID | FK → usuário | Usuário que encerrou |

## 6.5 Tabela: classificacao (plano_classificacao)

| Campo | Tipo | Restrição | Descrição |
| --- | --- | --- | --- |
| id | UUID | PK | Identificador único |
| classe | VARCHAR(50) | NOT NULL | Classe da classificação |
| subclasse | VARCHAR(50) | NULL | Subclasse da classificação |
| serie | VARCHAR(50) | NULL | Série da classificação |
| descricao | VARCHAR(500) | NULL | Descrição |
| temporalidade_id | UUID | FK → tabela_temporalidade | Temporalidade vinculada |

**Restrição UNIQUE:** (classe, subclasse, serie)

## 6.6 Tabela: tabela_temporalidade

| Campo | Tipo | Restrição | Descrição |
| --- | --- | --- | --- |
| id | UUID | PK | Identificador único |
| tipo_documental_id | UUID | FK → tipo_documental, NOT NULL | Tipo documental |
| prazo_retencao | INTEGER | NOT NULL | Prazo de retenção em anos |
| destinacao | ENUM | NOT NULL | Destinacao: eliminacao, guarda_permanente |
| observacao | VARCHAR(500) | NULL | Observações |

## 6.7 Tabela: assinatura

| Campo | Tipo | Restrição | Descrição |
| --- | --- | --- | --- |
| id | UUID | PK | Identificador único |
| documento_id | UUID | FK → documento, NOT NULL | Documento assinado |
| usuario_id | UUID | FK → usuário, NOT NULL | Signatário |
| certificado | TEXT | NULL | Certificado digital |
| data_assinatura | TIMESTAMP | NOT NULL | Data da assinatura |
| valida | BOOLEAN | DEFAULT TRUE | Indica se a assinatura é válida |
| hash_assinatura | VARCHAR(256) | NULL | Hash da assinatura |

**Restrição UNIQUE:** (documento_id, usuario_id)

## 6.8 Tabela: permissao_documento

| Campo | Tipo | Restrição | Descrição |
| --- | --- | --- | --- |
| id | UUID | PK | Identificador único |
| documento_id | UUID | FK → documento, NOT NULL | Documento |
| usuario_id | UUID | FK → usuário, NOT NULL | Usuário |
| unidade_id | UUID | FK → unidade_administrativa, NULL | Unidade |
| nivel_acesso | ENUM | NOT NULL | Nível: leitura, escrita, administracao |

**Restrição UNIQUE:** (documento_id, usuario_id)

## 6.9 Tabela: metadado_documento

| Campo | Tipo | Restrição | Descrição |
| --- | --- | --- | --- |
| id | UUID | PK | Identificador único |
| documento_id | UUID | FK → documento, NOT NULL | Documento |
| chave | VARCHAR(100) | NOT NULL | Chave do metadado |
| valor | TEXT | NOT NULL | Valor do metadado |

**Restrição UNIQUE:** (documento_id, chave)

## 6.10 Tabela: tipo_documental

| Campo | Tipo | Restrição | Descrição |
| --- | --- | --- | --- |
| id | UUID | PK | Identificador único |
| codigo | VARCHAR(20) | UNIQUE, NOT NULL | Código do tipo |
| nome | VARCHAR(200) | NOT NULL | Nome do tipo |
| descricao | VARCHAR(500) | NULL | Descrição |
| ativo | BOOLEAN | DEFAULT TRUE | Indica se está ativo |

## 6.11 Tabela: auditoria

| Campo | Tipo | Restrição | Descrição |
| --- | --- | --- | --- |
| id | UUID | PK | Identificador único |
| entidade | VARCHAR(100) | NOT NULL | Entidade afetada |
| entidade_id | UUID | NOT NULL | ID do registro afetado |
| operacao | VARCHAR(20) | NOT NULL | Operação: criar, atualizar, excluir |
| usuario_id | UUID | FK → usuário | Usuário responsável |
| data_hora | TIMESTAMP | NOT NULL | Data e hora da operação |
| ip_origem | VARCHAR(45) | NULL | IP de origem |
| dados_antigos | JSON | NULL | Dados anteriores |
| dados_novos | JSON | NULL | Dados novos |

---

# 7. Regras de Integridade

## 7.1 Integridade Referencial

1. Todo documento deve pertencer a uma unidade administrativa válida
2. Todo documento deve ter um tipo documental válido
3. Toda versão deve pertencer a um documento existente
4. Toda tramitação deve pertencer a um documento existente
5. Todo processo deve pertencer a uma unidade administrativa válida
6. Toda assinatura deve pertencer a um documento existente

## 7.2 Integridade de Negócio

1. O código do documento deve ser único (RN-GDO-001)
2. O hash SHA-256 deve ser calculado no momento da captura (RN-GDO-002)
3. Documentos assinados não podem ser alterados (RN-GDO-018)
4. Versões anteriores são imutáveis (RN-GDO-005)
5. Registros de auditoria não podem ser alterados ou excluídos (RN-GDO-028)

## 7.3 Regras de Estado

1. Documento: rascunho → registrado → em_tramitacao → arquivado → eliminado/guarda_permanente
2. Tramitação: pendente → recebido → devolvido
3. Processo: aberto → encerrado → reaberto

---

# 8. Índices Recomendados

| Tabela | Índice | Tipo | Justificativa |
| --- | --- | --- | --- |
| documento | codigo_unico | UNIQUE | Busca por código único |
| documento | unidade_id | BTREE | Filtro por unidade |
| documento | status | BTREE | Filtro por status |
| documento | data_criacao | BTREE | Ordenação temporal |
| tramitacao | documento_id | BTREE | Busca por documento |
| tramitacao | unidade_destino_id | BTREE | Busca por destinatário |
| tramitacao | status | BTREE | Filtro por status |
| processo_documental | numero | UNIQUE | Busca por número |
| processo_documental | unidade_id | BTREE | Filtro por unidade |
| assinatura | documento_id | BTREE | Busca por documento |
| auditoria | entidade, entidade_id | BTREE | Rastreabilidade |
| auditoria | data_hora | BTREE | Consulta temporal |

---

# 9. Refinamento Futuro

O modelo deste documento representa a primeira versão da modelagem do domínio.

Durante o refinamento, o modelo poderá:

* ser expandido com novas entidades;
* ser ajustado conforme evolução dos requisitos;
* ser normalizado ou desnormalizado conforme necessidades de performance;
* ser integrado com ferramentas de modelagem;
* ser implementado fisicamente no banco de dados.

---

# 10. Registro no Mapa Mestre

Este artefato deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

**Identificador do artefato:**

`MD-MAP-GDO-001`

**Tipo:**

Modelo de Dados.

**Domínio:**

Gestão Documental.

**Versão:**

2.0.

---

# 11. Próximo Artefato

O próximo artefato recomendado é:

`014-Modelo-de-Integracao-Gestao-Documental.md`

A cadeia de detalhamento ficará:

```text
000-Domínio
      ↓
001-Atores
      ↓
002-Capacidades
      ↓
003-Processos
      ↓
004-Serviços
      ↓
005-Casos de Uso
      ↓
006-Histórias de Usuário
      ↓
007-Regras de Negócio
      ↓
008-Requisitos Funcionais
      ↓
009-Requisitos Não Funcionais
      ↓
010-Especificações
      ↓
011-Critérios de Aceitação
      ↓
012-Matriz de Rastreabilidade
      ↓
013-Modelo de Dados
      ↓
014-Modelo de Integração
```

---

# 12. Controle de Versões

| Versão | Data       | Descrição |
| ------ | ---------- | --------- |
| 1.0    | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0    | 2026-09-02 | Conteúdo detalhado: 11 entidades, modelo lógico completo |

---

**Documento:** 013-Modelo-de-Dados-Gestao-Documental.md

**Última atualização:** 2026-09-02

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
