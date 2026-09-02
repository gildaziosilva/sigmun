# Casos-de-Uso.md

#### Casos de Uso

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Domínio:** Modelo de Negócio

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md
* Cadeia-de-Valor.md
* Mapa-de-Atores.md
* Mapa-de-Capacidades.md
* Mapa-de-Dominios.md
* Mapa-de-Processos.md
* Mapa-de-Secretarias.md
* Mapa-de-Servicos.md
* Modelo-de-Competencias.md
* Modelo-de-Governanca-Administrativa.md
* Glossario-de-Negocio.md
* 000G-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md
* 000F-Registro-de-Decisoes-Arquiteturais.md
* 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md

---

# 1. Objetivo

Este documento estabelece o **Catálogo Corporativo de Casos de Uso do SIGMUN**, definindo os principais cenários de interação entre atores, cidadãos, empresas, servidores, gestores, unidades administrativas, órgãos públicos e o Sistema Integrado de Gestão Municipal.

O documento tem como finalidade:

* estabelecer uma visão corporativa dos casos de uso do SIGMUN;
* padronizar a identificação e descrição dos casos de uso;
* relacionar casos de uso aos processos e serviços municipais;
* estabelecer rastreabilidade entre negócio, requisitos, sistemas e funcionalidades;
* orientar a especificação funcional dos módulos;
* apoiar a arquitetura de software;
* apoiar a elicitação e validação de requisitos;
* reduzir duplicidade de funcionalidades;
* facilitar testes e homologações;
* apoiar a evolução contínua do SIGMUN.

---

# 2. Escopo

Este documento contempla os **casos de uso corporativos e transversais** do SIGMUN.

Não substitui as especificações funcionais detalhadas de cada módulo.

Os casos de uso específicos deverão ser detalhados posteriormente nos respectivos domínios funcionais.

Exemplo:

```text
Modelo de Negócio
        ↓
Mapa de Processos
        ↓
Caso de Uso Corporativo
        ↓
Caso de Uso do Domínio
        ↓
Caso de Uso do Módulo
        ↓
Requisito Funcional
        ↓
Implementação
        ↓
Teste
```

---

# 3. Princípios

Os casos de uso do SIGMUN devem observar os seguintes princípios:

## 3.1 Orientação ao serviço público

Cada caso de uso deve estar relacionado a uma necessidade real do Município.

## 3.2 Orientação ao processo

Os casos de uso devem representar comportamentos inseridos em processos municipais.

## 3.3 Rastreabilidade

Todo caso de uso relevante deve possuir rastreabilidade para:

* processo;
* serviço;
* capacidade;
* domínio;
* requisito;
* módulo;
* ator;
* regra de negócio;
* teste.

## 3.4 Reutilização

Casos de uso transversais devem ser reutilizados pelos diferentes módulos sempre que possível.

## 3.5 Segurança

As interações devem respeitar:

* controle de acesso;
* segregação de funções;
* princípio do menor privilégio;
* classificação da informação;
* proteção de dados pessoais;
* trilhas de auditoria.

## 3.6 Transparência

Sempre que juridicamente e operacionalmente possível, os casos de uso devem permitir geração de informações destinadas à transparência pública.

## 3.7 Experiência do usuário

Os casos de uso devem ser projetados considerando os diferentes perfis de usuários e canais de atendimento.

---

# 4. Conceitos

## 4.1 Caso de Uso

Um caso de uso representa uma interação entre um ou mais atores e o SIGMUN para alcançar um objetivo específico.

## 4.2 Ator

Pessoa, organização, sistema ou agente externo que interage com o SIGMUN.

## 4.3 Sistema

O SIGMUN ou sistema externo integrado ao SIGMUN.

## 4.4 Objetivo

Resultado que o ator pretende alcançar por meio da interação.

## 4.5 Fluxo Principal

Sequência normal de eventos para conclusão bem-sucedida do caso de uso.

## 4.6 Fluxo Alternativo

Variação prevista do fluxo principal.

## 4.7 Exceção

Situação que impede ou altera a execução normal do caso de uso.

## 4.8 Pré-condição

Condição que deve existir antes da execução.

## 4.9 Pós-condição

Estado esperado após a conclusão do caso de uso.

---

# 5. Convenção de Identificação

Os casos de uso corporativos utilizarão o padrão:

```text
UC-XXX
```

Onde:

* `UC` = Use Case;
* `XXX` = número sequencial.

Exemplo:

```text
UC-001
UC-002
UC-003
```

Para casos de uso associados a domínios específicos, poderá ser utilizada uma identificação complementar.

Exemplo:

```text
UC-SAU-001
UC-EDU-001
UC-FIN-001
UC-RH-001
```

---

# 6. Classificação dos Casos de Uso

Os casos de uso serão classificados em:

## 6.1 Casos de Uso Corporativos

Abrangem funcionalidades utilizadas por diferentes secretarias e domínios.

Exemplos:

* autenticar usuário;
* consultar cadastro;
* emitir documento;
* registrar atendimento;
* consultar processo;
* registrar ocorrência;
* enviar notificação;
* consultar histórico.

## 6.2 Casos de Uso Funcionais

Relacionados diretamente a um domínio de negócio.

Exemplos:

* registrar matrícula escolar;
* emitir empenho;
* cadastrar paciente;
* registrar ocorrência de fiscalização.

## 6.3 Casos de Uso Transversais

Utilizados por diversos processos e módulos.

Exemplos:

* autenticar usuário;
* validar identidade;
* registrar auditoria;
* anexar documento;
* assinar digitalmente;
* consultar protocolo.

## 6.4 Casos de Uso Externos

Relacionados à interação com cidadãos, empresas, outros órgãos ou sistemas externos.

---

# 7. Atores Corporativos

Os principais atores do SIGMUN incluem:

* **Cidadão**
* **Servidor Público**
* **Gestor Municipal**
* **Secretário Municipal**
* **Prefeito**
* **Vereador**
* **Fornecedor**
* **Empresa**
* **Prestador de Serviço**
* **Contribuinte**
* **Responsável Legal**
* **Órgão Público**
* **Controladoria**
* **Auditoria**
* **Tribunal de Contas**
* **Ministério Público**
* **Sistema Externo**
* **Administrador do Sistema**
* **Gestor de Dados**
* **Gestor de Segurança**
* **Agente de Atendimento**
* **Agente de Fiscalização**

A relação definitiva de atores deverá ser mantida em conjunto com o `Mapa-de-Atores.md`.

---

# 8. Catálogo Corporativo de Casos de Uso

## UC-001 – Autenticar Usuário

**Objetivo:** Permitir que um usuário seja autenticado no SIGMUN.

**Atores principais:**

* Servidor Público
* Gestor Municipal
* Administrador do Sistema
* Usuário Externo

**Pré-condições:**

* Usuário cadastrado;
* credencial disponível;
* conta habilitada.

**Fluxo principal:**

1. Usuário informa suas credenciais.
2. SIGMUN valida as credenciais.
3. SIGMUN verifica as permissões.
4. SIGMUN registra o acesso.
5. SIGMUN disponibiliza os recursos autorizados.

**Resultado esperado:**

Usuário autenticado e autorizado conforme seu perfil.

---

## UC-002 – Consultar Cadastro

**Objetivo:** Permitir consulta às informações cadastrais autorizadas.

**Atores:**

* Servidor Público
* Gestor
* Cidadão
* Sistema Integrado

**Resultado esperado:**

Informações cadastrais apresentadas conforme as permissões aplicáveis.

---

## UC-003 – Cadastrar Pessoa

**Objetivo:** Registrar uma pessoa no Cadastro Único Municipal.

**Atores:**

* Servidor Público
* Agente de Atendimento
* Cidadão

**Resultado esperado:**

Pessoa registrada ou atualizada no Cadastro Único Municipal.

**Regras principais:**

* evitar duplicidade;
* validar dados;
* respeitar proteção de dados pessoais;
* registrar origem das informações;
* manter histórico de alterações.

---

## UC-004 – Atualizar Cadastro

**Objetivo:** Atualizar informações cadastrais existentes.

**Atores:**

* Servidor Público
* Cidadão
* Agente de Atendimento

**Resultado esperado:**

Cadastro atualizado e alteração registrada em trilha de auditoria.

---

## UC-005 – Registrar Atendimento

**Objetivo:** Registrar uma interação entre Município e usuário do serviço público.

**Atores:**

* Agente de Atendimento
* Servidor Público
* Cidadão

**Resultado esperado:**

Atendimento registrado e associado ao cidadão, serviço ou processo correspondente.

---

## UC-006 – Abrir Solicitação de Serviço

**Objetivo:** Permitir que um usuário solicite um serviço municipal.

**Atores:**

* Cidadão
* Empresa
* Servidor Público

**Resultado esperado:**

Solicitação registrada, protocolada e encaminhada ao fluxo correspondente.

---

## UC-007 – Consultar Solicitação

**Objetivo:** Permitir acompanhamento de uma solicitação.

**Atores:**

* Cidadão
* Servidor Público
* Gestor

**Resultado esperado:**

Situação atual e histórico da solicitação apresentados ao usuário autorizado.

---

## UC-008 – Registrar Protocolo

**Objetivo:** Formalizar uma solicitação, documento, processo ou atendimento.

**Atores:**

* Servidor Público
* Agente de Atendimento
* Cidadão
* Empresa

**Resultado esperado:**

Protocolo único gerado e associado ao objeto correspondente.

---

## UC-009 – Consultar Processo

**Objetivo:** Permitir consulta ao andamento de processo administrativo.

**Atores:**

* Servidor Público
* Gestor
* Cidadão
* Órgão de Controle

**Resultado esperado:**

Informações disponibilizadas conforme classificação e autorização de acesso.

---

## UC-010 – Criar Processo

**Objetivo:** Criar processo administrativo ou operacional.

**Atores:**

* Servidor Público
* Gestor

**Resultado esperado:**

Processo criado com identificação única, responsável, origem e fluxo definido.

---

## UC-011 – Encaminhar Processo

**Objetivo:** Encaminhar processo para unidade ou responsável.

**Atores:**

* Servidor Público
* Gestor

**Resultado esperado:**

Processo encaminhado e movimentação registrada.

---

## UC-012 – Analisar Processo

**Objetivo:** Permitir análise técnica ou administrativa de processo.

**Atores:**

* Servidor Público
* Analista
* Gestor

**Resultado esperado:**

Análise registrada e processo encaminhado para a próxima etapa.

---

## UC-013 – Aprovar Solicitação

**Objetivo:** Permitir aprovação de uma solicitação conforme alçada definida.

**Atores:**

* Gestor
* Autoridade Competente

**Resultado esperado:**

Solicitação aprovada, rejeitada ou devolvida para complementação.

---

## UC-014 – Assinar Documento

**Objetivo:** Permitir assinatura de documento oficial.

**Atores:**

* Servidor Público
* Gestor
* Autoridade Competente

**Resultado esperado:**

Documento assinado e registro da assinatura mantido para auditoria.

---

## UC-015 – Emitir Documento

**Objetivo:** Gerar documento oficial a partir de informações registradas no SIGMUN.

**Atores:**

* Servidor Público
* Gestor
* Cidadão

**Resultado esperado:**

Documento emitido com identificação, autenticidade e rastreabilidade.

---

## UC-016 – Anexar Documento

**Objetivo:** Associar documento digital a processo, cadastro, atendimento ou serviço.

**Atores:**

* Servidor Público
* Cidadão
* Empresa

**Resultado esperado:**

Documento armazenado e associado corretamente ao objeto de negócio.

---

## UC-017 – Registrar Auditoria

**Objetivo:** Registrar eventos relevantes executados no sistema.

**Atores:**

* SIGMUN

**Resultado esperado:**

Evento registrado com informações suficientes para rastreabilidade.

---

## UC-018 – Enviar Notificação

**Objetivo:** Comunicar usuário sobre evento, prazo, andamento ou decisão.

**Atores:**

* SIGMUN
* Servidor Público

**Canais possíveis:**

* portal;
* aplicativo;
* e-mail;
* SMS;
* outros canais integrados.

---

## UC-019 – Consultar Indicador

**Objetivo:** Permitir consulta aos indicadores municipais.

**Atores:**

* Gestor
* Secretário
* Servidor Público
* Cidadão
* Órgão de Controle

**Resultado esperado:**

Indicadores apresentados conforme nível de acesso.

---

## UC-020 – Gerar Relatório

**Objetivo:** Gerar relatório operacional, gerencial ou institucional.

**Atores:**

* Servidor Público
* Gestor
* Administrador

**Resultado esperado:**

Relatório produzido com dados autorizados.

---

## UC-021 – Consultar Dashboard

**Objetivo:** Disponibilizar visão consolidada das informações municipais.

**Atores:**

* Prefeito
* Secretário
* Gestor
* Servidor
* Cidadão

---

## UC-022 – Registrar Ocorrência

**Objetivo:** Registrar ocorrência relacionada a serviço, fiscalização ou operação municipal.

**Atores:**

* Servidor Público
* Agente de Campo
* Cidadão

**Resultado esperado:**

Ocorrência registrada, georreferenciada quando aplicável e encaminhada para tratamento.

---

## UC-023 – Executar Atividade de Campo

**Objetivo:** Permitir execução de atividades municipais fora das unidades administrativas.

**Atores:**

* Agente de Campo
* Fiscal
* Servidor Público

**Características:**

* funcionamento Offline First;
* coleta de evidências;
* geolocalização quando aplicável;
* sincronização posterior;
* registro de data e hora.

---

## UC-024 – Sincronizar Dados

**Objetivo:** Sincronizar dados entre dispositivos e a plataforma SIGMUN.

**Atores:**

* Dispositivo Móvel
* SIGMUN

**Resultado esperado:**

Dados sincronizados com controle de conflitos e integridade.

---

## UC-025 – Integrar Sistema Externo

**Objetivo:** Permitir comunicação entre SIGMUN e sistemas externos.

**Atores:**

* SIGMUN
* Sistema Externo

**Resultado esperado:**

Informações transmitidas ou recebidas conforme contratos de integração.

---

## UC-026 – Gerenciar Usuários

**Objetivo:** Administrar contas e usuários do SIGMUN.

**Atores:**

* Administrador do Sistema
* Gestor de Identidade

---

## UC-027 – Gerenciar Perfis e Permissões

**Objetivo:** Definir permissões de acesso conforme função e responsabilidade.

**Atores:**

* Administrador
* Gestor de Segurança

---

## UC-028 – Gerenciar Dados Mestres

**Objetivo:** Administrar dados corporativos utilizados por diversos módulos.

**Atores:**

* Gestor de Dados
* Administrador

---

## UC-029 – Consultar Histórico

**Objetivo:** Permitir consulta ao histórico de alterações e eventos.

**Atores:**

* Servidor Público
* Gestor
* Auditor
* Órgão de Controle

---

## UC-030 – Publicar Informação

**Objetivo:** Disponibilizar informação pública em canais institucionais.

**Atores:**

* Servidor Público
* Gestor
* SIGMUN

**Resultado esperado:**

Informação publicada conforme política de classificação e publicação de artefatos.

---

# 9. Estrutura Padrão para Casos de Uso Detalhados

Cada caso de uso detalhado deverá utilizar a seguinte estrutura:

```markdown
# UC-XXX – Nome do Caso de Uso

## Objetivo

Descrição do objetivo.

## Atores

- Ator principal
- Atores secundários

## Gatilho

Evento que inicia o caso de uso.

## Pré-condições

Condições necessárias.

## Pós-condições

Estado esperado após execução.

## Fluxo Principal

1. ...
2. ...
3. ...

## Fluxos Alternativos

### FA-01 – Nome

1. ...
2. ...

## Exceções

### EX-01 – Nome

1. ...
2. ...

## Regras de Negócio

- RN-XXX
- RN-XXX

## Dados Envolvidos

- ...

## Documentos

- ...

## Integrações

- ...

## Permissões

- ...

## Auditoria

- ...

## Indicadores

- ...

## Requisitos Relacionados

- RF-XXX

## Processos Relacionados

- PROC-XXX

## Serviços Relacionados

- SRV-XXX

## Testes Relacionados

- CT-XXX
```

---

# 10. Rastreabilidade

Cada caso de uso deverá possuir rastreabilidade bidirecional.

```text
Ator
  ↓
Serviço
  ↓
Processo
  ↓
Caso de Uso
  ↓
Regra de Negócio
  ↓
Requisito
  ↓
Funcionalidade
  ↓
Componente
  ↓
Teste
```

Também será possível realizar o caminho inverso:

```text
Teste
 ↓
Requisito
 ↓
Caso de Uso
 ↓
Processo
 ↓
Serviço
 ↓
Capacidade
 ↓
Objetivo Estratégico
```

---

# 11. Matriz Corporativa de Rastreabilidade

| Caso de Uso | Processo             | Serviço                 | Domínio     | Ator            | Requisito |
| ----------- | -------------------- | ----------------------- | ----------- | --------------- | --------- |
| UC-001      | Gestão de Identidade | Autenticação            | Transversal | Usuário         | RF-001    |
| UC-003      | Cadastro Único       | Cadastro de Pessoa      | Cadastro    | Servidor        | RF-003    |
| UC-005      | Atendimento          | Atendimento ao Cidadão  | Atendimento | Atendente       | RF-005    |
| UC-006      | Atendimento          | Solicitação de Serviço  | Atendimento | Cidadão         | RF-006    |
| UC-008      | Gestão Documental    | Protocolo               | Documental  | Servidor        | RF-008    |
| UC-010      | Gestão de Processos  | Processo Administrativo | Processos   | Servidor        | RF-010    |
| UC-014      | Gestão Documental    | Assinatura              | Documental  | Autoridade      | RF-014    |
| UC-017      | Auditoria            | Auditoria               | Segurança   | SIGMUN          | RF-017    |
| UC-019      | BI                   | Indicadores             | Analytics   | Gestor          | RF-019    |
| UC-023      | Serviços de Campo    | Atividade de Campo      | Operacional | Agente          | RF-023    |
| UC-024      | Integração           | Sincronização           | Tecnologia  | Dispositivo     | RF-024    |
| UC-025      | Integração           | Integração Externa      | Integração  | Sistema Externo | RF-025    |

A matriz deverá ser expandida conforme os domínios forem especificados.

---

# 12. Relação com os Domínios do SIGMUN

Os casos de uso deverão ser distribuídos entre os domínios corporativos e funcionais.

Exemplos:

### Administração

* UC-010 – Criar Processo
* UC-011 – Encaminhar Processo
* UC-012 – Analisar Processo

### Finanças

* empenhar despesa;
* liquidar despesa;
* pagar despesa;
* consultar execução orçamentária.

### Recursos Humanos

* cadastrar servidor;
* registrar frequência;
* processar folha;
* conceder benefício.

### Saúde

* cadastrar paciente;
* agendar atendimento;
* registrar atendimento;
* consultar prontuário autorizado.

### Educação

* cadastrar aluno;
* matricular aluno;
* registrar frequência;
* registrar avaliação.

### Tributação

* cadastrar contribuinte;
* lançar tributo;
* emitir guia;
* registrar pagamento.

### Obras e Serviços

* registrar solicitação;
* abrir ordem de serviço;
* executar serviço;
* registrar evidência.

### Assistência Social

* cadastrar família;
* realizar atendimento;
* registrar benefício;
* acompanhar atendimento.

---

# 13. Casos de Uso Transversais

Os seguintes casos de uso devem ser tratados como **serviços corporativos reutilizáveis**:

* autenticação;
* autorização;
* consulta cadastral;
* gestão documental;
* protocolo;
* notificações;
* auditoria;
* assinatura;
* anexação de documentos;
* pesquisa;
* geração de relatórios;
* indicadores;
* integração;
* sincronização;
* gestão de usuários;
* gestão de permissões;
* histórico;
* trilhas de auditoria.

A implementação desses recursos deve priorizar componentes compartilhados, evitando duplicação entre módulos.

---

# 14. Casos de Uso do Cidadão

O SIGMUN deverá priorizar experiências digitais centradas no cidadão.

Exemplos:

* realizar cadastro;
* atualizar dados;
* solicitar serviço;
* consultar solicitação;
* abrir protocolo;
* acompanhar processo;
* emitir documento;
* consultar débito;
* emitir guia;
* realizar pagamento;
* agendar atendimento;
* receber notificações;
* apresentar documentos;
* consultar informações públicas;
* registrar manifestação;
* acompanhar reclamação;
* acompanhar solicitação de manutenção urbana.

---

# 15. Casos de Uso do Servidor Público

Exemplos:

* autenticar;
* consultar cadastro;
* registrar atendimento;
* criar processo;
* tramitar processo;
* analisar processo;
* emitir documento;
* assinar documento;
* registrar ocorrência;
* executar atividade de campo;
* consultar indicadores;
* gerar relatório;
* consultar histórico;
* registrar decisão;
* encaminhar atividade;
* concluir atendimento.

---

# 16. Casos de Uso do Gestor

Exemplos:

* consultar indicadores;
* consultar dashboards;
* acompanhar processos;
* acompanhar serviços;
* aprovar solicitações;
* distribuir atividades;
* acompanhar desempenho;
* consultar orçamento;
* acompanhar metas;
* acompanhar riscos;
* acompanhar contratos;
* consultar auditorias.

---

# 17. Casos de Uso de Controle e Auditoria

Exemplos:

* consultar trilha de auditoria;
* consultar processo;
* consultar contratos;
* consultar pagamentos;
* consultar decisões;
* gerar evidências;
* verificar integridade dos registros;
* consultar indicadores;
* exportar informações autorizadas.

---

# 18. Casos de Uso de Integração

O SIGMUN deverá possuir casos de uso específicos para integração com:

* sistemas federais;
* sistemas estaduais;
* sistemas municipais;
* órgãos de controle;
* bancos;
* serviços de pagamento;
* serviços de autenticação;
* serviços de comunicação;
* plataformas de dados;
* sistemas especializados.

Cada integração deverá possuir especificação própria.

---

# 19. Casos de Uso Offline First

Para operações de campo, os casos de uso deverão considerar:

1. autenticação previamente autorizada;
2. disponibilização de dados necessários;
3. execução da atividade sem conexão;
4. armazenamento local seguro;
5. coleta de evidências;
6. registro de eventos;
7. sincronização posterior;
8. resolução de conflitos;
9. confirmação da sincronização.

Essa abordagem é particularmente importante para localidades com conectividade limitada.

---

# 20. Regras para Criação de Novos Casos de Uso

Um novo caso de uso deverá ser criado quando existir:

* objetivo de negócio claramente identificável;
* ator identificável;
* interação relevante com o sistema;
* resultado esperado;
* comportamento que precise ser especificado;
* necessidade de rastreabilidade.

Não deverão ser criados casos de uso apenas para representar:

* telas;
* botões;
* campos;
* componentes técnicos;
* consultas triviais;
* operações internas sem valor de negócio.

---

# 21. Critérios de Qualidade

Um caso de uso deverá ser:

* claro;
* objetivo;
* verificável;
* testável;
* rastreável;
* independente de implementação;
* orientado ao objetivo do ator;
* consistente com o processo;
* consistente com as regras de negócio.

---

# 22. Governança

A gestão dos casos de uso deverá seguir o modelo de governança documental e arquitetural do SIGMUN.

Alterações relevantes deverão ser:

* registradas;
* versionadas;
* revisadas;
* aprovadas quando necessário;
* relacionadas aos requisitos afetados;
* relacionadas aos processos afetados;
* avaliadas quanto ao impacto arquitetural.

Decisões arquiteturais relevantes deverão ser registradas no mecanismo de ADR.

---

# 23. Versionamento

Os casos de uso corporativos deverão seguir versionamento controlado.

Alterações estruturais deverão registrar:

* versão anterior;
* versão atual;
* data;
* responsável;
* justificativa;
* impacto;
* documentos relacionados.

---

# 24. Evolução do Catálogo

Este documento representa o **catálogo corporativo inicial**.

A partir dele, cada domínio poderá criar seus próprios catálogos especializados.

Exemplo:

```text
05-Modulos/
├── Administracao/
│   └── Casos-de-Uso.md
│
├── Financas/
│   └── Casos-de-Uso.md
│
├── Saude/
│   └── Casos-de-Uso.md
│
├── Educacao/
│   └── Casos-de-Uso.md
│
└── Recursos-Humanos/
    └── Casos-de-Uso.md
```

Os casos de uso especializados deverão manter referência ao catálogo corporativo.

---

# 25. Roadmap de Especificação

A evolução dos casos de uso deverá seguir preferencialmente esta sequência:

```text
1. Identificação dos atores
        ↓
2. Identificação dos serviços
        ↓
3. Identificação dos processos
        ↓
4. Identificação dos casos de uso
        ↓
5. Especificação dos fluxos
        ↓
6. Identificação das regras de negócio
        ↓
7. Identificação dos requisitos
        ↓
8. Implementação
        ↓
9. Testes
        ↓
10. Homologação
```

---

# 26. Relação com o Modelo Corporativo do SIGMUN

O catálogo de casos de uso integra a arquitetura corporativa da seguinte forma:

```text
Constituição do SIGMUN
          ↓
Objetivos Estratégicos
          ↓
Cadeia de Valor
          ↓
Capacidades
          ↓
Domínios
          ↓
Atores
          ↓
Serviços
          ↓
Processos
          ↓
Casos de Uso
          ↓
Requisitos
          ↓
Arquitetura de Software
          ↓
Implementação
          ↓
Testes
          ↓
Operação
          ↓
Indicadores
          ↓
Melhoria Contínua
```

Dessa forma, o caso de uso deixa de ser apenas uma especificação de software e passa a ser um **elemento de ligação entre a estratégia municipal, o negócio e a tecnologia**.

---

# 27. Próximos Documentos Relacionados

A partir deste documento, recomenda-se a criação e evolução de:

* `Regras-de-Negocio.md`
* `Requisitos-Funcionais.md`
* `Requisitos-Nao-Funcionais.md`
* `Matriz-de-Rastreabilidade.md`
* `Catalogo-de-Servicos.md`
* `Catalogo-de-Processos.md`
* `Catalogo-de-Regras-de-Negocio.md`
* `Modelo-de-Requisitos.md`

Esses artefatos deverão permanecer integrados ao **Framework Corporativo de Gestão de Requisitos e Rastreabilidade**.

---

# 28. Disposição Final

O `Casos-de-Uso.md` constitui o **catálogo corporativo de referência para as interações entre atores e o SIGMUN**.

Nenhum caso de uso relevante deverá ser desenvolvido de forma isolada quando existir processo, serviço, regra de negócio ou capacidade corporativa relacionada.

O catálogo deverá evoluir continuamente conforme:

* novos serviços sejam identificados;
* processos sejam redesenhados;
* novos módulos sejam incorporados;
* requisitos sejam levantados;
* integrações sejam estabelecidas;
* necessidades dos cidadãos sejam identificadas;
* mudanças legais sejam implementadas;
* decisões arquiteturais sejam tomadas.

O objetivo final é garantir que cada funcionalidade do SIGMUN possua **propósito de negócio, ator, processo, serviço, requisito, rastreabilidade e evidência de valor público**.

---

**Documento:** Casos-de-Uso.md

**Última atualização:** 2026-08-11

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
