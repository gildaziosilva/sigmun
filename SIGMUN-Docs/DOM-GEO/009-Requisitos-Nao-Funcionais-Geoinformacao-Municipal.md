# 009 – Requisitos Não Funcionais – Geoinformação Municipal

#### Requisitos Não Funcionais – Geoinformação Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GEO-009

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

Este artefato especifica as qualidades exigidas da solução do domínio de
Geoinformação Municipal, com o respectivo meio de verificação.

---

# 2. Convenções

* O padrão é `RNF-<DOMÍNIO>-<sequencial>`.
* Cada requisito declara a verificação que demonstra seu atendimento.

---

# 3. Requisitos Não Funcionais

| ID | Categoria | Requisito | Verificação |
| --- | | --- | | --- | |
| RNF-GEO-001 | Desempenho | As consultas de listagem devem responder paginadas, com tamanho de página entre 1 e 100 itens. | Teste de integração verificando o parâmetro `page_size` e a resposta paginada. |
| RNF-GEO-002 | Integridade | As invariantes de geometria, ciclo de vida e unicidade devem ser garantidas no banco de dados, e não apenas na aplicação. | Verificação dos 10 CHECK constraints e dos índices únicos parciais nas migrações do schema `geo`. |
| RNF-GEO-003 | Robustez | Identificadores malformados devem resultar em HTTP 404, e não em erro interno. | Round-trip E2E consultando identificadores não-UUID. |
| RNF-GEO-004 | Usabilidade | Violações de regra de negócio devem retornar mensagem descritiva com referência à regra violada. | Testes unitários verificando a mensagem de `RegraNegocioError` e a resposta HTTP 409. |
| RNF-GEO-005 | Rastreabilidade | Toda alteração deve registrar autoria (`created_by`) e data (`created_at`, `updated_at`). | Teste de integração verificando as colunas de auditoria após criação e alteração. |
| RNF-GEO-006 | Compatibilidade | A API deve manter contrato estável, versionado sob o prefixo `/api/v1/geo`. | Verificação do OpenAPI publicado e da contagem de 16 paths e 28 operações. |
| RNF-GEO-007 | Desacoplamento | O domínio não deve manter chave estrangeira física para outros bancos de domínios. | Inspeção da migração: nenhuma FK entre schemas; referências por identificador opaco. |
| RNF-GEO-008 | Interoperabilidade | O cadastro deve admitir os datuns e formatos de serviço usuais no geoportal municipal. | Testes unitários cobrindo datuns (`sirgas2000`, `sad69`, `wgs84`) e formatos de serviço. |


---

# 4. Categorias

| Categoria | Requisitos |
| --- | |
| Compatibilidade | RNF-GEO-006 |
| Desacoplamento | RNF-GEO-007 |
| Desempenho | RNF-GEO-001 |
| Integridade | RNF-GEO-002 |
| Interoperabilidade | RNF-GEO-008 |
| Rastreabilidade | RNF-GEO-005 |
| Robustez | RNF-GEO-003 |
| Usabilidade | RNF-GEO-004 |


---

# 5. Evidências de Verificação

* `npx tsc --noEmit` e `npm run build` no frontend administrativo.
* `ruff check` e `mypy` sobre o módulo de aplicação.
* Suíte `pytest tests/` do repositório.
* Round-trip E2E sobre PostgreSQL para as operações de escrita e leitura.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 009-Requisitos-Nao-Funcionais-Geoinformacao-Municipal.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_geoinformacao`. Alterações no código devem ser
> refletidas reexecutando o gerador.
