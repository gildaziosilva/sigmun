# 026 – Modelo-de-Dominio – Identidade e Acesso

#### Modelo-de-Dominio – Identidade e Acesso

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IDN-026

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

Este artefato detalha **o modelo de domínio** do domínio Identidade e Acesso (`DOM-IDN`), com base na implementação material identificada em `src/modules/sigmun_idn` e no conteúdo de negócio declarado no gerador.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| auditoria_logins | `AuditoriaLoginModel` | 8 |
| permissoes | `PermissaoModel` | 12 |
| role_permissoes | `RolePermissaoModel` | 5 |
| roles | `RoleModel` | 10 |
| sessoes | `SessaoModel` | 10 |
| usuario_roles | `UsuarioRoleModel` | 5 |
| usuarios | `UsuarioModel` | 14 |

---

# 3. Domínios de valor

### UsuarioStatus

| Membro | Valor |
| --- | --- |
| ATIVO | "ativo" |
| INATIVO | "inativo" |
| BLOQUEADO | "bloqueado" |
| PENDENTE | "pendente" |
### PermissaoEscopo

| Membro | Valor |
| --- | --- |
| GLOBAL | "global" |
| DOMINIO | "dominio" |
| UNIDADE | "unidade" |
| PROPRIO | "proprio" |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-IDN-001 | a autenticação emite par de tokens (acesso e renovação). |
| RN-IDN-002 | usuário bloqueado ou inativo não autentica. |
| RN-IDN-003 | permissão só vale dentro do escopo declarado. |
| RN-IDN-004 | toda tentativa de login é registrada em auditoria_logins. |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Identidade-e-Acesso-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
