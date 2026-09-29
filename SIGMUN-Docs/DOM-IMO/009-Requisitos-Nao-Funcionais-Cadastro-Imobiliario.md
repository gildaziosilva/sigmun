# 009 – Requisitos Não Funcionais – Cadastro Imobiliário

#### Requisitos Não Funcionais – Cadastro Imobiliário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IMO-009

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

Este artefato especifica as qualidades exigidas da solução do domínio de
Cadastro Imobiliário, com o respectivo meio de verificação.

---

# 2. Convenções

* O padrão é `RNF-<DOMÍNIO>-<sequencial>`.
* Cada requisito declara a verificação que demonstra seu atendimento.

---

# 3. Requisitos Não Funcionais

| ID | Categoria | Requisito | Verificação |
| --- | | --- | | --- | |
| RNF-IMO-001 | Desempenho | As consultas de listagem devem responder paginadas, com tamanho de página entre 1 e 100 itens. | Teste de integração verificando o parâmetro `page_size` e a resposta paginada. |
| RNF-IMO-002 | Integridade | As invariantes de inscrição, titularidade principal, avaliação e geometria devem ser garantidas no banco de dados. | Verificação dos índices `uq_imo_avaliacao_exercicio`, `uq_imo_titular_principal` e `uq_imo_geometria_lote`. |
| RNF-IMO-003 | Desacoplamento | O domínio não deve manter chave estrangeira física para o banco do DOM-TEL; o contrato é resolvido por API. | Inspeção da migração e do port `ConsultaPlantaValores`. |
| RNF-IMO-004 | Robustez | Identificadores malformados devem resultar em HTTP 404, e não em erro interno. | Round-trip E2E consultando identificadores não-UUID. |
| RNF-IMO-005 | Rastreabilidade | Toda alteração deve registrar autoria e data; avaliações preservam a memória por exercício. | Teste de integração verificando as colunas de auditoria e a coexistência de avaliações por ano. |
| RNF-IMO-006 | Precisão numérica | Os valores monetários devem ser gravados e retornados com duas casas decimais. | Round-trip E2E do cálculo do valor venal e do lançamento estimado. |
| RNF-IMO-007 | Compatibilidade | A API deve manter contrato estável, versionado sob o prefixo `/api/v1/imo`. | Verificação do OpenAPI publicado e da contagem de paths e operações. |


---

# 4. Categorias

| Categoria | Requisitos |
| --- | |
| Compatibilidade | RNF-IMO-007 |
| Desacoplamento | RNF-IMO-003 |
| Desempenho | RNF-IMO-001 |
| Integridade | RNF-IMO-002 |
| Precisão numérica | RNF-IMO-006 |
| Rastreabilidade | RNF-IMO-005 |
| Robustez | RNF-IMO-004 |


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

**Documento:** 009-Requisitos-Nao-Funcionais-Cadastro-Imobiliario.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_cadastro_imobiliario`. Alterações no código devem ser
> refletidas reexecutando o gerador.
