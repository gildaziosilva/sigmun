# ADR-0007 — Autenticação, revisão cadastral e compartilhamento de pessoa (DOM-CUM)

**Classificação da Informação:** Pública
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente

## 1. Contexto

Os artefatos `001`–`026` do `DOM-CUM` registravam três lacunas: uso de header
`X-Usuario-Id` provisório no lugar da autenticação do `DOM-IDN`; ausência de
política de revisão de dados cadastrais desatualizados; e ausência de contrato
formal de compartilhamento de pessoa com o `DOM-PES` e o `DOM-ASS`.

## 2. Decisão

### 2.1 Autenticação pelo DOM-IDN (lacuna resolvida)

As operações de escrita do cadastro passam a exigir credencial:

* `src/shared/security/jwt.py#get_current_user_hybrid` valida
  `Authorization: Bearer <access token>` emitido por
  `POST /api/v1/idn/auth/login/jwt` e **rejeita a requisição (401) quando não há
  credencial**;
* o header `X-Usuario-Id` permanece aceito **apenas** como compatibilidade
  durante a transição, com `X-Usuario-Papel` opcional, e está marcado como
  `[DEPRECADO]`;
* `POST`, `PATCH` e `DELETE` de `pessoas_router.py` e `unidades_router.py` usam a
  dependência obrigatória; consultas (`GET`) seguem o mesmo padrão quando
  expõem dado pessoal.

**Consequência:** o `created_by`/`updated_by` gravado no schema `core` passa a
refletir o usuário autenticado, e não um identificador livre enviado pelo cliente.
O `DELETE` já usava a dependência obrigatória; os demais endpoints foram
alinados.

### 2.2 Revisão periódica de dados cadastrais

* **Critério:** pessoa é considerada desatualizada quando
  `updated_at` (ou `created_at`) for anterior a **12 meses** e não houver
  atualização por outro domínio consumidor.
* **Periodicidade:** verificação mensal por tarefa agendada (Celery beat) e
  conferência trimestral pela governança cadastral.
* **Responsável:** `AT-CUM-001` (Operador de Cadastro) para a atualização;
  `AT-CUM-004` (Administrador do SIGMUN) pelo acompanhamento.
* **Efeito:** a pessoa recebe marca de revisão pendente e entra no relatório de
  qualidade; **não** há exclusão automática nem alteração de dado sem ato
  administrativo.
* **Indicador:** percentual de pessoas com cadastro revisado nos últimos 12 meses,
  publicado ao `DOM-IND`.

### 2.3 Compartilhamento de pessoa com DOM-PES e DOM-ASS

* O `DOM-CUM` é a **fonte oficial** de pessoa (`core.pessoas` e extensões) e de
  unidade administrativa; qualquer consumidor referencia por **identificador
  opaco** (`pessoa_id`/`unidade_id` em `TEXT`), sem chave estrangeira e sem cópia
  de dados.
* `DOM-PES` (servidor) e `DOM-ASS` (família CadÚnico) consomem o contrato do
  `DOM-CUM`; o `DOM-CUM` não recebe dados de vínculo funcional ou de benefício social.
* Dados pessoais/documentos trafegam pelo `DOM-IDN` (autenticação), `DOM-GDO`
  (anexos) e `DOM-MET` (classificação); o `DOM-CUM` mantém apenas o
  identificador do documento.
* Alteração de dado sensível no cadastro gera evento de auditoria para o
  consumidor, permitindo rastreabilidade sem acoplamento de schema.

## 3. Consequências

* **Positivamente:** a autorização deixa de depender de header controlado pelo cliente;
* a revisão periódica passa a ser rotina verificável, com indicador próprio;
* o compartilhamento deixa de ser implícito e passa a ter fonte oficial e
  fronteira explícita;
* o header legado permanece aceito até a desativação, anunciada em janela de
  transição, e então pode ser removido sem alteração de contrato dos domínios
  consumidores.

## 4. Alternativas consideradas

* Manter apenas o header `X-Usuario-Id`: rejeitada por permitir falsificação de
  autoria.
* Exigir token em toda consulta: rejeitada por impacto em integrações de
  servidor; a obrigatoriedade fica nas operações de escrita e nas consultas de
  dado pessoal.

## 5. Referências

* `src/shared/security/jwt.py`, `src/modules/sigmun_idn/presentation/api/__init__.py`
* `src/modules/sigmun_cadastro/presentation/api/{pessoas,unidades}_router.py`
* `SIGMUN-Docs/DOM-CUM/001-Mapa-de-Atores-Cadastro-Unico-Municipal.md`
* `031-Matriz-de-Correspondencia-DOM-MOD.md`
