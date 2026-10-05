# 010 – Especificacoes – Identidade e Acesso

#### Especificacoes – Identidade e Acesso

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IDN-010

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

Este artefato detalha **as especificações** do domínio Identidade e Acesso (`DOM-IDN`), com base na implementação material identificada em `src/modules/sigmun_idn` e no conteúdo de negócio declarado no gerador.

---

# 2. Contratos publicados

| Método | Caminho | Recurso | Corpo |
| --- | --- | --- | --- |
| POST | `/api/v1/idn/auth/login` | auth | JSON (payload do domínio) |
| POST | `/api/v1/idn/auth/login/jwt` | auth | JSON (payload do domínio) |
| POST | `/api/v1/idn/auth/logout` | auth | JSON (payload do domínio) |
| POST | `/api/v1/idn/auth/logout/jwt` | auth | JSON (payload do domínio) |
| GET | `/api/v1/idn/auth/me` | auth | JSON (payload do domínio) |
| POST | `/api/v1/idn/auth/refresh` | auth | JSON (payload do domínio) |
| GET | `/api/v1/idn/usuarios` | usuarios | JSON (payload do domínio) |
| POST | `/api/v1/idn/usuarios` | usuarios | JSON (payload do domínio) |
| GET | `/api/v1/idn/usuarios/{usuario_id}` | usuarios | JSON (payload do domínio) |
| POST | `/api/v1/idn/usuarios/{usuario_id}/ativar` | usuarios | JSON (payload do domínio) |
| POST | `/api/v1/idn/usuarios/{usuario_id}/bloquear` | usuarios | JSON (payload do domínio) |
| POST | `/api/v1/idn/usuarios/{usuario_id}/desativar` | usuarios | JSON (payload do domínio) |

---

# 3. Validações aplicadas

| Regra | Validação |
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

**Documento:** 010-Identidade-e-Acesso-Especificacoes.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
