# FAZER.md — Plano de Correções e Evolução do SIGMUN

> **Projeto:** SIGMUN — Sistema Integrado de Gestão Municipal (Prefeitura de Camacan-BA)
> **Data da auditoria:** 2026-09-28
> **Commit auditado:** `33d53da` — *feat(ass): implementa DOM-ASS (CadUnico local, beneficios eventuais, CRAS/CREAS)*
> **Escopo:** auditoria completa do repositório `sigmun-v1/` em todas as camadas
> (código, testes, qualidade estática, banco/migrações, segurança, CI/CD, frontend, mobile, documentação, higiene do repositório).

Este documento **não substitui** o `TODO.md` (backlog funcional de produto). Ele consolida o que foi
**verificado empiricamente** nesta auditoria e que está **incorreto, quebrado, ausente ou divergente**.

> ⚠️ **Regra de ouro deste documento:** nenhuma tarefa aqui pode ser marcada como concluída sem o
> respective **comando de verificação** (seção 2) sendo executado com sucesso.

---

## 1. Resumo Executivo — Saúde por Camada

| # | Camada | Volume | Estado | Diagnóstico resumido |
|---|--------|--------|--------|---------------------|
| 1 | Código backend | 820 arquivos `.py` (~60.254 LOC) | 🟡 | Funcional, mas 14 de 18 módulos sem autenticação |
| 2 | API (OpenAPI) | 245 paths / 364 rotas declaradas | 🟡 | Contratos de paginação inconsistentes entre módulos |
| 3 | Testes | 887 passed, 1 skipped | 🟠 | Passa em série, **falha sob concorrência** (banco compartilhado) |
| 4 | Qualidade — Ruff | — | 🔴 | **953 erros** (`make lint` falha) |
| 5 | Tipagem — Mypy | — | 🔴 | **1.166 erros em 90 arquivos** (`make type-check` falha) |
| 6 | Banco / Migrações | 36 migrações, 1 head | 🟢 | Cadeia íntegra, FKs presentes, HEAD único |
| 7 | Segurança | — | 🔴 | Sem auth em 14 módulos; CORS `*`; `SECRET_KEY` padrão fraco |
| 8 | CI/CD | 2 workflows | 🔴 | CI vermelho; **CD nunca executa nenhum deploy** |
| 9 | Frontend admin | 52 arquivos `.ts/.tsx` | 🟡 | `tsc` limpo; 32 warnings oxlint; sem testes |
| 10 | Mobile | 4 apps | 🔴 | Apenas `src/.gitkeep` — nenhum código |
| 11 | Documentação | 1.166 `.md` (9,2 MB) | 🟠 | Rica, porém `TODO.md` e `divergencias` desatualizados |
| 12 | Higiene do repo | 2.298 arquivos rastreados | 🟠 | 36 diretórios `puml/` não rastreados; 1,4 MB de lixo na raiz |

### 1.1 Divergência mais grave: Quality Gates documentados como verdes estão vermelhos

O `TODO.md` (Fase II, itens `II.1`, `II.2`, `II.3`) declara as tarefas como **concluídas (✅)** e afirma:

> *"`make lint` → `ruff check src/ tests/` → **"All checks passed!"** (0 violações)"*
> *"`make type-check` → `mypy src/` → **"Success: no issues found in 584 source files"**"*
> *"suíte completa **520 passed**"*

**Estado real medido hoje:**

| Gate | Afirmado no `TODO.md` | Real (2026-09-28) | Δ |
|------|----------------------|--------------------|---|
| `ruff check src/ tests/` | ✅ 0 violações | 🔴 **953 erros** | +953 |
| `mypy src/` | ✅ 0 issues | 🔴 **1.166 erros** (90 arquivos) | +1166 |
| `pytest tests/` | ✅ 520 passed | 🟡 887 passed, 1 skipped | +367 testes |

Como o `.github/workflows/ci.yml` executa `ruff` e `mypy` **antes** dos testes, **o pipeline está
vermelho desde o último commit**. Nenhum PR pode ser aprovado.

**Distribuição dos 953 erros do Ruff:**

| Código | Qtd. | Significado | Autocorrectável |
|--------|------|-------------|------------------|
| E501 | 399 | line-too-long | ❌ |
| E702 | 200 | múltiplos statements em uma linha (`;`) | ❌ |
| B904 | 133 | `raise` sem `from` dentro de `except` | ❌ |
| I001 | 61 | imports fora de ordem | ✅ |
| W292 | 45 | falta newline no fim do arquivo | ✅ |
| W293 | 37 | linha em branco com espaços | ⚠️ parcial |
| F401 | 23 | import não utilizado | ⚠️ parcial |
| E712 | 20 | comparação com `True`/`False` | ❌ |
| UP045 | 11 | `Optional[X]` em vez de `X \| None` | ✅ |
| E741 | 8 | nome ambíguo (`l`, `I`, `O`) | ❌ |
| B017 | 4 | `pytest.raises(Exception)` | ❌ |
| F541 | 3 | f-string sem placeholder | ✅ |
| SIM117 | 3 | `with` aninhados combináveis | ✅ |
| F841 | 2 | variável não utilizada | ❌ |
| SIM102 | 1 | `if` aninhado colapsável | ✅ |
| E402 | 1 | import fora do topo do arquivo | ❌ |
| F811 | 1 | redefinition | ❌ |
| C416 | 1 | compreensão desnecessária | ✅ |

**Distribuição dos 1.166 erros do Mypy:**

| Código | Qtd. | Interpretação |
|--------|------|---------------|
| `arg-type` | 392 | `Column[X] \| X` passado para entidade que espera `X` (padrão de repositórios) |
| `assignment` | 328 | idem, em atribuições |
| `no-untyped-def` | 225 | funções sem anotação de retorno |
| `no-any-return` | 117 | retorno de `Any` não permitido (`warn_return_any`) |
| `valid-type` | 41 | anotações inválidas |
| `misc` | 41 | diversos |
| `abstract` | 9 | métodos abstratos não implementados |
| `attr-defined` | 8 | atributo inexistente |
| `call-arg` | 3 | argumentos incompatíveis |
| `index` | 1 | erro de indexação |
| `import-untyped` | 1 | import sem stubs |

---
