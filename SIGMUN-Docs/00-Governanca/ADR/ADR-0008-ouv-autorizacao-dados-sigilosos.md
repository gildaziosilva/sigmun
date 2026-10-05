# ADR-0008 — Autorização e sigilo de dados de Ouvidoria (DOM-OUV)

**Classificação da Informação:** Pública
**Responsável:** Equipe SIGMUN
**Status da revisão:** Proposto — aguardando aprovação
**Data:** 2026-10-03
**Domínio:** DOM-OUV — Ouvidoria FalaBR / e-OUV Municipal
**Módulo:** `src/modules/sigmun_ouvidoria` (schema `ouv`)
**Origem:** `AUDITORIA-DOM-OUV-2026-10-03.md` (revisão 2.0) — achados C2 e C3
**Substitui:** nada

---

## 1. Contexto

A auditoria de 2026-10-03 (revisão 2.0) identificou dois achados críticos de segurança
no `DOM-OUV`:

* **C2** — nenhum dos 16 endpoints sob `/api/v1/ouv` exige autenticação ou autorização.
  `autor_id`, `usuario_id` e `respondido_por` chegam **do corpo da requisição**, sem
  verificação. Um `POST /manifestacoes` sem header `Authorization` foi confirmado
  gravando registro real (protocolo `2026-000004`) durante a auditoria.
* **C3** — `ServicoLGPD.mascarar_para_exibicao()` e `Denuncia.get_dados_sigilosos()`
  existem e estão corretos no domínio, mas **nunca são chamados** pela camada de
  apresentação. As respostas entregam `cpf` e `email` **em claro**.

Além disso, `GET /manifestacoes/{id}` recebe `usuario_perfil` e `usuario_autorizado`
como **query parameters livres** (`presentation/api/__init__.py:381-382`): quem os envia,
os controla.

**Regulamentação aplicável:**

* Lei 12.527/2011 (LAI), art. 24 — restrição de acesso a informações sob sigilo;
* Lei 13.709/2018 (LGPD), art. 6º III e art. 46 — necessidade e segurança do tratamento;
* Lei 13.460/2017 — dever de proteção ao cidadão e ao denunciante;
* Decreto 9.492/2018 — requisitos de transparência e proteção em ouvidoria.

A decisão sobre **quem pode ver o quê** é de negócio, não de engenharia. Este ADR fixa
essa decisão **antes** da implementação (Onda 1 do plano de trabalho).

---

## 2. Decisões

### 2.1 Autenticação pelo DOM-IDN (aplica-se o padrão já existente)

As 16 rotas passam a depender de `src/shared/security/jwt.py#get_current_user_hybrid`,
**já usada por 8 routers** de `sigmun_compras` e `sigmun_cadastro`:

* `Authorization: Bearer <access token>` (emitido por `POST /api/v1/idn/auth/login/jwt`)
  é a forma **obrigatória**;
* o header legado `X-Usuario-Id` permanece aceito **apenas** durante a transição, já
  marcado como `[DEPRECADO]` na assinatura da dependência;
* a identidade passa a derivar de `JWTUsuarioContexto` — `usuario_id`, `login`, `roles`,
  `unidades_ids` — e **não** do corpo da requisição.

**Consequência:** `created_by`, `updated_by` e `respondido_por` passam a refletir o
usuário autenticado, eliminando a auto-atribuição de autoria. Alinhamento com ADR-0007.

### 2.2 Exceção: manifestação anônima permanece pública

`POST /manifestacoes`, `POST /denuncias` e `POST /pedidos-lai` **aceitam requisição
anônima**, com `autor_id` derivado do token **quando presente** e vazio quando ausente.

**Justificativa:** a Lei 12.527/2011 e o Decreto 9.492/2018 exigem que o cidadão possa
protocolar **sem** conta no sistema. Impedir o registro anônimo violaria o direito de
manifestação. O domínio mantém `cidadao_anonimo` para qualificar esse fluxo.

**Limite:** a exceção vale **apenas** para criação. Toda consulta exige autenticação.

### 2.3 Papéis autorizados a acessar dados do denunciante

`ServicoLGPD.pode_acessar_dados_sensiveis` hoje referencia
`["ouvidor", "corregedor", "auditor", "admin"]`. Fica **confirmado**:

| Papel | Dados do denunciante | Denúncia como um todo |
| --- | --- | --- |
| `ouvidor` | Sim, integral | Sim |
| `corregedor` | Sim, integral | Sim |
| `auditor` | Sim, integral | Sim, somente leitura |
| `admin` | **Não** | Somente metadados agregados |
| `servidor` | **Não** | **Não** |

**Decisão-chave:** `admin` **não** tem acesso ao dado sensível. A administração técnica do
sistema não é autoridade funcional sobre a identificação de um denunciante. Só os papéis
com atribuição de proteção ao cidadão (ouvidoria, corregedoria, auditoria) o acessam.

### 2.4 Sigilo: negação total, não acesso parcial

Quando o solicitante **não** possui papel autorizado (2.3), a resposta à denúncia é
**omissiva**, não mascarada:

* o bloco `cidadao` é **ausente** (não `null`, não parcialmente preenchido);
* `servidor_envolvido` é **ausente**;
* os demais campos (assunto, descrição, tipo, status, prazos) permanecem, por serem
  necessários ao tratamento da denúncia.

**Justificativa:** mascaramento parcial (`***.123.***-45`) confirma ao solicitante **a
existência** de um CPF associado, o que já é informação protegida. A Lei 12.527/2011,
art. 24, e a LGPD, art. 46, favorecem negação total.

**Consequência:** `DadosCidadao.para_exibicao()` continua disponível para **exibição em
tela** a partir de um papel autorizado (filtro visual), mas **não** substitui a regra de
autorização.

### 2.5 Órgão de destino não tem acesso ao denunciante

O órgão externo receptor (MP, PF, TCE, TCU, CGU) de uma denúncia **não** recebe, por
meio do SIGMUN, o `cpf` do denunciante. O encaminhamento transmite os fatos e o número de
processo, não a identificação de origem.

**Justificativa:** o sigilo de fonte é proteção essencial em investigações de corrupção;
o órgão receptor trata a denúncia como recebida, sem vínculo com o denunciante no sistema.

### 2.6 Ações de tratamento exigem papel funcional

| Ação | Papéis | Rota |
| --- | --- | --- |
| Registrar manifestação | anônimo ou autenticado | `POST /manifestacoes` |
| Responder ao cidadão | `ouvidor`, `corregedor` | `POST /{id}/responder` |
| Alterar status | `ouvidor`, `corregedor` | `POST /{id}/status` |
| Prorogar prazo | `ouvidor`, `corregedor` | `POST /{id}/prorrogar` |
| Avaliar atendimento | `ouvidor`, `corregedor` | `POST /{id}/avaliar` |
| Encaminhar denúncia a órgão externo | `ouvidor`, `corregedor` | `POST /denuncias/{id}/encaminhar` |
| Decidir recurso LAI | `ouvidor`, `corregedor` | `POST /pedidos-lai/{id}/decidir-recurso` |
| Consultar listas e indicadores | `ouvidor`, `corregedor`, `auditor`, `admin` | `GET` diversos |

**Prorrogação e avaliação ficam restritas ao papel funcional** porque alteram a relação
de atendimento com o cidadão — não são ações administrativas de sistema.

### 2.7 Autenticação, não autorização, nos parâmetros livres
---

## 3. Consequências

### 3.1 Positivas

* Elimina a auto-atribuição de autoria e o acesso anônimo a dados pessoais.
* Alinha o `DOM-OUV` ao padrão já vigente em `sigmun_compras` e `sigmun_cadastro` — sem
  criar mecanismo novo de autenticação.
* Disponibiliza `ServicoLGPD` e `get_dados_sigilosos`, hoje código morto.
* Atende C2 e C3, pré-requisito para aprovação do domínio.

### 3.2 Negativas e riscos

| Risco | Mitigação |
| --- | --- |
| Quebrar clientes atuais que enviam `autor_id` | Migrar em duas etapas: aceitar e deprecá-lo antes de remover |
| Papel `ouvidor` não existir no seed do DOM-IDN | Verificar antes da Onda 1; se faltar, incluir no seed |
| Migrar de query param para token altera o contrato da API | Registrar no artefato `010-Especificacoes` e no OpenAPI |

### 3.3 Neutras

* A regra de sigilo passa a ser aplicada em **duas** camadas: omissão na resposta (2.4)
  e restrição de perfil (2.3). A segunda é obrigatória; a primeira é consequência.

---

## 4. Alternativas consideradas

| # | Alternativa | Por que **não** escolhida |
| --- | --- | --- |
| 1 | Manter query params `usuario_perfil`/`usuario_autorizado` | Inviável: são controlados pelo cliente, portanto não constituem autorização |
| 2 | Mascaramento parcial para não-autorizados | Rejeitada em 2.4 — confirma a existência do dado protegido |
| 3 | Criar autenticação específica do DOM-OUV | Rejeitada — o DOM-IDN já resolve; duplicaria credenciais |
| 4 | `admin` com acesso total aos dados | Rejeitada em 2.3 — separação entre função técnica e funcional |
| 5 | Negação total à denúncia inteira para não-autorizados | Rejeitada — impede o tratamento pelo citizen responsável |

---

## 5. Implementação

Planejada na **Onda 1** do `TODO-dom-ouv.md`:

| Tarefa | Descrição |
| --- | --- |
| 1.1 | Dependência `get_current_user_hybrid` nas 16 rotas |
| 1.2 | Remover `autor_id`/`usuario_id`/`respondido_por` do corpo |
| 1.3 | Remover `usuario_perfil`/`usuario_autorizado` da query |
| 1.4 | Aplicar `ServicoLGPD.mascarar_para_exibicao()` nos 3 mappers |
| 1.5 | Ativar `get_dados_sigilosos` conforme 2.4 |
| 1.6 | Testes de segurança (401, 403, ausência de CPF em claro) |

**Pré-requisito:** os papéis `ouvidor` e `corregedor` devem existir no `DOM-IDN`.

### 5.1 Constatação verificada em 2026-10-03 (bloqueante para a Onda 1)

A verificação no banco mostrou que **os papéis ainda não existem**:

```text
$ psql -c "select codigo, nome from idn.roles order by 1;"
ROLE_DEMO_COMPRAS_CONSULTA | Consulta de Compras — Demo
ROLE_DEMO_COMPRAS_GESTOR   | Gestão de Compras — Demo
ROLE_DEMO_COMPRAS_OPERADOR | Operador de Compras — Demo
(3 rows)

$ grep -rn 'ouvidor|corregedor' src/modules/sigmun_idn/ --include=*.py
(sem resultado)
```

Os únicos papéis cadastrados são demonstrativos e restritos ao DOM-Compras. **Não há
papel funcional de ouvidoria.** Sem criar `ROLE_OUVIDOR`, `ROLE_CORREGEDOR` e
`ROLE_AUDITOR`, a decisão 2.3 é inaplicável e toda requisição cairia em 403.

**Ação requerida (entrada da Onda 1):** criar os papéis em `idn.roles` e vinculá-los aos
usuários correspondentes em `idn.usuario_roles`, seguindo o padrão de codificação
`ROLE_<DOMINIO>_<PERFIL>` já observado (`ROLE_DEMO_COMPRAS_*`).

| Papel a criar | Codigo sugerido | Atribuição funcional |
| --- | --- | --- |
| Ouvidor | `ROLE_OUVIDOR` | Ouvidoria municipal |
| Corregedor | `ROLE_CORREGEDOR` | Corregedoria / controle interno |
| Auditor | `ROLE_AUDITOR` | Auditoria interna (read-only) |
| Administrador | `ROLE_ADMIN` | Administração técnica (sem acesso ao dado sensível) |

**Fora do escopo deste ADR:** o cadastro dos papéis pertence ao `DOM-IDN`. Este ADR
apenas registra a dependência.

### 5.2 Status — papéis criados em 2026-10-03 ✅

A dependência registrada em 5.1 foi resolvida. Os papéis foram criados no seed do
DOM-IDN, em `src/modules/sigmun_idn/infrastructure/database/seeds.py`:

* `PERMISSOES_OUV` — 10 permissões `OUV.*`;
* `ROLES_OUV` — 4 papéis (§5.1).

As funções `_criar_permissoes` e `_criar_roles` foram **generalizadas** para receber
listas de seeds como parâmetro, permitindo processar `PERMISSOES_DEMO_COMPRAS +
PERMISSOES_OUV` na mesma execução. A assinatura pública de `popular_seed_idn(session)`
foi preservada — `scripts/seed_idn.py` segue compatível sem alteração de chamada.

**Matriz aplicada e verificada no banco:**

```text
$ psql -c "select r.codigo, count(*), bool_or(p.codigo='OUV.DENUNCIA.SENSITIVOS_CONSULTAR')
           from idn.roles r join idn.role_permissoes rp on rp.role_id=r.id
           join idn.permissoes p on p.id=rp.permissao_id
           where p.codigo like 'OUV.%' group by r.codigo order by r.codigo;"

       role       | permissoes_ouv | tem_sensiveis
-----------------+----------------+---------------
 ROLE_ADMIN      |              2 | f     ← conforme §2.3
 ROLE_AUDITOR    |              3 | t
 ROLE_CORREGEDOR |             10 | t
 ROLE_OUVIDOR    |             10 | t
(4 rows)
```

**Evidência de execução:**

```text
$ .venv/bin/python scripts/seed_idn.py --dry-run
[dry-run] Alterações revertidas (nenhum dado gravado).
  Permissões criadas:      10
  Roles criadas:            4
  Associações criadas:     25

$ .venv/bin/python scripts/seed_idn.py
Seed DEMO do DOM-IDN aplicado com sucesso.
  Permissões criadas:      10
  Roles criadas:            4
  Associações criadas:     25

$ .venv/bin/python scripts/seed_idn.py     # 2ª execução (idempotência)
Seed DEMO do DOM-IDN aplicado com sucesso.
  Permissões criadas:       0
  Roles criadas:             0
  Associações criadas:      0
```

**Pendência resolvida em 2026-10-03 — usuário de teste criado.**

Foi criado o script `scripts/seed_ouv_usuario_teste.py`, que gera um usuário
**demonstrativo** vinculado à `ROLE_OUVIDOR`, para destravar a validação da Onda 1
enquanto a Ouvidoria não define quais servidores ocupam cada função.

```text
Login:  demo.ouvidoria.ouvidor
Nome:   Ouvidor — Demo
Papel:  ROLE_OUVIDOR
Status: ativo
Senha:  exibida apenas na criação (PBKDF2-SHA256, mesmo algoritmo de
        AutenticacaoService.criar_hash_senha)
```

**Evidência de execução:**

```text
$ .venv/bin/python scripts/seed_ouv_usuario_teste.py --dry-run
[dry-run] Alterações revertidas (nenhum dado gravado).
  Usuário criado: True | Vínculo criado: True

$ .venv/bin/python scripts/seed_ouv_usuario_teste.py
Usuário de teste da Ouvidoria aplicado com sucesso.
  Usuário criado: True | Vínculo criado: True

$ .venv/bin/python scripts/seed_ouv_usuario_teste.py     # 2ª execução (idempotência)
  Usuário criado: False | Vínculo criado: False
  Nada a fazer — usuario e vinculo ja existiam.

$ psql -c "select u.login, u.status, r.codigo from idn.usuarios u
           join idn.usuario_roles ur on ur.usuario_id=u.id
           join idn.roles r on r.id=ur.role_id where u.login like 'demo.ouvidoria%';"
          login          | status |    papel
------------------------+--------+--------------
 demo.ouvidoria.ouvidor | ativo  | ROLE_OUVIDOR
```

A senha foi validada contra o hash armazenado
(`AutenticacaoService._verificar_senha`): senha correta → `True`, senha errada → `False`.

**Ciclo de vida:** quando os servidores reais forem definidos, este usuário deve ser
desativado (`status='inativo'`) e removido, e substituído pelos vínculos reais.
**Não é permitido uso em produção.**

---

## 6. Critérios de aceite

- [ ] Nenhuma das 16 rotas responde 200 sem `Authorization`, exceto a criação anônima (2.2).
- [ ] Nenhuma resposta a não-autorizado contém `cpf`, `email` ou `servidor_envolvido`.
- [ ] `admin` recebe 403 ao tentar acessar dados do denunciante.
- [ ] `created_by` e `respondido_por` gravam o UUID do token, não valor do corpo.
- [ ] Testes cobrem 401, 403 e ausência de dado sensível em claro.

---

## 7. Referências

* `AUDITORIA-DOM-OUV-2026-10-03.md` (revisão 2.0) — achados C2, C3
* `ADR-0007-cadastro-autenticacao-revisao-compartilhamento.md` — padrão de autenticação
* `src/shared/security/jwt.py` — `get_current_user_hybrid`, `JWTUsuarioContexto`, `require_roles_hybrid`
* `src/modules/sigmun_ouvidoria/domain/services/__init__.py` — `ServicoLGPD`
* `src/modules/sigmun_ouvidoria/domain/entities/__init__.py` — `Denuncia.get_dados_sigilosos`

---

**Documento:** ADR-0008-ouv-autorizacao-dados-sigilosos.md
**Última atualização:** 2026-10-03
**Responsável:** Equipe SIGMUN
**Status da revisão:** Proposto — aguardando aprovação
**Próxima revisão:** após aprovação, ou se a legislação municipal exigir ajuste

`usuario_perfil` e `usuario_autorizado` deixam de ser query parameters e passam a ser
derivados de `usuario_atual`. O caso de uso que hoje os recebe é removido da assinatura
da rota.

