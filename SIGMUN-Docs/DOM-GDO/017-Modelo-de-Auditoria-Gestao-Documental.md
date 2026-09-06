# 017 – Modelo de Auditoria – Gestão Documental

#### Modelo de Auditoria – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-017

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
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

---

# 1. Finalidade

Este documento define o **Modelo de Auditoria do Domínio de Gestão Documental do SIGMUN**.

O modelo estabelece os princípios, mecanismos, eventos, registros, controles e responsabilidades necessários para garantir a rastreabilidade das operações realizadas no domínio.

A auditoria deverá permitir reconstruir, quando necessário:

```text
Quem
  ↓
Fez o quê
  ↓
Quando
  ↓
Onde
  ↓
Sobre qual recurso
  ↓
Qual era o estado anterior
  ↓
Qual foi o novo estado
  ↓
Qual foi o resultado
```

---

# 2. Objetivos

São objetivos deste modelo:

1. garantir rastreabilidade;
2. registrar operações relevantes;
3. preservar evidências;
4. apoiar controles internos;
5. apoiar auditorias administrativas;
6. apoiar auditorias de segurança;
7. detectar operações indevidas;
8. permitir investigação de incidentes;
9. apoiar prestação de contas;
10. aumentar a transparência;
11. apoiar conformidade;
12. preservar histórico dos processos;
13. permitir reconstrução da linha do tempo dos eventos.

---

# 3. Princípios de Auditoria

## 3.1 Rastreabilidade

Toda operação relevante deverá ser rastreável até o usuário, serviço ou sistema responsável.

## 3.2 Integridade

Os registros de auditoria deverão ser protegidos contra alterações indevidas.

## 3.3 Imutabilidade

Sempre que tecnicamente possível, os registros deverão ser armazenados de forma que alterações posteriores sejam impedidas ou detectáveis.

## 3.4 Responsabilização

As operações deverão permitir identificar o responsável pela sua execução.

## 3.5 Segregação

Os mecanismos de auditoria deverão possuir controles independentes dos mecanismos de operação do processo.

## 3.6 Evidência

Os registros de auditoria deverão servir como evidência para controles internos, auditorias e prestação de contas.

---

# 4. Eventos de Auditoria

## 4.1 Eventos de Documento

| Evento | Descrição | Categoria | Obrigatoriedade |
| --- | --- | --- | --- |
| DOCUMENTO_CRIADO | Documento criado | Criação | Obrigatório |
| DOCUMENTO_ATUALIZADO | Metadados atualizados | Atualização | Obrigatório |
| DOCUMENTO_CLASSIFICADO | Documento classificado | Classificação | Obrigatório |
| DOCUMENTO_RECLASSIFICADO | Documento reclassificado | Classificação | Obrigatório |
| DOCUMENTO_ASSINADO | Documento assinado | Assinatura | Obrigatório |
| DOCUMENTO_VERSIONADO | Nova versão criada | Versionamento | Obrigatório |
| DOCUMENTO_RESTAURADO | Versão restaurada | Versionamento | Obrigatório |
| DOCUMENTO_VISUALIZADO | Documento consultado | Consulta | Obrigatório |
| DOCUMENTO_BAIXADO | Documento baixado | Download | Obrigatório |

## 4.2 Eventos de Tramitação

| Evento | Descrição | Categoria | Obrigatoriedade |
| --- | --- | --- | --- |
| DOCUMENTO_TRAMITADO | Documento tramitado | Tramitação | Obrigatório |
| DOCUMENTO_RECEBIDO | Documento recebido | Tramitação | Obrigatório |
| DOCUMENTO_DEVOLVIDO | Documento devolvido | Tramitação | Obrigatório |

## 4.3 Eventos de Processo

| Evento | Descrição | Categoria | Obrigatoriedade |
| --- | --- | --- | --- |
| PROCESSO_ABERTO | Processo aberto | Processo | Obrigatório |
| DOCUMENTO_INCLUIDO | Documento incluído | Processo | Obrigatório |
| PROCESSO_ENCERRADO | Processo encerrado | Processo | Obrigatório |
| PROCESSO_REABERTO | Processo reaberto | Processo | Obrigatório |

## 4.4 Eventos de Destinação

| Evento | Descrição | Categoria | Obrigatoriedade |
| --- | --- | --- | --- |
| DOCUMENTO_AVALIADO | Documento avaliado | Destinação | Obrigatório |
| DOCUMENTO_ELIMINADO | Documento eliminado | Destinação | Obrigatório |
| DOCUMENTO_GUARDA_PERMANENTE | Guarda permanente | Destinação | Obrigatório |
| PRAZO_PRORROGADO | Prazo prorrogado | Destinação | Obrigatório |

## 4.5 Eventos de Segurança

| Evento | Descrição | Categoria | Obrigatoriedade |
| --- | --- | --- | --- |
| ACESSO_NEGADO | Tentativa de acesso negado | Segurança | Obrigatório |
| PERMISSAO_ALTERADA | Permissão alterada | Segurança | Obrigatório |
| SIGILO_ALTERADO | Nível de sigilo alterado | Seguranca | Obrigatório |
| AUTENTICACAO_FALHA | Falha de autenticação | Segurança | Obrigatório |
| AUTENTICACAO_SUCESSO | Autenticação bem-sucedida | Segurança | Opcional |

## 4.6 Eventos de Administração

| Evento | Descrição | Categoria | Obrigatoriedade |
| --- | --- | --- | --- |
| PLANO_CONFIGURADO | Plano de classificação configurado | Admin | Obrigatório |
| TEMPORALIDADE_CONFIGURADA | Temporalidade configurada | Admin | Obrigatório |
| TAXONOMIA_CONFIGURADA | Taxonomia configurada | Admin | Obrigatório |
| PERFIL_CRIADO | Perfil de acesso criado | Admin | Obrigatório |

---

# 5. Registros de Auditoria

## 5.1 Estrutura do Registro

| Campo | Tipo | Descrição |
| --- | --- | --- |
| id | UUID | Identificador único do registro |
| evento | VARCHAR(100) | Tipo do evento |
| entidade | VARCHAR(100) | Entidade afetada |
| entidade_id | UUID | ID do registro afetado |
| usuario_id | UUID | Usuário responsável |
| data_hora | TIMESTAMP | Data e hora da operação |
| ip_origem | VARCHAR(45) | IP de origem |
| dados_antigos | JSON | Estado anterior |
| dados_novos | JSON | Novo estado |
| resultado | VARCHAR(20) | SUCESSO ou ERRO |
| observacao | TEXT | Observações adicionais |

## 5.2 Retenção

* Período mínimo de retenção: 5 anos
* Armazenamento seguro e imutável
* Backup dos registros de auditoria

---

# 6. Controles de Auditoria

## 6.1 Controles Preventivos

| Controle | Descrição |
| --- | --- |
| Autenticação obrigatória | Verificar identidade antes de qualquer operação |
| Autorização | Verificar permissões antes de executar operações |
| Validação de entrada | Validar dados antes de processar |
| Segregação de funções | Separar operações incompatíveis |

## 6.2 Controles Detectivos

| Controle | Descrição |
| --- | --- |
| Logs de auditoria | Registrar todas as operações relevantes |
| Alertas de segurança | Notificar operações suspeitas |
| Monitoramento de acesso | Acompanhar padrões de acesso |
| Detecção de anomalias | Identificar comportamentos incomuns |

## 6.3 Controles Corretivos

| Controle | Descrição |
| --- | --- |
| Investigação de incidentes | Analisar eventos de segurança |
| Bloqueio de acesso | Suspender acessos comprometidos |
| Recuperação de dados | Restaurar dados em caso de problemas |
| Notificação | Comunicar autoridades competentes |

---

# 7. Relatórios de Auditoria

## 7.1 Relatórios Operacionais

| Relatório | Descrição | Frequência |
| --- | --- | --- |
| Acesso por usuário | Listar acessos por usuário | Diário |
| Operações por documento | Histórico de operações | Sob demanda |
| Tramitações | Movimentações de documentos | Diário |
| Destinações | Documentos destinados | Mensal |

## 7.2 Relatórios de Segurança

| Relatório | Descrição | Frequência |
| --- | --- | --- |
| Tentativas de acesso negado | Listar acessos negados | Diário |
| Alterações de permissões | Mudanças em permissões | Diário |
| Alterações de sigilo | Mudanças em classificação | Diário |
| Autenticações suspeitas | Padrões anormais | Tempo real |

## 7.3 Relatórios de Conformidade

| Relatório | Descrição | Frequência |
| --- | --- | --- |
| Integridade de documentos | Verificação de hash | Mensal |
| Retenção de documentos | Prazos de retenção | Mensal |
| Operações por perfil | Atividade por perfil | Trimestral |
| Auditoria completa | Relatório abrangente | Anual |

---

# 8. Responsabilidades

## 8.1 Equipe de Gestão Documental

* Configurar parâmetros de auditoria
* Analisar relatórios operacionais
* Investigar incidentes identificados

## 8.2 Equipe de Segurança

* Monitorar alertas de segurança
* Investigar incidentes de segurança
* Analisar relatórios de segurança

## 8.3 Auditoria Interna

* Realizar auditorias periódicas
* Verificar conformidade
* Emitir relatórios de auditoria

## 8.4 Administrador GDO

* Configurar eventos de auditoria
* Gerenciar retenção de registros
* Administrar perfis de acesso

---

# 9. Refinamento Futuro

O modelo deste documento representa a primeira versão da auditoria do domínio.

Durante o refinamento, o modelo poderá:

* ser expandido com novos eventos;
* ser ajustado conforme evolução dos requisitos;
* ser integrado com SIEM corporativo;
* ser atualizado conforme novas regulamentações.

---

# 10. Registro no Mapa Mestre

Este artefato deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

**Identificador do artefato:**

`AUD-MAP-GDO-001`

**Tipo:**

Modelo de Auditoria.

**Domínio:**

Gestão Documental.

**Versão:**

2.0.

---

# 11. Próximo Artefato

O próximo artefato recomendado é:

`018-Plano-de-Testes-Gestao-Documental.md`

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
      ↓
013-Modelo de Dados
      ↓
014-Modelo de Integração
      ↓
015-Arquitetura de Serviços
      ↓
016-Modelo de Segurança
      ↓
017-Modelo de Auditoria
      ↓
018-Plano de Testes
```

---

# 12. Controle de Versões

| Versão | Data       | Descrição |
| ------ | ---------- | --------- |
| 1.0    | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0    | 2026-09-02 | Conteúdo detalhado: eventos, controles, relatórios |

---

**Documento:** 017-Modelo-de-Auditoria-Gestao-Documental.md

**Última atualização:** 2026-09-02

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
