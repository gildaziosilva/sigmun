# AUDITORIA — DOM-ATE (ATENDIMENTO AO CIDADÃO) — 2026-09-29

**Classificação da Informação:** Pública
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
**Data:** 2026-09-29
**Domínio:** DOM-ATE — Atendimento Presencial e Online
**Módulo previsto:** `sigmun_ate` (schema `ate`) — **não implementado**
**Tipo:** Auditoria de reconciliação entre modelo proposto, código e banco
**Status da auditoria:** Aprovada em 2026-09-29 — reconciliação documental autorizada

---

## 1. Objetivo

Reconciliar o modelo de persistência **proposto** em `SIGMUN-Docs/DOM-ATE/puml/` com o
estado real do **código** e do **banco de dados**, antes de qualquer implementação, e
registrar as divergências que exigem decisão.

Este documento **não** afirma que o DOM-ATE esteja implementado. Ao contrário: fixa o que
está apenas proposto e o que ainda não existe.

---

## 2. Os três estratos

A distinção abaixo é o eixo central desta auditoria. Confundi-los é o risco que se quer
evitar: um PUML bem desenhado **não** é evidência de código, e código **não** é evidência
de banco aplicado.

| # | Estrato | Evidência | Estado |
| --- | --- | --- | --- |
| 1 | **Modelo PUML proposto** | `SIGMUN-Docs/DOM-ATE/puml/` — 6 diagramas, 14.070 bytes | Existe |
| 2 | **Modelo implementado (código)** | `src/modules/sigmun_ate/`, migração, router, testes | Inexistente |
| 3 | **Modelo físico (PostgreSQL)** | schema `ate` | Inexistente |

### 2.1 Evidência do estrato 1 — PUML proposto

| Arquivo | Bytes | Conteúdo |
| --- | --- | --- |
| `000-Visao-Arquitetural.puml` | 1.857 | Componentes e fluxo macro |
| `001-Modelo-de-Dominio.puml` | 2.455 | 11 classes de domínio |
| `002-DOM-ATE-Fluxo-de-Atendimento.puml` | 1.589 | Fluxo presencial e online |
| `003-Maquina-de-Estados.puml` | 1.619 | 8 estados da senha |
| `004-Integracoes.puml` | 2.884 | Integrações com IDN, GDO, domínios especializados |
| `005-Persistencia.puml` | 3.666 | 11 tabelas no schema `ate` |

### 2.2 Evidência do estrato 2 — nada implementado

| Verificação | Comando | Resultado |
| --- | --- | --- |
| Módulo | `ls src/modules/ \| grep ate` | não existe |
| Migração | `ls alembic/versions/ \| grep ate` | nenhuma |
| Banco | `alembic current` | `20260929_04_dom_obr_models (head)` |
| Artefatos | `SIGMUN-Docs/DOM-ATE/001`–`026` | 26 esboços padronizados |
| Catálogo | `05-Modulos/` | sem entrada para DOM-ATE |
| Matriz DOM↔MOD | `031-Matriz-de-Correspondencia-DOM-MOD.md` | sem linha para DOM-ATE |

### 2.3 Evidência do estrato 3 — schema inexistente no PostgreSQL

```sql
select nspname from pg_namespace where nspname = 'ate';
-- 0 linhas
```

Busca por tabelas de nome semelhante retorna apenas `ass.atendimentos_sociais` e
`sau.atendimentos`, que pertencem a outros domínios e **não** são o DOM-ATE.

**Conclusão:** o DOM-ATE está **integralmente na fase documental**. Não há risco de
divergência entre código e banco, porque não existe nenhum dos dois.

---

## 3. Divergências entre o PUML e a convenção vigente

Comparação do PUML contra o que foi medido nos quatro domínios territoriais já
implementados (`tel`, `imo`, `geo`, `obr`), que são a referência arquitetural vigente.

Cada divergência traz: o que o PUML propõe, o que a convenção exige, a evidência e o
impacto. **Nenhuma correção foi aplicada** — este documento apenas registra.

### D1 — Chaves estrangeiras físicas

| | |
| --- | --- |
| **PUML** | 13 colunas marcadas `<<FK>>` e 12 relações `\|\|--o{` / `\|\|--o\|` |
| **Convenção** | Nenhuma FK física, **inclusive dentro do próprio schema** |
| **Evidência** | `grep ForeignKey` nos modelos de `geo` e `obr` → vazio |
| **Impacto** | Modelar com FK criaria um padrão distinto dos 4 domínios e dificultaria reordenar migrations futuras. Referência por identificador opaco + validação no domínio mantém a mesma garantia. |

**Resolução proposta:** manter as colunas de referência, **sem** constraint de FK,
validando a existência na camada de aplicação.

### D2 — Tipos das colunas de referência

| | |
| --- | --- |
| **PUML** | 24 colunas `UUID`, incluindo as de referência |
| **Convenção** | PK `id` = `uuid`; referências (`*_id`) = `text` |
| **Evidência** | `information_schema` em `geo`/`obr`: PKs = `uuid`; `mapa_id`, `obra_id`, `camada_id` = `text` |
| **Impacto** | Adotar `uuid` nas referências criaria dois regimes de tipo no mesmo schema. O `text` é o identificador opaco que sustenta a ausência de FK. |

**Resolução proposta:** `id` como `uuid`, referências como `text`.

### D3 — Colunas de auditoria e exclusão lógica

| | |
| --- | --- |
| **PUML** | Nenhuma das 11 tabelas declara `created_at`, `updated_at`, `created_by` ou `is_deleted` |
| **Convenção** | As 4 colunas em todas as tabelas de `geo` e `obr` |
| **Evidência** | `information_schema` → 5/5 tabelas `geo` com as 4 colunas |
| **Impacto** | Sem elas, o DOM-ATE não teria trilha de auditoria nem exclusão lógica — quebraria a rastreabilidade exigida pelo SIGMUN. |

**Resolução proposta:** adicionar as 4 colunas às 11 tabelas.

### D4 — Ausência de restrições CHECK e UNIQUE

| | |
| --- | --- |
| **PUML** | Nenhuma restrição além de PK e FK |
| **Convenção** | CHECKs nomeados para invariantes e UNIQUE para unicidade |
| **Evidência** | `geo` possui `ck_geo_mapa_zoom`, `ck_geo_feature_vertices`, `uq_geo_mapa_camada` |
| **Impacto** | As invariantes dos 4 domínios vivem em três camadas (domínio, banco, teste). O DOM-ATE ficaria apenas com a primeira. |

**Resolução proposta:** criar CHECKs para os estados da senha, faixas de prioridade, nota
de avaliação e datas de atendimento.

### D5 — Cardinalidade Triagem ↔ Senha

| | |
| --- | --- |
| **PUML** | `triagens \|\|--\|\| senhas : determina` e `Triagem "1" -- "1" Senha` — exatamente uma para uma, obrigatória |
| **Convenção/Fluxo** | O fluxo `002` mostra triagem **sem** fila, encaminhando direto ao atendimento, sem emitir senha |
| **Evidência** | `002-DOM-ATE-Fluxo`: `if (Atendimento requer fila?) then (Sim)` — no ramo "Não" não há emissão de senha |
| **Impacto** | A cardinalidade 1:1 obrigatória é **irrealizável**: uma triagem sem fila não terá senha. Também inverteria a dependência, já que é a triagem que **origina** a senha. |

**Resolução proposta:** `Triagem 0..1 → Senha`, com `senhas.triagem_id` **NOT NULL** —
a senha sempre nasce de uma triagem, mas nem toda triagem gera senha.

### D6 — Tabela `chamadas` incompleta

| | |
| --- | --- |
| **PUML (005)** | `chamadas` tem 5 colunas: `senha_id`, `guiche_id`, `data_hora`, `ordem`, `resultado` |
| **PUML (003)** | A nota da máquina de estados afirma que a chamada identifica **senha, guichê, unidade, data/hora e operador responsável** |
| **Impacto** | Faltam `unidade_id` e `operador` — dois campos que o próprio PUML exige. Sem `unidade_id`, não é possível validar que o guichê pertence à unidade correta; sem `operador`, a chamada não é atribuível. |

**Resolução proposta:** adicionar `unidade_id` e `operador` a `chamadas`.

### D7 — Estado `Rechamada` sem suporte no modelo de persistência

| | |
| --- | --- |
| **PUML (003)** | Estado `Rechamada` com a nota: *"A quantidade e o intervalo das rechamadas devem ser definidos por regra parametrizável da unidade"* |
| **PUML (005)** | Nenhum campo de rechamada, tentativa ou limite em nenhuma tabela |
| **Evidência** | `grep -i 'rechamada\|tentativa\|max_' 005-Persistencia.puml` → nenhuma ocorrência |
| **Impacto** | O estado é **inexprimível**: sem contador de tentativas não se sabe quando marcar `Ausente`, e sem limite parametrizável não há como implementar a regra descrita. É o defeito mais substantivo do PUML. |

**Resolução proposta:** adicionar `chamadas.tentativa` (contador, >= 0) e
`unidades.max_rechamadas` (limite parametrizável). Rechamada acima do limite transiciona
a senha para `Ausente`.

### D8 — Inconsistência interna: `FilaAtendimento`

| | |
| --- | --- |
| **PUML (001)** | Classe com apenas `id`, `data`, `status` |
| **PUML (005)** | Tabela com `unidade_id`, `servico_id`, `data`, `status` |
| **Impacto** | Os dois diagramas do mesmo domínio discordam. A versão de 005 é a única compatível com a regra de ordenação da máquina de estados, que depende de serviço e unidade. |

**Resolução proposta:** adotar a versão de 005 e corrigir a classe em `001`.

### D9 — `prioridade` declarada em três tabelas, sem semântica

| | |
| --- | --- |
| **PUML (005)** | `servicos.prioridade` (l. 51), `triagens.prioridade` (l. 71), `senhas.prioridade` (l. 82) |
| **Impacto** | Os três níveis são legítimos, mas **o PUML não declara a relação entre eles** nem define a faixa válida. Sem isso, a ordenação da fila fica ambígua. |

**Resolução proposta:** documentar os três níveis como *prioridade padrão do serviço* →
*prioridade atribuída pela triagem* → *prioridade efetiva de ordenação*, esta última
copiada da triagem no momento da emissão da senha. Definir faixa `>= 1` nas três.

### D10 — `canais_atendimento` sem `ativo` e sem ciclo de vida

| | |
| --- | --- |
| **PUML** | Apenas `codigo`, `nome`, `tipo` — sem `ativo`; é a única das 11 tabelas sem essa coluna |
| **Convenção** | Unidades, guichês e serviços têm `ativo`; canais são cadastrais equivalentes |
| **Impacto** | Não haveria como desativar um canal (ex.: temporariamente fora do ar) sem apagar o histórico de atendimentos. |

**Resolução proposta:** adicionar `ativo` a `canais_atendimento`.

### 3.1 Resumo das divergências

| # | Divergência | Gravidade | Origem |
| --- | --- | --- | --- |
| D1 | FKs físicas | Convenção | PUML vs 4 domínios |
| D2 | Tipo das referências (`uuid` vs `text`) | Convenção | PUML vs 4 domínios |
| D3 | Colunas de auditoria ausentes | Convenção | PUML vs 4 domínios |
| D4 | CHECK/UNIQUE ausentes | Convenção | PUML vs 4 domínios |
| D5 | Cardinalidade Triagem↔Senha 1:1 | **Alta** | Contradição interna do PUML |
| D6 | `chamadas` sem unidade e operador | **Alta** | Contradição interna do PUML |
| D7 | `Rechamada` sem suporte | **Alta** | Contradição interna do PUML |
| D8 | `FilaAtendimento` divergente | Média | Contradição interna do PUML |
| D9 | `prioridade` sem semântica | Média | Lacuna do PUML |
| D10 | Canal sem `ativo` | Baixa | Lacuna do PUML |

**D5, D6 e D7 são contradições internas do próprio PUML** — independem de qualquer
decisão sobre convenções e precisam ser corrigidas no modelo antes de codificar.

---

## 4. Decisões aprovadas

A auditoria foi **aprovada em 2026-09-29**. A implementação permanece bloqueada; o que
se autoriza é a **reconciliação do modelo proposto**.

| # | Decisão | Ação aprovada |
| --- | --- | --- |
| D1 | Aprovado | Remover FKs físicas dos PUMLs |
| D2 | Aprovado | `id` = UUID; referências = `text` |
| D3 | Aprovado | Adicionar `created_at`, `updated_at`, `created_by`, `is_deleted` |
| D4 | Aprovado | Definir CHECKs e UNIQUEs relevantes |
| D5 | Aprovado, **com ajuste** | A referência fica em `senhas.triagem_id`, não em `triagens.senha_id` |
| D6 | Aprovado | Adicionar `unidade_id` e `operador` a `chamadas` |
| D7 | Aprovado, **com melhoria** | Adicionar `tentativa` e `max_rechamadas`, com semântica de sequência |
| D8 | Aprovado | Alinhar `001` com a estrutura de `005` |
| D9 | Aprovado | Formalizar a cadeia de prioridade |
| D10 | Aprovado | Adicionar `ativo` aos canais |

### 4.1 Ajuste aprovado em D5 — posição da referência

A auditoria propôs a cardinalidade `Triagem 0..1 → Senha`, mas o PUML posicionava a
chave em `triagens.senha_id`. A decisão aprovada inverte a posição:

```text
Uma Triagem
    ├── pode não gerar senha
    └── pode gerar uma única senha

Uma Senha
    └── sempre pertence a uma Triagem
```

Com a referência em **`senhas.triagem_id : text NOT NULL`**, e **sem**
`triagens.senha_id`. A diferença é semântica: a chave passa a expressar a
**pertencimento** (toda senha nasce de uma triagem) em vez de uma referência
circular que a triagem manteria para a senha que originou.

### 4.2 Melhora aprovada em D7 — `tentativa` é sequencial por senha

Mantêm-se `unidades.max_rechamadas` e `chamadas.tentativa`, acrescendo-se a
definição de que `tentativa` é o **número sequencial da chamada da mesma senha**:

```text
Senha 001
 ├── Chamada tentativa 1
 ├── Chamada tentativa 2
 └── Chamada tentativa 3
```

Quando `tentativa > max_rechamadas`, a senha pode transicionar para `Ausente`.
Isso torna a máquina de estados implementável **sem criar entidade adicional**
para rechamada.

### 4.3 Cadeia de prioridade formalizada (D9)

```text
ServicoAtendimento.prioridade
          ↓  valor padrão
     Triagem.prioridade
          ↓  classificação
     Senha.prioridade
          ↓  prioridade efetiva da fila
```

| Estrutura | Significado |
| --- | --- |
| `servicos_atendimento.prioridade` | Prioridade padrão do serviço |
| `triagens.prioridade` | Prioridade atribuída pela triagem |
| `senhas.prioridade` | Prioridade efetiva utilizada pela ordenação da fila |

As três recebem `CHECK (prioridade >= 1)`.

### 4.4 Invariantes de persistência aprovadas em D4

```sql
CHECK (senhas.prioridade >= 1)
CHECK (triagens.prioridade >= 1)
CHECK (servicos_atendimento.prioridade >= 1)
CHECK (chamadas.tentativa >= 1)
CHECK (unidades.max_rechamadas >= 0)
CHECK (atendimentos.fim >= atendimentos.inicio)
```

### 4.5 Unicidades **não** fixadas — semântica pendente

As duas hipóteses abaixo **não** serão transformadas em restrição física antes de a
semântica funcional ser registrada (ver §4.6).

### 4.6 Semânticas pendentes de registro

| # | Questão | Por que não pode ser imposta ainda |
| --- | --- | --- |
| Q1 | O número do guichê é único **por unidade**? | O PUML nomeia a coluna `guiches.numero`, não `codigo`; a restrição `UNIQUE (unidade_id, numero)` depende de definir se a unicidade é por unidade, por unidade e dia, ou global. |
| Q2 | O número da senha é único **por fila**, ou por unidade e dia? | `UNIQUE (fila_id, numero)` pressupõe unicidade por fila. Se a numeração for reiniciada por dia, a restrição correta muda. |

Nenhuma alteração no código ou no banco foi feita. Nenhuma promoção do `MOD-ATE` foi
realizada.

---

## 5. Estado do DOM-ATE após a decisão

```text
DOM-ATE
│
├── PUML proposto
│   └── precisa ser corrigido
│
├── Código
│   └── inexistente
│
├── Banco
│   └── inexistente
│
└── Implementação
    └── BLOQUEADA até reconciliação documental
```

O `MOD-ATE` **não** consta na matriz DOM↔MOD e **não** é promovido a *candidata*
nem a *confirmada*. Quando a implementação ocorrer, a promoção seguirá o mesmo rito
dos demais domínios: artefatos `001`–`026` gerados a partir do código e conferidos
por `python scripts/gerar_artefatos_territoriais.py --verificar`.

### 5.1 Sequência autorizada

1. Corrigir `001-Modelo-de-Dominio.puml`.
2. Corrigir `003-Maquina-de-Estados.puml`.
3. Reconstruir `005-Persistencia.puml` conforme D1–D10.
4. Segunda auditoria, restrita aos seis PUMLs.
5. Só então considerar a especificação documental estabilizada.

---

**Documento:** `AUDITORIA-DOM-ATE-2026-09-29.md`
**Última atualização:** 2026-09-29
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
