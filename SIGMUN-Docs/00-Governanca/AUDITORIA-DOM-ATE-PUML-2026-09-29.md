# AUDITORIA — DOM-ATE — SEGUNDA AUDITORIA (PUMLS) — 2026-09-29

**Classificação da Informação:** Pública
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
**Data:** 2026-09-29
**Domínio:** DOM-ATE — Atendimento Presencial e Online
**Escopo:** exclusivamente os seis diagramas em `SIGMUN-Docs/DOM-ATE/puml/`
**Documento anterior:** `AUDITORIA-DOM-ATE-2026-09-29.md`
**Tipo:** Verificação da reconciliação do modelo proposto
**Status da auditoria:** Concluída — D1 a D10 aplicadas e verificadas

---

## 1. Objetivo

Verificar, diagrama a diagrama, se as dez decisões aprovadas na auditoria anterior
foram efetivamente aplicadas ao modelo proposto, e se os seis PUMLs passaram a ser
internamente coerentes e sintaticamente válidos.

Nenhuma linha de código e nenhuma migration foi criada: o DOM-ATE permanece na fase
documental.

---

## 2. Método

A verificação é **mecânica**, não visual: cada decisão foi conferida por contagem e
comparação no conteúdo dos arquivos, e a sintaxe foi validada renderizando os seis
diagramas com PlantUML.

```bash
java -jar plantuml.jar -tsvg -o <destino> <arquivos.puml>
```

A estratificação dos arquivos (remoção das cercas ```` ``` ````) foi feita antes da
renderização, pois os `.puml` do repositório são blocos Markdown.

---

## 3. Verificação das decisões

| # | Decisão | Verificação | Esperado | Obtido | |
| --- | --- | --- | --- | --- | --- |
| D1 | Sem FKs físicas | `grep -c '<<FK>>' 005` | 0 | 0 | OK |
| D2 | `id` UUID, referências text | PKs `UUID` / refs `TEXT` | 11 / 14 | 11 / 14 | OK |
| D3 | Auditoria e exclusão lógica | 4 colunas x 11 tabelas | 44 | 44 | OK |
| D4 | CHECKs declarados | 6 invariantes | 6 | 6 | OK |
| D5 | Referência em `senhas` | `triagens.senha_id` / `senhas.triagem_id` | 0 / 1 | 0 / 1 | OK |
| D6 | `unidade_id` e `operador` em `chamadas` | presença no modelo | 2 | 2 | OK |
| D7 | `tentativa` e `max_rechamadas` | presença no modelo | 2 | 2 | OK |
| D8 | `FilaAtendimento` alinhado | campos em `001` | unidade, serviço | ambos | OK |
| D9 | Cadeia de prioridade | 3 níveis documentados | 3 | 3 | OK |
| D10 | `ativo` nos canais | presença em `001` e `005` | 2 | 2 | OK |

### 3.1 Observação sobre D2

A contagem de referências é **14**, e não as 13 do modelo original. A diferença é
intencional: D6 introduziu a relação `unidades ||--o{ chamadas`, o que adiciona
`chamadas.unidade_id`. Sem essa relação, não seria possível validar que o guichê da
chamada pertence à unidade correta.

### 3.2 Unicidades não impostas (D4)

As duas hipóteses de unicidade constam apenas como **nota declarando pendência**, sem
restrição física:

- `UNIQUE (unidade_id, numero)` — Q1 em aberto
- `UNIQUE (fila_id, numero)` — Q2 em aberto

Nenhuma aparece como restrição de entidade no diagrama.

---

## 4. Achado adicional — D11

**Nota multilinha com aspas: erro de sintaxe pré-existente.**

A validação por renderização revelou que `001-Modelo-de-Dominio.puml` **não renderizava**
antes desta correção, por um defeito que não havia sido detectado na auditoria anterior:

```plantuml
note "A identificação do cidadão/usuário deve referenciar
os domínios de identidade e cadastro aplicáveis,
sem duplicar dados cadastrais no DOM-ATE." as N1
```

O PlantUML não aceita quebra de linha dentro de uma nota entre aspas. O erro é
reproduzido no arquivo original preservado para comparação (linha 116).

**Correção aplicada:** conversão para a forma de bloco.

```plantuml
note as N1
A identificação do cidadão/usuário deve referenciar
os domínios de identidade e cadastro aplicáveis,
sem duplicar dados cadastrais no DOM-ATE.
end note
```

A lição de método é registrada: a auditoria anterior, feita por leitura, não detectou
o defeito; só a **renderização real** o revelou. Para artefatos de modelo, comprovar
que o diagrama compila é parte da verificação.

| # | Achado | Gravidade | Origem | Status |
| --- | --- | --- | --- | --- |
| D11 | Nota multilinha com aspas impede a renderização | Média | Defeito no PUML | **Corrigido** |

---

## 5. Coerência entre os seis diagramas

### 5.1 Entidades e tabelas

As 11 entidades de `001` correspondem uma a uma às 11 tabelas de `005`:

| Entidade (001) | Tabela (005) |
| --- | --- |
| UnidadeAtendimento | unidades_atendimento |
| Guiche | guiches |
| CanalAtendimento | canais_atendimento |
| ServicoAtendimento | servicos_atendimento |
| FilaAtendimento | filas_atendimento |
| Triagem | triagens |
| Senha | senhas |
| Chamada | chamadas |
| Atendimento | atendimentos |
| Encaminhamento | encaminhamentos |
| AvaliacaoAtendimento | avaliacoes_atendimento |

A contradição D8 — `FilaAtendimento` com três campos em `001` e cinco em `005` — está
eliminada: as duas versões declaram `unidade` e `servico`.

### 5.2 Coerência da rechamada entre `002` e `003`

O fluxo (`002`) e a máquina de estados (`003`) descrevem agora o **mesmo** mecanismo:

- `003`: `Chamada --> Rechamada : ausência` e
  `Rechamada --> Ausente : tentativa > max_rechamadas`
- `002`: `:Incrementar tentativa da chamada;` seguido de
  `if (tentativa > max_rechamadas?)`

Antes, `002` dizia apenas "Executar regra de rechamada", sem definir o mecanismo, e
`003` descrevia um estado sem qualquer suporte no modelo de persistência.

### 5.3 Diagramas sem alteração

| Arquivo | Situação |
| --- | --- |
| `000-Visao-Arquitetural.puml` | Sem FK, sem colunas de domínio: não afetado |
| `004-Integracoes.puml` | Não cita colunas nem restrições do schema `ate`: não afetado |

---

## 6. Validação de sintaxe

Os seis diagramas foram renderizados com PlantUML (`plantuml.jar` 2.18.1, Found via
extensão `jebbs.plantuml`).

| Arquivo | Resultado |
| --- | --- |
| `000-Visao-Arquitetural.puml` | Renderiza |
| `001-Modelo-de-Dominio.puml` | Renderiza (após D11) |
| `002-DOM-ATE-Fluxo-de-Atendimento.puml` | Renderiza |
| `003-Maquina-de-Estados.puml` | Renderiza |
| `004-Integracoes.puml` | Renderiza |
| `005-Persistencia.puml` | Renderiza |

Além da checagem de erro de sintaxe, a renderização confirma a estrutura: 11 entidades
com as colunas esperadas, PKs `UUID`, referências `TEXT`, colunas de auditoria nas 11
tabelas, nota de CHECKs e nota de unicidades pendentes.

---

## 7. Estado do DOM-ATE

```text
DOM-ATE
│
├── PUML proposto
│   └── reconciliado (D1-D11 aplicadas e verificadas)
│
├── Código
│   └── inexistente
│
├── Banco
│   └── inexistente
│
└── Implementação
    └── BLOQUEADA — aguarda decisão de início
```

**A especificação documental do DOM-ATE está estabilizada no escopo do modelo
proposto.** Permanecem as semânticas pendentes Q1 e Q2 (§4.6 da auditoria anterior),
que devem ser resolvidas antes de qualquer decisão sobre restrição física de
unicidade.

A implementação continua **não iniciada**, conforme a decisão de manter o DOM-ATE na
fase documental. O `MOD-ATE` não é promovido a *candidata* nem a *confirmada*.

---

**Documento:** `AUDITORIA-DOM-ATE-PUML-2026-09-29.md`
**Última atualização:** 2026-09-29
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
