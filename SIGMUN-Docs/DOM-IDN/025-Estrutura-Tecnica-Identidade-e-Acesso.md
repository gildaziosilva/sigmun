# 025 – Estrutura-Tecnica – Identidade e Acesso

#### Estrutura-Tecnica – Identidade e Acesso

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IDN-025

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

Este artefato detalha **a estrutura técnica** do domínio Identidade e Acesso (`DOM-IDN`), com base na implementação material identificada em `src/modules/sigmun_idn` e no conteúdo de negócio declarado no gerador.

---

# 2. Módulo `sigmun_idn`

| Arquivo | Linhas |
| --- | --- |
| `src/modules/sigmun_idn/__init__.py` | 0 |
| `src/modules/sigmun_idn/application/__init__.py` | 0 |
| `src/modules/sigmun_idn/application/interfaces/__init__.py` | 15 |
| `src/modules/sigmun_idn/application/interfaces/repositories.py` | 201 |
| `src/modules/sigmun_idn/application/services/__init__.py` | 0 |
| `src/modules/sigmun_idn/application/use_cases/__init__.py` | 25 |
| `src/modules/sigmun_idn/application/use_cases/auth_use_cases.py` | 327 |
| `src/modules/sigmun_idn/application/use_cases/usuario_use_cases.py` | 270 |
| `src/modules/sigmun_idn/domain/__init__.py` | 121 |
| `src/modules/sigmun_idn/domain/entities/__init__.py` | 19 |
| `src/modules/sigmun_idn/domain/entities/usuario.py` | 236 |
| `src/modules/sigmun_idn/domain/events/__init__.py` | 43 |
| `src/modules/sigmun_idn/domain/events/usuario_events.py` | 164 |
| `src/modules/sigmun_idn/domain/exceptions.py` | 102 |
| `src/modules/sigmun_idn/domain/services/__init__.py` | 11 |
| `src/modules/sigmun_idn/domain/services/auth_service.py` | 179 |
| `src/modules/sigmun_idn/domain/value_objects/__init__.py` | 5 |
| `src/modules/sigmun_idn/domain/value_objects/email.py` | 34 |
| `src/modules/sigmun_idn/domain/value_objects/login.py` | 41 |
| `src/modules/sigmun_idn/domain/value_objects/senha.py` | 39 |
| `src/modules/sigmun_idn/infrastructure/__init__.py` | 0 |
| `src/modules/sigmun_idn/infrastructure/database/__init__.py` | 23 |
| `src/modules/sigmun_idn/infrastructure/database/models.py` | 206 |
| `src/modules/sigmun_idn/infrastructure/database/seeds.py` | 590 |
| `src/modules/sigmun_idn/infrastructure/models/__init__.py` | 0 |
| `src/modules/sigmun_idn/infrastructure/repositories/__init__.py` | 25 |
| `src/modules/sigmun_idn/infrastructure/repositories/sqlalchemy_auditoria_repository.py` | 86 |
| `src/modules/sigmun_idn/infrastructure/repositories/sqlalchemy_permissao_repository.py` | 123 |
| `src/modules/sigmun_idn/infrastructure/repositories/sqlalchemy_role_repository.py` | 164 |
| `src/modules/sigmun_idn/infrastructure/repositories/sqlalchemy_sessao_repository.py` | 98 |
| `src/modules/sigmun_idn/infrastructure/repositories/sqlalchemy_usuario_repository.py` | 240 |
| `src/modules/sigmun_idn/infrastructure/repositories/uuid_utils.py` | 21 |
| `src/modules/sigmun_idn/presentation/api/__init__.py` | 432 |
| `src/modules/sigmun_idn/presentation/schemas/__init__.py` | 184 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 025-Identidade-e-Acesso-Estrutura-Tecnica.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
