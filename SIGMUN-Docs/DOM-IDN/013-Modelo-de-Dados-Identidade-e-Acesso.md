# 013 – Modelo-de-Dados – Identidade e Acesso

#### Modelo-de-Dados – Identidade e Acesso

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IDN-013

**Domínio:** Identidade e Acesso

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Identidade-e-Acesso.md`
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

Este artefato detalha **o modelo de dados** do domínio Identidade e Acesso (`DOM-IDN`), com base na implementação material identificada em `src/modules/sigmun_idn` e no conteúdo de negócio declarado no gerador.

---

# 2. Tabelas no schema `idn`

### auditoria_logins (`AuditoriaLoginModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| usuario_id : UUID | opcional |
| login : TEXT <<NN>> | NOT NULL |
| ip_origem : TEXT | opcional |
| user_agent : TEXT | opcional |
| sucesso : BOOLEAN <<NN>> | NOT NULL |
| motivo_falha : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |

### permissoes (`PermissaoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<UQ, NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| escopo : TEXT <<NN>> | NOT NULL |
| modulo : TEXT <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : UUID | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : UUID | opcional |

### role_permissoes (`RolePermissaoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| role_id : UUID <<NN>> | NOT NULL |
| permissao_id : UUID <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |

### roles (`RoleModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| codigo : TEXT <<UQ, NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| descricao : TEXT | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : UUID | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : UUID | opcional |

### sessoes (`SessaoModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| usuario_id : UUID <<NN>> | NOT NULL |
| token : TEXT <<UQ, NN>> | NOT NULL |
| ip_origem : TEXT | opcional |
| user_agent : TEXT | opcional |
| is_active : BOOLEAN <<NN>> | NOT NULL |
| expires_at : DATETIME | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |

### usuario_roles (`UsuarioRoleModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| usuario_id : UUID <<NN>> | NOT NULL |
| role_id : UUID <<NN>> | NOT NULL |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |

### usuarios (`UsuarioModel`)

| Coluna | Obrigatoriedade |
| --- | --- |
| id : UUID <<PK>> | opcional |
| login : TEXT <<UQ, NN>> | NOT NULL |
| email : TEXT <<UQ, NN>> | NOT NULL |
| nome : TEXT <<NN>> | NOT NULL |
| status : TEXT <<NN>> | NOT NULL |
| senha_hash : TEXT <<NN>> | NOT NULL |
| unidades_ids : TEXT <<NN>> | NOT NULL |
| last_login : DATETIME | opcional |
| created_at : DATETIME <<NN>> | NOT NULL |
| created_by : UUID | opcional |
| updated_at : DATETIME <<NN>> | NOT NULL |
| updated_by : UUID | opcional |
| deleted_at : DATETIME | opcional |
| deleted_by : UUID | opcional |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 013-Identidade-e-Acesso-Modelo-de-Dados.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
