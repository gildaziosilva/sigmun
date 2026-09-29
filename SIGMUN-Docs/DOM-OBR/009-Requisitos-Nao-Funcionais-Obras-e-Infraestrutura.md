# 009 – Requisitos Não Funcionais – Obras e Infraestrutura

#### Requisitos Não Funcionais – Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OBR-009

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

Este artefato especifica as qualidades exigidas da solução do domínio de
Obras e Infraestrutura, com o respectivo meio de verificação.

---

# 2. Convenções

* O padrão é `RNF-<DOMÍNIO>-<sequencial>`.
* Cada requisito declara a verificação que demonstra seu atendimento.

---

# 3. Requisitos Não Funcionais

| ID | Categoria | Requisito | Verificação |
| --- | | --- | | --- | |
| RNF-OBR-001 | Desempenho | As consultas de listagem devem responder paginadas, com tamanho de página entre 1 e 100 itens. | Teste de integração verificando o parâmetro `page_size` e a resposta paginada. |
| RNF-OBR-002 | Integridade | A coerência físico-financeira e a unicidade devem ser garantidas no banco de dados, e não apenas na aplicação. | Verificação dos 7 CHECK constraints e do índice único parcial `uq_obr_medicao_numero` nas migrações do schema `obr`. |
| RNF-OBR-003 | Robustez | Identificadores malformados devem resultar em HTTP 404, e não em erro interno. | Round-trip E2E consultando identificadores não-UUID. |
| RNF-OBR-004 | Usabilidade | Violações de regra de negócio devem retornar mensagem descritiva com referência à regra violada. | Testes unitários verificando a mensagem de `RegraNegocioError` e a resposta HTTP 409. |
| RNF-OBR-005 | Rastreabilidade | Toda medição, despesa, etapa e vistoria deve estar vinculada a uma obra existente e registrar autoria e data. | Testes unitários e de integração verificando as referências e as colunas de auditoria. |
| RNF-OBR-006 | Compatibilidade | A API deve manter contrato estável, versionado sob o prefixo `/api/v1/obr`. | Verificação do OpenAPI publicado e da contagem de 21 paths e 24 operações. |
| RNF-OBR-007 | Desacoplamento | O domínio não deve manter chave estrangeira física para outros bancos de domínios. | Inspeção da migração: nenhuma FK entre schemas; referências por identificador opaco. |
| RNF-OBR-008 | Consistência do recálculo | O avanço físico e financeiro da obra deve ser sempre recomposto a partir das medições aprovadas e das despesas registradas. | Round-trip E2E comparando os valores da obra com a soma das medições aprovadas e das despesas. |


---

# 4. Categorias

| Categoria | Requisitos |
| --- | |
| Compatibilidade | RNF-OBR-006 |
| Consistência do recálculo | RNF-OBR-008 |
| Desacoplamento | RNF-OBR-007 |
| Desempenho | RNF-OBR-001 |
| Integridade | RNF-OBR-002 |
| Rastreabilidade | RNF-OBR-005 |
| Robustez | RNF-OBR-003 |
| Usabilidade | RNF-OBR-004 |


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

**Documento:** 009-Requisitos-Nao-Funcionais-Obras-e-Infraestrutura.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_obras`. Alterações no código devem ser
> refletidas reexecutando o gerador.
