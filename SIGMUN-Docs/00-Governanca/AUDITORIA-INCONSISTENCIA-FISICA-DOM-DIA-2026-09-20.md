# AUDITORIA — INCONSISTÊNCIA FÍSICA DO DOM-DIA — 2026-09-20

**Classificação da Informação:** Pública
**Responsável:** Gildazio
**Status da revisão:** Vigente
**Data:** 2026-09-20
**Domínio:** DOM-DIA — Gestão de Diárias, Viagens e Deslocamentos
**Tipo:** Ocorrência técnica / Reconciliação de estado físico
**Status da ocorrência:** Corrigida

---

## 1. Objetivo

Registrar a divergência identificada entre o estado lógico registrado pelo Alembic e o estado físico do PostgreSQL para o domínio DOM-DIA, bem como documentar a correção aplicada.

Este registro preserva a rastreabilidade da ocorrência e estabelece o contrato físico vigente do domínio.

---

## 2. Resumo da ocorrência

Foi identificada uma divergência entre a cadeia de migrations do SIGMUN e os objetos físicos existentes no banco de dados.

A migration:

```text
20260918_01_dom_dia_models
```

define o contrato físico do DOM-DIA no schema:

```text
dia
```

Entretanto, após o banco ter sido reconciliado e registrado no head:

```text
20260919_06_dom_con_contabil
```

os objetos físicos previstos para o schema `dia` não estavam presentes.

No mesmo banco existia um conjunto independente de objetos no schema:

```text
dom_dia
```

composto por:

```text
dom_dia.viagens
dom_dia.diarias
dom_dia.prestacoes_contas
```

A existência desse schema não correspondia ao contrato atual registrado no código, ORM ou migrations do SIGMUN.

---

## 3. Evidências levantadas

### 3.1 Contrato Alembic

Antes da correção, o banco apresentava:

```text
alembic current
20260919_06_dom_con_contabil
```

A migration `20260918_01_dom_dia_models` pertence à cadeia histórica imediatamente anterior às migrations posteriores do DOM-PES, DOM-ORC e DOM-CON.

A revisão define explicitamente:

```text
schema="dia"
```

para os objetos do DOM-DIA.

---

### 3.2 Contrato de aplicação

O ORM do DOM-DIA utiliza o schema:

```text
dia
```

para as entidades:

```text
ViagemModel
DiariaModel
PrestacaoContasModel
EventoDiariaModel
```

A API do domínio também opera sobre essas entidades.

Não foi identificado, no código atual, ORM ou migration que estabeleça `dom_dia` como contrato de persistência do DOM-DIA.

---

### 3.3 Estado físico anterior à correção

Antes da aplicação da migration de reparo, a consulta ao PostgreSQL retornava:

```text
 schemaname |     tablename
------------+-------------------
 dom_dia    | diarias
 dom_dia    | prestacoes_contas
 dom_dia    | viagens
```

Não existiam tabelas físicas no schema `dia`.

As tabelas `dom_dia.*` foram verificadas como vazias.

---

### 3.4 Evidência de backups

Os backups existentes no projeto continham:

```text
dom_dia.viagens
dom_dia.diarias
dom_dia.prestacoes_contas
```

e não continham o conjunto físico `dia.*`.

As tabelas `dom_dia.*` estavam sem dados de negócio.

Essa evidência foi considerada suficiente para preservar os objetos legados durante a correção, sem utilizá-los como substitutos do contrato atual.

---

### 3.5 Evidência funcional

Antes da correção, os endpoints do DOM-DIA retornavam erros relacionados à ausência das relações físicas:

```text
dia.viagens
dia.diarias
dia.prestacoes_contas
```

Isso confirmou que a divergência física afetava diretamente a execução da API.

---

## 4. Classificação da divergência

A ocorrência foi classificada como:

> **Divergência entre estado lógico de migration e estado físico do PostgreSQL.**

Não foi classificada como alteração do contrato corporativo do DOM-DIA.

O schema `dom_dia` existente no banco não foi promovido a contrato oficial e não foi utilizado como substituto do schema `dia`.

---

## 5. Decisão técnica

Fica registrado que:

1. O contrato vigente do DOM-DIA é o schema:

   ```text
   dia
   ```

2. A migration `20260918_01_dom_dia_models` permanece parte integrante do histórico do projeto.

3. O histórico Alembic existente não será reescrito.

4. A migration `20260918_01_dom_dia_models` não será alterada para acomodar o estado físico legado.

5. O schema `dom_dia` não será tratado como equivalente ao schema `dia`.

6. Os objetos `dom_dia.*` foram preservados durante a correção.

7. Qualquer futura remoção do schema `dom_dia` deverá ser objeto de decisão e migration própria, após avaliação de dependências.

---

## 6. Correção aplicada

Foi criada a migration corretiva:

```text
3b584e46028d_repair_restaura_objetos_fisicos_do_dom_.py
```

com:

```text
Revision:
3b584e46028d

Parent:
20260919_06_dom_con_contabil
```

A migration materializa fisicamente o contrato já definido para o DOM-DIA no schema `dia`.

Foram restauradas as tabelas:

```text
dia.viagens
dia.diarias
dia.prestacoes_contas
dia.eventos_diarias
```

e seus respectivos índices.

A migration foi aplicada com sucesso através de:

```text
alembic upgrade head
```

O banco passou a registrar:

```text
3b584e46028d (head)
```

---

## 7. Validação física após a correção

Após a aplicação da migration, o PostgreSQL passou a apresentar:

```text
dia        | diarias
dia        | eventos_diarias
dia        | prestacoes_contas
dia        | viagens
dom_dia    | diarias
dom_dia    | prestacoes_contas
dom_dia    | viagens
```

Contagem física:

```text
schema   | tabelas
---------+--------
dia      | 4
dom_dia  | 3
```

O schema `dia` possui os índices esperados, incluindo:

```text
viagens_pkey
ix_viagens_servidor
ix_viagens_dota

diarias_pkey
ix_diarias_servidor
ix_diarias_dota

prestacoes_contas_pkey
ix_prestacoes_diaria

eventos_diarias_pkey
ix_eventos_diarias_diaria
```

---

## 8. Validação funcional

Após a correção, foram testados os endpoints:

```text
GET /api/v1/dia/viagens/servidor/{servidor_id}
GET /api/v1/dia/diarias/servidor/{servidor_id}
GET /api/v1/dia/diarias/status/{status}
GET /api/v1/dia/prestacoes/abertas
```

Todos retornaram:

```text
HTTP/1.1 200 OK
```

com resposta:

```json
[]
```

O resultado vazio é esperado porque as tabelas físicas do DOM-DIA estavam sem dados de negócio.

A ausência anterior das relações `dia.*` deixou de ocorrer.

---

## 9. Estado final

O estado final do contrato é:

```text
DOM-DIA
│
├── Código / ORM
│   └── schema: dia
│
├── Alembic
│   └── 3b584e46028d (head)
│
├── PostgreSQL
│   └── dia
│       ├── viagens
│       ├── diarias
│       ├── prestacoes_contas
│       └── eventos_diarias
│
└── Legado físico preservado
    └── dom_dia
        ├── viagens
        ├── diarias
        └── prestacoes_contas
```

---

## 10. Impacto

A ocorrência afetava a persistência e a consulta do DOM-DIA.

Após a correção:

* o schema `dia` está fisicamente materializado;
* a cadeia Alembic possui um head único;
* os endpoints de consulta do DOM-DIA alcançam as tabelas corretas;
* não houve migração ou alteração de dados entre `dom_dia` e `dia`;
* o conjunto legado `dom_dia` foi preservado;
* o contrato atual da aplicação permanece alinhado ao código e às migrations.

---

## 11. Não ações

Como parte da correção, foram deliberadamente evitadas as seguintes ações:

* não foi executado `alembic stamp`;
* não foi executado `alembic downgrade`;
* não foi alterado o histórico das migrations existentes;
* não foi executado `Base.metadata.create_all()`;
* não foi renomeado `dom_dia` para `dia`;
* não foi copiado dado de `dom_dia` para `dia`;
* não foi removido o schema `dom_dia`;
* não foi alterado o contrato ORM do DOM-DIA para acomodar o legado.

---

## 12. Encaminhamento

A ocorrência de divergência física está considerada **corrigida**.

Permanece como pendência separada a avaliação futura do schema legado:

```text
dom_dia
```

Essa avaliação deverá determinar, com evidência de dependências, se os objetos podem ser formalmente descontinuados e removidos.

Essa eventual remoção deverá ocorrer por migration própria e não fará parte desta ocorrência de reparo.

---

## 13. Rastreabilidade

### Migration original

```text
20260918_01_dom_dia_models
```

### Migration corretiva

```text
3b584e46028d
```

### Head anterior

```text
20260919_06_dom_con_contabil
```

### Head registrado na correção inicial

```text
3b584e46028d
```

### Domínio

```text
DOM-DIA
```

### Responsável pela execução

```text
Gildazio
```

---

## 13A. Atualização / Reconciliação posterior — 2026-09-21

Após a correção física do DOM-DIA, a validação da cadeia Alembic identificou
um segundo branch originado no mesmo head anterior:

```text
20260919_06_dom_con_contabil
```

Esse branch correspondia à sequência de migrations do TRI, PAT e FRO:

```text
20260920_01_dom_tri_models
        ↓
20260920_02_dom_pat_models
        ↓
20260920_03_dom_fro_models
```

A migration de reparo do DOM-DIA permaneceu em seu próprio branch:

```text
3b584e46028d
```

As duas linhas eram independentes e não exigiam alteração dos objetos físicos
do DOM-DIA para serem reconciliadas.

Foi criada uma migration de merge exclusivamente para reconciliar os dois heads:

```text
b2fe9a5c6929
```

A migration de merge não executa DDL e possui apenas a finalidade de reconciliar
o histórico da cadeia Alembic.

### Estado final da cadeia Alembic

```text
alembic current
→ b2fe9a5c6929 (head) (mergepoint)

alembic heads
→ b2fe9a5c6929 (head)

alembic check
→ No new upgrade operations detected.
```

### Estado físico final

Schemas físicos confirmados:

```text
dia
dom_dia
fro
pat
trib
```

Tabelas do contrato atual do DOM-DIA:

```text
dia.diarias
dia.eventos_diarias
dia.prestacoes_contas
dia.viagens
```

Objetos legados preservados:

```text
dom_dia.diarias
dom_dia.prestacoes_contas
dom_dia.viagens
```

Demais objetos físicos reconciliados:

```text
fro.abastecimentos
fro.manutencoes
fro.rotas
fro.veiculos

pat.bens
pat.depreciacoes
pat.transferencias

trib.certidoes
trib.contribuintes
trib.divida_ativa
trib.imoveis
trib.lancamentos
```

A reconciliação do histórico Alembic não promoveu o schema legado `dom_dia`,
não alterou o contrato ORM do DOM-DIA e não implicou movimentação ou migração de dados.

## 14. Conclusão

A ocorrência consistia em uma divergência entre o estado registrado pela cadeia Alembic e a materialização física correspondente ao contrato vigente do DOM-DIA.

O contrato vigente foi preservado:

```text
DOM-DIA → schema dia
```

A divergência foi corrigida por uma migration posterior ao head anteriormente registrado, sem reescrever o histórico e sem modificar ou promover o schema legado `dom_dia`.

O estado físico e os endpoints principais do DOM-DIA foram validados após a correção.

**Status final: Corrigida e reconciliada.**

---

**Classificação da Informação:** Pública
**Responsável:** Gildazio
**Status da revisão:** Vigente
