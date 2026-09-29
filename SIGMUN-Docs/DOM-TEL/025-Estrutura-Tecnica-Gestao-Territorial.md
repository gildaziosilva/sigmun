# 025 – Estrutura Técnica – Gestão Territorial

#### Estrutura Técnica – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-025

**Domínio:** Gestão Territorial

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Territorial.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000C-HIERARQUIA-DOCUMENTAL.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `030-Roadmap-de-Implementacao-dos-Dominios.md`
* `Mapa-de-Dominios.md`
* `Modelo-Logico.md`
* `Modelo-Fisico.md`
* `Dicionario-de-dados.md`

---

# 1. Finalidade

Este artefato descreve a estrutura técnica do módulo `sigmun_territorial` e seus componentes
implementados.

---

# 2. Árvore de Módulos

| Camada | Caminho | Responsabilidade |
| --- | --- | --- |
| Domínio | `src/modules/sigmun_territorial/domain/entities` | Entidades, invariantes e enums |
| Domínio | `src/modules/sigmun_territorial/domain/exceptions.py` | Exceções de negócio |
| Aplicação | `src/modules/sigmun_territorial/application/interfaces.py` | Ports de repositório |
| Aplicação | `src/modules/sigmun_territorial/application/use_cases*.py` | Casos de uso |
| Infraestrutura | `src/modules/sigmun_territorial/infrastructure/database/models.py` | Modelos ORM (schema `tel`) |
| Infraestrutura | `src/modules/sigmun_territorial/infrastructure/database/seeds*.py` | Seed DEMO |
| Infraestrutura | `src/modules/sigmun_territorial/infrastructure/repositories/` | Adaptadores SQLAlchemy |
| Apresentação | `src/modules/sigmun_territorial/presentation/schemas/` | Schemas Pydantic |
| Apresentação | `src/modules/sigmun_territorial/presentation/api/` | Endpoints e dependências |

---

# 3. Casos de Uso Implementados

| Caso de uso | Descrição | `execute(...)` |
| --- | --- | --- |
| `CadastrarBairroUseCase` | Cadastra uma divisão territorial (RN-TEL-001). | dto |
| `AtualizarBairroUseCase` | Atualiza a cadastro de uma divisão territorial (RN-TEL-001). | dto |
| `ExcluirBairroUseCase` | Exclui (soft-delete) uma divisão territorial (RN-TEL-006). | bairro_id |
| `CadastrarLogradouroUseCase` | Cadastra um logradouro público vinculado a bairro (RN-TEL-002). | dto |
| `AtualizarLogradouroUseCase` | Atualiza o cadastro de um logradouro público (RN-TEL-002). | dto |
| `ExcluirLogradouroUseCase` | Exclui (soft-delete) um logradouro público. | logradouro_id |
| `CadastrarPlantaValoresUseCase` | Cadastra uma planta genérica de valores (RN-TEL-003). | dto |
| `AtualizarPlantaValoresUseCase` | Atualiza os valores de uma planta genérica de valores. | dto |
| `AtivarPlantaValoresUseCase` | Ativa uma planta genérica de valores em rascunho (RN-TEL-003/004). | planta_id |
| `RevogarPlantaValoresUseCase` | Revoga uma planta genérica de valores vigente (RN-TEL-004). | planta_id, motivo |
| `RegistrarGeorreferenciaUseCase` | Registra a georreferência de um bairro ou logradouro (RN-TEL-005). | dto |
| `ExcluirGeorreferenciaUseCase` | Exclui (soft-delete) uma georreferência territorial. | georreferencia_id |

---

# 4. Registração da Aplicação

* O router é registrado em `src/main.py`.
* O prefixo publicado é `/api/v1/tel`.
* A migração é `alembic/versions/20260929_01_dom_tel_models.py`.

---

# 5. Frontend

| Arquivo | Responsabilidade |
| --- | --- |
| `frontend/admin/src/pages/territorial/TelPage.tsx` | Módulo territorial (DOM-TEL) |
| `frontend/admin/src/pages/territorial/ImoPage.tsx` | Módulo imobiliário (DOM-IMO) |
| `frontend/admin/src/pages/territorial/TerrShared.tsx` | Componentes e formatadores compartilhados |
| `frontend/admin/src/lib/api.ts` | Cliente HTTP dos dois domínios |

---

# 6. Scripts

| Script | Responsabilidade |
| --- | --- |
| `scripts/seed_tel.py` | Carga DEMO do DOM-TEL (`--dry-run`, `--limpar`) |
| `scripts/seed_imo.py` | Carga DEMO do DOM-IMO (`--dry-run`, `--limpar`) |
| `scripts/gerar_artefatos_territoriais.py` | Geração dos artefatos documentais |

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 025-Estrutura-Tecnica-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
