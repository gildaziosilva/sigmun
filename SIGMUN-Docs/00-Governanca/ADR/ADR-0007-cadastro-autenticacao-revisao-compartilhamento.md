# ADR-0007 — Autenticação, revisão cadastral e compartilhamento de pessoa (DOM-CUM)

**Classificação da Informação:** Pública
**Responsável:** Equipe SIGMUN
**Status da decisão:** Registrada neste ADR; aprovação institucional não documentada
**Status da revisão:** Vigente

## 1. Contexto

Os artefatos `001`–`026` do `DOM-CUM` registravam três lacunas: uso de header
`X-Usuario-Id` provisório no lugar da autenticação do `DOM-IDN`; ausência de
política de revisão de dados cadastrais desatualizados; e ausência de contrato
formal de compartilhamento de pessoa com o `DOM-PES` e o `DOM-ASS`.

## 2. Decisão

### 2.1 Autenticação pelo DOM-IDN (lacuna resolvida)

As operações de escrita do cadastro exigem credencial JWT validada pelo DOM-IDN:

* `Authorization: Bearer <access token>`, emitido por
  `POST /api/v1/idn/auth/login/jwt`, é a credencial de autenticação esperada;
* `get_current_user_hybrid` pode manter compatibilidade técnica com headers
  legados somente quando `ALLOW_LEGACY_HEADERS=True`. Conforme o ADR-0009,
  essa flag tem padrão `False`; portanto, o fallback legado fica desabilitado
  por padrão e não deve ser habilitado em produção;
* `X-Usuario-Id` e `X-Usuario-Papel` não constituem credenciais válidas para
  autorizar operações nem para atribuir papéis. O ADR-0009 determina que
  `require_roles_hybrid()` utilize JWT estrito por meio de
  `get_current_user_jwt()`; headers legados nunca conferem papel;
* a ativação temporária da flag em `tests/conftest.py`, descrita no ADR-0009,
  é restrita ao processo de testes para compatibilidade com testes legados e
  não representa configuração autorizada para produção;
* `POST`, `PATCH` e `DELETE` de `pessoas_router.py` e `unidades_router.py` usam a
  dependência obrigatória; consultas (`GET`) seguem o mesmo padrão quando
  expõem dado pessoal, conforme a política de acesso aplicável.

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

* **Positivamente:** a autorização deixa de depender de headers controlados pelo cliente;
* o fallback legado fica desabilitado por padrão (`ALLOW_LEGACY_HEADERS=False`),
  conforme o ADR-0009; eventual uso restrito a testes não altera essa regra;
* a revisão periódica passa a ser rotina verificável, com indicador próprio;
* o compartilhamento deixa de ser implícito e passa a ter fonte oficial e
  fronteira explícita.

## 4. Alternativas consideradas

* Manter apenas o header `X-Usuario-Id`: rejeitada por permitir falsificação de
  autoria.
* Utilizar headers legados como fallback de autenticação em produção: não
  adotada; o ADR-0009 estabelece `ALLOW_LEGACY_HEADERS=False` por padrão e
  determina que headers legados nunca confiram papéis.
* Exigir token em toda consulta: rejeitada por impacto em integrações de
  servidor; a obrigatoriedade fica nas operações de escrita e nas consultas de
  dado pessoal.

## 5. Referências

* `src/shared/security/jwt.py`, `src/modules/sigmun_idn/presentation/api/__init__.py`
* `src/modules/sigmun_cadastro/presentation/api/{pessoas,unidades}_router.py`
* `SIGMUN-Docs/DOM-CUM/001-Mapa-de-Atores-Cadastro-Unico-Municipal.md`
* `031-Matriz-de-Correspondencia-DOM-MOD.md`
