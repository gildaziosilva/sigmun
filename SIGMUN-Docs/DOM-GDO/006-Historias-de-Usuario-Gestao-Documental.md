# 006 – Histórias de Usuário – Gestão Documental

#### Histórias de Usuário – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-006

**Domínio:** Gestão Documental

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Documental.md`
* `001-Mapa-de-Atores-Gestao-Documental.md`
* `002-Mapa-de-Capacidades-Gestao-Documental.md`
* `003-Mapa-de-Processos-Gestao-Documental.md`
* `004-Mapa-de-Servicos-Gestao-Documental.md`
* `005-Casos-de-Uso-Gestao-Documental.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

---

# 1. Finalidade

Este documento define as **Histórias de Usuário do Domínio de Gestão Documental** do SIGMUN.

As histórias de usuário representam necessidades dos atores do domínio sob a perspectiva do valor que esperam obter do sistema.

Elas serão utilizadas como base para a elaboração de:

* requisitos funcionais;
* regras de negócio;
* especificações;
* critérios de aceitação;
* testes;
* planejamento de desenvolvimento.

---

# 2. Padrão das Histórias de Usuário

As histórias seguirão preferencialmente o formato:

> **Como** [ator], **quero** [ação ou necessidade], **para** [benefício ou resultado].

Exemplo:

> Como servidor gestor documental, quero realizar o upload de um documento digital com metadados obrigatórios, para que o documento seja corretamente registrado e rastreável no sistema.

---

# 3. Convenção de Identificação

As histórias utilizarão o padrão:

```text
HU-GDO-XXX
```

Exemplo:

```text
HU-GDO-001
```

O identificador deverá permanecer estável durante o ciclo de vida da história.

---

# 4. Relação com Casos de Uso

A rastreabilidade seguirá:

```text
SERV-GDO
      ↓
UC-GDO
      ↓
HU-GDO
      ↓
RF-GDO
      ↓
RN-GDO
      ↓
CA-GDO
      ↓
TEST-GDO
```

Uma história poderá originar mais de um requisito funcional.

Um caso de uso poderá possuir várias histórias de usuário.

---

# 5. Histórias de Usuário — Captura e Registro

## HU-GDO-001 — Criar Documento Digital

**Caso de Uso:** `UC-GDO-001`

**Como** servidor gestor documental,

**quero** criar um documento digital diretamente no sistema com atribuição de metadados obrigatórios (título, tipo documental, data, unidade, classificação),

**para** que o documento seja oficialmente registrado e rastreável no acervo municipal.

---

## HU-GDO-002 — Digitalizar Documento Físico

**Caso de Uso:** `UC-GDO-002`

**Como** servidor gestor documental,

**quero** digitalizar documentos físicos por meio de scanner integrado ao sistema,

**para** que documentos em papel sejam convertidos ao formato digital com qualidade e preservação do conteúdo original.

---

## HU-GDO-003 — Criar Documento por Importação

**Caso de Uso:** `UC-GDO-003`

**Como** servidor gestor documental,

**quero** importar documentos de sistemas externos (protocolo eletrônico, sistemas legados) com seus metadados originais,

**para** centralizar o acervo documental no SIGMUN sem perda de informações ou necessidade de re-digitização.

---

# 6. Histórias de Usuário — Classificação Arquivística

## HU-GDO-004 — Classificar Documento

**Caso de Uso:** `UC-GDO-004`

**Como** servidor gestor documental,

**quero** classificar um documento conforme o plano de classificação hierárquico vigente (classe, subclasse, série),

**para** que o documento seja organizado segundo a estrutura arquivística municipal e facilmente recuperável.

---

## HU-GDO-005 — Reclassificar Documento

**Caso de Uso:** `UC-GDO-005`

**Como** servidor gestor documental,

**quero** reclassificar um documento quando identificar erro na classificação original,

**para** corrigir a organização do acervo mantendo o registro de auditoria da alteração realizada.

---

# 7. Histórias de Usuário — Tramitação

## HU-GDO-006 — Tramitar Documento entre Unidades

**Caso de Uso:** `UC-GDO-006`

**Como** servidor gestor documental,

**quero** tramitar um documento de minha unidade para outra unidade administrativa,

**para** que o documento siga o fluxo de trabalho necessário até sua conclusão ou arquivamento.

---

## HU-GDO-007 — Despachar Documento com Instruções

**Caso de Uso:** `UC-GDO-007`

**Como** servidor gestor documental,

**quero** anexar um despacho com instruções e observações ao tramitar um documento,

**para** que o destinatário receba orientações claras sobre as ações esperadas.

---

## HU-GDO-008 — Receber Documento Tramitado

**Caso de Uso:** `UC-GDO-008`

**Como** servidor gestor documental,

**quero** receber e confirmar o recebimento de documentos tramitados para minha unidade,

**para** que haja rastreabilidade do fluxo documental e ciência formal do destinatário.

---

## HU-GDO-009 — Devolver Documento à Unidade de Origem

**Caso de Uso:** `UC-GDO-009`

**Como** servidor gestor documental,

**quero** devolver um documento à unidade de origem com justificativa,

**para** que documentos encaminhados indevidamente ou com pendências sejam corrigidos pelo remetente.

---

# 8. Histórias de Usuário — Arquivamento

## HU-GDO-010 — Arquivar Documento Corrente

**Caso de Uso:** `UC-GDO-010`

**Como** servidor gestor documental,

**quero** arquivar um documento na fase corrente após sua conclusão,

**para** que o documento seja preservado com acesso facilitado às unidades interessadas.

---

## HU-GDO-011 — Desarquivar Documento

**Caso de Uso:** `UC-GDO-011`

**Como** servidor gestor documental,

**quero** desarquivar um documento quando houver necessidade de nova movimentação,

**para** que documentos possam retornar ao fluxo de trabalho quando necessário, com registro da ação.

---

# 9. Histórias de Usuário — Destinação

## HU-GDO-012 — Avaliar Documento para Destinação

**Caso de Uso:** `UC-GDO-012`

**Como** servidor gestor documental,

**quero** avaliar documentos quanto ao prazo de retenção e propor eliminação ou guarda permanente,

**para** cumprir a tabela de temporalidade e otimizar o espaço de armazenamento.

---

## HU-GDO-013 — Eliminar Documento com Homologação

**Caso de Uso:** `UC-GDO-013`

**Como** autoridade homologadora,

**quero** aprovar a eliminação de documentos avaliados e dentro do prazo de retenção,

**para** que documentos sem valor permanente sejam descartados conforme a legislação arquivística.

---

## HU-GDO-014 — Destinar Documento à Guarda Permanente

**Caso de Uso:** `UC-GDO-014`

**Como** autoridade homologadora,

**quero** aprovar a transferência de documentos para guarda permanente,

**para** que documentos com valor histórico ou probatório sejam preservados indefinidamente.

---

## HU-GDO-015 — Prorrogar Prazo de Retenção

**Caso de Uso:** `UC-GDO-015`

**Como** servidor gestor documental,

**quero** solicitar a prorrogação do prazo de retenção de um documento com justificativa,

**para** que documentos com vigência legal ou administrativa prolongada sejam mantidos pelo tempo necessário.

---

# 10. Histórias de Usuário — Processos

## HU-GDO-016 — Abrir Processo Documental

**Caso de Uso:** `UC-GDO-016`

**Como** servidor gestor documental,

**quero** abrir um novo processo documental com identificação, assunto e unidade interessada,

**para** iniciar formalmente a tramitação de documentos relacionados a um assunto específico.

---

## HU-GDO-017 — Incluir Documento em Processo

**Caso de Uso:** `UC-GDO-017`

**Como** servidor gestor documental,

**quero** incluir um documento em um processo existente,

**para** que todos os documentos relacionados a um assunto fiquem agrupados e rastreáveis.

---

## HU-GDO-018 — Encerrar Processo

**Caso de Uso:** `UC-GDO-018`

**Como** servidor gestor documental,

**quero** encerrar um processo quando todas as providências forem concluídas,

**para** que o processo seja arquivado e seu histórico preservado para consultas futuras.

---

## HU-GDO-019 — Reabrir Processo Encerrado

**Caso de Uso:** `UC-GDO-019`

**Como** administrador GDO,

**quero** reabrir um processo anteriormente encerrado com justificativa formal,

**para** que novas providências possam ser adotadas quando necessário, mantendo o registro da reabertura.

---

# 11. Histórias de Usuário — Pesquisa e Consulta

## HU-GDO-020 — Pesquisar Documentos com Filtros

**Caso de Uso:** `UC-GDO-020`

**Como** servidor gestor documental,

**quero** pesquisar documentos utilizando filtros por unidade, período, tipo documental, classificação e palavras-chave,

**para** localizar rapidamente documentos específicos no acervo municipal.

---

## HU-GDO-021 — Consultar Documento Público

**Caso de Uso:** `UC-GDO-021`

**Como** cidadão ou público em geral,

**quero** consultar documentos de acesso público disponíveis no portal de transparência,

**para** exercer o direito de acesso às informações públicas garantido por lei.

---

# 12. Histórias de Usuário — Assinatura Digital

## HU-GDO-022 — Assinar Documento Digitalmente

**Caso de Uso:** `UC-GDO-022`

**Como** servidor gestor documental ou autoridade,

**quero** assinar um documento digitalmente com certificado ICP-Brasil,

**para** garantir autenticidade, integridade e validade jurídica ao documento eletrônico.

---

## HU-GDO-023 — Validar Assinatura Digital

**Caso de Uso:** `UC-GDO-023`

**Como** servidor gestor documental ou cidadão,

**quero** validar a assinatura digital de um documento,

**para** verificar se o documento é autêntico e não foi alterado após a assinatura.

---

# 13. Histórias de Usuário — Auditoria

## HU-GDO-024 — Consultar Histórico de Auditoria

**Caso de Uso:** `UC-GDO-024`

**Como** administrador GDO ou auditor,

**quero** consultar o histórico completo de auditoria de um documento (criação, alterações, tramitações, acessos),

**para** garantir a rastreabilidade e a conformidade dos procedimentos documentais.

---

# 14. Histórias de Usuário — Segurança e Acesso

## HU-GDO-025 — Configurar Permissões de Acesso ao Documento

**Caso de Uso:** `UC-GDO-001` (complementar)

**Como** administrador GDO,

**quero** configurar permissões de acesso por documento (público, restrito, sigiloso),

**para** controlar quem pode visualizar, editar ou tramitar cada documento conforme sua classificação de sigilo.

---

## HU-GDO-026 — Classificar Sigilo do Documento

**Caso de Uso:** `UC-GDO-004` (complementar)

**Como** administrador GDO,

**quero** classificar o nível de sigilo de um documento (público, reservado, secreto),

**para** proteger informações sensíveis conforme a Lei de Acesso à Informação e a LGPD.

---

# 15. Histórias de Usuário — Versionamento

## HU-GDO-027 — Criar Nova Versão de Documento

**Caso de Uso:** `UC-GDO-001` (complementar)

**Como** servidor gestor documental,

**quero** criar uma nova versão de um documento existente,

**para** atualizar o conteúdo mantendo o histórico de versões anteriores para consulta e auditoria.

---

## HU-GDO-028 — Restaurar Versão Anterior

**Caso de Uso:** `UC-GDO-001` (complementar)

**Como** servidor gestor documental,

**quero** restaurar uma versão anterior de um documento,

**para** reverter alterações indevidas ou recuperar conteúdo de versões prévias.

---

# 16. Histórias de Usuário — Digitalização e OCR

## HU-GDO-029 — Aplicar OCR em Documento Digitalizado

**Caso de Uso:** `UC-GDO-002` (complementar)

**Como** servidor gestor documental,

**quero** aplicar reconhecimento óptico de caracteres (OCR) em documentos digitalizados,

**para** tornar o conteúdo pesquisável e indexável automaticamente.

---

## HU-GDO-030 — Corrigir Texto OCR

**Caso de Uso:** `UC-GDO-002` (complementar)

**Como** servidor gestor documental,

**quero** corrigir manualmente o texto extraído pelo OCR,

**para** garantir a fidelidade do conteúdo reconhecido digitalmente.

---

# 17. Histórias de Usuário — Indexação e Metadados

## HU-GDO-031 — Atribuir Metadados ao Documento

**Caso de Uso:** `UC-GDO-001` (complementar)

**Como** servidor gestor documental,

**quero** atribuir metadados estruturados a um documento (autor, destinatário, assunto, palavras-chave),

**para** facilitar a recuperação e a organização do acervo documental.

---

## HU-GDO-032 — Configurar Taxonomia de Indexação

**Caso de Uso:** `UC-GDO-004` (complementar)

**Como** administrador GDO,

**quero** configurar a taxonomia e os vocários controlados para indexação de documentos,

**para** padronizar a terminologia utilizada na classificação e recuperação de documentos.

---

# 18. Histórias de Usuário — Preservação

## HU-GDO-033 — Configurar Plano de Preservação Digital

**Caso de Uso:** `UC-GDO-010` (complementar)

**Como** administrador GDO,

**quero** configurar políticas de preservação digital (formatos aceitos, migração, checksum),

**para** garantir a integridade e a acessibilidade dos documentos a longo prazo.

---

## HU-GDO-034 — Verificar Integridade de Documentos

**Caso de Uso:** `UC-GDO-010` (complementar)

**Como** administrador GDO,

**quero** verificar periodicamente a integridade dos documentos armazenados por meio de checksum,

**para** detectar e corrigir corrupção de arquivos antes que o conteúdo seja perdido.

---

# 19. Histórias de Usuário — Temporalidade

## HU-GDO-035 — Configurar Tabela de Temporalidade

**Caso de Uso:** `UC-GDO-012` (complementar)

**Como** administrador GDO,

**quero** configurar a tabela de temporalidade documental com prazos de retenção e destinação por tipo documental,

**para** automatizar a gestão do ciclo de vida documental conforme a legislação arquivística.

---

## HU-GDO-036 — Receber Alerta de Temporalidade

**Caso de Uso:** `UC-GDO-012` (complementar)

**Como** servidor gestor documental,

**quero** receber alertas quando documentos atingirem o prazo de retenção,

**para** que a avaliação de destinação seja realizada em tempo hábil.

---

# 20. Histórias de Usuário — Indicadores e Relatórios

## HU-GDO-037 — Gerar Relatório de Acervo Documental

**Caso de Uso:** `UC-GDO-020` (complementar)

**Como** gestor administrativo,

**quero** gerar relatórios sobre o acervo documental (quantidade por tipo, unidade, período),

**para** subsidiar decisões sobre capacidade de armazenamento e políticas documentais.

---

## HU-GDO-038 — Acompanhar Indicadores de Desempenho

**Caso de Uso:** `UC-GDO-024` (complementar)

**Como** gestor administrativo,

**quero** acompanhar indicadores de desempenho da gestão documental (tempo médio de tramitação, % digitalizados, documentos classificados),

**para** monitorar a eficiência dos processos documentais e identificar melhorias.

---

# 21. Histórias de Usuário — Integração

## HU-GDO-039 — Integrar Documento com Processo de Compras

**Caso de Uso:** `UC-GDO-017` (complementar)

**Como** servidor gestor documental,

**quero** vincular documentos a processos de compras e contratações,

**para** que toda a documentação de uma licitação esteja organizada e rastreável.

---

## HU-GDO-040 — Publicar Documento no Portal da Transparência

**Caso de Uso:** `UC-GDO-021` (complementar)

**Como** servidor gestor documental,

**quero** publicar documentos diretamente no portal de transparência,

**para** cumprir as obrigações de publicidade e acesso à informação de forma automatizada.

---

# 22. Histórias de Usuário — Consulta Pública

## HU-GDO-041 — Pesquisar Documentos Públicos como Cidadão

**Caso de Uso:** `UC-GDO-021` (complementar)

**Como** cidadão,

**quero** pesquisar documentos públicos por assunto, período ou unidade,

**para** acessar informações de interesse público de forma autônoma e transparente.

---

## HU-GDO-042 — Solicitar Via de Documento

**Caso de Uso:** `UC-GDO-021` (complementar)

**Como** cidadão,

**quero** solicitar uma via digital de documento público,

**para** obter cópia de documentos sem necessidade de atendimento presencial.

---

# 23. Histórias de Usuário — Administração do Sistema

## HU-GDO-043 — Configurar Plano de Classificação

**Caso de Uso:** `UC-GDO-004` (complementar)

**Como** administrador GDO,

**quero** configurar o plano de classificação hierárquico (classes, subclasses, séries),

**para** estruturar a organização do acervo documental conforme a realidade municipal.

---

## HU-GDO-044 — Gerenciar Perfis de Acesso ao GDO

**Caso de Uso:** `UC-GDO-024` (complementar)

**Como** administrador GDO,

**quero** gerenciar perfis de acesso ao módulo de gestão documental (leitura, escrita, administração),

**para** garantir a segregação de funções e a segurança da informação documental.

---

# 24. Relação com Casos de Uso

| História de Usuário | Caso de Uso | Serviço |
| --- | --- | --- |
| HU-GDO-001 | UC-GDO-001 | SERV-GDO-001 |
| HU-GDO-002 | UC-GDO-002 | SERV-GDO-002 |
| HU-GDO-003 | UC-GDO-003 | SERV-GDO-003 |
| HU-GDO-004 | UC-GDO-004 | SERV-GDO-004 |
| HU-GDO-005 | UC-GDO-005 | SERV-GDO-005 |
| HU-GDO-006 | UC-GDO-006 | SERV-GDO-006 |
| HU-GDO-007 | UC-GDO-007 | SERV-GDO-007 |
| HU-GDO-008 | UC-GDO-008 | SERV-GDO-008 |
| HU-GDO-009 | UC-GDO-009 | SERV-GDO-009 |
| HU-GDO-010 | UC-GDO-010 | SERV-GDO-010 |
| HU-GDO-011 | UC-GDO-011 | SERV-GDO-011 |
| HU-GDO-012 | UC-GDO-012 | SERV-GDO-012 |
| HU-GDO-013 | UC-GDO-013 | SERV-GDO-013 |
| HU-GDO-014 | UC-GDO-014 | SERV-GDO-014 |
| HU-GDO-015 | UC-GDO-015 | SERV-GDO-015 |
| HU-GDO-016 | UC-GDO-016 | SERV-GDO-016 |
| HU-GDO-017 | UC-GDO-017 | SERV-GDO-017 |
| HU-GDO-018 | UC-GDO-018 | SERV-GDO-018 |
| HU-GDO-019 | UC-GDO-019 | SERV-GDO-019 |
| HU-GDO-020 | UC-GDO-020 | SERV-GDO-020 |
| HU-GDO-021 | UC-GDO-021 | SERV-GDO-021 |
| HU-GDO-022 | UC-GDO-022 | SERV-GDO-022 |
| HU-GDO-023 | UC-GDO-023 | SERV-GDO-023 |
| HU-GDO-024 | UC-GDO-024 | SERV-GDO-024 |
| HU-GDO-025 | UC-GDO-001 | SERV-GDO-025 |
| HU-GDO-026 | UC-GDO-004 | SERV-GDO-026 |
| HU-GDO-027 | UC-GDO-001 | SERV-GDO-027 |
| HU-GDO-028 | UC-GDO-001 | SERV-GDO-028 |
| HU-GDO-029 | UC-GDO-002 | SERV-GDO-029 |
| HU-GDO-030 | UC-GDO-002 | SERV-GDO-030 |
| HU-GDO-031 | UC-GDO-001 | SERV-GDO-031 |
| HU-GDO-032 | UC-GDO-004 | SERV-GDO-032 |
| HU-GDO-033 | UC-GDO-010 | SERV-GDO-033 |
| HU-GDO-034 | UC-GDO-010 | SERV-GDO-034 |
| HU-GDO-035 | UC-GDO-012 | SERV-GDO-035 |
| HU-GDO-036 | UC-GDO-012 | SERV-GDO-036 |
| HU-GDO-037 | UC-GDO-020 | SERV-GDO-037 |
| HU-GDO-038 | UC-GDO-024 | SERV-GDO-038 |
| HU-GDO-039 | UC-GDO-017 | SERV-GDO-039 |
| HU-GDO-040 | UC-GDO-021 | SERV-GDO-040 |
| HU-GDO-041 | UC-GDO-021 | SERV-GDO-041 |
| HU-GDO-042 | UC-GDO-021 | SERV-GDO-042 |
| HU-GDO-043 | UC-GDO-004 | SERV-GDO-043 |
| HU-GDO-044 | UC-GDO-024 | SERV-GDO-044 |

---

# 25. Agrupamento por Tema

| Tema | Histórias | Quantidade |
| --- | --- | --- |
| Captura e Registro | HU-GDO-001 a 003 | 3 |
| Classificação Arquivística | HU-GDO-004 a 005, 026, 032, 043 | 5 |
| Tramitação | HU-GDO-006 a 009 | 4 |
| Arquivamento | HU-GDO-010 a 011, 033, 034 | 4 |
| Destinação | HU-GDO-012 a 015, 035, 036 | 6 |
| Processos | HU-GDO-016 a 019, 039 | 5 |
| Pesquisa e Consulta | HU-GDO-020 a 021, 037, 040, 041, 042 | 7 |
| Assinatura Digital | HU-GDO-022 a 023 | 2 |
| Auditoria | HU-GDO-024, 038, 044 | 3 |
| Segurança e Acesso | HU-GDO-025, 026, 044 | 3 |
| Versionamento | HU-GDO-027 a 028 | 2 |
| Digitalização e OCR | HU-GDO-029 a 030 | 2 |
| Indexação e Metadados | HU-GDO-031 a 032 | 2 |
| Preservação | HU-GDO-033 a 034 | 2 |
| Temporalidade | HU-GDO-035 a 036 | 2 |
| Indicadores e Relatórios | HU-GDO-037 a 038 | 2 |
| Integração | HU-GDO-039 a 040 | 2 |
| Consulta Pública | HU-GDO-041 a 042 | 2 |
| Administração do Sistema | HU-GDO-043 a 044 | 2 |

---

# 26. Refinamento Futuro

As histórias deste documento representam a primeira decomposição das necessidades do domínio.

Durante o refinamento, uma história poderá:

* ser dividida em várias histórias;
* ser combinada com outra;
* ser descartada;
* ser transformada em requisito transversal;
* depender de serviço corporativo;
* gerar múltiplos requisitos;
* gerar múltiplos critérios de aceitação.

Nenhuma história deverá ser considerada tecnicamente implementada apenas pela sua existência neste documento.

---

# 27. Registro no Mapa Mestre

Este artefato deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

**Identificador do artefato:**

`HU-MAP-GDO-001`

**Tipo:**

Mapa de Histórias de Usuário.

**Domínio:**

Gestão Documental.

**Versão:**

2.0.

---

# 28. Próximo Artefato

O próximo artefato recomendado é:

`007-Regras-de-Negocio-Gestao-Documental.md`

A cadeia de detalhamento ficará:

```text
000-Domínio
      ↓
001-Atores
      ↓
002-Capacidades
      ↓
003-Processos
      ↓
004-Serviços
      ↓
005-Casos de Uso
      ↓
006-Histórias de Usuário
      ↓
007-Regras de Negócio
      ↓
008-Requisitos Funcionais
      ↓
009-Requisitos Não Funcionais
      ↓
010-Especificações
      ↓
011-Critérios de Aceitação
      ↓
012-Matriz de Rastreabilidade
```

---

# 29. Controle de Versões

| Versão | Data       | Descrição                                                                       |
| ------ | ---------- | ------------------------------------------------------------------------------- |
| 1.0    | 2026-08-20 | Criação do esboço inicial padronizado do artefato                               |
| 2.0    | 2026-09-02 | Conteúdo detalhado: 44 histórias de usuário, rastreabilidade, agrupamentos       |

---

**Documento:** 006-Historias-de-Usuario-Gestao-Documental.md

**Última atualização:** 2026-09-02

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
