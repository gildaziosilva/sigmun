# 025 – Estrutura Técnica – Geoinformação Municipal

#### Estrutura Técnica – Geoinformação Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GEO-025

**Domínio:** Geoinformação Municipal

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Geoinformacao-Municipal.md`
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

Este artefato descreve a estrutura técnica do módulo `sigmun_geoinformacao` e seus componentes
implementados.

---

# 2. Árvore de Módulos

| Camada | Caminho | Responsabilidade |
| --- | --- | --- |
| Domínio | `src/modules/sigmun_geoinformacao/domain/entities` | Entidades, invariantes e enums |
| Domínio | `src/modules/sigmun_geoinformacao/domain/exceptions.py` | Exceções de negócio |
| Aplicação | `src/modules/sigmun_geoinformacao/application/interfaces.py` | Ports de repositório |
| Aplicação | `src/modules/sigmun_geoinformacao/application/use_cases*.py` | Casos de uso |
| Infraestrutura | `src/modules/sigmun_geoinformacao/infrastructure/database/models.py` | Modelos ORM (schema `geo`) |
| Infraestrutura | `src/modules/sigmun_geoinformacao/infrastructure/database/seeds*.py` | Seed DEMO |
| Infraestrutura | `src/modules/sigmun_geoinformacao/infrastructure/repositories/` | Adaptadores SQLAlchemy |
| Apresentação | `src/modules/sigmun_geoinformacao/presentation/schemas/` | Schemas Pydantic |
| Apresentação | `src/modules/sigmun_geoinformacao/presentation/api/` | Endpoints e dependências |

---

# 3. Casos de Uso Implementados

| Caso de uso | Descrição | `execute(...)` |
| --- | --- | --- |
| `CadastrarCamadaUseCase` | Cadastra uma camada de mapa no geoportal (RN-GEO-001). | dto |
| `AtualizarCamadaUseCase` | Atualiza o cadastro de uma camada de mapa. | dto |
| `AtivarCamadaUseCase` | Ativa uma camada de mapa para publicação (RN-GEO-006). | camada_id, autor_id |
| `DesativarCamadaUseCase` | Desativa uma camada de mapa (RN-GEO-006). | camada_id, autor_id |
| `ExcluirCamadaUseCase` | Exclui (soft-delete) uma camada de mapa (RN-GEO-006). | camada_id |
| `CadastrarMapaUseCase` | Cadastra um mapa SIG em rascunho (RN-GEO-002). | dto |
| `AtualizarMapaUseCase` | Atualiza os dados de um mapa SIG em rascunho (RN-GEO-004). | dto |
| `ComporCamadaUseCase` | Adiciona uma camada à composição de um mapa (RN-GEO-004, RN-GEO-008). | dto |
| `RemoverComposicaoUseCase` | Remove uma camada da composição de um mapa (RN-GEO-004). | vinculo_id |
| `PublicarMapaUseCase` | Publica o mapa SIG no geoportal (RN-GEO-004). | mapa_id, autor_id |
| `ArquivarMapaUseCase` | Arquiva um mapa publicado, retirando-o do geoportal (RN-GEO-004). | mapa_id, autor_id |
| `ExcluirMapaUseCase` | Exclui (soft-delete) um mapa SIG em rascunho ou arquivado (RN-GEO-004). | mapa_id |
| `RegistrarFeatureUseCase` | Registra um elemento geoespacial em uma camada cadastrada. | dto |
| `ExcluirFeatureUseCase` | Exclui (soft-delete) um elemento geoespacial. | feature_id |
| `CadastrarServicoUseCase` | Cadastra um serviço geoespacial no geoportal (RN-GEO-007). | dto |
| `AtualizarServicoUseCase` | Atualiza o cadastro de um serviço geoespacial. | dto |
| `InativarServicoUseCase` | Inativa um serviço geoespacial (RN-GEO-007). | servico_id, autor_id |
| `ExcluirServicoUseCase` | Exclui (soft-delete) um serviço geoespacial. | servico_id |

---

# 4. Registração da Aplicação

* O router é registrado em `src/main.py`.
* O prefixo publicado é `/api/v1/geo`.
* A migração é `alembic/versions/20260929_03_dom_geo_models.py`.

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

**Documento:** 025-Estrutura-Tecnica-Geoinformacao-Municipal.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_geoinformacao`. Alterações no código devem ser
> refletidas reexecutando o gerador.
