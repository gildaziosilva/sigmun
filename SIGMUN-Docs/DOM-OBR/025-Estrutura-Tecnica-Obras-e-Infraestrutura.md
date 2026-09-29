# 025 – Estrutura Técnica – Obras e Infraestrutura

#### Estrutura Técnica – Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OBR-025

**Domínio:** Obras e Infraestrutura

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Obras-e-Infraestrutura.md`
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

Este artefato descreve a estrutura técnica do módulo `sigmun_obras` e seus componentes
implementados.

---

# 2. Árvore de Módulos

| Camada | Caminho | Responsabilidade |
| --- | --- | --- |
| Domínio | `src/modules/sigmun_obras/domain/entities` | Entidades, invariantes e enums |
| Domínio | `src/modules/sigmun_obras/domain/exceptions.py` | Exceções de negócio |
| Aplicação | `src/modules/sigmun_obras/application/interfaces.py` | Ports de repositório |
| Aplicação | `src/modules/sigmun_obras/application/use_cases*.py` | Casos de uso |
| Infraestrutura | `src/modules/sigmun_obras/infrastructure/database/models.py` | Modelos ORM (schema `obr`) |
| Infraestrutura | `src/modules/sigmun_obras/infrastructure/database/seeds*.py` | Seed DEMO |
| Infraestrutura | `src/modules/sigmun_obras/infrastructure/repositories/` | Adaptadores SQLAlchemy |
| Apresentação | `src/modules/sigmun_obras/presentation/schemas/` | Schemas Pydantic |
| Apresentação | `src/modules/sigmun_obras/presentation/api/` | Endpoints e dependências |

---

# 3. Casos de Uso Implementados

| Caso de uso | Descrição | `execute(...)` |
| --- | --- | --- |
| `CadastrarObraUseCase` | Cadastra uma obra pública em situação PLANEJADA (RN-OBR-001). | dto |
| `AtualizarObraUseCase` | Atualiza os dados cadastrais de uma obra não concluída (RN-OBR-002). | dto |
| `IniciarExecucaoObraUseCase` | Inicia a execução física da obra (RN-OBR-002, RN-OBR-003). | obra_id, data, autor_id |
| `ConcluirObraUseCase` | Conclui a obra, exigindo 100% do avanço físico (RN-OBR-005). | obra_id, data, autor_id |
| `SuspenderObraUseCase` | Suspende a execução da obra (RN-OBR-002). | obra_id, motivo, autor_id |
| `CancelarObraUseCase` | Cancela a obra (RN-OBR-002). | obra_id, motivo, autor_id |
| `ExcluirObraUseCase` | Exclui (soft-delete) uma obra sem dependências financeiras (RN-OBR-006). | obra_id |
| `RegistrarMedicaoUseCase` | Registra uma medição de avanço em obra em execução (RN-OBR-005). | dto |
| `AprovarMedicaoUseCase` | Aprova a medição e recompõe o avanço da obra (RN-OBR-005). | medicao_id, autor_id |
| `GlosarMedicaoUseCase` | Glosa uma medição conferida (RN-OBR-005). | medicao_id, motivo, autor_id |
| `CancelarMedicaoUseCase` | Cancela uma medição não aprovada (RN-OBR-005). | medicao_id, motivo, autor_id |
| `RegistrarDespesaUseCase` | Registra a despesa e recompõe o avanço financeiro da obra (RN-OBR-006). | dto |
| `ExcluirDespesaUseCase` | Exclui (soft-delete) uma despesa e recompõe o avanço da obra. | despesa_id |
| `CadastrarEtapaUseCase` | Cadastra uma etapa de execução em uma obra existente (RN-OBR-007). | dto |
| `AtualizarEtapaUseCase` | Atualiza o avanço físico de uma etapa (RN-OBR-007). | etapa_id, percentual_realizado, situacao, autor_id |
| `ConcluirEtapaUseCase` | Conclui uma etapa, exigindo 100% do previsto (RN-OBR-007). | etapa_id, data |
| `RegistrarVistoriaUseCase` | Registra a vistoria de avanço físico na obra (RN-OBR-008). | dto |

---

# 4. Registração da Aplicação

* O router é registrado em `src/main.py`.
* O prefixo publicado é `/api/v1/obr`.
* A migração é `alembic/versions/20260929_04_dom_obr_models.py`.

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

**Documento:** 025-Estrutura-Tecnica-Obras-e-Infraestrutura.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_obras`. Alterações no código devem ser
> refletidas reexecutando o gerador.
