# 009 – Requisitos Não Funcionais – Gestão Territorial

#### Requisitos Não Funcionais – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-009

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

Este artefato especifica as qualidades exigidas da solução do domínio de
Gestão Territorial, com o respectivo meio de verificação.

---

# 2. Convenções

* O padrão é `RNF-<DOMÍNIO>-<sequencial>`.
* Cada requisito declara a verificação que demonstra seu atendimento.

---

# 3. Requisitos Não Funcionais

| ID | Categoria | Requisito | Verificação |
| --- | | --- | | --- | |
| RNF-TEL-001 | Desempenho | As consultas de listagem devem responder paginadas, com tamanho de página entre 1 e 100 itens. | Teste de integração verificando o parâmetro `page_size` e a resposta paginada. |
| RNF-TEL-002 | Integridade | As invariantes de unicidade e de vínculo devem ser garantidas no banco de dados, e não apenas na aplicação. | Verificação dos índices únicos parciais e da constraint `ck_tel_geo_referencia` na migração. |
| RNF-TEL-003 | Robustez | Identificadores malformados devem resultar em HTTP 404, e não em erro interno. | Round-trip E2E consultando identificadores não-UUID. |
| RNF-TEL-004 | Usabilidade | Violações de regra de negócio devem retornar mensagem descritiva com referência à regra violada. | Testes unitários verificando a mensagem de `RegraNegocioError` e a resposta HTTP 409. |
| RNF-TEL-005 | Rastreabilidade | Toda alteração deve registrar autoria (`created_by`) e data (`created_at`, `updated_at`). | Teste de integração verificando as colunas de auditoria após criação e alteração. |
| RNF-TEL-006 | Compatibilidade | A API deve manter contrato estável, versionado sob o prefixo `/api/v1/tel`. | Verificação do OpenAPI publicado e da contagem de paths e operações. |
| RNF-TEL-007 | Desacoplamento | O domínio não deve manter chave estrangeira física para outros bancos de domínios. | Inspeção da migração: nenhuma FK entre schemas; referências por identificador opaco. |


---

# 4. Categorias

| Categoria | Requisitos |
| --- | |
| Compatibilidade | RNF-TEL-006 |
| Desacoplamento | RNF-TEL-007 |
| Desempenho | RNF-TEL-001 |
| Integridade | RNF-TEL-002 |
| Rastreabilidade | RNF-TEL-005 |
| Robustez | RNF-TEL-003 |
| Usabilidade | RNF-TEL-004 |


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

**Documento:** 009-Requisitos-Nao-Funcionais-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
