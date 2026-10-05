# 005 – Casos-de-Uso – Identidade e Acesso

#### Casos-de-Uso – Identidade e Acesso

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IDN-005

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

Este artefato detalha **os casos de uso** do domínio Identidade e Acesso (`DOM-IDN`), com base na implementação material identificada em `src/modules/sigmun_idn` e no conteúdo de negócio declarado no gerador.

---

# 2. Casos de uso implementados

| Identificador | Caso de uso | Classe | Resumo |
| --- | --- | --- | --- |
| CU-IDN-001 | CriarUsuario | `CriarUsuarioUseCase` | Caso de uso para criar um novo usuário. |
| CU-IDN-002 | RegistrarUsuario | `RegistrarUsuarioUseCase` | Caso de uso para criar um novo usuário. |
| CU-IDN-003 | AtivarUsuario | `AtivarUsuarioUseCase` | Caso de uso para ativar um usuário. |
| CU-IDN-004 | DesativarUsuario | `DesativarUsuarioUseCase` | Caso de uso para desativar um usuário. |
| CU-IDN-005 | BloquearUsuario | `BloquearUsuarioUseCase` | Caso de uso para bloquear um usuário. |
| CU-IDN-006 | BuscarUsuario | `BuscarUsuarioUseCase` | Caso de uso para buscar usuários. |
| CU-IDN-007 | ConsultarUsuario | `ConsultarUsuarioUseCase` | Caso de uso para buscar usuários. |
| CU-IDN-008 | ListarUsuarios | `ListarUsuariosUseCase` | Caso de uso para listar usuários com paginação. |
| CU-IDN-009 | AutenticarUsuario | `AutenticarUsuarioUseCase` | Caso de uso para autenticar um usuário. |
| CU-IDN-010 | Logout | `LogoutUseCase` | Caso de uso para realizar logout. |

---

# 3. Cobertura

Casos de uso no código: **10**. Operações publicadas: **12**.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 005-Identidade-e-Acesso-Casos-de-Uso.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
