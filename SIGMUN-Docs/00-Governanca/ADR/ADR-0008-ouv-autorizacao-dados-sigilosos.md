# ADR-0008 — Autorização e sigilo de dados de Ouvidoria (DOM-OUV)

**Classificação da Informação:** Pública  
**Responsável:** Equipe SIGMUN  
**Status da decisão:** Proposta — aguardando aprovação da autoridade municipal competente  
**Status da revisão:** Revisado editorialmente; aprovação de negócio pendente  
**Data de criação:** 2026-10-03  
**Última revisão documental:** 2026-11-18  
**Domínio:** DOM-OUV — Ouvidoria FalaBR / e-OUV Municipal  
**Módulo de referência:** `src/modules/sigmun_ouvidoria` (schema `ouv`)  
**Origem:** `AUDITORIA-DOM-OUV-2026-10-03.md` (revisão 2.0), achados C2 e C3  
**Substitui:** Nenhum

---

## 1. Finalidade e natureza deste registro

Este ADR registra uma **proposta técnica e de negócio** para autenticação, autorização e proteção de dados pessoais e sigilosos tratados pelo DOM-OUV.

As regras descritas neste documento — especialmente a matriz de papéis, os limites de acesso aos dados de denunciantes, o tratamento de manifestações anônimas e o compartilhamento com órgãos externos — **não devem ser consideradas política municipal aprovada**. Sua adoção depende de manifestação expressa da autoridade municipal competente, após análise pelas áreas responsáveis pela Ouvidoria, proteção de dados, controle interno e assessoria jurídica, conforme as competências locais.

A revisão documental de 2026-11-18 organiza o conteúdo e separa proposta, histórico de implementação e critérios de validação. Ela **não equivale à aprovação da proposta**, não atesta conformidade jurídica e não comprova que o comportamento atual do sistema corresponda ao descrito.

## 2. Contexto e achados que motivaram a proposta

A auditoria de 2026-10-03 (revisão 2.0) registrou dois achados críticos de segurança no DOM-OUV:

- **C2** — a auditoria informou que nenhum dos 16 endpoints sob `/api/v1/ouv` exigia autenticação ou autorização. Também registrou que `autor_id`, `usuario_id` e `respondido_por` eram recebidos no corpo da requisição sem validação da identidade. Segundo o relatório, um `POST /manifestacoes` sem `Authorization` gravou um registro real durante a auditoria (protocolo `2026-000004`).
- **C3** — a auditoria identificou os métodos `ServicoLGPD.mascarar_para_exibicao()` e `Denuncia.get_dados_sigilosos()`, mas informou que eles não eram chamados pela camada de apresentação, expondo campos como CPF e e-mail sem a proteção esperada.

O relatório também apontou que `GET /manifestacoes/{id}` recebia `usuario_perfil` e `usuario_autorizado` como parâmetros de consulta controlados pelo cliente, o que não constitui fonte confiável de autorização.

Esses registros são **achados históricos atribuídos à auditoria de 2026-10-03**. A situação atual deve ser confirmada por inspeção do código, testes e verificação do ambiente antes de qualquer conclusão sobre exposição vigente.

### 2.1 Referencial normativo a considerar

A proposta considera, entre outras normas cuja aplicação concreta deve ser validada pelas áreas competentes:

- Lei nº 12.527/2011 (Lei de Acesso à Informação);
- Lei nº 13.709/2018 (Lei Geral de Proteção de Dados Pessoais);
- Lei nº 13.460/2017 (direitos dos usuários dos serviços públicos);
- Decreto nº 9.492/2018, quando aplicável ao arranjo institucional de ouvidoria.

A citação dessas normas não representa parecer jurídico nem afirma que uma regra específica deste ADR decorra automaticamente de um dispositivo legal. A interpretação, a base legal do tratamento, as hipóteses de sigilo e os procedimentos de compartilhamento precisam de validação jurídica e institucional.

## 3. Regras propostas de negócio e proteção da informação

As subseções seguintes preservam a matriz e as regras constantes da proposta original. Todas permanecem **sujeitas à aprovação municipal**.

### 3.1 Identidade e autenticação pelo DOM-IDN

Propõe-se utilizar o mecanismo de autenticação compartilhado do DOM-IDN, tomando como referência técnica `src/shared/security/jwt.py#get_current_user_hybrid` e o contexto `JWTUsuarioContexto`.

A identidade do usuário autenticado deverá ser obtida de credencial validada pelo servidor — por exemplo, token Bearer válido — e não de identificadores ou perfis declarados livremente no corpo ou em parâmetros da requisição.

A proposta original também menciona a aceitação transitória do header legado `X-Usuario-Id`. Essa possibilidade não deve ser interpretada como autorização para confiar isoladamente nesse header: sua utilização, se ainda existir, depende de validação de segurança específica e de prazo formal de descontinuação. A política-alvo deve evitar mecanismos que permitam ao cliente escolher a identidade que o sistema atribui à operação.

Os campos de auditoria, como `created_by`, `updated_by` e `respondido_por`, devem derivar da identidade autenticada e validada pelo servidor.

### 3.2 Manifestações anônimas

Propõe-se que os fluxos de criação de manifestações, denúncias e pedidos LAI possam admitir protocolo sem autenticação, caso essa modalidade seja confirmada como necessária e juridicamente adequada ao serviço municipal.

As rotas de criação anônima deverão ser explicitamente delimitadas. A possibilidade de protocolar anonimamente não implica acesso anônimo a consultas, documentos, dados pessoais, denúncias ou informações de acompanhamento restrito.

Quando houver identidade autenticada, ela poderá ser associada ao registro conforme a finalidade e a base legal aplicáveis. Quando não houver, o sistema deverá representar corretamente a ausência de identificação, sem aceitar que o cliente atribua arbitrariamente a manifestação a outro usuário.

**Atenção:** a definição das rotas efetivamente anônimas, dos dados mínimos exigidos, dos recibos e dos mecanismos de acompanhamento depende de aprovação funcional e validação jurídica. Não se deve presumir que todos os três endpoints citados na proposta original devam permanecer públicos sem autenticação.

### 3.3 Matriz proposta de acesso por papel

A matriz abaixo reproduz a proposta original. Não constitui concessão de acesso vigente nem substitui a definição formal de atribuições, segregação de funções e perfis pela Prefeitura.

| Papel proposto | Dados de identificação do denunciante | Acesso à denúncia |
| --- | --- | --- |
| `ouvidor` | Integral, quando necessário à atribuição funcional | Sim, conforme atribuição |
| `corregedor` | Integral, quando necessário à atribuição funcional | Sim, conforme atribuição |
| `auditor` | Conforme necessidade, escopo e autorização formal de auditoria | Somente leitura, conforme escopo |
| `admin` | Não, segundo a proposta | Apenas metadados técnicos ou agregados, sem identificação |
| `servidor` | Não, segundo a proposta | Não, salvo atribuição formal específica a ser deliberada |

**Princípio proposto:** administração técnica da plataforma não confere, por si só, autoridade funcional para consultar a identidade de denunciantes. Acesso a dados sensíveis deve observar necessidade, finalidade, atribuição, rastreabilidade e autorização formal.

A proposta original prevê acesso integral para os papéis `ouvidor` e `corregedor`, e acesso de leitura para `auditor`. A extensão e os limites desse acesso — inclusive o significado de “integral” — precisam ser definidos pela autoridade municipal e validados juridicamente antes da aprovação.

### 3.4 Omissão de dados para usuários não autorizados

A proposta original prefere a **omissão dos campos protegidos**, em vez de mascaramento parcial, para usuários sem autorização.

Como comportamento-alvo proposto:

- os campos de identificação do denunciante não devem ser retornados a quem não tenha autorização;
- campos de identificação de servidor envolvido devem ser protegidos conforme a classificação e a finalidade;
- os dados operacionais estritamente necessários ao tratamento poderão ser apresentados conforme perfil, atribuição e necessidade;
- a ausência de um campo protegido deve ser consistente em respostas, exportações, relatórios, logs acessíveis e demais canais de apresentação.

O mascaramento visual não substitui autorização no servidor. Da mesma forma, omitir um campo em uma tela não é suficiente se ele continuar disponível por API, exportação, log ou outro endpoint.

A definição de quais campos podem ser apresentados em cada contexto deve constar de especificação funcional e ser validada com as áreas competentes.

### 3.5 Compartilhamento com órgãos externos

A proposta original estabelece como regra de proteção que o encaminhamento de denúncia a órgão externo não inclua automaticamente a identificação do denunciante.

Propõe-se que qualquer compartilhamento seja limitado à finalidade, à competência do destinatário e à base legal aplicável, com registro de quem realizou o envio, quando, para quem, quais dados foram compartilhados e sob qual justificativa.

A regra não deve ser interpretada como proibição absoluta de compartilhamento em qualquer hipótese. As situações em que a identificação possa ou deva ser compartilhada precisam de análise jurídica e decisão institucional específica.

### 3.6 Ações de tratamento e papéis funcionais

A tabela abaixo preserva a distribuição funcional proposta originalmente. Ela depende de validação pela área municipal responsável pela Ouvidoria e pelas unidades envolvidas.

| Ação | Papéis propostos | Observação |
| --- | --- | --- |
| Registrar manifestação | Anônimo ou autenticado, conforme fluxo aprovado | Apenas criação; não concede acesso a consultas |
| Responder ao cidadão | `ouvidor`, `corregedor` | Conforme atribuição formal |
| Alterar status | `ouvidor`, `corregedor` | Conforme atribuição formal |
| Prorrogar prazo | `ouvidor`, `corregedor` | Conforme atribuição formal e regras do serviço |
| Avaliar atendimento | `ouvidor`, `corregedor` | Conforme atribuição formal |
| Encaminhar denúncia a órgão externo | `ouvidor`, `corregedor` | Com finalidade, destinatário e dados autorizados |
| Decidir recurso LAI | A definir pela autoridade competente | Não presumir competência apenas pelo papel técnico |
| Consultar listas e indicadores | Conforme perfil e conteúdo | Indicadores devem evitar exposição indevida de dados pessoais |

A competência para decidir recursos LAI e as atribuições de cada papel devem ser confirmadas à luz da regulamentação municipal. A matriz não substitui essa definição.

### 3.7 Parâmetros de perfil e autorização

Os parâmetros `usuario_perfil` e `usuario_autorizado` recebidos do cliente não podem ser tratados como prova de identidade ou autorização.

Propõe-se removê-los das interfaces públicas de consulta e derivar as permissões do contexto autenticado, das atribuições vigentes e das regras de autorização aplicadas no servidor. O caso de uso e as rotas correspondentes devem receber contexto confiável, não declarações de perfil fornecidas pelo solicitante.

---

## 4. Consequências esperadas

### 4.1 Benefícios esperados

- Reduzir o risco de autoatribuição de autoria e de acesso indevido a dados pessoais.
- Centralizar a identidade no mecanismo de autenticação compartilhado.
- Aplicar autorização no servidor, e não em parâmetros controlados pelo cliente.
- Tornar explícitas as regras de proteção de dados em consultas, relatórios e exportações.
- Estabelecer rastreabilidade para operações de acesso e compartilhamento.

Esses benefícios são objetivos esperados da proposta, não resultados comprovados por este ADR.

### 4.2 Riscos e dependências

| Risco ou dependência | Tratamento proposto |
| --- | --- |
| Clientes atuais dependem de identificadores enviados no corpo | Inventariar consumidores, definir migração e descontinuação compatíveis |
| Papéis funcionais não existem ou não estão vinculados corretamente | Validar catálogo, atribuições e vínculos com a Administração Municipal |
| Mudanças afetam contratos de API | Atualizar especificações, OpenAPI e consumidores antes da implantação |
| Regras de sigilo não estão formalmente aprovadas | Obter aprovação funcional e jurídica antes de ativar controles definitivos |
| Acesso excessivo por perfis privilegiados | Aplicar menor privilégio, segregação de funções e auditoria de acesso |
| Dados podem vazar por canais secundários | Testar APIs, relatórios, exportações, logs, tarefas assíncronas e integrações |

## 5. Alternativas consideradas

As alternativas abaixo foram registradas na proposta original e permanecem sujeitas à reavaliação durante a aprovação:

| Alternativa | Avaliação registrada na proposta |
| --- | --- |
| Manter `usuario_perfil` e `usuario_autorizado` como parâmetros livres | Rejeitada como mecanismo de autorização, pois são controlados pelo cliente |
| Utilizar apenas mascaramento parcial para usuários não autorizados | Considerada insuficiente como controle de acesso; não substitui a omissão ou a autorização no servidor |
| Criar autenticação independente para o DOM-OUV | Não recomendada se o DOM-IDN fornecer mecanismo adequado e validado |
| Conceder acesso irrestrito a dados sensíveis ao administrador técnico | Rejeitada pela proposta, em razão da separação entre administração técnica e atribuição funcional |
| Negar toda a denúncia a qualquer usuário sem acesso à identidade | Alternativa a avaliar conforme a necessidade de tratamento, sem expor os campos protegidos |

## 6. Histórico de implementação registrado em 2026-10-03

Esta seção preserva informações que constavam na versão anterior do ADR. Elas são **registros históricos transcritos do documento**, não certificação de que o código, o banco de dados ou o ambiente atual continuam no mesmo estado.

### 6.1 Papéis e permissões no seed do DOM-IDN

A versão anterior registrava que os papéis e permissões de Ouvidoria haviam sido incluídos em `src/modules/sigmun_idn/infrastructure/database/seeds.py`, com os seguintes identificadores:

- `PERMISSOES_OUV`: conjunto de permissões `OUV.*`;
- `ROLE_OUVIDOR`;
- `ROLE_CORREGEDOR`;
- `ROLE_AUDITOR`;
- `ROLE_ADMIN`.

O registro anterior também descrevia a generalização das funções `_criar_permissoes` e `_criar_roles`, mantendo a assinatura de `popular_seed_idn(session)`.

A versão anterior continha uma consulta de banco que indicava 10 permissões OUV para `ROLE_OUVIDOR` e `ROLE_CORREGEDOR`, 3 para `ROLE_AUDITOR` e 2 para `ROLE_ADMIN`. A consulta indicava que `ROLE_ADMIN` não possuía a permissão `OUV.DENUNCIA.SENSITIVOS_CONSULTAR`, enquanto os outros três papéis a possuíam.

**Ressalva:** essa evidência é histórica e não demonstra o estado atual do seed ou de qualquer banco. A matriz técnica efetiva deve ser reconsultada e comparada com a política que vier a ser aprovada.

### 6.2 Usuário demonstrativo de Ouvidoria

A versão anterior registrava a criação de um script `scripts/seed_ouv_usuario_teste.py` para gerar um usuário demonstrativo vinculado à `ROLE_OUVIDOR`, com login `demo.ouvidoria.ouvidor`.

O registro também afirmava que o usuário foi criado e que o vínculo foi verificado no banco. A senha não é reproduzida neste ADR.

O documento anterior declarava expressamente que esse usuário era demonstrativo, não poderia ser utilizado em produção e deveria ser desativado e substituído por vínculos de servidores reais quando as designações funcionais fossem definidas.

**Ressalva:** a existência, o estado e os vínculos atuais desse usuário não foram revalidados nesta revisão. A conta demonstrativa deve ser verificada e, se ainda existir, permanecer bloqueada para uso operacional e ser removida ou desativada conforme procedimento seguro antes de qualquer implantação produtiva.

### 6.3 Evidências de execução anteriormente registradas

A versão anterior apresentava saídas atribuídas às execuções de:

- `.venv/bin/python scripts/seed_idn.py --dry-run`;
- `.venv/bin/python scripts/seed_idn.py`;
- segunda execução do seed para demonstrar idempotência;
- `.venv/bin/python scripts/seed_ouv_usuario_teste.py --dry-run`;
- execução e segunda execução do script de usuário demonstrativo;
- consulta SQL para verificar o usuário e seu vínculo.

Essas saídas foram preservadas como histórico documental. Não foram repetidas nem verificadas no âmbito desta revisão do ADR.

---

## 7. Critérios de aceite e validação

Os critérios abaixo são requisitos propostos. Permanecem **pendentes de comprovação atual**; nenhum deve ser considerado concluído apenas porque a implementação foi descrita na seção 6.

- [ ] Todas as rotas de consulta e tratamento exigem autenticação e autorização adequadas.
- [ ] As exceções de criação anônima estão formalmente aprovadas, delimitadas e testadas.
- [ ] Nenhuma resposta a usuário não autorizado expõe CPF, e-mail, identificação do denunciante ou outros campos protegidos.
- [ ] O papel administrativo técnico não obtém acesso aos dados sensíveis apenas por possuir privilégio de administração.
- [ ] A autoria das operações deriva da identidade autenticada no servidor, não de valores fornecidos pelo cliente.
- [ ] Os parâmetros `usuario_perfil` e `usuario_autorizado` não são aceitos como fonte de autorização.
- [ ] Testes automatizados cobrem, no mínimo, respostas 401 e 403, fluxos anônimos aprovados, segregação de papéis e ausência de dados sensíveis em respostas e exportações.
- [ ] O acesso a dados sensíveis e o compartilhamento externo possuem trilha de auditoria.
- [ ] Os papéis, permissões e vínculos de usuários foram verificados no ambiente-alvo.
- [ ] O usuário demonstrativo, se ainda existente, foi desativado ou removido antes da produção.
- [ ] Contratos de API, OpenAPI, documentação funcional e consumidores foram atualizados e validados.

A marcação de cada critério como concluído exige evidência reproduzível, com identificação do ambiente, comando ou procedimento, resultado e data da verificação.

## 8. Pendências para aprovação

Antes de transformar esta proposta em decisão vigente, é necessário:

1. Identificar formalmente a autoridade municipal competente para aprovar a política de acesso e sigilo do DOM-OUV.
2. Submeter a matriz de papéis e os limites de acesso às áreas de Ouvidoria, Corregedoria, Controle Interno e proteção de dados.
3. Obter validação jurídica das regras de anonimato, sigilo, tratamento de dados pessoais e compartilhamento com órgãos externos.
4. Confirmar as competências para resposta, prorrogação, avaliação, encaminhamento e decisão de recursos LAI.
5. Registrar a aprovação, a autoridade responsável, a data, o escopo e eventuais ressalvas.
6. Revalidar tecnicamente a implementação e preencher os critérios de aceite com evidências atuais.

Até que essas etapas sejam cumpridas, o status permanece **Proposta — aguardando aprovação**. A existência de código, seeds, testes ou registros históricos de execução não substitui a aprovação da política de negócio.

## 9. Referências

- `AUDITORIA-DOM-OUV-2026-10-03.md` (revisão 2.0) — achados C2 e C3.
- `ADR-0007-cadastro-autenticacao-revisao-compartilhamento.md` — referência arquitetural de autenticação e contexto de usuário, sujeita à compatibilidade com a implementação vigente.
- `src/shared/security/jwt.py` — referências técnicas citadas na proposta original: `get_current_user_hybrid`, `JWTUsuarioContexto` e `require_roles_hybrid`.
- `src/modules/sigmun_ouvidoria/domain/services/__init__.py` — referência histórica a `ServicoLGPD`.
- `src/modules/sigmun_ouvidoria/domain/entities/__init__.py` — referência histórica a `Denuncia.get_dados_sigilosos`.
- Legislação citada na seção 2.1, cuja aplicação concreta deve ser validada pelas áreas competentes.

---

**Documento:** `ADR-0008-ouv-autorizacao-dados-sigilosos.md`  
**Responsável pelo registro:** Equipe SIGMUN  
**Última atualização:** 2026-11-18  
**Status da decisão:** Proposta — aguardando aprovação da autoridade municipal competente  
**Próxima revisão:** após manifestação formal da autoridade competente ou quando houver alteração relevante de legislação, política municipal, arquitetura ou implementação.
