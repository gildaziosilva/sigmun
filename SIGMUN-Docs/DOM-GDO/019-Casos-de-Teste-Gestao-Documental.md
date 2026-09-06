# 019 – Casos de Teste – Gestão Documental

#### Casos de Teste – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-019

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
* `006-Historias-de-Usuario-Gestao-Documental.md`
* `007-Regras-de-Negocio-Gestao-Documental.md`
* `008-Requisitos-Funcionais-Gestao-Documental.md`
* `009-Requisitos-Nao-Funcionais-Gestao-Documental.md`
* `010-Especificacoes-Gestao-Documental.md`
* `011-Criterios-de-Aceitacao-Gestao-Documental.md`
* `012-Matriz-de-Rastreabilidade-Gestao-Documental.md`
* `013-Modelo-de-Dados-Gestao-Documental.md`
* `014-Modelo-de-Integracao-Gestao-Documental.md`
* `015-Arquitetura-de-Servicos-Gestao-Documental.md`
* `016-Modelo-de-Seguranca-Gestao-Documental.md`
* `017-Modelo-de-Auditoria-Gestao-Documental.md`
* `018-Plano-de-Testes-Gestao-Documental.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

---

# 1. Finalidade

Este documento define os **Casos de Teste do Domínio de Gestão Documental do SIGMUN**.

Os casos de teste representam verificações executáveis destinadas a comprovar o comportamento esperado do sistema em relação aos:

* requisitos funcionais;
* requisitos não funcionais;
* regras de negócio;
* casos de uso;
* histórias de usuário;
* critérios de aceitação;
* integrações;
* controles de segurança;
* controles de auditoria.

---

# 2. Objetivos

Os casos de teste têm como objetivos:

1. verificar o comportamento esperado das funcionalidades;
2. validar regras de negócio;
3. validar fluxos positivos;
4. validar fluxos negativos;
5. verificar permissões;
6. verificar transições de estado;
7. verificar integrações;
8. verificar auditoria;
9. verificar consistência dos dados;
10. fornecer evidências para homologação;
11. apoiar testes de regressão;
12. manter rastreabilidade entre requisitos e execução.

---

# 3. Convenção de Identificação

Cada caso de teste deverá possuir identificador único.

Formato:

```text
CT-GDO-XXX

Onde:

CT  = Caso de Teste
GDO = Gestão Documental
XXX = Número sequencial
```

Exemplos:

```text
CT-GDO-001
CT-GDO-002
CT-GDO-003
```

---

# 4. Estrutura do Caso de Teste

Cada caso deverá possuir:

| Campo | Descrição |
| --- | --- |
| Código | Identificador único |
| Título | Descrição resumida |
| Objetivo | O que se pretende verificar |
| Tipo | Funcional, Integração, Segurança, Performance |
| Prioridade | Crítica, Alta, Média, Baixa |
| Pré-condições | Estado necessário para execução |
| Dados de Entrada | Dados necessários |
| Passos | Sequência de ações |
| Resultado Esperado | Comportamento esperado |
| Resultado Obtido | Resultado da execução |
| Status | Passou, Falhou, Bloqueado |
| Evidência | Print, log, arquivo |
| Defeito | Referência ao defeito (se aplicável) |
| Requisitos Relacionados | RF-GDO-XXX |
| Regras Relacionadas | RN-GDO-XXX |
| Critérios de Aceitação | CA-GDO-XXX |

---

# 5. Classificação dos Casos de Teste

Os casos poderão ser classificados como:

| Tipo | Descrição |
| --- | --- |
| Funcional | Verifica comportamento funcional |
| Integração | Verifica comunicação entre componentes |
| Segurança | Verifica controles de segurança |
| Performance | Verifica tempo de resposta e carga |
| Regressão | Verifica manutenção de funcionalidades |
| Aceitação | Validação com usuário de negócio |

---

# 6. Casos de Teste — Captura e Registro

## CT-GDO-001 — Criar Documento Digital com Sucesso

**Título:** Criar documento digital com todos os metadados obrigatórios

**Objetivo:** Verificar a criação de um documento digital com sucesso

**Tipo:** Funcional

**Prioridade:** Crítica

**Pré-condições:**
* Usuário autenticado com perfil USUARIO_GDO
* Unidade do usuário definida

**Dados de Entrada:**
* Tipo documental: "Ofício"
* Título: "Ofício de Teste"
* Autor: "Usuário Teste"
* Data: "2026-09-02"
* Unidade: "Secretaria de Administração"
* Classificação: "001.001.001"

**Passos:**
1. Acessar a funcionalidade de criar documento
2. Preencher todos os metadados obrigatórios
3. Anexar arquivo PDF
4. Confirmar criação

**Resultado Esperado:**
* Documento criado com sucesso
* Código único gerado
* Hash SHA-256 calculado
* Log de auditoria registrado

**Requisitos Relacionados:** RF-GDO-001, RF-GDO-004, RF-GDO-005

**Regras Relacionadas:** RN-GDO-001, RN-GDO-002, RN-GDO-003

**Critérios de Aceitação:** CA-GDO-001

---

## CT-GDO-002 — Criar Documento sem Metadados Obrigatórios

**Título:** Tentar criar documento sem metadados obrigatórios

**Objetivo:** Verificar validação de metadados obrigatórios

**Tipo:** Funcional

**Prioridade:** Alta

**Pré-condições:**
* Usuário autenticado com perfil USUARIO_GDO

**Dados de Entrada:**
* Tipo documental: "Ofício"
* Título: (vazio)

**Passos:**
1. Acessar a funcionalidade de criar documento
2. Preencher apenas o tipo documental
3. Confirmar criação

**Resultado Esperado:**
* Mensagem de erro informando campos obrigatórios
* Documento não criado

**Requisitos Relacionados:** RF-GDO-001

**Regras Relacionadas:** RN-GDO-003

**Critérios de Aceitação:** CA-GDO-001

---

## CT-GDO-003 — Importar Documento Externo

**Título:** Importar documento de sistema externo

**Objetivo:** Verificar importação de documento externo

**Tipo:** Integração

**Prioridade:** Alta

**Pré-condições:**
* Usuário autenticado
* Arquivo externo disponível

**Dados de Entrada:**
* Arquivo PDF externo
* Metadados originais

**Passos:**
1. Acessar funcionalidade de importação
2. Selecionar arquivo externo
3. Confirmar importação

**Resultado Esperado:**
* Documento importado com sucesso
* Metadados preservados
* Código único gerado

**Requisitos Relacionados:** RF-GDO-003

**Regras Relacionadas:** RN-GDO-001, RN-GDO-003

**Critérios de Aceitação:** CA-GDO-003

---

# 7. Casos de Teste — Classificação

## CT-GDO-004 — Classificar Documento com Sucesso

**Título:** Classificar documento conforme plano de classificação

**Objetivo:** Verificar classificação de documento

**Tipo:** Funcional

**Prioridade:** Crítica

**Pré-condições:**
* Documento registrado
* Plano de classificação configurado

**Dados de Entrada:**
* Classe: "001"
* Subclasse: "001"
* Série: "001"

**Passos:**
1. Selecionar documento
2. Acessar funcionalidade de classificação
3. Atribuir código de classificação
4. Confirmar classificação

**Resultado Esperado:**
* Documento classificado com sucesso
* Temporalidade vinculada automaticamente
* Log de auditoria registrado

**Requisitos Relacionados:** RF-GDO-006, RF-GDO-008

**Regras Relacionadas:** RN-GDO-004, RN-GDO-005

**Critérios de Aceitação:** CA-GDO-004

---

## CT-GDO-005 — Classificar Documento sem Hierarquia Completa

**Título:** Tentar classificar documento sem hierarquia completa

**Objetivo:** Verificar validação de hierarquia de classificação

**Tipo:** Funcional

**Prioridade:** Alta

**Pré-condições:**
* Documento registrado

**Dados de Entrada:**
* Classe: "001"
* Subclasse: (vazio)
* Série: "001"

**Passos:**
1. Selecionar documento
2. Tentar classificar sem subclasse
3. Confirmar classificação

**Resultado Esperado:**
* Mensagem de erro sobre hierarquia incompleta
* Classificação não aplicada

**Requisitos Relacionados:** RF-GDO-006

**Regras Relacionadas:** RN-GDO-005

**Critérios de Aceitação:** CA-GDO-004

---

# 8. Casos de Teste — Tramitação

## CT-GDO-006 — Tramitar Documento com Sucesso

**Título:** Tramitar documento entre unidades

**Objetivo:** Verificar tramitação de documento

**Tipo:** Funcional

**Prioridade:** Crítica

**Pré-condições:**
* Documento registrado e classificado
* Unidade destinatária definida

**Dados de Entrada:**
* Unidade destino: "Secretaria de Finanças"
* Observacao: "Para análise"

**Passos:**
1. Selecionar documento
2. Acessar funcionalidade de tramitação
3. Definir unidade destino
4. Adicionar observação
5. Confirmar tramitação

**Resultado Esperado:**
* Documento tramitado com sucesso
* Destinatário notificado
* Log de auditoria registrado

**Requisitos Relacionados:** RF-GDO-009, RF-GDO-010

**Regras Relacionadas:** RN-GDO-006

**Critérios de Aceitação:** CA-GDO-006

---

## CT-GDO-007 — Receber Documento Tramitado

**Título:** Confirmar recebimento de documento tramitado

**Objetivo:** Verificar recebimento de documento

**Tipo:** Funcional

**Prioridade:** Crítica

**Pré-condições:**
* Documento em tramitação para a unidade do usuário

**Dados de Entrada:**
* Confirmação de ciência

**Passos:**
1. Acessar documento pendente
2. Confirmar ciência do recebimento

**Resultado Esperado:**
* Ciência registrada
* Status atualizado para "Recebido"
* Log de auditoria registrado

**Requisitos Relacionados:** RF-GDO-011

**Regras Relacionadas:** RN-GDO-007

**Critérios de Aceitação:** CA-GDO-008

---

# 9. Casos de Teste — Assinatura Digital

## CT-GDO-008 — Assinar Documento Digitalmente

**Título:** Assinar documento com certificado digital ICP-Brasil

**Objetivo:** Verificar assinatura digital

**Tipo:** Funcional

**Prioridade:** Crítica

**Pré-condições:**
* Documento registrado
* Certificado digital válido

**Dados de Entrada:**
* Certificado digital A1 ou A3
* PIN do certificado

**Passos:**
1. Selecionar documento
2. Acessar funcionalidade de assinatura
3. Inserir certificado e PIN
4. Confirmar assinatura

**Resultado Esperado:**
* Documento assinado com sucesso
* Certificado registrado
* Documento bloqueado para alterações
* Log de auditoria registrado

**Requisitos Relacionados:** RF-GDO-025

**Regras Relacionadas:** RN-GDO-017, RN-GDO-018

**Critérios de Aceitação:** CA-GDO-022

---

## CT-GDO-009 — Tentar Alterar Documento Assinado

**Título:** Tentar alterar documento já assinado

**Objetivo:** Verificar imutabilidade de documento assinado

**Tipo:** Funcional

**Prioridade:** Alta

**Pré-condições:**
* Documento assinado

**Passos:**
1. Selecionar documento assinado
2. Tentar editar metadados

**Resultado Esperado:**
* Mensagem de erro informando que documento assinado não pode ser alterado
* Edição não permitida

**Requisitos Relacionados:** RF-GDO-025

**Regras Relacionadas:** RN-GDO-018

**Critérios de Aceitação:** CA-GDO-022

---

# 10. Casos de Teste — Segurança

## CT-GDO-010 — Acesso Negado sem Autenticação

**Título:** Tentar acessar funcionalidade sem autenticação

**Objetivo:** Verificar controle de acesso

**Tipo:** Segurança

**Prioridade:** Crítica

**Pré-condições:**
* Usuário não autenticado

**Passos:**
1. Tentar acessar endpoint de criar documento sem token

**Resultado Esperado:**
* Retorno 401 Unauthorized
* Mensagem de erro apropriada

**Requisitos Relacionados:** RNF-GDO-001

**Critérios de Aceitação:** —

---

## CT-GDO-011 — Acesso a Documento Sigiloso sem Permissão

**Título:** Tentar acessar documento sigiloso sem permissão

**Objetivo:** Verificar controle de acesso por sigilo

**Tipo:** Segurança

**Prioridade:** Alta

**Pré-condições:**
* Usuário autenticado sem permissão
* Documento classificado como sigiloso

**Passos:**
1. Tentar consultar documento sigiloso

**Resultado Esperado:**
* Retorno 403 Forbidden
* Mensagem de acesso negado

**Requisitos Relacionados:** RF-GDO-029, RF-GDO-030

**Regras Relacionadas:** RN-GDO-019

**Critérios de Aceitação:** CA-GDO-025

---

# 11. Casos de Teste — Performance

## CT-GDO-012 — Tempo de Resposta de Pesquisa

**Título:** Verificar tempo de resposta da pesquisa de documentos

**Objetivo:** Verificar performance da pesquisa

**Tipo:** Performance

**Prioridade:** Alta

**Pré-condições:**
* Base de dados com 10.000 documentos

**Passos:**
1. Executar pesquisa com filtros
2. Medir tempo de resposta

**Resultado Esperado:**
* Tempo de resposta <= 2 segundos

**Requisitos Relacionados:** RNF-GDO-009

**Critérios de Aceitação:** —

---

## CT-GDO-013 — Upload de Documento Grande

**Título:** Verificar upload de documento de 100MB

**Objetivo:** Verificar performance de upload

**Tipo:** Performance

**Prioridade:** Média

**Pré-condições:**
* Arquivo de 100MB disponível

**Passos:**
1. Selecionar arquivo de 100MB
2. Realizar upload
3. Medir tempo de processamento

**Resultado Esperado:**
* Upload concluído em <= 30 segundos

**Requisitos Relacionados:** RNF-GDO-010

**Critérios de Aceitação:** —

---

# 12. Casos de Teste — Integração

## CT-GDO-014 — Integração com DOM-IDN

**Título:** Verificar integração com domínio de identidade

**Objetivo:** Verificar autenticação via DOM-IDN

**Tipo:** Integração

**Prioridade:** Crítica

**Pré-condições:**
* DOM-IDN disponível
* Token JWT válido

**Passos:**
1. Enviar requisição com token válido
2. Verificar resposta

**Resultado Esperado:**
* Autenticação bem-sucedida
* Permissões corretas retornadas

**Requisitos Relacionados:** RNF-GDO-001

**Critérios de Aceitação:** —

---

## CT-GDO-015 — Integração com DOM-CUM

**Título:** Verificar consulta de unidades administrativas

**Objetivo:** Verificar integração com DOM-CUM

**Tipo:** Integração

**Prioridade:** Alta

**Pré-condições:**
* DOM-CUM disponível

**Passos:**
1. Consultar unidades administrativas
2. Verificar dados retornados

**Resultado Esperado:**
* Lista de unidades retornada corretamente

**Requisitos Relacionados:** —

**Critérios de Aceitação:** —

---

# 13. Resumo dos Casos de Teste

| Código | Título | Tipo | Prioridade |
| --- | --- | --- | --- |
| CT-GDO-001 | Criar Documento Digital com Sucesso | Funcional | Crítica |
| CT-GDO-002 | Criar Documento sem Metadados Obrigatórios | Funcional | Alta |
| CT-GDO-003 | Importar Documento Externo | Integração | Alta |
| CT-GDO-004 | Classificar Documento com Sucesso | Funcional | Crítica |
| CT-GDO-005 | Classificar Documento sem Hierarquia Completa | Funcional | Alta |
| CT-GDO-006 | Tramitar Documento com Sucesso | Funcional | Crítica |
| CT-GDO-007 | Receber Documento Tramitado | Funcional | Crítica |
| CT-GDO-008 | Assinar Documento Digitalmente | Funcional | Crítica |
| CT-GDO-009 | Tentar Alterar Documento Assinado | Funcional | Alta |
| CT-GDO-010 | Acesso Negado sem Autenticação | Segurança | Crítica |
| CT-GDO-011 | Acesso a Documento Sigiloso sem Permissão | Segurança | Alta |
| CT-GDO-012 | Tempo de Resposta de Pesquisa | Performance | Alta |
| CT-GDO-013 | Upload de Documento Grande | Performance | Média |
| CT-GDO-014 | Integração com DOM-IDN | Integração | Crítica |
| CT-GDO-015 | Integração com DOM-CUM | Integração | Alta |

---

# 14. Refinamento Futuro

Os casos deste documento representam a primeira versão dos testes do domínio.

Durante o refinamento, os casos poderão:

* ser expandidos com novos cenários;
* ser ajustados conforme evolução dos requisitos;
* ser automatizados;
* ser atualizados conforme novas regulamentações.

---

# 15. Registro no Mapa Mestre

Este artefato deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

**Identificador do artefato:**

`CT-MAP-GDO-001`

**Tipo:**

Casos de Teste.

**Domínio:**

Gestão Documental.

**Versão:**

2.0.

---

# 16. Controle de Versões

| Versão | Data       | Descrição |
| ------ | ---------- | --------- |
| 1.0    | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0    | 2026-09-02 | Conteúdo detalhado: 15 casos de teste |

---

**Documento:** 019-Casos-de-Teste-Gestao-Documental.md

**Última atualização:** 2026-09-02

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
