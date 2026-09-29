# 025 – Estrutura Técnica – Cadastro Imobiliário

#### Estrutura Técnica – Cadastro Imobiliário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IMO-025

**Domínio:** Cadastro Imobiliário

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Cadastro-Imobiliario.md`
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

Este artefato descreve a estrutura técnica do módulo `sigmun_cadastro_imobiliario` e seus componentes
implementados.

---

# 2. Árvore de Módulos

| Camada | Caminho | Responsabilidade |
| --- | --- | --- |
| Domínio | `src/modules/sigmun_cadastro_imobiliario/domain/entities` | Entidades, invariantes e enums |
| Domínio | `src/modules/sigmun_cadastro_imobiliario/domain/exceptions.py` | Exceções de negócio |
| Aplicação | `src/modules/sigmun_cadastro_imobiliario/application/interfaces.py` | Ports de repositório |
| Aplicação | `src/modules/sigmun_cadastro_imobiliario/application/use_cases*.py` | Casos de uso |
| Infraestrutura | `src/modules/sigmun_cadastro_imobiliario/infrastructure/database/models.py` | Modelos ORM (schema `imo`) |
| Infraestrutura | `src/modules/sigmun_cadastro_imobiliario/infrastructure/database/seeds*.py` | Seed DEMO |
| Infraestrutura | `src/modules/sigmun_cadastro_imobiliario/infrastructure/repositories/` | Adaptadores SQLAlchemy |
| Apresentação | `src/modules/sigmun_cadastro_imobiliario/presentation/schemas/` | Schemas Pydantic |
| Apresentação | `src/modules/sigmun_cadastro_imobiliario/presentation/api/` | Endpoints e dependências |

---

# 3. Casos de Uso Implementados

| Caso de uso | Descrição | `execute(...)` |
| --- | --- | --- |
| `CadastrarImovelUseCase` | Cadastra uma unidade imobiliária (RN-IMO-001/002). | dto |
| `AtualizarImovelUseCase` | Atualiza o cadastro de uma unidade imobiliária (RN-IMO-003). | dto |
| `AlterarSituacaoImovelUseCase` | Altera a situação do imóvel respeitando a máquina de estados (RN-IMO-004). | imovel_id, situacao |
| `ExcluirImovelUseCase` | Exclui (soft-delete) uma unidade imobiliária (RN-IMO-003). | imovel_id |
| `VincularProprietarioUseCase` | Vincula um proprietário à unidade imobiliária (RN-IMO-006). | dto |
| `RemoverProprietarioUseCase` | Remove o vínculo de propriedade de uma unidade imobiliária (RN-IMO-006). | vinculo_id |
| `AvaliarImovelUseCase` | Avalia o imóvel aplicando os valores unitários vigentes (RN-IMO-005). | dto |
| `ConcluirAvaliacaoUseCase` | Conclui uma avaliação em rascunho (RN-IMO-005). | avaliacao_id |
| `CancelarAvaliacaoUseCase` | Cancela uma avaliação ainda não concluída (RN-IMO-005). | avaliacao_id, motivo |
| `RegistrarCaracteristicaUseCase` | Registra a característica construtiva vigente do imóvel. | dto |
| `RegistrarGeometriaUseCase` | Registra a geometria georreferenciada do lote (RN-IMO-007). | dto |

---

# 4. Registração da Aplicação

* O router é registrado em `src/main.py`.
* O prefixo publicado é `/api/v1/imo`.
* A migração é `alembic/versions/20260929_02_dom_imo_models.py`.

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

**Documento:** 025-Estrutura-Tecnica-Cadastro-Imobiliario.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_cadastro_imobiliario`. Alterações no código devem ser
> refletidas reexecutando o gerador.
