# 011 – Critérios de Aceitação – Gestão Documental

#### Critérios de Aceitação – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-011

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
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

---

# 1. Finalidade

Este documento define os **Critérios de Aceitação do Domínio de Gestão Documental** do SIGMUN.

Os critérios de aceitação estabelecem as condições objetivas que deverão ser satisfeitas para que uma funcionalidade, serviço, processo ou requisito seja considerado **aceito**.

Os critérios deverão transformar os requisitos e especificações em condições:

* verificáveis;
* mensuráveis quando aplicável;
* testáveis;
* rastreáveis;
* reproduzíveis;
* compreensíveis pelas áreas de negócio e pelas equipes técnicas.

---

# 2. Objetivos

Os critérios de aceitação têm como objetivos:

1. definir claramente o resultado esperado;
2. reduzir ambiguidades;
3. estabelecer condições de aprovação;
4. apoiar homologação;
5. orientar testes;
6. permitir rastreabilidade;
7. evitar interpretação subjetiva;
8. estabelecer condições mínimas para entrada em produção;
9. apoiar auditoria;
10. preservar conhecimento institucional.

---

# 3. Princípios

Os critérios deverão observar:

* clareza;
* objetividade;
* verificabilidade;
* rastreabilidade;
* independência de implementação quando possível;
* foco no resultado;
* consistência;
* segurança;
* acessibilidade;
* conformidade;
* auditabilidade.

---

# 4. Convenção de Identificação

Os critérios utilizarão o padrão:

```text
CA-GDO-XXX
```

Exemplo:

```text
CA-GDO-001
```

Quando necessário, poderão existir critérios derivados:

```text
CA-GDO-001.1
CA-GDO-001.2
CA-GDO-001.3
```

---

# 5. Critérios de Aceitação — Captura e Registro

## CA-GDO-001 — Criar Documento Digital

**Requisito:** RF-GDO-001

**Critérios:**

1. O sistema deve permitir criar um documento digital com metadados obrigatórios
2. O código do documento deve ser gerado automaticamente e ser único
3. O hash SHA-256 deve ser calculado e registrado no momento da captura
4. O documento deve estar disponível para consulta após o registro
5. O log de auditoria deve registrar a criação com usuário, data/hora e IP
6. Deve ser exibida mensagem de erro quando metadados obrigatórios não forem preenchidos
7. Deve ser exibida mensagem de erro quando o formato do arquivo não for suportado

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

## CA-GDO-002 — Digitalizar Documento Físico

**Requisito:** RF-GDO-002

**Critérios:**

1. O sistema deve permitir digitalizar documentos via scanner integrado
2. A digitalização deve gerar arquivo em formato PDF/A
3. O código do documento deve ser gerado automaticamente
4. O hash SHA-256 deve ser calculado e registrado
5. O documento digitalizado deve estar disponível para consulta
6. Deve ser exibida mensagem de erro quando o scanner não estiver disponível

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

## CA-GDO-003 — Importar Documento Externo

**Requisito:** RF-GDO-003

**Critérios:**

1. O sistema deve permitir importar documentos de sistemas externos
2. Os metadados originais devem ser preservados quando disponíveis
3. O código do documento deve ser gerado automaticamente
4. O hash SHA-256 deve ser calculado e registrado
5. O documento importado deve estar disponível para consulta

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

# 6. Critérios de Aceitação — Classificação Arquivística

## CA-GDO-004 — Classificar Documento

**Requisito:** RF-GDO-006

**Critérios:**

1. O sistema deve permitir classificar documento conforme plano de classificação
2. A hierarquia deve ser respeitada (Classe → Subclasse → Série)
3. A temporalidade deve ser vinculada automaticamente
4. A classificação deve ser registrada em auditoria
5. Deve ser exibida mensagem de erro quando a hierarquia estiver incompleta

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

## CA-GDO-005 — Reclassificar Documento

**Requisito:** RF-GDO-007

**Critérios:**

1. O sistema deve permitir reclassificar documento
2. A alteração deve ser registrada em auditoria
3. A temporalidade deve ser atualizada automaticamente

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

# 7. Critérios de Aceitação — Tramitação

## CA-GDO-006 — Tramitar Documento entre Unidades

**Requisito:** RF-GDO-009

**Critérios:**

1. O sistema deve permitir tramitar documento entre unidades
2. Devem ser registrados: origem, destino, data/hora, usuário e observação
3. O destinatário deve ser notificado
4. A tramitação deve ser registrada em auditoria
5. Deve ser exibida mensagem de erro quando o destinatário for inválido

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

## CA-GDO-007 — Despachar Documento com Instruções

**Requisito:** RF-GDO-010

**Critérios:**

1. O sistema deve permitir anexar despacho com instruções ao tramitar
2. O despacho deve ficar vinculado à tramitação
3. O destinatário deve ter acesso ao despacho

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

## CA-GDO-008 — Receber Documento Tramitado

**Requisito:** RF-GDO-011

**Critérios:**

1. O sistema deve permitir confirmar ciência do recebimento
2. Sem ciência, o documento deve permanecer como "pendente de recebimento"
3. A ciência deve ser registrada em auditoria
4. Deve ser exibida mensagem de erro quando o usuário não pertencer ao destino

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

## CA-GDO-009 — Devolver Documento à Unidade de Origem

**Requisito:** RF-GDO-012

**Critérios:**

1. O sistema deve permitir devolver documento com justificativa
2. A devolução deve ser registrada em auditoria
3. A unidade de origem deve ser notificada

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

# 8. Critérios de Aceitação — Arquivamento

## CA-GDO-010 — Arquivar Documento Corrente

**Requisito:** RF-GDO-013

**Critérios:**

1. O sistema deve permitir arquivar documento após conclusão da tramitação
2. Documentos em tramitação não podem ser arquivados
3. O arquivamento deve ser registrado em auditoria
4. Deve ser exibida mensagem de erro quando a tramitação não estiver concluída

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

## CA-GDO-011 — Desarquivar Documento

**Requisito:** RF-GDO-014

**Critérios:**

1. O sistema deve permitir desarquivar documento
2. Devem ser registrados: motivo, data/hora, usuário e nova destinação
3. O desarquivamento deve ser registrado em auditoria

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

# 9. Critérios de Aceitação — Destinação

## CA-GDO-012 — Avaliar Documento para Destinação

**Requisito:** RF-GDO-015

**Critérios:**

1. O sistema deve permitir avaliar documentos quanto ao prazo de retenção
2. Deve ser possível propor eliminação ou guarda permanente
3. A avaliação deve ser registrada em auditoria

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

## CA-GDO-013 — Aprovar Eliminação de Documento

**Requisito:** RF-GDO-016

**Critérios:**

1. Apenas autoridade homologadora pode aprovar eliminação
2. Documentos em fase corrente não podem ser eliminados sem autorização
3. Deve ser gerado termo de eliminação
4. A decisão deve ser registrada em auditoria
5. Deve ser exibida mensagem de erro quando o perfil for insuficiente
6. Deve ser exibida mensagem de erro quando o prazo não tiver sido atingido

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

## CA-GDO-014 — Destinar Documento à Guarda Permanente

**Requisito:** RF-GDO-017

**Critérios:**

1. Apenas autoridade homologadora pode aprovar guarda permanente
2. Deve ser registrado o valor histórico ou probatório
3. A decisão deve ser registrada em auditoria

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

## CA-GDO-015 — Prorrogar Prazo de Retenção

**Requisito:** RF-GDO-018

**Critérios:**

1. O sistema deve permitir solicitar prorrogação com justificativa
2. A justificativa deve ser obrigatória
3. A prorrogação deve ser registrada em auditoria

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

# 10. Critérios de Aceitação — Processos Documentais

## CA-GDO-016 — Abrir Processo Documental

**Requisito:** RF-GDO-019

**Critérios:**

1. O sistema deve permitir abrir processo com identificação, assunto e unidade
2. O processo deve possuir ao menos um documento inicial
3. A abertura deve ser registrada em auditoria

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

## CA-GDO-017 — Incluir Documento em Processo

**Requisito:** RF-GDO-020

**Critérios:**

1. O sistema deve permitir incluir documento em processo existente
2. O documento deve ficar vinculado ao processo
3. A inclusão deve ser registrada em auditoria

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

## CA-GDO-018 — Encerrar Processo

**Requisito:** RF-GDO-021

**Critérios:**

1. O sistema deve permitir encerrar processo quando todas as tramitações estiverem concluídas
2. Processos com tramitações pendentes não podem ser encerrados
3. O encerramento deve ser registrado em auditoria

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

## CA-GDO-019 — Reabrir Processo Encerrado

**Requisito:** RF-GDO-022

**Critérios:**

1. Apenas administrador GDO pode reabrir processo
2. Deve ser informada justificativa formal
3. A reabertura deve ser registrada em auditoria

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

# 11. Critérios de Aceitação — Pesquisa e Consulta

## CA-GDO-020 — Pesquisar Documentos com Filtros

**Requisito:** RF-GDO-023

**Critérios:**

1. O sistema deve permitir pesquisa por unidade, período, tipo, classificação e palavras-chave
2. Os resultados devem ser retornados em até 2 segundos para até 10.000 registros
3. Deve ser possível combinar múltiplos filtros

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

## CA-GDO-021 — Consultar Documento Público

**Requisito:** RF-GDO-024

**Critérios:**

1. O sistema deve permitir consulta de documentos públicos sem autenticação
2. Documentos sigilosos não devem aparecer na consulta pública
3. Deve ser possível pesquisar por assunto, período ou unidade

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

# 12. Critérios de Aceitação — Assinatura Digital

## CA-GDO-022 — Assinar Documento Digitalmente

**Requisito:** RF-GDO-025

**Critérios:**

1. O sistema deve permitir assinatura com certificado ICP-Brasil válido
2. Certificados vencidos ou revogados não devem ser aceitos
3. Após assinatura, o documento não pode ser alterado
4. A assinatura deve ser registrada em auditoria
5. Deve ser exibida mensagem de erro quando o certificado for inválido

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

## CA-GDO-023 — Validar Assinatura Digital

**Requisito:** RF-GDO-026

**Critérios:**

1. O sistema deve permitir validar assinatura digital
2. Deve ser exibida informação sobre autenticidade e integridade
3. Deve ser exibido certificado do signatário

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

# 13. Critérios de Aceitação — Auditoria

## CA-GDO-024 — Consultar Histórico de Auditoria

**Requisito:** RF-GDO-027

**Critérios:**

1. O sistema deve permitir consultar histórico completo de auditoria
2. Devem ser exibidas: criação, alterações, tramitações e acessos
3. Cada registro deve conter: usuário, data/hora, ação e IP
4. Registros de auditoria não podem ser alterados ou excluídos

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

# 14. Critérios de Aceitação — Segurança e Acesso

## CA-GDO-025 — Configurar Permissões de Acesso ao Documento

**Requisito:** RF-GDO-029

**Critérios:**

1. O sistema deve permitir configurar permissões por documento
2. Devem ser suportados níveis: público, reservado, secreto
3. A configuração deve ser registrada em auditoria

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

## CA-GDO-026 — Classificar Sigilo do Documento

**Requisito:** RF-GDO-030

**Critérios:**

1. O sistema deve permitir classificar sigilo em três níveis
2. Documentos sem classificação devem ser tratados como restritos
3. A classificação deve ser registrada em auditoria

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

# 15. Critérios de Aceitação — Versionamento

## CA-GDO-027 — Criar Nova Versão de Documento

**Requisito:** RF-GDO-031

**Critérios:**

1. O sistema deve permitir criar nova versão de documento
2. Versões anteriores devem ser preservadas (imutáveis)
3. Documentos assinados não podem ter novas versões
4. Deve ser informada justificativa obrigatória
5. A nova versão deve ser registrada em auditoria

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

## CA-GDO-028 — Restaurar Versão Anterior

**Requisito:** RF-GDO-032

**Critérios:**

1. O sistema deve permitir restaurar versão anterior
2. A restauração deve gerar uma nova versão
3. O histórico de versões deve ser preservado
4. A restauração deve ser registrada em auditoria

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

# 16. Critérios de Aceitação — Temporalidade

## CA-GDO-029 — Configurar Tabela de Temporalidade

**Requisito:** RF-GDO-039

**Critérios:**

1. O sistema deve permitir configurar prazos por tipo documental
2. Deve ser possível definir prazo de retenção e destinação
3. A configuração deve ser registrada em auditoria

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

## CA-GDO-030 — Gerar Alerta de Temporalidade

**Requisito:** RF-GDO-040

**Critérios:**

1. O sistema deve gerar alerta quando documentos atingirem 80% do prazo
2. O alerta deve notificar o responsável pela avaliação
3. O alerta deve ser registrado em auditoria

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

# 17. Critérios de Aceitação — Administração do Sistema

## CA-GDO-031 — Configurar Plano de Classificação

**Requisito:** RF-GDO-047

**Critérios:**

1. Apenas administrador GDO pode configurar plano de classificação
2. Deve ser possível definir classes, subclasses e séries
3. A configuração deve ser registrada em auditoria

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

## CA-GDO-032 — Gerenciar Perfis de Acesso ao GDO

**Requisito:** RF-GDO-048

**Critérios:**

1. O sistema deve permitir gerenciar perfis de acesso
2. Devem ser suportados perfis: leitura, escrita, administração
3. A configuração deve ser registrada em auditoria

**Condições de aceitação:** Todos os critérios devem ser satisfeitos

---

# 18. Relação com Requisitos

| Critério | Requisito | Especificação |
| --- | --- | --- |
| CA-GDO-001 | RF-GDO-001 | ESP-GDO-001 |
| CA-GDO-002 | RF-GDO-002 | ESP-GDO-002 |
| CA-GDO-003 | RF-GDO-003 | ESP-GDO-001 |
| CA-GDO-004 | RF-GDO-006 | ESP-GDO-003 |
| CA-GDO-005 | RF-GDO-007 | ESP-GDO-003 |
| CA-GDO-006 | RF-GDO-009 | ESP-GDO-004 |
| CA-GDO-007 | RF-GDO-010 | ESP-GDO-004 |
| CA-GDO-008 | RF-GDO-011 | ESP-GDO-005 |
| CA-GDO-009 | RF-GDO-012 | ESP-GDO-004 |
| CA-GDO-010 | RF-GDO-013 | ESP-GDO-006 |
| CA-GDO-011 | RF-GDO-014 | ESP-GDO-006 |
| CA-GDO-012 | RF-GDO-015 | ESP-GDO-007 |
| CA-GDO-013 | RF-GDO-016 | ESP-GDO-007 |
| CA-GDO-014 | RF-GDO-017 | ESP-GDO-007 |
| CA-GDO-015 | RF-GDO-018 | ESP-GDO-007 |
| CA-GDO-016 | RF-GDO-019 | — |
| CA-GDO-017 | RF-GDO-020 | — |
| CA-GDO-018 | RF-GDO-021 | — |
| CA-GDO-019 | RF-GDO-022 | — |
| CA-GDO-020 | RF-GDO-023 | — |
| CA-GDO-021 | RF-GDO-024 | — |
| CA-GDO-022 | RF-GDO-025 | ESP-GDO-008 |
| CA-GDO-023 | RF-GDO-026 | ESP-GDO-008 |
| CA-GDO-024 | RF-GDO-027 | — |
| CA-GDO-025 | RF-GDO-029 | ESP-GDO-009 |
| CA-GDO-026 | RF-GDO-030 | ESP-GDO-009 |
| CA-GDO-027 | RF-GDO-031 | ESP-GDO-010 |
| CA-GDO-028 | RF-GDO-032 | ESP-GDO-010 |
| CA-GDO-029 | RF-GDO-039 | — |
| CA-GDO-030 | RF-GDO-040 | — |
| CA-GDO-031 | RF-GDO-047 | — |
| CA-GDO-032 | RF-GDO-048 | — |

---

# 19. Refinamento Futuro

Os critérios deste documento representam a primeira decomposição das necessidades do domínio.

Durante o refinamento, um critério poderá:

* ser dividido em vários critérios;
* ser combinado com outro;
* ser descartado;
* ser transformado em requisito transversal;
* depender de serviço corporativo;
* gerar múltiplos casos de teste.

Nenhum critério deverá ser considerado tecnicamente implementado apenas pela sua existência neste documento.

---

# 20. Registro no Mapa Mestre

Este artefato deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

**Identificador do artefato:**

`CA-MAP-GDO-001`

**Tipo:**

Mapa de Critérios de Aceitação.

**Domínio:**

Gestão Documental.

**Versão:**

2.0.

---

# 21. Próximo Artefato

O próximo artefato recomendado é:

`012-Matriz-de-Rastreabilidade-Gestao-Documental.md`

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

# 22. Controle de Versões

| Versão | Data       | Descrição |
| ------ | ---------- | --------- |
| 1.0    | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0    | 2026-09-02 | Conteúdo detalhado: 32 critérios de aceitação, rastreabilidade completa |

---

**Documento:** 011-Criterios-de-Aceitacao-Gestao-Documental.md

**Última atualização:** 2026-09-02

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
