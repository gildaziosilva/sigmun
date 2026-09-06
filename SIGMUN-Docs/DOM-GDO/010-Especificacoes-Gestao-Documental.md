# 010 – Especificações – Gestão Documental

#### Especificações – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-010

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
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

---

# 1. Finalidade

Este documento define as **Especificações do Domínio de Gestão Documental** do SIGMUN.

As especificações representam o nível de detalhamento necessário para transformar:

* capacidades;
* processos;
* serviços;
* casos de uso;
* histórias de usuário;
* regras de negócio;
* requisitos funcionais;
* requisitos não funcionais;

em definições suficientemente precisas para orientar:

* arquitetura;
* desenvolvimento;
* configuração;
* integração;
* testes;
* homologação;
* implantação;
* operação.

Este documento não substitui os requisitos. Ele os **detalha e operacionaliza**.

---

# 2. Objetivos

As especificações deverão:

1. eliminar ambiguidades dos requisitos;
2. definir comportamentos esperados;
3. estabelecer entradas e saídas;
4. definir validações;
5. definir estados e transições;
6. estabelecer integrações;
7. definir eventos;
8. estabelecer regras de persistência;
9. definir requisitos de segurança;
10. permitir elaboração dos critérios de aceitação;
11. permitir implementação técnica;
12. preservar rastreabilidade.

---

# 3. Princípios

As especificações deverão observar:

* simplicidade;
* clareza;
* consistência;
* rastreabilidade;
* segurança;
* auditabilidade;
* interoperabilidade;
* reutilização;
* parametrização;
* baixa acoplagem;
* alta coesão;
* preservação histórica;
* transparência;
* conformidade normativa.

---

# 4. Estrutura das Especificações

Cada especificação deverá possuir, quando aplicável:

```text
Identificador
Título
Objetivo
Origem
Atores
Pré-condições
Entradas
Validações
Processamento
Regras
Saídas
Estados
Eventos
Integrações
Persistência
Auditoria
Segurança
Exceções
Pós-condições
Requisitos relacionados
Critérios de aceitação
```

---

# 5. Convenção de Identificação

As especificações utilizarão o padrão:

```text
ESP-GDO-XXX
```

Exemplo:

```text
ESP-GDO-001
```

O identificador deverá permanecer estável durante o ciclo de vida da especificação.

---

# 6. Especificações — Captura e Registro

## ESP-GDO-001 — Criar Documento Digital

**Objetivo:** Permitir a criação de um documento digital no sistema.

**Origem:** RF-GDO-001

**Atores:** Servidor/Gestor Documental

**Pré-condições:**
* Usuário autenticado com perfil USUARIO_GDO
* Unidade do usuário definida

**Entradas:**
* Tipo documental
* Título do documento
* Conteúdo do documento (arquivo ou texto)
* Metadados obrigatórios (autor, data, classificação)

**Validações:**
* Todos os metadados obrigatórios devem estar preenchidos
* Tipo documental deve ser válido
* Arquivo deve ter formato suportado

**Processamento:**
1. Validar metadados obrigatórios
2. Gerar código único de documento (RN-GDO-001)
3. Calcular hash SHA-256 do conteúdo (RN-GDO-002)
4. Armazenar documento no repositório
5. Indexar para pesquisa
6. Registrar log de auditoria

**Regras:**
* RN-GDO-001 (Unicidade de código documental)
* RN-GDO-002 (Integridade obrigatória por hash)
* RN-GDO-003 (Metadados obrigatórios)

**Saídas:**
* Código único do documento gerado
* Confirmação de registro
* Hash SHA-256 registrado

**Estados:** Rascunho → Registrado

**Eventos:** DocumentoCriado

**Integrações:** DOM-IDN (autenticação), DOM-MET (metadados)

**Persistência:** Tabela documentos, tabela versoes, tabela metadados

**Auditoria:** Registrar criação com usuário, data/hora e IP

**Segurança:** Verificar permissão de escrita na unidade

**Exceções:**
* Metadados incompletos → MSG001
* Formato não suportado → MSG002

**Pós-condições:** Documento registrado e disponível para tramitação

**Requisitos relacionados:** RF-GDO-001, RF-GDO-004, RF-GDO-005

**Critérios de aceitação:**
* Documento criado com código único
* Hash SHA-256 calculado e registrado
* Log de auditoria registrado

---

## ESP-GDO-002 — Digitalizar Documento Físico

**Objetivo:** Converter documento físico em digital via scanner.

**Origem:** RF-GDO-002

**Atores:** Servidor/Gestor Documental

**Pré-condições:**
* Scanner disponível e configurado
* Usuário autenticado

**Entradas:**
* Configurações de digitalização (resolução, formato)
* Documento físico para digitalização

**Validações:**
* Scanner conectado e funcional
* Resolução mínima de 300 DPI

**Processamento:**
1. Capturar imagem do scanner
2. Aplicar OCR se configurado
3. Converter para formato PDF/A
4. Gerar código único
5. Calcular hash SHA-256
6. Armazenar documento

**Regras:**
* RN-GDO-001
* RN-GDO-002
* RN-GDO-003

**Saídas:**
* Documento digitalizado
* Texto OCR (se aplicável)

**Estados:** Digitalizando → Digitalizado

**Eventos:** DocumentoDigitalizado

**Integrações:** DOM-IDN

**Persistência:** Tabela documentos, tabela versoes

**Auditoria:** Registrar digitalização

**Segurança:** Verificar permissão de escrita

**Exceções:**
* Scanner não disponível → MSG003
* Falha na digitalização → MSG004

**Pós-condições:** Documento digitalizado e disponível

**Requisitos relacionados:** RF-GDO-002, RF-GDO-033, RF-GDO-034

**Critérios de aceitação:**
* Documento digitalizado com qualidade
* OCR aplicado quando configurado

---

# 7. Especificações — Classificação Arquivística

## ESP-GDO-003 — Classificar Documento

**Objetivo:** Atribuir classificação arquivística ao documento.

**Origem:** RF-GDO-006

**Atores:** Servidor/Gestor Documental

**Pré-condições:**
* Documento registrado
* Plano de classificação configurado

**Entradas:**
* Código de classificação (classe, subclasse, série)

**Validações:**
* Hierarquia deve ser respeitada (Classe → Subclasse → Série)
* Classificação deve existir no plano

**Processamento:**
1. Validar hierarquia de classificação
2. Atribuir código de classificação
3. Vincular temporalidade automaticamente
4. Atualizar documento
5. Registrar auditoria

**Regras:**
* RN-GDO-004 (Temporalidade define destinação)
* RN-GDO-005 (Hierarquia obrigatória)

**Saídas:**
* Classificação atribuída
* Temporalidade vinculada

**Estados:** Sem classificação → Classificado

**Eventos:** DocumentoClassificado

**Integrações:** DOM-MET (metadados)

**Persistência:** Tabela documentos (atualização)

**Auditoria:** Registrar classificação

**Segurança:** Verificar permissão de classificação

**Exceções:**
* Hierarquia incompleta → MSG005
* Classificação inválida → MSG006

**Pós-condições:** Documento classificado com temporalidade definida

**Requisitos relacionados:** RF-GDO-006, RF-GDO-008, RF-GDO-047

**Critérios de aceitação:**
* Classificação atribuída corretamente
* Temporalidade vinculada automaticamente

---

# 8. Especificações — Tramitação

## ESP-GDO-004 — Tramitar Documento entre Unidades

**Objetivo:** Encaminhar documento entre unidades administrativas.

**Origem:** RF-GDO-009

**Atores:** Servidor/Gestor Documental (origem)

**Pré-condições:**
* Documento registrado e classificado
* Destinatário definido

**Entradas:**
* Unidade/pessoa destinatária
* Observações/despacho
* Documentos anexados (se aplicável)

**Validações:**
* Destinatário deve ser válido
* Unidade destinatária deve existir

**Processamento:**
1. Validar destinatário
2. Registrar origem, destino, data/hora
3. Criar movimentação de tramitação
4. Notificar destinatário
5. Atualizar status do documento
6. Registrar auditoria

**Regras:**
* RN-GDO-006 (Rastreabilidade da tramitação)

**Saídas:**
* Tramitação registrada
* Notificação ao destinatário

**Estados:** Na origem → Em tramitação → No destino

**Eventos:** DocumentoTramitado

**Integrações:** DOM-IDN, Serviço de Notificações

**Persistência:** Tabela tramitacoes, tabela documentos

**Auditoria:** Registrar tramitação completa

**Segurança:** Verificar permissão de tramitação

**Exceções:**
* Destinatário inválido → MSG007
* Unidade inexistente → MSG008

**Pós-condições:** Documento em tramitação para destino

**Requisitos relacionados:** RF-GDO-009, RF-GDO-010

**Critérios de aceitação:**
* Tramitação registrada com todos os dados
* Destinatário notificado

---

## ESP-GDO-005 — Receber Documento Tramitado

**Objetivo:** Confirmar recebimento de documento tramitado.

**Origem:** RF-GDO-011

**Atores:** Servidor/Gestor Documental (destino)

**Pré-condições:**
* Documento em tramitação para a unidade do usuário

**Entradas:**
* Confirmação de ciência

**Validações:**
* Usuário deve pertencer à unidade destinatária

**Processamento:**
1. Validar pertinência do usuário ao destino
2. Registrar ciência do recebimento
3. Atualizar status da tramitação
4. Registrar auditoria

**Regras:**
* RN-GDO-007 (Ciência obrigatória para recebimento)

**Saídas:**
* Ciência registrada
* Status atualizado

**Estados:** Em tramitação → Recebido

**Eventos:** DocumentoRecebido

**Integrações:** DOM-IDN

**Persistência:** Tabela tramitacoes (atualização)

**Auditoria:** Registrar recebimento

**Segurança:** Verificar pertinência à unidade

**Exceções:**
* Usuário não pertence ao destino → MSG009

**Pós-condições:** Documento recebido na unidade

**Requisitos relacionados:** RF-GDO-011

**Critérios de aceitação:**
* Ciência registrada com sucesso
* Status atualizado para "Recebido"

---

# 9. Especificações — Arquivamento

## ESP-GDO-006 — Arquivar Documento Corrente

**Objetivo:** Arquivar documento após conclusão da tramitação.

**Origem:** RF-GDO-013

**Atores:** Servidor/Gestor Documental

**Pré-condições:**
* Documento com tramitação concluída

**Entradas:**
* Confirmação de arquivamento

**Validações:**
* Todas as tramitações devem estar concluídas

**Processamento:**
1. Validar conclusão da tramitação
2. Alterar status para "Arquivado"
3. Definir fase como "Corrente"
4. Registrar auditoria

**Regras:**
* RN-GDO-008 (Arquivamento somente após conclusão)

**Saídas:**
* Documento arquivado

**Estados:** Concluído → Arquivado (corrente)

**Eventos:** DocumentoArquivado

**Integrações:** DOM-IDN

**Persistência:** Tabela documentos (atualização)

**Auditoria:** Registrar arquivamento

**Segurança:** Verificar permissão de arquivamento

**Exceções:**
* Tramitação não concluída → MSG010

**Pós-condições:** Documento arquivado na fase corrente

**Requisitos relacionados:** RF-GDO-013, RF-GDO-014

**Critérios de aceitação:**
* Documento arquivado com sucesso
* Status alterado para "Arquivado"

---

# 10. Especificações — Destinação

## ESP-GDO-007 — Aprovar Eliminação de Documento

**Objetivo:** Autoridade homologadora aprovar eliminação de documentos.

**Origem:** RF-GDO-016

**Atores:** Autoridade Homologadora

**Pré-condições:**
* Documento avaliado para destinação
* Prazo de retenção atingido

**Entradas:**
* Decisão (aprovar/rejeitar)
* Justificativa (se rejeitar)

**Validações:**
* Usuário deve ter perfil AUTORIDADE_GDO
* Prazo de retenção deve ter sido atingido

**Processamento:**
1. Validar perfil de autoridade homologadora
2. Validar prazo de retenção
3. Registrar decisão
4. Se aprovado: eliminar documento
5. Gerar termo de eliminação
6. Registrar auditoria

**Regras:**
* RN-GDO-010 (Não eliminar sem autorização)
* RN-GDO-011 (Eliminação requer autoridade homologadora)

**Saídas:**
* Decisão registrada
* Termo de eliminação (se aprovado)

**Estados:** Em avaliação → Eliminado

**Eventos:** DocumentoEliminado

**Integrações:** DOM-IDN

**Persistência:** Tabela documentos (atualização), tabela eliminacoes

**Auditoria:** Registrar decisão de eliminação

**Segurança:** Verificar perfil de autoridade homologadora

**Exceções:**
* Perfil insuficiente → MSG011
* Prazo não atingido → MSG012

**Pós-condições:** Documento eliminado ou decisão registrada

**Requisitos relacionados:** RF-GDO-015, RF-GDO-016

**Critérios de aceitação:**
* Decisão registrada com segurança
* Termo de eliminação gerado quando aplicável

---

# 11. Especificações — Assinatura Digital

## ESP-GDO-008 — Assinar Documento Digitalmente

**Objetivo:** Assinar documento com certificado digital ICP-Brasil.

**Origem:** RF-GDO-025

**Atores:** Servidor/Gestor Documental, Autoridade

**Pré-condições:**
* Documento registrado
* Certificado digital válido

**Entradas:**
* Certificado digital (A1 ou A3)
* PIN do certificado

**Validações:**
* Certificado deve ser válido (ICP-Brasil)
* Certificado não pode estar vencido ou revogado

**Processamento:**
1. Validar certificado digital
2. Solicitar PIN do certificado
3. Assinar documento digitalmente
4. Registrar assinatura
5. Bloquear alterações no documento
6. Registrar auditoria

**Regras:**
* RN-GDO-017 (Assinatura requer certificado válido)
* RN-GDO-018 (Documento assinado não pode ser alterado)

**Saídas:**
* Documento assinado digitalmente
* Certificado do signatário registrado

**Estados:** Registrado → Assinado

**Eventos:** DocumentoAssinado

**Integrações:** DOM-IDN, Certificador Digital (ICP-Brasil)

**Persistência:** Tabela documentos, tabela assinaturas

**Auditoria:** Registrar assinatura com certificado

**Segurança:** Validar certificado ICP-Brasil

**Exceções:**
* Certificado inválido → MSG013
* Certificado vencido → MSG014
* PIN incorreto → MSG015

**Pós-condições:** Documento assinado e imutável

**Requisitos relacionados:** RF-GDO-025, RF-GDO-026

**Critérios de aceitação:**
* Documento assinado com sucesso
* Assinatura válida e verificável
* Documento bloqueado para alterações

---

# 12. Especificações — Segurança e Acesso

## ESP-GDO-009 — Configurar Permissões de Acesso ao Documento

**Objetivo:** Definir permissões de acesso por documento.

**Origem:** RF-GDO-029

**Atores:** Administrador GDO

**Pré-condições:**
* Usuário com perfil ADMIN_GDO

**Entradas:**
* Nível de sigilo (público, reservado, secreto)
* Permissões por unidade/pessoa

**Validações:**
* Nível de sigilo deve ser válido
* Unidades/pessoas devem existir

**Processamento:**
1. Validar perfil de administrador
2. Aplicar classificação de sigilo
3. Configurar permissões específicas
4. Registrar auditoria

**Regras:**
* RN-GDO-019 (Classificação de sigilo obrigatória)

**Saídas:**
* Permissões configuradas

**Estados:** Sem restrição → Com restrição

**Eventos:** PermissaoConfigurada

**Integrações:** DOM-IDN

**Persistência:** Tabela permissoes_documento

**Auditoria:** Registrar configuração de permissões

**Segurança:** Verificar perfil de administrador

**Exceções:**
* Perfil insuficiente → MSG016
* Nível de sigilo inválido → MSG017

**Pós-condições:** Documento com acesso controlado

**Requisitos relacionados:** RF-GDO-029, RF-GDO-030

**Critérios de aceitação:**
* Permissões configuradas corretamente
* Acesso restrito conforme configuração

---

# 13. Especificações — Versionamento

## ESP-GDO-010 — Criar Nova Versão de Documento

**Objetivo:** Criar nova versão preservando histórico imutável.

**Origem:** RF-GDO-031

**Atores:** Servidor/Gestor Documental

**Pré-condições:**
* Documento registrado
* Documento não assinado

**Entradas:**
* Novo conteúdo do documento
* Justificativa da versão

**Validações:**
* Documento não pode estar assinado
* Justificativa obrigatória

**Processamento:**
1. Validar que documento não está assinado
2. Preservar versão anterior (imutável)
3. Criar nova versão
4. Gerar novo hash SHA-256
5. Incrementar número da versão
6. Registrar auditoria

**Regras:**
* RN-GDO-005 (Versão imutável)
* RN-GDO-025 (Nova versão preserva histórico)

**Saídas:**
* Nova versão do documento
* Histórico preservado

**Estados:** Versão N → Versão N+1

**Eventos:** NovaVersaoCriada

**Integrações:** DOM-IDN

**Persistência:** Tabela versoes

**Auditoria:** Registrar criação de nova versão

**Segurança:** Verificar permissão de escrita

**Exceções:**
* Documento assinado → MSG018
* Justificativa não informada → MSG019

**Pós-condições:** Nova versão criada com histórico preservado

**Requisitos relacionados:** RF-GDO-031, RF-GDO-032

**Critérios de aceitação:**
* Nova versão criada
* Versão anterior preservada (imutável)
* Histórico completo disponível

---

# 14. Relação com Requisitos

| Especificação | Requisito Funcional | Requisito Não Funcional |
| --- | --- | --- |
| ESP-GDO-001 | RF-GDO-001, RF-GDO-004, RF-GDO-005 | RNF-GDO-001, RNF-GDO-003 |
| ESP-GDO-002 | RF-GDO-002, RF-GDO-033 | RNF-GDO-010, RNF-GDO-011 |
| ESP-GDO-003 | RF-GDO-006, RF-GDO-008 | RNF-GDO-024 |
| ESP-GDO-004 | RF-GDO-009, RF-GDO-010 | RNF-GDO-024 |
| ESP-GDO-005 | RF-GDO-011 | RNF-GDO-024 |
| ESP-GDO-006 | RF-GDO-013 | RNF-GDO-024 |
| ESP-GDO-007 | RF-GDO-016 | RNF-GDO-001, RNF-GDO-002 |
| ESP-GDO-008 | RF-GDO-025 | RNF-GDO-001, RNF-GDO-003 |
| ESP-GDO-009 | RF-GDO-029, RF-GDO-030 | RNF-GDO-001, RNF-GDO-002, RNF-GDO-005 |
| ESP-GDO-010 | RF-GDO-031, RF-GDO-032 | RNF-GDO-016, RNF-GDO-028 |

---

# 15. Refinamento Futuro

As especificações deste documento representam a primeira decomposição das necessidades do domínio.

Durante o refinamento, uma especificação poderá:

* ser dividida em várias especificações;
* ser combinada com outra;
* ser descartada;
* ser transformada em requisito transversal;
* depender de serviço corporativo;
* gerar múltiplos critérios de aceitação.

Nenhuma especificação deverá ser considerada tecnicamente implementada apenas pela sua existência neste documento.

---

# 16. Registro no Mapa Mestre

Este artefato deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

**Identificador do artefato:**

`ESP-MAP-GDO-001`

**Tipo:**

Mapa de Especificações.

**Domínio:**

Gestão Documental.

**Versão:**

2.0.

---

# 17. Próximo Artefato

O próximo artefato recomendado é:

`011-Criterios-de-Aceitacao-Gestao-Documental.md`

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

# 18. Controle de Versões

| Versão | Data       | Descrição |
| ------ | ---------- | --------- |
| 1.0    | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0    | 2026-09-02 | Conteúdo detalhado: 10 especificações, estrutura completa |

---

**Documento:** 010-Especificacoes-Gestao-Documental.md

**Última atualização:** 2026-09-02

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
