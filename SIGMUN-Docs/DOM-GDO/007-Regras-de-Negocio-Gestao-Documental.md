# 007 – Regras de Negócio – Gestão Documental

#### Regras de Negócio – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-007

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
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

---

# 1. Finalidade

Este documento estabelece as **Regras de Negócio do Domínio de Gestão Documental** do SIGMUN.

As regras de negócio representam condições, restrições, políticas, validações e comportamentos que devem ser respeitados pelos processos de gestão documental municipal.

As regras aqui definidas deverão orientar:

* requisitos funcionais;
* requisitos não funcionais;
* especificações;
* fluxos de processos;
* casos de uso;
* histórias de usuário;
* critérios de aceitação;
* testes;
* integrações;
* controles;
* auditoria;
* relatórios;
* indicadores.

---

# 2. Princípios das Regras de Negócio

As regras deste domínio deverão observar os princípios de:

* legalidade;
* autenticidade;
* integridade;
* disponibilidade;
* rastreabilidade;
* classificação;
* temporalidade;
* preservação;
* sigilo;
* transparência;
* segregação de funções;
* economicidade;
* segurança;
* proteção de dados;
* interoperabilidade.

---

# 3. Convenção de Identificação

As regras utilizarão o padrão:

```text
RN-GDO-XXX
```

Exemplo:

```text
RN-GDO-001
```

O identificador deverá permanecer estável durante o ciclo de vida da regra.

---

# 4. Classificação das Regras

As regras classificam-se em:

| Tipo | Descrição | Exemplo |
| --- | --- | --- |
| **Restrição** | Condição que impede uma ação | Não eliminar documento sem autorização |
| **Validação** | Critério que deve ser verificado | Unicidade de código documental |
| **Obrigatoriedade** | Requisito que deve ser cumprido | Metadados obrigatórios |
| **Cálculo** | Fórmula ou método de cálculo | Prazo de retenção |
| **Fluxo** | Sequência obrigatória | Temporalidade define destinação |

---

# 5. Regras de Negócio — Captura e Registro

## RN-GDO-001 — Unicidade de Código Documental

**Tipo:** Restrição

**Processo:** GDO-PRO-001 (Captura e Registro)

**Descrição:** Cada documento possuirá código único e irrepetível no sistema, composto por: tipo documental + ano + número sequencial + unidade.

**Justificativa:** Garantir rastreabilidade e evitar duplicidade de documentos no acervo.

**Histórias relacionadas:** HU-GDO-001, HU-GDO-002, HU-GDO-003

---

## RN-GDO-002 — Integridade Obrigatória por Hash (SHA-256)

**Tipo:** Validação

**Processo:** GDO-PRO-001 (Captura e Registro)

**Descrição:** Todo documento armazenado deverá ter seu hash SHA-256 calculado e registrado no momento da captura. O hash será verificado periodicamente para detectar corrupção.

**Justificativa:** Garantir a integridade e autenticidade dos documentos armazenados.

**Histórias relacionadas:** HU-GDO-001, HU-GDO-002, HU-GDO-003, HU-GDO-034

---

## RN-GDO-003 — Metadados Obrigatórios

**Tipo:** Obrigatoriedade

**Processo:** GDO-PRO-001 (Captura e Registro)

**Descrição:** Todo documento deverá possuir os metadados obrigatórios preenchidos antes de ser registrado:

* tipo documental;
* autor;
* data;
* unidade;
* classificação.

**Justificativa:** Garantir a rastreabilidade e organização do acervo documental.

**Histórias relacionadas:** HU-GDO-001, HU-GDO-002, HU-GDO-003, HU-GDO-031

---

# 6. Regras de Negócio — Classificação Arquivística

## RN-GDO-004 — Temporalidade Define Destinação

**Tipo:** Fluxo

**Processo:** GDO-PRO-002 (Classificação)

**Descrição:** A classificação arquivística de um documento determinará automaticamente sua temporalidade (prazo de retenção e destinação final) conforme a tabela de temporalidade vigente.

**Justificativa:** Garantir conformidade com a legislação arquivística e padronizar a destinação documental.

**Histórias relacionadas:** HU-GDO-004, HU-GDO-005, HU-GDO-012, HU-GDO-035

---

## RN-GDO-005 — Versão Imutável

**Tipo:** Restrição

**Processo:** GDO-PRO-001 (Captura e Registro)

**Descrição:** Versões anteriores de um documento não poderão ser alteradas ou excluídas. Cada nova versão preserva o histórico completo de forma imutável.

**Justificativa:** Garantir a integridade e rastreabilidade do histórico documental, permitindo auditoria e recuperação de versões anteriores.

**Histórias relacionadas:** HU-GDO-027, HU-GDO-028, HU-GDO-025

---

# 7. Regras de Negócio — Tramitação

## RN-GDO-006 — Rastreabilidade da Tramitação

**Tipo:** Obrigatoriedade

**Processo:** GDO-PRO-003 (Tramitação)

**Descrição:** Toda tramitação de documento entre unidades deverá registrar: origem, destino, data/hora, usuário e observação. O documento não poderá ser tramitado sem destinatário definido.

**Justificativa:** Garantir a rastreabilidade do fluxo documental.

**Histórias relacionadas:** HU-GDO-006, HU-GDO-007, HU-GDO-008, HU-GDO-009

---

## RN-GDO-007 — Ciência Obrigatória para Recebimento

**Tipo:** Restrição

**Processo:** GDO-PRO-003 (Tramitação)

**Descrição:** O destinatário deverá confirmar ciência do recebimento para que a tramitação seja considerada concluída. Sem ciência, o documento permanece como "pendente de recebimento".

**Justificativa:** Garantir formalidade e comprovação do recebimento documental.

**Histórias relacionadas:** HU-GDO-008

---

# 8. Regras de Negócio — Arquivamento

## RN-GDO-008 — Arquivamento Somente Após Conclusão

**Tipo:** Restrição

**Processo:** GDO-PRO-004 (Arquivamento)

**Descrição:** Um documento somente poderá ser arquivado após a conclusão de sua tramitação. Documentos em tramitação não podem ser arquivados.

**Justificativa:** Preservar a integridade do fluxo documental.

**Histórias relacionadas:** HU-GDO-010, HU-GDO-011

---

## RN-GDO-009 — Registro de Desarquivamento

**Tipo:** Obrigatoriedade

**Processo:** GDO-PRO-004 (Arquivamento)

**Descrição:** Todo desarquivamento deverá registrar: motivo, data/hora, usuário responsável e nova destinação do documento.

**Justificativa:** Manter rastreabilidade do ciclo de vida documental.

**Histórias relacionadas:** HU-GDO-011

---

# 9. Regras de Negócio — Destinação

## RN-GDO-010 — Não Eliminar Documento em Fase Corrente sem Autorização

**Tipo:** Restrição

**Processo:** GDO-PRO-005 (Destinação)

**Descrição:** Documentos em fase corrente ou intermediária não poderão ser eliminados sem autorização formal da autoridade homologadora.

**Justificativa:** Proteger documentos com valor administrativo ou legal vigente.

**Histórias relacionadas:** HU-GDO-012, HU-GDO-013

---

## RN-GDO-011 — Eliminação Requer Autoridade Homologadora

**Tipo:** Restrição

**Processo:** GDO-PRO-005 (Destinação)

**Descrição:** A eliminação de documentos deverá ser aprovada exclusivamente pela autoridade homologadora, após avaliação do prazo de retenção.

**Justificativa:** Garantir segregação de funções e conformidade legal.

**Histórias relacionadas:** HU-GDO-013

---

## RN-GDO-012 — Guarda Permanente Requer Homologação

**Tipo:** Restrição

**Processo:** GDO-PRO-005 (Destinação)

**Descrição:** A transferência de documentos para guarda permanente deverá ser aprovada pela autoridade homologadora, atestando o valor histórico ou probatório.

**Justificativa:** Garantir a preservação de documentos com valor permanente.

**Histórias relacionadas:** HU-GDO-014

---

## RN-GDO-013 — Prorrogação Requer Justificativa

**Tipo:** Obrigatoriedade

**Processo:** GDO-PRO-005 (Destinação)

**Descrição:** A prorrogação do prazo de retenção de um documento deverá ser acompanhada de justificativa formal (vigência legal, processo judicial, interesse administrativo).

**Justificativa:** Documentar a decisão de manter documentos além do prazo regular.

**Histórias relacionadas:** HU-GDO-015

---

# 10. Regras de Negócio — Processos Documentais

## RN-GDO-014 — Processo Deve Ter Documento Inicial

**Tipo:** Obrigatoriedade

**Processo:** GDO-PRO-006 (Gestão de Processos)

**Descrição:** Todo processo documental deverá possuir ao menos um documento inicial (requerimento, petição, ofício) que motive sua abertura.

**Justificativa:** Garantir que todo processo tenha fundamentação documental.

**Histórias relacionadas:** HU-GDO-016, HU-GDO-017

---

## RN-GDO-015 — Encerramento Requer Conclusão de Tramitação

**Tipo:** Restrição

**Processo:** GDO-PRO-006 (Gestão de Processos)

**Descrição:** Um processo somente poderá ser encerrado quando todos os documentos incluídos estiverem com tramitação concluída.

**Justificativa:** Garantir que processos não sejam encerrados prematuramente.

**Histórias relacionadas:** HU-GDO-018

---

## RN-GDO-016 — Reabertura Requer Justificativa

**Tipo:** Obrigatoriedade

**Processo:** GDO-PRO-006 (Gestão de Processos)

**Descrição:** A reabertura de um processo encerrado deverá ser acompanhada de justificativa formal e registrada em auditoria.

**Justificativa:** Manter rastreabilidade das decisões de reabertura.

**Histórias relacionadas:** HU-GDO-019

---

# 11. Regras de Negócio — Assinatura Digital

## RN-GDO-017 — Assinatura Requer Certificado Válido

**Tipo:** Validação

**Processo:** GDO-PRO-008 (Assinatura)

**Descrição:** A assinatura digital de documentos requer certificado digital ICP-Brasil válido. Certificados vencidos ou revogados não serão aceitos.

**Justificativa:** Garantir validade jurídica das assinaturas digitais.

**Histórias relacionadas:** HU-GDO-022

---

## RN-GDO-018 — Documento Assinado Não Pode Ser Alterado

**Tipo:** Restrição

**Processo:** GDO-PRO-008 (Assinatura)

**Descrição:** Após a assinatura digital, o documento não poderá ser alterado. Qualquer modificação exigirá nova versão com nova assinatura.

**Justificativa:** Preservar a integridade e autenticidade do documento assinado.

**Histórias relacionadas:** HU-GDO-022, HU-GDO-027

---

# 12. Regras de Negócio — Segurança e Acesso

## RN-GDO-019 — Classificação de Sigilo Obrigatória

**Tipo:** Obrigatoriedade

**Processo:** GDO-PRO-011 (Segurança/Acesso)

**Descrição:** Todo documento deverá ter sua classificação de sigilo definido: público, reservado ou secreto. Documentos sem classificação serão tratados como restritos.

**Justificativa:** Garantir proteção adequada das informações conforme a Lei de Acesso à Informação.

**Histórias relacionadas:** HU-GDO-025, HU-GDO-026

---

## RN-GDO-020 — Segregação de Funções

**Tipo:** Restrição

**Processo:** GDO-PRO-011 (Segurança/Acesso)

**Descrição:** O usuário que cria um documento não poderá ser o mesmo que autoriza sua eliminação. A autoridade homologadora não poderá criar documentos.

**Justificativa:** Garantir segregação de funções e prevenir fraudes.

**Histórias relacionadas:** HU-GDO-013, HU-GDO-044

---

# 13. Regras de Negócio — Temporalidade

## RN-GDO-021 — Alerta de Vencimento Automático

**Tipo:** Fluxo

**Processo:** GDO-PRO-005 (Destinação)

**Descrição:** O sistema deverá gerar alerta automático quando documentos atingirem 80% do prazo de retenção, notificando o responsável pela avaliação de destinação.

**Justificativa:** Garantir que a avaliação de destinação seja realizada em tempo hábil.

**Histórias relacionadas:** HU-GDO-036

---

## RN-GDO-022 — Prazos Configuráveis por Tipo Documental

**Tipo:** Obrigatoriedade

**Processo:** GDO-PRO-005 (Destinação)

**Descrição:** Os prazos de retenção deverão ser configuráveis por tipo documental, conforme a tabela de temporalidade documental vigente.

**Justificativa:** Permitir adequação às diferentes naturezas documentais.

**Histórias relacionadas:** HU-GDO-035

---

# 14. Regras de Negócio — Preservação

## RN-GDO-023 — Formatos Aceitos para Preservação

**Tipo:** Restrição

**Processo:** GDO-PRO-004 (Arquivamento)

**Descrição:** Documentos para guarda permanente deverão ser armazenados em formatos abertos e padronizados (PDF/A, TIFF, XML). Formatos proprietários não serão aceitos para preservação de longo prazo.

**Justificativa:** Garantir acessibilidade futura aos documentos preservados.

**Histórias relacionadas:** HU-GDO-033

---

## RN-GDO-024 — Verificação Periódica de Integridade

**Tipo:** Obrigatoriedade

**Processo:** GDO-PRO-004 (Arquivamento)

**Descrição:** A integridade dos documentos armazenados deverá ser verificada periodicamente por meio de comparação de hash SHA-256.

**Justificativa:** Detectar e corrigir corrupção de arquivos.

**Histórias relacionadas:** HU-GDO-034

---

# 15. Regras de Negócio — Versionamento

## RN-GDO-025 — Nova Versão Preserva Histórico

**Tipo:** Obrigatoriedade

**Processo:** GDO-PRO-001 (Captura e Registro)

**Descrição:** Ao criar uma nova versão de um documento, todas as versões anteriores deverão ser preservadas e acessíveis para consulta e auditoria.

**Justificativa:** Manter o histórico completo de alterações documentais.

**Histórias relacionadas:** HU-GDO-027, HU-GDO-028

---

## RN-GDO-026 — Restauração Gera Nova Versão

**Tipo:** Fluxo

**Processo:** GDO-PRO-001 (Captura e Registro)

**Descrição:** A restauração de uma versão anterior deverá gerar uma nova versão do documento, preservando o histórico de versões.

**Justificativa:** Manter rastreabilidade das ações de restauração.

**Histórias relacionadas:** HU-GDO-028

---

# 16. Regras de Negócio — Auditoria

## RN-GDO-027 — Registro Automático de Ações

**Tipo:** Obrigatoriedade

**Processo:** GDO-PRO-010 (Auditoria)

**Descrição:** Todas as ações realizadas sobre um documento (criação, edição, tramitação, arquivamento, eliminação) deverão ser registradas automaticamente em log de auditoria com: usuário, data/hora, ação realizada e IP de origem.

**Justificativa:** Garantir rastreabilidade e responsabilização.

**Histórias relacionadas:** HU-GDO-024

---

## RN-GDO-028 — Imutabilidade do Log de Auditoria

**Tipo:** Restrição

**Processo:** GDO-PRO-010 (Auditoria)

**Descrição:** Registros de auditoria não poderão ser alterados ou excluídos, nem mesmo por administradores do sistema.

**Justificativa:** Garantir a integridade e confiabilidade dos registros de auditoria.

**Histórias relacionadas:** HU-GDO-024

---

# 17. Relação com Processos

| Regra | Processo | Tipo |
| --- | --- | --- |
| RN-GDO-001 | GDO-PRO-001 Captura e Registro | Restrição |
| RN-GDO-002 | GDO-PRO-001 Captura e Registro | Validação |
| RN-GDO-003 | GDO-PRO-001 Captura e Registro | Obrigatoriedade |
| RN-GDO-004 | GDO-PRO-002 Classificação | Fluxo |
| RN-GDO-005 | GDO-PRO-001 Captura e Registro | Restrição |
| RN-GDO-006 | GDO-PRO-003 Tramitação | Obrigatoriedade |
| RN-GDO-007 | GDO-PRO-003 Tramitação | Restrição |
| RN-GDO-008 | GDO-PRO-004 Arquivamento | Restrição |
| RN-GDO-009 | GDO-PRO-004 Arquivamento | Obrigatoriedade |
| RN-GDO-010 | GDO-PRO-005 Destinação | Restrição |
| RN-GDO-011 | GDO-PRO-005 Destinação | Restrição |
| RN-GDO-012 | GDO-PRO-005 Destinação | Restrição |
| RN-GDO-013 | GDO-PRO-005 Destinação | Obrigatoriedade |
| RN-GDO-014 | GDO-PRO-006 Processos | Obrigatoriedade |
| RN-GDO-015 | GDO-PRO-006 Processos | Restrição |
| RN-GDO-016 | GDO-PRO-006 Processos | Obrigatoriedade |
| RN-GDO-017 | GDO-PRO-008 Assinatura | Validação |
| RN-GDO-018 | GDO-PRO-008 Assinatura | Restrição |
| RN-GDO-019 | GDO-PRO-011 Segurança | Obrigatoriedade |
| RN-GDO-020 | GDO-PRO-011 Segurança | Restrição |
| RN-GDO-021 | GDO-PRO-005 Destinação | Fluxo |
| RN-GDO-022 | GDO-PRO-005 Destinação | Obrigatoriedade |
| RN-GDO-023 | GDO-PRO-004 Arquivamento | Restrição |
| RN-GDO-024 | GDO-PRO-004 Arquivamento | Obrigatoriedade |
| RN-GDO-025 | GDO-PRO-001 Captura e Registro | Obrigatoriedade |
| RN-GDO-026 | GDO-PRO-001 Captura e Registro | Fluxo |
| RN-GDO-027 | GDO-PRO-010 Auditoria | Obrigatoriedade |
| RN-GDO-028 | GDO-PRO-010 Auditoria | Restrição |

---

# 18. Refinamento Futuro

As regras deste documento representam a primeira decomposição das necessidades do domínio.

Durante o refinamento, uma regra poderá:

* ser dividida em várias regras;
* ser combinada com outra;
* ser descartada;
* ser transformada em requisito transversal;
* depender de serviço corporativo;
* gerar múltiplos requisitos;
* gerar múltiplos critérios de aceitação.

Nenhuma regra deverá ser considerada tecnicamente implementada apenas pela sua existência neste documento.

---

# 19. Registro no Mapa Mestre

Este artefato deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

**Identificador do artefato:**

`RN-MAP-GDO-001`

**Tipo:**

Mapa de Regras de Negócio.

**Domínio:**

Gestão Documental.

**Versão:**

2.0.

---

# 20. Próximo Artefato

O próximo artefato recomendado é:

`008-Requisitos-Funcionais-Gestao-Documental.md`

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

# 21. Controle de Versões

| Versão | Data       | Descrição                                                                |
| ------ | ---------- | ------------------------------------------------------------------------ |
| 1.0    | 2026-08-20 | Criação do esboço inicial padronizado do artefato                        |
| 2.0    | 2026-09-02 | Conteúdo detalhado: 28 regras de negócio, classificação, rastreabilidade  |

---

**Documento:** 007-Regras-de-Negocio-Gestao-Documental.md

**Última atualização:** 2026-09-02

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
