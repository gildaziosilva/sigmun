# AUDITORIA — DOM-OUV (OUVIDORIA FALABR / e-OUV MUNICIPAL) — 2026-10-03

**Revisão:** 2 — reexecução integral da auditoria
**Classificação da Informação:** Pública
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
**Data:** 2026-10-03
**Domínio:** DOM-OUV — Ouvidoria FalaBR / e-OUV Municipal
**Módulo:** `sigmun_ouvidoria` (schema `ouv`) — implementado
**Tipo:** Auditoria de reconciliação entre modelo proposto, código e banco
**Status da auditoria:** ❌ **Reprovado para produção** — bloqueado por defeito funcional (HTTP 500), ausência de autenticação e LGPD não aplicada
**Substitui:** revisão 1 deste mesmo arquivo (ver §1.3 — a revisão 1 continha afirmações incorretas, corrigidas aqui)

---

## 1. Objetivo, método e correções

### 1.1 Objetivo

Reconciliar o modelo proposto (`SIGMUN-Docs/DOM-OUV/`), o código
(`src/modules/sigmun_ouvidoria/`), a API REST (`/api/v1/ouv`) e o schema físico `ouv`
no PostgreSQL, confrontando-os com:

- Lei 13.460/2017 — Código de Defesa do Usuário de Serviços Públicos
- Lei 12.527/2011 — Lei de Acesso à Informação (LAI)
- Lei 13.709/2018 — LGPD
- Decreto 9.492/2018 — e-OUV Federal
- Padrões FalaBR / e-OUV Municipal

Este documento registra o estado **verificado** e as pendências que impedem a
declaração de "DOM-OUV concluído para produção".

### 1.2 Método

Todos os itens abaixo foram executados nesta revisão; nenhum estado foi inferido de
documentação anterior.

| Verificação | Ferramenta | Resultado |
| --- | --- | --- |
| Estrutura do módulo | `find` / `ls` | 4 camadas + 3 pacotes vazios |
| Import do router | `python3 -c "from src.modules.sigmun_ouvidoria.presentation.api import router"` | `Router OK` |
| Bootstrap da aplicação | `python3 -c "from src.main import app"` | `Main OK` |
| Rotas publicadas | introspecção de `app.routes` | 16 rotas em `/api/v1/ouv` |
| Comportamento HTTP | `TestClient` (9 chamadas reais, sem mock) | 2 × HTTP 500, 1 × HTTP 201 sem token |
| Schema físico | `psql` em `localhost:5433/sigmun` | 6 tabelas, 7 enums, 17 índices |
| Dados | `psql` | 3 manifestações, 1 denúncia, 1 pedido LAI, 3 tramitações |
| Cadeia de migrations | `alembic current` / `heads` / `upgrade head` | 2 heads; `upgrade head` **falha** |
| Estático backend | `ruff check --select F,B` e padrão completo | 61 e **404** violações |
| Frontend | `npx tsc -b --pretty false` | **153** erros, todos em `pages/ouv` |
| Testes | `find tests -iname '*ouv*'` | 0 arquivos |

### 1.3 Correções em relação à revisão 1

A revisão 1 **não pode ser mantida** porque contém afirmações que a verificação
contradiz. As correções são relevantes para o histórico de governança:

| # | Afirmação da revisão 1 | Estado verificado |
| --- | --- | --- |
| 1 | "PUML **não existe**" | ❌ Falso — existem 6 arquivos `.puml`, 24.926 bytes |
| 2 | "17 endpoints" | ❌ Falso — são **16** rotas |
| 3 | "20 use cases" | ❌ Falso — são **15** classes `*UseCase` |
| 4 | "~85 erros TypeScript em 7 arquivos" | ❌ Falso — são **153** erros em **4** arquivos |
| 5 | "Backend **100% implementado**, aprovado para produção" | ❌ Falso — há defeito que retorna HTTP 500 no fluxo de consulta |
| 6 | "Autenticação: Bearer token JWT via `/api/v1/idn/auth/login`" | ❌ Falso — **nenhum** endpoint do DOM-OUV exige autenticação |
| 7 | "100% dos requisitos funcionais cobertos" | ❌ Falso — sigilo LGPD não é aplicado nas respostas |
| 8 | "Tramitação: histórico completo ✅" | ⚠️ Parcial — o histórico é gravado, mas **nunca devolvido** pela API |
| 9 | "Documentação 001–026 pendente" | ⚠️ Incompleto — os artefatos **existem**, mas são stubs com placeholders |

---

## 2. Os três estratos

A distinção abaixo é o eixo central desta auditoria. Confundi-los é o risco que se quer
evitar: um PUML bem desenhado **não** é evidência de código, e código **não** é evidência
de banco aplicado.

| # | Estrato | Evidência | Estado |
| --- | --- | --- | --- |
| 1 | **Modelo proposto** | `SIGMUN-Docs/DOM-OUV/` — 6 `.puml` + 27 artefatos `.md` | Existe, **divergente do código** |
| 2 | **Modelo implementado (código)** | `src/modules/sigmun_ouvidoria/`, 16 rotas, 15 use cases | Implementado, **com defeito crítico** |
| 3 | **Modelo físico (PostgreSQL)** | schema `ouv`: 6 tabelas, 7 enums, 17 índices | Aplicado via Alembic |

### 2.1 Evidência do estrato 1 — modelo proposto

**Diagramas PUML** (`SIGMUN-Docs/DOM-OUV/puml/`, 24.926 bytes):

| Arquivo | Bytes | Conteúdo verificado |
| --- | --- | --- |
| `000-Visao-Arquitetural.puml` | 3.234 | Componentes e fluxo macro |
| `001-Modelo-de-Dominio.puml` | 4.031 | 15 classes de domínio |
| `002-DOM-OUV-Fluxo-de-Manifestacao.puml` | 2.956 | Fluxo de captação e triagem |
| `003-Maquina-de-Estados.puml` | 3.425 | Estados e transições |
| `004-Integracoes.puml` | 5.285 | Integrações com IDN, GDO, INT |
| `005-Persistencia.puml` | 5.995 | 12 entidades de persistência propostas |

> **Nota de nomenclatura:** o arquivo de fluxo é `002-DOM-OUV-Fluxo-de-Manifestacao.puml`.
> A revisão 1 o-citava como `002-Fluxo-Manifestacoes.puml`. O padrão real segue o de
> DOM-ATE (`002-DOM-ATE-Fluxo-de-Atendimento.puml`).

**Artefatos Markdown** — `000` a `026` e `index.md` existem (2.357 linhas no total).

### 2.2 Divergência entre o modelo proposto e o implementado

Esta é a divergência mais relevante do estrato 1: o PUML e o artefato `013-Modelo-de-Dados`
descrevem um modelo **que não é o que foi implementado**.

| Entidade no PUML / artefato 013 | Existe no código/banco? |
| --- | --- |
| `manifestacoes` | ✅ Sim |
| `denuncias` | ✅ Sim |
| `pedidos_lai` | ✅ Sim |
| `unidades_ouvidoria` | ❌ Não existe |
| `canais_ouvidoria` | ❌ Não existe — canal é `enum` na própria manifestação |
| `classificacoes_manifestacao` | ❌ Não existe — tipo é `enum` |
| `encaminhamentos_ouvidoria` | ❌ Não existe — viável apenas para denúncias, via colunas booleanas |
| `prazos_ouvidoria` | ❌ Não existe — prazo é colunado em `manifestacoes` |
| `tratamentos_manifestacao` | ❌ Não existe |
| `respostas_ouvidoria` | ❌ Não existe — resposta é colunada em `manifestacoes` |
| `recursos_lai` | ⚠️ Parcial — implementado como auto-relacionamento em `pedidos_lai` |
| `avaliacoes_ouvidoria` | ❌ Não existe — colunas `avaliacao_cidadao` / `comentario_avaliacao` |
| — | ✅ `protocolos` e `anexos` existem **apenas** na implementação, não no PUML |

**Consequência:** o artefato `013-Modelo-de-Dados-Ouvidoria.md` **não descreve o banco
real**. Qualquer terceiro que use esse artefato como referência incauterá um modelo
inexistente. Este é o achado documental mais grave e exige correção antes de qualquer
uso do artefato.

Além disso, os artefatos `001`–`026` carregam o aviso literal:

> "este artefato descreve o **modelo proposto**; o domínio ainda não possui módulo implementado."

A frase é **falsa** — o módulo existe e está aplicado no banco desde 2026-10-02. Todos
os artefatos foram gerados por `scripts/gerar_artefatos_dominio.py` em 2026-09-30, antes da
implementação, e não foram regenerados depois.

### 2.3 Evidência do estrato 2 — código implementado

| Verificação | Comando | Resultado |
| --- | --- | --- |
| Módulo | `ls src/modules/ \| grep ouvidoria` | `sigmun_ouvidoria` ✅ |
| Domain | `ls src/modules/sigmun_ouvidoria/domain/` | `entities`, `value_objects`, `events`, `services`, `exceptions.py` ✅ |
| Application | `ls src/modules/sigmun_ouvidoria/application/` | `use_cases`, `interfaces.py`, `commands/`, `queries/` ⚠️ |
| Infrastructure | `ls src/modules/sigmun_ouvidoria/infrastructure/` | `database`, `repositories`, `integrations/` ⚠️ |
| Presentation | `ls src/modules/sigmun_ouvidoria/presentation/` | `api`, `schemas` ✅ |
| Entidades | `grep -cE '^class ' domain/entities/` | 5 (4 entidades + `Prioridade`) ✅ |
| Value objects | `grep -cE '^class ' domain/value_objects/` | 10 ✅ |
| Eventos | `grep -cE '^class ' domain/events/` | 10 ⚠️ **nenhum é usado** |
| Serviços | `grep -cE '^class ' domain/services/` | 6 ✅ |
| Exceções | `grep -cE '^class ' domain/exceptions.py` | 9 ✅ |
| Ports | `grep -c '^class Repositorio' application/interfaces.py` | 6 ✅ |
| Use cases | `grep -cE '^class .*UseCase' application/use_cases/` | **15** ✅ |
| Repositórios | `grep -cE '^class SQLAlchemy' infrastructure/repositories/` | 6 ✅ |
| Schemas Pydantic | `grep -cE '^class ' presentation/schemas/` | 21 ✅ |
| Endpoints | `grep -c '@router\.' presentation/api/` | **16** ✅ |
| Testes | `find tests -iname '*ouv*'` | **0** ❌ |

**Observação sobre `commands/`, `queries/` e `integrations/`:** os três diretórios
contêm apenas `__init__.py` vazio. São esqueletos de arquitetura Clean Architecture
não preenchidos. Não são defeito funcional, mas indicam escopo incompleto —
notadamente `integrations/`, que deveria conter a integração com FalaBR/e-OUV
(veja §7, R10).

### 2.4 Evidência do estrato 3 — modelo físico aplicado

**Migração:** `alembic/versions/20261002_01_dom_ouv_models.py` (revision `20261002_01`,
`down_revision = 20261002_01_ate_models`).

```text
$ psql -c "select table_name from information_schema.tables where table_schema='ouv';"
anexos
denuncias
manifestacoes
pedidos_lai
protocolos
tramitacoes
                                    → 6 tabelas (a revisão 1 afirmava 7)

$ psql -c "select typname from pg_type ... typtype='e';"
canal_recebimento_ouv
forma_resposta_ouv
nivel_sigilo_ouv
prioridade_ouv
status_manifestacao_ouv
tipo_denuncia_ouv
tipo_manifestacao_ouv
                                    → 7 enums ✅

$ psql -c "select count(*) from pg_indexes where schemaname='ouv';"
17                                    → 9 ix_* + 6 *_pkey + 2 *_key
```

**Constraint reais** (`pg_constraint`):

| Constraint | Definição |
| --- | --- |
| `manifestacoes_protocolo_key` | `UNIQUE (protocolo)` |
| `protocolos_ano_sequencial_key` | `UNIQUE (ano, sequencial)` |
| `anexos_manifestacao_id_fkey` | `FOREIGN KEY → ouv.manifestacoes(id)` |
| `denuncias_id_fkey` | `FOREIGN KEY → ouv.manifestacoes(id)` |
| `pedidos_lai_id_fkey` | `FOREIGN KEY → ouv.manifestacoes(id)` |
| `pedidos_lai_pedido_original_id_fkey` | `FOREIGN KEY → ouv.pedidos_lai(id)` |
| `tramitacoes_manifestacao_id_fkey` | `FOREIGN KEY → ouv.manifestacoes(id)` |

**Dados presentes no banco:**

| Tabela | Linhas |
| --- | --- |
| `ouv.protocolos` | 1 (ano 2026, sequencial 3) |
| `ouv.manifestacoes` | 3 |
| `ouv.denuncias` | 1 |
| `ouv.pedidos_lai` | 1 |
| `ouv.anexos` | 0 |
| `ouv.tramitacoes` | 3 |

Os 3 registros correspondem a `2026-000001` (solicitação), `2026-000002` (denúncia)
e `2026-000003` (pedido LAI) — seeds da auditoria anterior. A existência dessas linhas
confirma que a escrita funciona; **porém**, como demonstra o achado C1 (§3), a leitura por
identificador está quebrada para dois dos três tipos.

### 2.5 Problema na cadeia de migrations

A revisão 1 declarava `alembic current → 20261002_01 (head)` e afirmava ter testado
`downgrade`/`upgrade`. A verificação mostra que a cadeia tem **duas cabeças**:

```text
$ alembic heads
20260929_04_dom_obr_models (head)
20261002_01 (head)

$ alembic current
20260929_04_dom_obr_models (head)
20261002_01 (head)

$ alembic upgrade head
ERROR [alembic.util.messaging] Multiple head revisions are present for given
argument 'head'; please specify a specific target revision
```

---

## 3. Achado crítico — bloqueio de produção

### C1 — `GET /manifestacoes/{identificador}` retorna HTTP 500 em 2 de 3 casos

**Severidade:** 🔴 Crítica — indisponibilidade do endpoint de consulta.

**Local:** `src/modules/sigmun_ouvidoria/presentation/api/__init__.py:389`

```python
@router.get("/manifestacoes/{identificador}", response_model=ManifestacaoResponse)
def obter_manifestacao(identificador: str, repo, repo_d, repo_l,
                      usuario_perfil: str = Query(""),
                      usuario_autorizado: bool = Query(False)):
    try:
        m = ObterManifestacaoUseCase(repo, repo_d, repo_l).execute(
            identificador, usuario_perfil, usuario_autorizado)
        if hasattr(m, 'tipo_denuncia'):        # É denúncia
            return _to_denuncia_response(m)
        if hasattr(p, 'informacao_solicitada'):  # ← BUG: `p` não existe
            return _to_pedido_lai_response(m)
    except ManifestacaoNaoEncontradaError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    return _to_manifestacao_response(m)
```

A variável **`p` nunca é declarada**. O `ruff` confirma:

```text
$ ruff check --select F821 presentation/api/__init__.py
F821 Undefined name `p`
  --> src/modules/sigmun_ouvidoria/presentation/api/__init__.py:389:20
```

**Reprodução em runtime** (`TestClient`, banco real, sem mock):

```text
GET /api/v1/ouv/manifestacoes/2026-000001 (solicitação)     → 500 Internal Server Error
GET /api/v1/ouv/manifestacoes/2026-000002 (denúncia)        → 200 OK
GET /api/v1/ouv/manifestacoes/2026-000003 (pedido LAI)       → 500 Internal Server Error
```

Traceback capturado pelo `CorrelationIDMiddleware`:

```text
"exception": {
  "type": "NameError",
  "message": "name 'p' is not defined",
  "correlation_id": "ac782681-40cc-48c5-a8cf-81cc83d68c67"
}
```

**Por que a denúncia funciona:** o `return` dentro de `if hasattr(m, 'tipo_denuncia')`
interrompe a função antes de alcançar a linha com `p`.

**Por que a manifestação comum também falha:** após os dois `hasattr` (o segundo estoura
`NameError`), a execução jamais chega ao `return _to_manifestacao_response(m)`. O
`NameError` não é capturado pelo `except ManifestacaoNaoEncontradaError`.

**Impacto:**
- Cidadão não consegue consultar sua manifestação por ID nem por protocolo — o caso de uso
  mais básico do serviço.
- Todo pedido LAI é inacessível por identificador, inclusive para o cidadão que acabou de
  protocolá-lo. Viola frontalmente o **art. 8º da Lei 12.527/2011**, que assegura ao
  cidadão o acesso à informação **relativa a seu próprio pedido**.
- Só a rota de denúncia funciona — por acidente de fluxo de controle.

### C1b — Protocolo inexistente retorna HTTP 500 em vez de 404

**Severidade:** 🔴 Crítica — achado **descoberto durante a correção do C1**.

**Local:** `infrastructure/repositories/__init__.py` — linhas 266, 561 e 834.

Os três repositórios convertem o identificador recebido direto para `UUID`:

```python
def get_by_id(self, manifestacao_id: str) -> Optional[Manifestacao]:
    model = self._session.get(ManifestacaoModel, UUID(manifestacao_id))
```

`ObterManifestacaoUseCase.execute` tenta `get_by_protocolo` (aceita string) e depois
`get_by_id`. Quando o cliente consulta um **protocolo** — é o uso normal do cidadão —
que não existe, as três chamadas `get_by_id` lançam:

```text
ValueError: badly formed hexadecimal UUID string
```

O `except ManifestacaoNaoEncontradaError` da apresentação **não captura `ValueError`**,
resultando em **500 Internal Server Error** onde o correto é **404 Not Found**.

**Reprodução:**

```text
GET /api/v1/ouv/manifestacoes/2026-999999  →  500  (esperado 404)
```

**Impacto:** qualquer cidadão que digite um protocolo com dígito errado, ou consulte um
protocolo de outro ano sem registro, recebe erro 500 em vez de "não encontrado". Também
envenena os logs com stack traces e pode ser usado para enumeração de identificadores.

**Correção:** validar o formato em `ObterManifestacaoUseCase.execute` antes de chamar
`get_by_id`, devolvendo `None` quando o identificador não for um UUID válido.

**Por que a auditoria 2.0 não detectou:** não havia teste e a auditoria exercitou apenas
identificadores existentes. Surge ao validar a correção — ver §9.4.
  cidadão o acesso à informação **relativa a seu próprio pedido**.
### C2 — Nenhum endpoint exige autenticação ou autorização

**Severidade:** 🔴 Crítica — exposição de dados pessoais e de integridade funcional.

A revisão 1 afirmava "Autenticação: Bearer token JWT via `/api/v1/idn/auth/login`".
A verificação mostra que **não existe nenhuma dependência de autenticação** no router:

```bash
$ grep -nE 'current_user|get_current|Depends\(get_user|Security\(' presentation/api/__init__.py
(sem resultado)
```

Os únicos middlewares globais são `CORSMiddleware` e `CorrelationIDMiddleware` — nenhum
de autenticação. Consequentemente, `autor_id`, `usuario_id` e `respondido_por` chegam
**do corpo da requisição**, sem verificação:

```text
# POST sem Authorization — gravou no banco de verdade
POST /api/v1/ouv/manifestacoes  (sem header Authorization)
  → 201 Created
  → protocolo 2026-000004 gravado em ouv.manifestacoes
```

**Consequências:**

| Cenário | Situação atual | Consequência |
| --- | --- | --- |
| `POST /denuncias` anônimas | Sem auth, sigilo default `true` | Denúncia anônima real, mas sem trilha de autor |
| `GET /manifestacoes` | Sem auth | Lista **todas** as manifestações de todos os cidadãos |
| `GET /denuncias` | Sem auth | Lista denúncias com `local_fato`, `servidor_envolvido`, `valor_envolvido` |
| `POST /{id}/status` | Sem auth, `usuario_id` do body | Qualquer um move o status e se declara autor |
| `POST /{id}/responder` | Sem auth | Qualquer um responde como se fosse o órgão |
| `GET /estatisticas` | Sem auth | Indicadores institucionais públicos |

**Agravante de LGPD:** `_to_denuncia_response` devolve `cidadao.cpf` e `cidadao.email`
**em claro**, porque o schema de resposta não aplica mascaramento (C3). Combinado com a
ausência de auth, um `GET /denuncias` expõe CPF e e-mail de todos os denunciantes a
qualquer requisição anônima.

**Correção:** aplicar a dependência de usuário autenticado do DOM-IDN em todas as rotas
e remover `autor_id`/`usuario_id`/`respondido_por` do corpo, passando-os do token.

### C3 — Mascaramento LGPD existe no domínio mas nunca é aplicado

**Severidade:** 🔴 Crítica — descumprimento da LGPD (art. 6º, III; art. 46).

`ServicoLGPD` e `DadosCidadao.para_exibicao()` existem e funcionam:

```python
# domain/services/__init__.py
class ServicoLGPD:
    @staticmethod
    def mascarar_para_exibicao(cidadao: DadosCidadao) -> dict:
        return cidadao.para_exibicao()   # "***.123.***-45", "f***@dominio"

# domain/value_objects/__init__.py
def _mascarar_cpf(cpf): return f"***.{cpf[3:6]}.***-{cpf[9:]}"
def _mascarar_email(email): return f"{local[0]}***@{dominio}"
```

**Porém, `ServicoLGPD` é importado em `application/use_cases/__init__.py:45` e nunca
chamado.** Todos os mappers de resposta expõem os dados crus:

```python
# presentation/api/__init__.py:135-142  (_to_manifestacao_response)
cidadao={
    "nome": m.cidadao.nome,
    "cpf": m.cidadao.cpf,      # ← sem máscara
    "email": m.cidadao.email,  # ← sem máscara
    ...
}
```

O mesmo padrão se repete em `_to_denuncia_response` e `_to_pedido_lai_response`.
O método `Denuncia.get_dados_sigilosos(usuario_autorizado)` — que implementa corretamente
a restrição RN-OUV-030 — **nunca é chamado pela camada de apresentação**.

**Conclusão:** a RN-OUV-030 está implementada no domínio e **desligada na aplicação**.
Documentá-la como "✅" (como fez a revisão 1) descreve uma intenção, não o comportamento.

### C4 — Ausência total de testes

**Severidade:** 🔴 Crítica — nenhuma proteção contra regressão.

```bash
$ find tests -iname '*ouv*'
(vazio)

$ find tests -name 'test_*.py' | wc -l
73                            ← o projeto tem 73 arquivos de teste; OUV não tem nenhum
```

Existe `tests/unit/`, `tests/integration/` e `tests/e2e/` com 73 arquivos para outros
domínios. O padrão existe e não foi aplicado ao OUV. Cobertura efetiva: **0%**.

Isto explica diretamente C1: um teste de integração de 10 linhas
(`GET /manifestacoes/{protocolo}` → 200) teria barrado o defeito antes da entrega.

### C5 — 404 violações de lint no módulo

**Severidade:** 🟠 Alta — bloqueia o quality gate do projeto.

```text
$ ruff check src/modules/sigmun_ouvidoria
Found 404 errors.            (237 fixable automaticamente)

$ ruff check --select F,B src/modules/sigmun_ouvidoria
Found 61 errors.
```

Códigos predominantes: `UP006` (`List` → `list`), `UP045` (`Optional[X]` → `X | None`),
`B904` (exceções sem `from exc`). Além do `F821` de C1, há `F401` de import não usado
(por exemplo `ServicoEstatisticas` importado dentro da função `obter_estatisticas` sem uso),
o que indica código escrito sem verificação.

### C6 — Cadeia Alembic com duas cabeças

**Severidade:** 🟠 Alta — `alembic upgrade head` falha (detalhado em §2.5).

---

## 4. Achados de severidade média

### M1 — Frontend: 153 erros TypeScript em 4 arquivos

**Severidade:** 🟡 Média — bloqueia `npm run build`, mas não afeta o backend.

```text
$ npx tsc -b --pretty false | grep -c 'error TS'
153

$ ... | grep 'error TS' | sed 's/(.*//' | sort | uniq -c | sort -rn
52 src/pages/ouv/PedidosLaiOuv.tsx
49 src/pages/ouv/DenunciasOuv.tsx
41 src/pages/ouv/ManifestacoesOuv.tsx
11 src/pages/ouv/OuvPage.tsx

$ ... | grep -oP 'error TS\d+' | sort | uniq -c | sort -rn
139 error TS2304     (Cannot find name '...')
  7 error TS6133     (declared but never read)
  4 error TS7006     (implicit 'any')
  3 error TS2739     (missing properties)
```

**Causa raiz única:** os 139 `TS2304` decorrem de imports ausentes. Os 4 arquivos com
erro **não importam nada de `react`** (`grep -c "from 'react'"` → 0), o que faz
`useState`, `useEffect` e `FormEvent` serem desconhecidos. Somam-se a isso Tipos e
componentes de `OuvShared` e funções de `lib/api` não importados.

| Arquivo | Erros | Import de `react` | Observação |
| --- | --- | --- | --- |
| `PedidosLaiOuv.tsx` | 52 | ❌ ausente | Pior caso; falta também `lib/api` e `Field`/`SelectField` |
| `DenunciasOuv.tsx` | 49 | ❌ ausente | Falta `lib/api`, `FormEvent`, componentes de formulário |
| `ManifestacoesOuv.tsx` | 41 | ❌ ausente | Falta `lib/api`, `TabelaEstado` |
| `OuvPage.tsx` | 11 | ❌ ausente | Falta `useEffect`, tipos implícitos |
| `VisaoGeralOuv.tsx` | 0 | ❌ ausente | Não usa React — **não é obstáculo** |
| `EstatisticasOuv.tsx` | 0 | ❌ ausente | Não usa React — **não é obstáculo** |
| `OuvShared.tsx` | 0 | ✅ presente | OK |

**Correção:** adicionar as declarações de import ausentes. A revisão 1 estimava
"~85 erros em 7 arquivos"; o número real é **153 em 4 arquivos** — a divergência muda o
esforço estimado.

**Nota:** o backend não depende do frontend. O `DOM-OUV` pode ser promovido como
serviço de API mesmo sem a interface corrigida, desde que C1–C3 sejam resolvidos.

### M2 — Eventos de domínio declarados e nunca emitidos

**Severidade:** 🟡 Média — Functionalidade futura tratada como entregue.

`domain/events/__init__.py` define 10 classes de evento (`ManifestacaoRegistradaEvento`,
`DenunciaEncaminhadaEvento`, `PedidoLaiRespondidoEvento`, `PrazoVencidoEvento`, etc.) e o
enum `TipoEventoOuv` com 19 membros. A verificação:

```bash
$ grep -rn 'EventoOuvidoria\|TipoEventoOuv' src/modules/sigmun_ouvidoria/ --include=*.py \
    | grep -v 'domain/events'
(vazio)
```

**Nenhum evento é emitido, publicado ou persistido.** `ServicoEncaminhamento.encaminhar_denuncia`
inclusive contém o comentário `# Disparar evento de integração` seguido de nenhum código.

Impacto: a integração com DOM-INT (notificação ao cidadão) e a trilha de auditoria
declarada no artefato `017-Modelo-de-Auditoria` **não existem**. O artefato 014
(`Modelo-de-Integracao`) descreve integrações que não foram implementadas.

### M3 — Histórico de tramitação gravado mas nunca devolvido

**Severidade:** 🟡 Média — dado existe, não é acessível.

Os repositórios gravam tramitação corretamente (`save()` → `Registro inicial` e
`Alteração de status`; 3 linhas confirmadas no banco). Porém **todos os mappers de
resposta devolvem lista vazia**:

```python
tramitacoes=[],  # Carregado separadamente se necessário
```

Ocorrências: `_to_manifestacao_response:165`, `_to_denuncia_response:227`,
`_to_pedido_lai_response:281`. Não existe endpoint dedicado de histórico, apesar de o
schema `TramitacaoSchema` existir e o repositório `list_by_manifestacao` estar implementado.

**Impacto:** o cidadão e o ouvidor **não conseguem auditar a trajetória** de um
atendimento — requisito central deOuvidoria e do Decreto 9.492/2018. A revisão 1
marcou "Tramitação ✅ Histórico completo", o que é correto quanto à gravação e incorreto
quanto à disponibilidade.

### M4 — Artefatos 001–026 são stubs com afirmações falsas

**Severidade:** 🟡 Média — risco de induzir a erro em quem os consultar.

Todos os 26 artefatos (68–96 linhas cada) foram gerados por script em 2026-09-30 e
declaram, em seção idêntica:

> "este artefato descreve o **modelo proposto**; o domínio ainda não possui módulo implementado."

Problemas específicos observados:

| Artefato | Problema |
| --- | --- |
| `001-Mapa-de-Atores` | Matriz ator × capacidade com **células vazias** |
| `004-Mapa-de-Servicos` | Declara "1 operação, sem implementação registrada"; a API tem **16 rotas** |
| `012-Matriz-de-Rastreabilidade` | Regras declaradas como `RF-CUM-001` — **identificador do DOM-CUM**, erro de copy-paste |
| `012` | Citações sem espaço: "Recepçãodemanifestação" |
| `013-Modelo-de-Dados` | Descreve **12 tabelas que não existem** (ver §2.2) |
| `index.md` | Status "Em elaboração" e maturidade "Preparado / Candidata" — desatualizado |

**Impacto:** o `index.md` do domínio afirma que o módulo é "Preparado; Candidata; validar
escopo", e a `031-Matriz-de-Correspondencia-DOM-MOD.md` repete. A governança ainda trata
o OUV como não implementado, apesar do código em produção.

### M5 — Nomenclatura de prazos semanticamente incorreta

**Severidade:** 🟡 Média — prazo legal nomeado como "úteis", calculado como corridos.

O campo chama-se `dias_uteis` e a Lei 12.527/2011, art. 11, trata de **dias corridos**.
O cálculo usa `timedelta(days=base)`, ou seja, dias corridos, sob o nome `dias_uteis`:

```python
# domain/services/__init__.py — CalculadoraPrazo.calcular
data_limite = data_registro + timedelta(days=base)
return PrazoResposta(data_limite=data_limite, dias_uteis=base, ...)
```

Não há impacto no cálculo (o valor é legalmente correto), mas o nome sugere dias úteis e
pode induzir erro em regra de negócio futura. Recomenda-se renomear para `dias_prazo` /
`prazo_dias`.

---

## 5. Achados de severidade baixa

### B1 — Duplicação de método em `PedidoLai`

`PedidoLai.registrar_resposta` está definido **duas vezes** de forma idêntica
(`domain/entities/__init__.py:309` e `:319`). A segunda sobrescreve a primeira.
Não altera o comportamento, mas indica falta de revisão e deve ser removida.

### B2 — `__table_args__` declarado duas vezes em `ProtocoloModel`

```python
class ProtocoloModel(Base):
    __tablename__ = "protocolos"
    __table_args__ = ({"schema": "ouv"},)          # linha 33 — sobrescrita

    ...
    __table_args__ = (                              # linha 41 — a que vale
        UniqueConstraint("ano", "sequencial", name="uq_protocolo_ano_sequencial"),
        {"schema": "ouv"},
    )
```

A primeira atribuição é inócua (é sobrescrita), mas o nome `uq_protocolo_ano_sequencial`
declarado no código **não bate** com o índice real no banco
(`protocolos_ano_sequencial_key`, gerado pelo `UNIQUE (ano, sequencial)` inline do SQL).
Como a migração usa SQL direto, não há impacto — mas a constatação impede usar
`Base.metadata.create_all()`.

### B3 — `registrar_protocolo` é no-op

`SQLAlchemyProtocoloRepository.registrar_protocolo` contém apenas `pass` com o comentário
"Já tratado em obter_proximo_sequencial". O `GeradorProtocolo.registrar()` chama-o sempre.
É funcional (a unicidade vem do `sequencial` incrementado em memória da sessão), mas
`obter_proximo_sequencial` **não usa lock**: em concorrência, dois requests podem ler o
mesmo `sequencial` antes do `flush`, gerando `UNIQUE (ano, sequencial)` violado.
Recomenda-se `SELECT ... FOR UPDATE` ou `INSERT ... ON CONFLICT`.

### B4 — Pacotes vazios

`application/commands/`, `application/queries/` e `infrastructure/integrations/`
contêm apenas `__init__.py` vazio (ver §2.3).

### B5 — `datetime.utcnow()` depreciado

---

## 6. Cobertura funcional vs. requisitos legais

A tabela abaixo substitui a da revisão 1, que marcava quase tudo como "✅" sem
verificar o comportamento observável.

| Requisito | Implementação | Evidência | Estado |
| --- | --- | --- | --- |
| **13.460/2017** — manifestação com protocolo único | `GeradorProtocolo` + `protocolos` | Protocolo `2026-000001` gravado | ✅ |
| **13.460/2017** — consulta da manifestação | `ObterManifestacaoUseCase` | `GET` → **500** | ❌ **C1** |
| **13.460/2017** — resposta ao cidadão | `Manifestacao.registrar_resposta` | Endpoint existe; sem teste | ⚠️ sem teste |
| **13.460/2017** — avaliação (1–5) | `Manifestacao.avaliar` | Regra `1 <= nota <= 5` | ✅ |
| **LAI art. 8º** — acesso ao próprio pedido | `GET /manifestacoes/{id}` | **500 em 2 de 3 tipos** | ❌ **C1** |
| **LAI art. 11** — prazo 20 dias + 10 (§1º) | `CalculadoraPrazo.PRAZOS_BASE` | LAI = 20; `+10` em `calcular_prorrogacao` | ✅ |
| **LAI art. 15** — recurso | `interpor_recurso` / `decidir_recurso` | Restringido a pedido `ARQUIVADA` | ✅ |
| **LAI art. 24** — sigilo com fundamentação | `PedidoLai.validar` exige `fundamentacao_sigilo` | ✅ | ✅ |
| **LGPD art. 6º/46** — mascaramento | `ServicoLGPD` existe, **nunca chamado** | CPF/e-mail em claro nas respostas | ❌ **C3** |
| **LGPD art. 18** — restrição ao denunciante | `get_dados_sigilosos` existe, **nunca chamado** | Sigilo default `true` mas inefetivo | ❌ **C3** |
| **Segurança** — autenticação/autorização | **Inexistente** | `POST` sem token → **201** | ❌ **C2** |
| **Decreto 9.492/2018** — tramitação | Gravado em `tramitacoes` (3 linhas) | **Não devolvido** pela API | ⚠️ **M3** |
| **Decreto 9.492/2018** — prazos por tipo | `PRAZOS_BASE` 20/30 dias | ✅ | ✅ |
| **FalaBR** — canais de atendimento | `CanalRecebimento` com 7 valores | Enum no banco | ✅ |
| **FalaBR** — anonimização de denúncia | `cidadao_anonimo` default `true` | ✅ | ✅ |
| **FalaBR** — encaminhamento MP/PF/TCE | `ServicoEncaminhamento.ORGAOS_EXTERNOS` | 5 órgãos mapeados | ✅ |
| **Estatísticas/indicadores** | `ServicoEstatisticas` | `GET /estatisticas` → 200 com totais | ✅ |
| **Eventos de domínio** | 10 classes, **0 emissões** | `grep` sem resultado fora de `events` | ❌ **M2** |
| **Integração FalaBR/e-OUV** | `integrations/` vazio | — | ❌ **M2** |
| **Rastreabilidade de tramitação** | Colunado, sem endpoint | — | ⚠️ **M3** |

**Conclusão:** o domínio tem **boa cobertura de regras de negócio no núcleo**, mas
**falha em segurança, privacidade e disponibilidade**. O veredito anterior de
"100% dos requisitos funcionais cobertos" não se sustenta.

Usado em 12 pontos (`entities`, `events`, `value_objects`). Depreciado no Python 3.12;
recomenda-se `datetime.now(timezone.utc)`, coerente com as colunas `TIMESTAMPTZ`.
---

## 7. API REST — inventário real

16 rotas sob o prefixo `/api/v1/ouv`, registradas em `src/main.py:342`.

| # | Método | Rota | Handler | Estado verificado |
| --- | --- | --- | --- | --- |
| 1 | POST | `/manifestacoes` | `registrar_manifestacao` | ✅ 201 |
| 2 | GET | `/manifestacoes` | `listar_manifestacoes` | ✅ 200 |
| 3 | GET | `/manifestacoes/{identificador}` | `obter_manifestacao` | ❌ **500** |
| 4 | POST | `/manifestacoes/{id}/responder` | `responder_manifestacao` | ⚠️ não testado |
| 5 | POST | `/manifestacoes/{id}/status` | `alterar_status` | ⚠️ não testado |
| 6 | POST | `/manifestacoes/{id}/prorrogar` | `prorrogar_prazo` | ⚠️ não testado |
| 7 | POST | `/manifestacoes/{id}/avaliar` | `avaliar_manifestacao` | ⚠️ não testado |
| 8 | POST | `/denuncias` | `registrar_denuncia` | ✅ (via lista) |
| 9 | GET | `/denuncias` | `listar_denuncias` | ✅ 200 |
| 10 | POST | `/denuncias/{id}/encaminhar` | `encaminhar_denuncia` | ⚠️ não testado |
| 11 | POST | `/pedidos-lai` | `registrar_pedido_lai` | ✅ (via lista) |
| 12 | GET | `/pedidos-lai` | `listar_pedidos_lai` | ✅ 200 |
| 13 | POST | `/pedidos-lai/{id}/recurso` | `interpor_recurso_lai` | ⚠️ não testado |
| 14 | POST | `/pedidos-lai/{id}/decidir-recurso` | `decidir_recurso_lai` | ⚠️ não testado |
| 15 | GET | `/estatisticas` | `obter_estatisticas` | ✅ 200 |
| 16 | GET | `/manifestacoes-vencendo` | `manifestacoes_vencendo_prazo` | ✅ 200 |

**Observações adicionais:**
- **Não há rota de leitura de denúncia ou de pedido LAI por ID** — apenas a genérica em
  `/manifestacoes/{id}`, que é justamente a quebrada (C1).
- **Não há rota de tramitação** (M3).
- **Não há rota de anexo** (upload) — anexos são referenciados por URL externa
  (`Anexo.url`), sem integração com DOM-GDO.
- `usuario_perfil` e `usuario_autorizado` são **query parameters** livres
  (`api/__init__.py:381-382`), sem vínculo com identidade — quem os enviar os controla.

---

## 8. Regras de negócio — rastreabilidade

| Regra | Onde está implementada | Verificado em runtime |
| --- | --- | --- |
| RN-OUV-001 — Protocolo único `AAAA-NNNNNN` | `GeradorProtocolo.gerar`, `protocolos` | ✅ `2026-000001..000004` |
| RN-OUV-002 — Denúncia anônima; demais exigem identidade | `ManifestacaoBase.validar` | ⚠️ regra existe, C2 anula a proteção |
| RN-OUV-003 — LAI: 20 dias + 10 | `CalculadoraPrazo` | ✅ sem teste |
| RN-OUV-010 — Transições de status controladas | `StatusManifestacao.pode_transicionar_para` | ✅ 9 estados mapeados |
| RN-OUV-020 — Prazos por tipo (20/30) | `CalculadoraPrazo.PRAZOS_BASE` | ✅ sem teste |
| RN-OUV-030 — Sigilo do denunciante (LGPD) | `ServicoLGPD`, `get_dados_sigilosos` | ❌ **C3** nunca chamado |
| LAI art. 11 §1º — Prorrogação de 10 dias | `calcular_prorrogacao` | ✅ sem teste |
| LAI art. 15 — Recurso | `interpor_recurso`, `decidir_recurso` | ✅ sem teste |
| LGPD — Mascaramento de CPF/e-mail | `DadosCidadao.para_exibicao` | ❌ **C3** nunca chamado |
| LGPD art. 18 — Acesso a dados sensíveis | `ServicoLGPD.pode_acessar_dados_sensiveis` | ❌ **C3** nunca chamado |

**Achado relevante:** 3 das 10 regras (RN-OUV-002, RN-OUV-030 e as duas de LGPD) existem
no domínio mas **não têm efeito na aplicação**. A validação é correta; o desligamento
acontece na camada de apresentação.
---

## 9. Evidências de validação

### 9.1 Comandos de reprodução dos achados críticos

```bash
cd /home/gildazio/Projetos-Python/sigmun-v1/sigmun-v1

# C1 — NameError
.venv/bin/python -m ruff check --select F821 src/modules/sigmun_ouvidoria/presentation/api/__init__.py
# → F821 Undefined name `p` (linha 389)

# C2 — ausência de autenticação
grep -nE 'current_user|get_current|Depends\(get_user|Security\(' \
  src/modules/sigmun_ouvidoria/presentation/api/__init__.py
# → sem resultado

# C3 — LGPD não aplicada
grep -rn 'ServicoLGPD' src/modules/sigmun_ouvidoria/ --include=*.py
# → só a definição e o import não usado; nenhuma chamada

# C4 — ausência de testes
find tests -iname '*ouv*'          # → vazio
find tests -name 'test_*.py' | wc -l   # → 73 (nenhum do OUV)

# C5 — lint
.venv/bin/python -m ruff check src/modules/sigmun_ouvidoria     # → 404 errors
.venv/bin/python -m ruff check --select F,B src/modules/sigmun_ouvidoria  # → 61 errors

# C6 — duas cabeças
alembic heads                       # → 20260929_04_dom_obr_models (head) / 20261002_01 (head)
alembic upgrade head                # → ERROR: Multiple head revisions are present

# M1 — frontend
cd frontend/admin && npx tsc -b --pretty false | grep -c 'error TS'   # → 153

# M2 — eventos nunca emitidos
grep -rn 'EventoOuvidoria\|TipoEventoOuv' src/modules/sigmun_ouvidoria/ --include=*.py \
  | grep -v 'domain/events'
# → vazio
```

### 9.2 Verificação funcional em runtime (banco real, sem mock)

Executado com `TestClient` sobre `src.main:app`, banco `localhost:5433/sigmun`:

```text
GET  /api/v1/ouv/manifestacoes/2026-000001  (solicitação)  → 500  ← C1
GET  /api/v1/ouv/manifestacoes/2026-000002  (denúncia)     → 200
GET  /api/v1/ouv/manifestacoes/2026-000003  (pedido LAI)    → 500  ← C1
GET  /api/v1/ouv/manifestacoes?page=1&page_size=10          → 200
GET  /api/v1/ouv/denicias                                     → 200
GET  /api/v1/ouv/pedidos-lai                                  → 200
GET  /api/v1/ouv/estatisticas                                 → 200
GET  /api/v1/ouv/manifestacoes-vencendo?dias=30               → 200  (total: 3)
POST /api/v1/ouv/manifestacoes  (SEM Authorization)          → 201  ← C2
```

Payload de `/estatisticas` retornado:

```json
{"gerais":{"total":3,"respondidas":0,"concluidas":0,"vencidas":0,
           "taxa_resposta":0.0,"taxa_conclusao":0.0},
 "por_tipo":{"manifestacoes":{"solicitacao":1},
             "denuncias":{"corrupcao":1},
             "pedidos_lai":{"nivel_sigilo":{"publico":1}}},
 "vencendo_5_dias":0,"vencendo_10_dias":0}
```

O registro criado pela chamada sem token foi removido após o teste; o banco foi
restaurado ao estado anterior (3 manifestações, 3 tramitações, sequencial 3).

### 9.3 Verificação do schema físico

```bash
PGPASSWORD=sigmun psql -h localhost -p 5433 -U sigmun -d sigmun -c "\dt ouv.*"
```

<details>
<summary>Resultado</summary>

```text
          Schema |    Name
-------------------+-------------------
 ouv               |protocolos
 ouv               |manifestacoes
 ouv               |denuncias
 ouv               |pedidos_lai
 ouv               |anexos
 ouv               |tramitacoes
(6 rows)
```
</details>

```sql
-- Colunas de ouv.manifestacoes (32 colunas)
id, protocolo, ano_protocolo, numero_protocolo, tipo, status, prioridade,
assunto, descricao, cidadao_nome, cidadao_cpf, cidadao_email, cidadao_telefone,
cidadao_endereco, cidadao_anonimo, canal, orgao_destino, setor_responsavel,
prazo_data_limite, prazo_dias_uteis, prazo_prorrogado, prazo_data_prorrogacao,
prazo_justificativa_prorrogacao, resposta, forma_resposta, data_resposta,
respondido_por, avaliacao_cidadao, comentario_avaliacao,
created_at, updated_at, created_by, updated_by, is_deleted
```

---

## 10. Critérios de conclusão (Definition of Done)

| Critério | Revisão 1 | Revisão 2 | Evidência |
| --- | --- | --- | --- |
| Módulo com 4 camadas | ✅ | ✅ | `domain`, `application`, `infrastructure`, `presentation` |
| Modelos e persistência | ✅ | ✅ | 6 tabelas, 7 enums, 17 índices |
| Casos de uso | ✅ (20) | ✅ (**15**) | `grep -cE '^class .*UseCase'` |
| API REST | ✅ (17) | ✅ (**16**) | 16 rotas em `/api/v1/ouv` |
| Regras de prazo | ✅ | ✅ | `CalculadoraPrazo` |
| Tramitação gravada | ✅ | ✅ | 3 linhas em `ouv.tramitacoes` |
| Estatísticas | ✅ | ✅ | `/estatisticas` → 200 |
| **Consulta por identificador** | ✅ *(não verificado)* | ❌ | **HTTP 500 — C1** |
| **Autenticação/autorização** | ✅ *(inexistente)* | ❌ | **C2** |
| **LGPD mascaramento** | ✅ *(não aplicado)* | ❌ | **C3** |
| **Testes unitários** | ❌ | ❌ | 0 arquivos — C4 |
| **Testes de integração** | ❌ | ❌ | 0 arquivos — C4 |
| **Lint limpo** | ⏳ | ❌ | 404 violações — C5 |
| **Migrations aplicáveis** | ✅ *(2 heads)* | ❌ | `upgrade head` falha — C6 |
| Frontend sem erros TS | ❌ (~85) | ❌ (**153**) | M1 |
| Build de produção | ❌ | ❌ | M1 |
| Artefatos 001–026 | ⏳ | ⚠️ | existem, mas stub — M4 |
| Modelo de dados documentado | ⏳ | ❌ | descreve 12 tabelas inexistentes — §2.2 |

---

## 11. Decisão de auditoria

### Veredito: ❌ **DOM-OUV — NÃO APROVADO PARA PRODUÇÃO**

A revisão 1 concedeu "aprovado para produção" ao backend. Esta revisão **retira** essa
aprovação. O módulo tem boa основа — o domínio está bem modelado, o schema é coerente e
o núcleo de regras de negócio está implementado — mas **não pode ir a produção** enquanto
quatro defeitos críticos existirem:

| # | Achado | Severidade | Por que bloqueia |
| --- | --- | --- | --- |
| **C1** | `NameError` → HTTP 500 na consulta | 🔴 | Serviço básico indisponível; viola LAI art. 8º |
| **C2** | Zero autenticação/autorização | 🔴 | Qualquer anônimo lê e altera dados de cidadãos |
| **C3** | LGPD não aplicada nas respostas | 🔴 | CPF e e-mail em claro, expostos sem auth |
| **C4** | Zero testes | 🔴 | Nenhuma proteção contra regressão |

| Estrato | Status |
| --- | --- |
| **Modelo proposto** | ⚠️ Existe e divergente do código — requer revisão (M4, §2.2) |
| **Backend (código)** | ❌ Reprovado — C1, C2, C3, C4, C5 |
| **Banco (schema `ouv`)** | ✅ Estrutura aprovada; ⚠️ cadeia de migrations a corrigir (C6) |
| **Frontend** | ⚠️ 153 erros — não bloqueia o backend (M1) |
| **Deploy produção** | 🔴 **Bloqueado** |

### 11.1 Plano de ação priorizado

**P0 — bloqueia produção (estimativa: ~1 dia)**

1. **C1** — `presentation/api/__init__.py:389`: `hasattr(p, ...)` → `hasattr(m, ...)`.
2. **C3** — aplicar `ServicoLGPD.mascarar_para_exibicao()` nos 3 mappers de resposta;
   substituir `usuario_autorizado` (query param livre) por identidade do token.
3. **C2** — aplicar a dependência de autenticação do DOM-IDN nas 16 rotas; remover
   `autor_id`/`usuario_id`/`respondido_por` do corpo das requisições.
4. **C4** — criar `tests/unit/test_sigmun_ouvidoria_domain.py` (prazos, transições,
   mascaramento) e `tests/integration/test_ouv_api.py` (as 16 rotas). O caso do
   `GET /manifestacoes/{protocolo}` deve ser o primeiro.

**P1 — necessário para conformidade (estimativa: ~2 dias)**

5. **C6** — criar revision de merge para unificar as duas cabeças do Alembic.
6. **C5** — `ruff check --fix` (237 correções automáticas) e resolver as 167 restantes.
7. **M3** — popular `tramitacoes` nos responses ou criar `GET /manifestacoes/{id}/tramitacoes`.
8. **M2** — emitir eventos de domínio ou remover as 10 classes não utilizadas.

**P2 — qualidade e conclusão (estimativa: ~2 dias)**

9. **M1** — adicionar os imports ausentes em 4 arquivos `.tsx` (resolve 153 erros).
10. **M4** — regenerar artefatos 001–026 a partir do código, corrigindo o
    `013-Modelo-de-Dados` (12 tabelas inexistentes) e o `index.md`.
11. **B1–B5** — limpeza: método duplicado, `__table_args__`, lock no protocolo,
    remover pacotes vazios, `datetime.now(timezone.utc)`.
12. **B3** — adicionar `SELECT ... FOR UPDATE` em `obter_proximo_sequencial`.

### 11.2 Sobre a promoção do `MOD-OUV` na governança

**Não promover ainda.** Registrado para decisão posterior:

| Artefato de governança | Estado atual | Valor a atualizar (após correções) |
| --- | --- | --- |
| `031-Matriz-de-Correspondencia-DOM-MOD.md` | "Preparado / Candidata; validar escopo" | "Implementado e validado" |
| `05-Modulos/index.md` | "Preparado / Candidata" | idem |
| `DOM-OUV/index.md` | "Em elaboração / Preparado" | "Vigente / Implementado" |
| `030-Roadmap-de-Implementacao-dos-Dominios.md` | #30, prioridade Alta | manter |

A atualização deve ocorrer **após** a aprovação da terceira auditoria, para não
divergir do estado real.

---

## 12. Anexos

### A1 — Estrutura de arquivos implementados

```text
src/modules/sigmun_ouvidoria/
├── application/
│   ├── interfaces.py          # 6 Repository ports
│   ├── commands/__init__.py    # vazio
│   ├── queries/__init__.py     # vazio
│   └── use_cases/
│       └── __init__.py        # 11 DTOs + 15 Use Cases
├── domain/
│   ├── entities/
│   │   └── __init__.py        # 4 entidades + Prioridade
│   ├── value_objects/
│   │   └── __init__.py        # 10 VOs + 5 enums
│   ├── events/
│   │   └── __init__.py        # 10 eventos (NENHUM usado)
│   ├── exceptions.py          # 9 exceções de domínio
│   └── services/
│       └── __init__.py        # 6 serviços (ServicoLGPD não usado)
├── infrastructure/
│   ├── database/
│   │   └── __init__.py        # 6 modelos SQLAlchemy + Base
│   ├── repositories/
│   │   └── __init__.py        # 6 repositórios SQLAlchemy
│   └── integrations/__init__.py   # vazio
└── presentation/
    ├── api/
    │   └── __init__.py        # 16 endpoints REST
    └── schemas/
        └── __init__.py        # 21 schemas Pydantic

alembic/versions/20261002_01_dom_ouv_models.py   # migração (revision 20261002_01)

frontend/admin/src/pages/ouv/
├── OuvPage.tsx            # 11 erros TS
├── OuvShared.tsx          # OK
├── VisaoGeralOuv.tsx      # OK
├── ManifestacoesOuv.tsx   # 41 erros TS
├── DenunciasOuv.tsx       # 49 erros TS
├── PedidosLaiOuv.tsx      # 52 erros TS
└── EstatisticasOuv.tsx    # OK

frontend/admin/src/lib/api.ts   # linhas 2837-3102: cliente DOM-OUV
frontend/admin/src/pages/Dashboard.tsx:20  # import e rota `rotaPermitida === 'ouv'`

SIGMUN-Docs/DOM-OUV/
├── index.md               # desatualizado
├── 000- a 026-*.md        # 26 stubs gerados por script
└── puml/                  # 6 diagramas, 24.926 bytes
```

### A2 — Comandos de validação rápida

```bash
# Backend — deve passar
cd /home/gildazio/Projetos-Python/sigmun-v1/sigmun-v1
.venv/bin/python -c "from src.modules.sigmun_ouvidoria.presentation.api import router; print('Router OK')"
.venv/bin/python -c "from src.main import app; print('Main OK')"

# Deve falhar até a criação do merge (C6)
alembic upgrade head

# Deve retornar 0 após as correções (C5)
.venv/bin/python -m ruff check src/modules/sigmun_ouvidoria

# Deve retornar 0 após a correção de C1
.venv/bin/python -m ruff check --select F821 src/modules/sigmun_ouvidoria

# Deve passar após a correção de M1
cd frontend/admin && npx tsc -b --pretty false

# Banco
PGPASSWORD=sigmun psql -h localhost -p 5433 -U sigmun -d sigmun -c "\dt ouv.*"
```

### A3 — Teste de regressão para o defeito C1

Este teste é o que teria evitado a entrega do defeito. Deve ser o primeiro
`tests/integration/test_ouv_api.py`:

```python
def test_obter_manifestacao_por_protocolo(client, seed_manifestacao):
    """C1: GET por protocolo deve responder 200 para todos os tipos."""
    for protocolo in ("2026-000001", "2026-000002", "2026-000003"):
        r = client.get(f"/api/v1/ouv/manifestacoes/{protocolo}")
        assert r.status_code == 200, f"{protocolo} → {r.status_code}"
```

### A4 — Riscos de não conformidade

| Risco | Probabilidade | Impacto | Mitigação |
| --- | --- | --- | --- |
| Exposição de CPF/e-mail de denunciantes | Alta (ocorre hoje) | Multa LGPD + dano reputacional | C2 + C3 |
| Cliente sem conseguir consultar o protocolo | Alta (ocorre hoje) | Reclamação pública | C1 |
| Colisão de protocolo em concorrência | Média | Duplicidade de protocolo | B3 (`FOR UPDATE`) |
| Implantação bloqueada por 2 heads | Alta | Pipeline novo falha | C6 (merge revision) |
| Documentação induziu decisão errada | Ocorrida | Retrabalho | M4 (regenerar artefatos) |

---

## 13. Registro de revisão

| Versão | Data | Descrição | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-10-03 | Auditoria inicial: backend declarado aprovado para produção | Equipe SIGMUN |
| 2.0 | 2026-10-03 | Reexecução integral com verificação em runtime; 9 afirmações da v1.0 corrigidas; aprovação retirada | Equipe SIGMUN |

**Nota metodológica:** a revisão 2 não herdou nenhum resultado da revisão 1. Todos os
números foram medidos novamente. Onde há divergência, prevalece a medição.

---

**Documento:** `AUDITORIA-DOM-OUV-2026-10-03.md`
**Revisão:** 2.0
**Data:** 2026-10-03
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
**Status da auditoria:** Reprovado para produção — C1, C2, C3, C4 em aberto
**Próxima revisão:** após resolução dos itens P0 e execução da suíte de testes
