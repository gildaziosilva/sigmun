# 004 – Mapa-de-Servicos – Identidade e Acesso

#### Mapa-de-Servicos – Identidade e Acesso

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IDN-004

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

Este artefato detalha **o mapa de serviços** do domínio Identidade e Acesso (`DOM-IDN`), com base na implementação material identificada em `src/modules/sigmun_idn` e no conteúdo de negócio declarado no gerador.

---

# 2. Operações publicadas em `/api/v1/idn`

| Método | Caminho | Recurso | Resumo |
| --- | --- | --- | --- |
| POST | `/api/v1/idn/auth/login` | auth | Autentica um usuário (Legacy - Session Token) |
| POST | `/api/v1/idn/auth/login/jwt` | auth | Autentica um usuário e retorna JWT token pair (access + refresh) |
| POST | `/api/v1/idn/auth/logout` | auth | Realiza logout (compatível: session token ou JWT) |
| POST | `/api/v1/idn/auth/logout/jwt` | auth | Realiza logout JWT (invalida refresh token) |
| GET | `/api/v1/idn/auth/me` | auth | Retorna dados do usuário autenticado (valida JWT ou legacy header) |
| POST | `/api/v1/idn/auth/refresh` | auth | Renova access token usando refresh token (rotation) |
| GET | `/api/v1/idn/usuarios` | usuarios | Lista usuários com paginação |
| POST | `/api/v1/idn/usuarios` | usuarios | Cria um novo usuário |
| GET | `/api/v1/idn/usuarios/{usuario_id}` | usuarios | Busca usuário por ID |
| POST | `/api/v1/idn/usuarios/{usuario_id}/ativar` | usuarios | Ativa um usuário |
| POST | `/api/v1/idn/usuarios/{usuario_id}/bloquear` | usuarios | Bloqueia um usuário |
| POST | `/api/v1/idn/usuarios/{usuario_id}/desativar` | usuarios | Desativa um usuário |

---

# 3. Recursos publicados

| Recurso | Operações |
| --- | --- |
| auth | 6 |
| usuarios | 6 |

---

# 4. Lacunas a validar

* Definir a janela de desativação do header X-Usuario-Id.
* Definir a rotação de segredos de assinatura do token.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 004-Identidade-e-Acesso-Mapa-de-Servicos.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
