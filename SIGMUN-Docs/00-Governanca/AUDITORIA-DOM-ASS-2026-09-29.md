# AUDITORIA — DOM-ASS (ASSISTÊNCIA SOCIAL) — 2026-09-29

**Classificação da Informação:** Pública
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
**Data:** 2026-09-29
**Domínio:** DOM-ASS — Assistência Social
**Módulo:** `sigmun_assistencia_social` (schema `ass`)
**Commit auditado:** `33d53da` — *feat(ass): implementa DOM-ASS (CadUnico local, beneficios eventuais, CRAS/CREAS)*
**Tipo:** Auditoria técnica de código, persistência, qualidade estática e documentação
**Status da auditoria:** Concluída — achados corrigidos

---

## 1. Objetivo

Auditar o domínio DOM-ASS em todas as camadas verificáveis (domínio, aplicação, infraestrutura, apresentação, persistência, testes, qualidade estática e documentação), confirmar as evidências declaradas no commit `33d53da` e corrigir as divergências encontradas.

A auditoria **não** alterou o escopo funcional do domínio: nenhuma entidade, regra de negócio, caso de uso, endpoint ou contrato de API foi criado ou removido.

---

## 2. Escopo e método

| Item | Verificação |
| --- | --- |
| Suíte unitária | `pytest tests/unit` |
| Suíte de integração do domínio | `pytest tests/integration/test_ass_seeds.py` |
| Lint | `ruff check src/modules/sigmun_assistencia_social/` |
| Tipagem | `mypy src/modules/sigmun_assistencia_social/` |
| Persistência | `alembic heads`, `information_schema`, `pg_constraint` no PostgreSQL |
| Contrato da API | `app.openapi()` filtrado por `/api/v1/ass` |
| Comportamento | round-trip E2E pelos casos de uso reais, com commit e releitura |

---

## 3. Achados e correções

### 3.1 Divergência ORM × migration em `beneficios_eventuais.quantidade` — **Corrigido**

O modelo ORM declarava a coluna `quantidade` como `Text`, enquanto a migration
`20260927_01_dom_ass_models` e a coluna física no PostgreSQL são `integer`.

O repositório compensava a inconsistência com coerções explícitas
(`quantidade=str(...)` na escrita e `int(model.quantidade or 1)` na leitura),
o que **mascarava** a divergência e fixava `1` como valor padrão silencioso
para quantidades ausentes.

- **Correção:** `Mapped[int]` no ORM, coerções `str()` removidas.
- **Evidência:** comparação col a col entre `Base.metadata` e `information_schema`
  não reporta mais divergência em `quantidade`.
- **Verificação:** round-trip E2E retorna `quantidade = 7` (`int`) após commit e releitura.

### 3.2 Truncamento silencioso de data em `atendimentos_sociais.data` — **Corrigido**

`AtendimentoSocial.data` era anotada como `datetime`, mas a coluna é `DATE` e os
schemas Pydantic (`AtendimentoCreateRequest`, `AtendimentoResponse`) já usavam `date`.
Ao gravar, o PostgreSQL **truncava a hora sem erro**:

```text
datetime(2026, 9, 29, 13, 45) -> date(2026, 9, 29)
```

- **Correção:** entidade tipada como `date`, com `date.today()` como padrão;
  `RegistrarAtendimentoUseCase` deixou de gravar `datetime.utcnow()`.
- **Verificação:** `mypy` não reporta mais `arg-type` em `AtendimentoSocial.data`;
  round-trip E2E retorna `date(2026, 9, 29)`.

### 3.3 Docstring da RN-ASS-003 divergente da implementação — **Corrigido**

O cabeçalho de `domain/entities` descrevia RN-ASS-003 como *"benefícios eventuais
têm estoque controlado por tipo"*, mas **não existe controle de estoque** no domínio.
O que a regra realmente implementa é a máquina de estados
`SOLICITADO → APROVADO | NEGADO → ENTREGUE`, com `CANCELADO` antes da entrega.

- **Correção:** docstring reescrita para refletir a regra implementada.
- **Observação:** `EstoqueInsuficienteError` permanece em `exceptions.py` sem uso —
  mantido por compatibilidade de superfície, sem decisão sobre remoção.

### 3.4 Perda de encadeamento de exceções (B904) — **Corrigido**

Os 31 `raise HTTPException(...)` dentro de blocos `except` não encadeavam a
exceção original, apagando a causa raiz em logs e rastreabilidade.

- **Correção:** `raise ... from exc` em todos os 31 pontos, adicionando
  `as exc` onde faltava.

### 3.5 Comparações `== False` com `# noqa` inoperante (E712) — **Corrigido**

As 7 comparações usavam `== False` com `# noqa: E712` posicionado na linha do
fechamento da chamada — local onde a diretiva **não** suprime o erro.

- **Correção:** adoção de `.is_(False)`, forma correta no SQLAlchemy 2.0;
  diretivas `noqa` inoperantes removidas.

### 3.6 Documentação desatualizada do módulo — **Corrigido**

`SIGMUN-Docs/05-Modulos/sigmun_assistencia_social/index.md` afirmava
*"apenas scaffolding"*, *"Nenhum router registrado"* e *"Nenhum teste encontrado"* —
afirmações contrariadas pela implementação entregue em `33d53da`.
O catálogo `05-Modulos/index.md` e a matriz `031-Matriz-de-Correspondencia-DOM-MOD.md`
também classificavam o módulo como *Preparado*.

---

## 4. Evidências de verificação

| Gate | Antes (2026-09-28) | Depois (2026-09-29) |
| --- | --- | --- |
| `ruff check` (módulo DOM-ASS) | 137 erros | **All checks passed** |
| `mypy` (módulo DOM-ASS) | 155 erros em 5 arquivos | **Success: no issues found in 18 source files** |
| `pytest tests/unit` | 651 passed | 651 passed |
| `pytest tests/integration/test_ass_seeds.py` | 5 passed | 5 passed |
| Head Alembic | `20260927_01_dom_ass_models` | `20260927_01_dom_ass_models` (único) |

Verificações complementares:

- **Contrato da API:** 20 paths e 31 operações em `/api/v1/ass` (inalterado).
- **Persistência:** ORM × `information_schema` sem divergência estrutural;
  as 15 diferenças restantes são aliases de tipo equivalentes
  (`DATETIME`≡`TIMESTAMP`, `FLOAT`≡`DOUBLE PRECISION`).
- **Round-trip E2E** com commit e releitura: `quantidade` preservada como `int`,
  `data` preservada como `date`, benefício chegando a `entregue`.

---

## 5. Achados não corrigidos (fora do escopo do DOM-ASS)

Registrados para o backlog; **não** foram tratados nesta auditoria por serem
dívidas preexistentes e transversais a todo o repositório:

1. **Dívida global de qualidade estática** — `make lint` e `make type-check`
   permanecem vermelhos no conjunto de `src/` e `tests/`, por módulos não
   relacionados ao DOM-ASS. O commit `33d53da` declarava apenas o gate
   reduzido `ruff --select E9,F821,F401`, que permanece limpo.
2. **Ausência de chaves estrangeiras no schema `ass`** — `familia_id`,
   `pessoa_id` e `unidade_id` são `Text` sem FK. Trata-se da convenção
   vigente em todo o repositório (só `sigmun_con`, `sigmun_dad` e `sigmun_orc`
   declaram FK), e a sua adoção isolada no DOM-ASS exigiria decisão de arquitetura.
3. **Diretórios `puml/` não rastreados** — 36 diretórios; apenas
   `00-Governanca` (11 arquivos) e `DOM-DIA` (5) têm conteúdo. Higiene do repositório.
4. **Artefatos documentais `DOM-ASS/001`–`026` em esboço** — situação
   compartilhada com `DOM-EDU` e demais domínios; o preenchimento do conteúdo
   não faz parte do escopo desta auditoria técnica.

---

## 6. Conclusão

O módulo `sigmun_assistencia_social` está **funcional e consistente**: as duas
divergências de tipo encontradas entre domínio, ORM e banco foram corrigidas na
origem, o encadeamento de exceções foi restaurado e a documentação foi alinhada
ao estado real da implementação. O módulo passa a qualidade limpa nos gates de
lint e tipagem, sem qualquer regressão na suíte de testes.

**Ressalva de escopo:** a promoção da correspondência `MOD-ASS` de *candidata*
para *confirmada* **não** foi realizada, por depender da conciliação dos
artefatos documentais `DOM-ASS/001`–`026`, que permanecem em esboço.

---

*Auditoria registrada pela Equipe de Desenvolvimento do SIGMUN.*
*Regra de governança: tarefa concluída somente com evidência técnica e documental.*


- **Correção:** índice do módulo reescrito com escopo, endpoints, testes e
  qualidade estática verificados; maturidade atualizada para *Implementação
  identificada* no catálogo e na matriz.
