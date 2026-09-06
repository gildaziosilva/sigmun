# 008 – Requisitos Funcionais – Gestão Documental

#### Requisitos Funcionais – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-008

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
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

---

# 1. Finalidade

Este documento define os **Requisitos Funcionais do Domínio de Gestão Documental** do SIGMUN.

Os requisitos funcionais descrevem comportamentos, funcionalidades, operações e respostas que o sistema deverá oferecer para atender às necessidades identificadas nas:

* capacidades;
* processos;
* serviços;
* casos de uso;
* histórias de usuário;
* regras de negócio.

Os requisitos deste documento deverão servir como base para:

* especificações;
* desenvolvimento;
* testes;
* critérios de aceitação;
* integrações;
* estimativas;
* planejamento de releases;
* rastreabilidade.

---

# 2. Convenção de Identificação

Os requisitos funcionais utilizarão o padrão:

```text
RF-GDO-XXX
```

Exemplo:

```text
RF-GDO-001
```

O identificador deverá permanecer estável durante o ciclo de vida do requisito.

---

# 3. Estrutura do Requisito

Cada requisito deverá possuir:

* identificador;
* título;
* descrição;
* origem;
* regra de negócio relacionada;
* prioridade;
* dependências;
* observações, quando aplicável.

Modelo:

```text
RF-GDO-XXX – Título

O sistema deverá ...

Origem:
HU-GDO-XXX

Regras:
RN-GDO-XXX

Prioridade:
P1
```

---

# 4. Classificação de Prioridade

| Prioridade | Significado            |
| ---------- | ---------------------- |
| P0         | Essencial / bloqueante |
| P1         | Alta                   |
| P2         | Média                  |
| P3         | Baixa                  |

A prioridade poderá ser revista durante o planejamento do produto.

---

# 5. Requisitos Funcionais — Captura e Registro

## RF-GDO-001 — Criar Documento Digital

O sistema deverá permitir criar um documento digital diretamente no sistema com atribuição de metadados obrigatórios (título, tipo documental, data, unidade, classificação).

**Origem:**
* HU-GDO-001

**Regras relacionadas:**
* RN-GDO-001
* RN-GDO-002
* RN-GDO-003

**Prioridade:** P0

---

## RF-GDO-002 — Digitalizar Documento Físico

O sistema deverá permitir digitalizar documentos físicos por meio de scanner integrado, convertendo para formato digital com qualidade.

**Origem:**
* HU-GDO-002

**Regras relacionadas:**
* RN-GDO-002

**Prioridade:** P1

---

## RF-GDO-003 — Importar Documento Externo

O sistema deverá permitir importar documentos de sistemas externos (protocolo eletrônico, sistemas legados) com seus metadados originais.

**Origem:**
* HU-GDO-003

**Regras relacionadas:**
* RN-GDO-001
* RN-GDO-003

**Prioridade:** P1

---

## RF-GDO-004 — Gerar Código Único de Documento

O sistema deverá gerar automaticamente código único e irrepetível para cada documento, composto por: tipo documental + ano + número sequencial + unidade.

**Origem:**
* HU-GDO-001

**Regras relacionadas:**
* RN-GDO-001

**Prioridade:** P0

---

## RF-GDO-005 — Calcular Hash SHA-256

O sistema deverá calcular e registrar automaticamente o hash SHA-256 de todo documento no momento da captura.

**Origem:**
* HU-GDO-001

**Regras relacionadas:**
* RN-GDO-002

**Prioridade:** P0

---

# 6. Requisitos Funcionais — Classificação Arquivística

## RF-GDO-006 — Classificar Documento

O sistema deverá permitir classificar um documento conforme o plano de classificação hierárquico vigente (classe, subclasse, série).

**Origem:**
* HU-GDO-004

**Regras relacionadas:**
* RN-GDO-004
* RN-GDO-005

**Prioridade:** P0

---

## RF-GDO-007 — Reclassificar Documento

O sistema deverá permitir reclassificar um documento quando identificar erro na classificação original, mantendo registro de auditoria da alteração.

**Origem:**
* HU-GDO-005

**Regras relacionadas:**
* RN-GDO-004

**Prioridade:** P2

---

## RF-GDO-008 — Vincular Temporalidade Automaticamente

O sistema deverá vincular automaticamente a temporalidade (prazo de retenção e destinação) conforme a classificação atribuída e a tabela de temporalidade vigente.

**Origem:**
* HU-GDO-004

**Regras relacionadas:**
* RN-GDO-004

**Prioridade:** P0

---

# 7. Requisitos Funcionais — Tramitação

## RF-GDO-009 — Tramitar Documento entre Unidades

O sistema deverá permitir tramitar um documento de uma unidade para outra unidade administrativa, registrando origem, destino, data/hora, usuário e observação.

**Origem:**
* HU-GDO-006

**Regras relacionadas:**
* RN-GDO-006

**Prioridade:** P0

---

## RF-GDO-010 — Despachar Documento com Instruções

O sistema deverá permitir anexar um despacho com instruções e observações ao tramitar um documento.

**Origem:**
* HU-GDO-007

**Regras relacionadas:**
* RN-GDO-006

**Prioridade:** P1

---

## RF-GDO-011 — Receber Documento Tramitado

O sistema deverá permitir receber e confirmar o recebimento de documentos tramitados, registrando ciência formal.

**Origem:**
* HU-GDO-008

**Regras relacionadas:**
* RN-GDO-007

**Prioridade:** P0

---

## RF-GDO-012 — Devolver Documento à Unidade de Origem

O sistema deverá permitir devolver um documento à unidade de origem com justificativa.

**Origem:**
* HU-GDO-009

**Regras relacionadas:**
* RN-GDO-006

**Prioridade:** P1

---

# 8. Requisitos Funcionais — Arquivamento

## RF-GDO-013 — Arquivar Documento Corrente

O sistema deverá permitir arquivar um documento na fase corrente após conclusão de sua tramitação.

**Origem:**
* HU-GDO-010

**Regras relacionadas:**
* RN-GDO-008

**Prioridade:** P1

---

## RF-GDO-014 — Desarquivar Documento

O sistema deverá permitir desarquivar um documento quando houver necessidade de nova movimentação, registrando motivo, data/hora e usuário.

**Origem:**
* HU-GDO-011

**Regras relacionadas:**
* RN-GDO-009

**Prioridade:** P2

---

# 9. Requisitos Funcionais — Destinação

## RF-GDO-015 — Avaliar Documento para Destinação

O sistema deverá permitir avaliar documentos quanto ao prazo de retenção e propor eliminação ou guarda permanente.

**Origem:**
* HU-GDO-012

**Regras relacionadas:**
* RN-GDO-010

**Prioridade:** P1

---

## RF-GDO-016 — Aprovar Eliminação de Documento

O sistema deverá permitir que a autoridade homologadora aprove a eliminação de documentos avaliados e dentro do prazo de retenção.

**Origem:**
* HU-GDO-013

**Regras relacionadas:**
* RN-GDO-010
* RN-GDO-011

**Prioridade:** P0

---

## RF-GDO-017 — Destinar Documento à Guarda Permanente

O sistema deverá permitir que a autoridade homologadora aprove a transferência de documentos para guarda permanente.

**Origem:**
* HU-GDO-014

**Regras relacionadas:**
* RN-GDO-012

**Prioridade:** P1

---

## RF-GDO-018 — Prorrogar Prazo de Retenção

O sistema deverá permitir solicitar a prorrogação do prazo de retenção de um documento com justificativa formal.

**Origem:**
* HU-GDO-015

**Regras relacionadas:**
* RN-GDO-013

**Prioridade:** P2

---

# 10. Requisitos Funcionais — Processos Documentais

## RF-GDO-019 — Abrir Processo Documental

O sistema deverá permitir abrir um novo processo documental com identificação, assunto e unidade interessada.

**Origem:**
* HU-GDO-016

**Regras relacionadas:**
* RN-GDO-014

**Prioridade:** P0

---

## RF-GDO-020 — Incluir Documento em Processo

O sistema deverá permitir incluir um documento em um processo existente.

**Origem:**
* HU-GDO-017

**Regras relacionadas:**
* RN-GDO-014

**Prioridade:** P0

---

## RF-GDO-021 — Encerrar Processo

O sistema deverá permitir encerrar um processo quando todas as providências forem concluídas e todos os documentos estiverem com tramitação concluída.

**Origem:**
* HU-GDO-018

**Regras relacionadas:**
* RN-GDO-015

**Prioridade:** P1

---

## RF-GDO-022 — Reabrir Processo Encerrado

O sistema deverá permitir reabrir um processo anteriormente encerrado com justificativa formal, mediante perfil de administrador GDO.

**Origem:**
* HU-GDO-019

**Regras relacionadas:**
* RN-GDO-016

**Prioridade:** P2

---

# 11. Requisitos Funcionais — Pesquisa e Consulta

## RF-GDO-023 — Pesquisar Documentos com Filtros

O sistema deverá permitir pesquisar documentos utilizando filtros por unidade, período, tipo documental, classificação e palavras-chave.

**Origem:**
* HU-GDO-020

**Regras relacionadas:**
* RN-GDO-003

**Prioridade:** P0

---

## RF-GDO-024 — Consultar Documento Público

O sistema deverá permitir consultar documentos de acesso público disponíveis no portal de transparência.

**Origem:**
* HU-GDO-021

**Regras relacionadas:**
* RN-GDO-019

**Prioridade:** P1

---

# 12. Requisitos Funcionais — Assinatura Digital

## RF-GDO-025 — Assinar Documento Digitalmente

O sistema deverá permitir assinar um documento digitalmente com certificado digital ICP-Brasil válido.

**Origem:**
* HU-GDO-022

**Regras relacionadas:**
* RN-GDO-017
* RN-GDO-018

**Prioridade:** P0

---

## RF-GDO-026 — Validar Assinatura Digital

O sistema deverá permitir validar a assinatura digital de um documento, verificando autenticidade e integridade.

**Origem:**
* HU-GDO-023

**Regras relacionadas:**
* RN-GDO-017

**Prioridade:** P1

---

# 13. Requisitos Funcionais — Auditoria

## RF-GDO-027 — Consultar Histórico de Auditoria

O sistema deverá permitir consultar o histórico completo de auditoria de um documento (criação, alterações, tramitações, acessos).

**Origem:**
* HU-GDO-024

**Regras relacionadas:**
* RN-GDO-027
* RN-GDO-028

**Prioridade:** P0

---

## RF-GDO-028 — Registrar Log Automaticamente

O sistema deverá registrar automaticamente todas as ações realizadas sobre um documento (criação, edição, tramitação, arquivamento, eliminação) com usuário, data/hora, ação e IP de origem.

**Origem:**
* HU-GDO-024

**Regras relacionadas:**
* RN-GDO-027

**Prioridade:** P0

---

# 14. Requisitos Funcionais — Segurança e Acesso

## RF-GDO-029 — Configurar Permissões de Acesso ao Documento

O sistema deverá permitir configurar permissões de acesso por documento (público, restrito, sigiloso).

**Origem:**
* HU-GDO-025

**Regras relacionadas:**
* RN-GDO-019

**Prioridade:** P0

---

## RF-GDO-030 — Classificar Sigilo do Documento

O sistema deverá permitir classificar o nível de sigilo de um documento (público, reservado, secreto).

**Origem:**
* HU-GDO-026

**Regras relacionadas:**
* RN-GDO-019

**Prioridade:** P0

---

# 15. Requisitos Funcionais — Versionamento

## RF-GDO-031 — Criar Nova Versão de Documento

O sistema deverá permitir criar uma nova versão de um documento existente, preservando todas as versões anteriores.

**Origem:**
* HU-GDO-027

**Regras relacionadas:**
* RN-GDO-005
* RN-GDO-025

**Prioridade:** P1

---

## RF-GDO-032 — Restaurar Versão Anterior

O sistema deverá permitir restaurar uma versão anterior de um documento, gerando uma nova versão com o conteúdo restaurado.

**Origem:**
* HU-GDO-028

**Regras relacionadas:**
* RN-GDO-005
* RN-GDO-026

**Prioridade:** P2

---

# 16. Requisitos Funcionais — Digitalização e OCR

## RF-GDO-033 — Aplicar OCR em Documento Digitalizado

O sistema deverá aplicar reconhecimento óptico de caracteres (OCR) em documentos digitalizados para tornar o conteúdo pesquisável.

**Origem:**
* HU-GDO-029

**Regras relacionadas:**
* RN-GDO-002

**Prioridade:** P2

---

## RF-GDO-034 — Corrigir Texto OCR

O sistema deverá permitir corrigir manualmente o texto extraído pelo OCR.

**Origem:**
* HU-GDO-030

**Regras relacionadas:**
* RN-GDO-002

**Prioridade:** P3

---

# 17. Requisitos Funcionais — Indexação e Metadados

## RF-GDO-035 — Atribuir Metadados ao Documento

O sistema deverá permitir atribuir metadados estruturados a um documento (autor, destinatário, assunto, palavras-chave).

**Origem:**
* HU-GDO-031

**Regras relacionadas:**
* RN-GDO-003

**Prioridade:** P0

---

## RF-GDO-036 — Configurar Taxonomia de Indexação

O sistema deverá permitir configurar a taxonomia e os vocários controlados para indexação de documentos (perfil administrador GDO).

**Origem:**
* HU-GDO-032

**Regras relacionadas:**
* RN-GDO-003

**Prioridade:** P2

---

# 18. Requisitos Funcionais — Preservação

## RF-GDO-037 — Configurar Plano de Preservação Digital

O sistema deverá permitir configurar políticas de preservação digital (formatos aceitos, migração, checksum).

**Origem:**
* HU-GDO-033

**Regras relacionadas:**
* RN-GDO-023

**Prioridade:** P2

---

## RF-GDO-038 — Verificar Integridade de Documentos

O sistema deverá verificar periodicamente a integridade dos documentos armazenados por meio de comparação de hash SHA-256.

**Origem:**
* HU-GDO-034

**Regras relacionadas:**
* RN-GDO-002
* RN-GDO-024

**Prioridade:** P1

---

# 19. Requisitos Funcionais — Temporalidade

## RF-GDO-039 — Configurar Tabela de Temporalidade

O sistema deverá permitir configurar a tabela de temporalidade documental com prazos de retenção e destinação por tipo documental.

**Origem:**
* HU-GDO-035

**Regras relacionadas:**
* RN-GDO-004
* RN-GDO-022

**Prioridade:** P1

---

## RF-GDO-040 — Gerar Alerta de Temporalidade

O sistema deverá gerar alerta automático quando documentos atingirem 80% do prazo de retenção.

**Origem:**
* HU-GDO-036

**Regras relacionadas:**
* RN-GDO-021

**Prioridade:** P1

---

# 20. Requisitos Funcionais — Indicadores e Relatórios

## RF-GDO-041 — Gerar Relatório de Acervo Documental

O sistema deverá permitir gerar relatórios sobre o acervo documental (quantidade por tipo, unidade, período).

**Origem:**
* HU-GDO-037

**Regras relacionadas:**
* RN-GDO-003

**Prioridade:** P2

---

## RF-GDO-042 — Acompanhar Indicadores de Desempenho

O sistema deverá permitir acompanhar indicadores de desempenho da gestão documental (tempo médio de tramitação, % digitalizados, documentos classificados).

**Origem:**
* HU-GDO-038

**Regras relacionadas:**
* RN-GDO-004

**Prioridade:** P2

---

# 21. Requisitos Funcionais — Integração

## RF-GDO-043 — Integrar Documento com Processo de Compras

O sistema deverá permitir vincular documentos a processos de compras e contratações.

**Origem:**
* HU-GDO-039

**Regras relacionadas:**
* RN-GDO-014

**Prioridade:** P2

---

## RF-GDO-044 — Publicar Documento no Portal da Transparência

O sistema deverá permitir publicar documentos diretamente no portal de transparência.

**Origem:**
* HU-GDO-040

**Regras relacionadas:**
* RN-GDO-019

**Prioridade:** P2

---

# 22. Requisitos Funcionais — Consulta Pública

## RF-GDO-045 — Pesquisar Documentos Públicos

O sistema deverá permitir pesquisar documentos públicos por assunto, período ou unidade (acesso cidadão).

**Origem:**
* HU-GDO-041

**Regras relacionadas:**
* RN-GDO-019

**Prioridade:** P1

---

## RF-GDO-046 — Solicitar Via de Documento

O sistema deverá permitir solicitar uma via digital de documento público.

**Origem:**
* HU-GDO-042

**Regras relacionadas:**
* RN-GDO-019

**Prioridade:** P2

---

# 23. Requisitos Funcionais — Administração do Sistema

## RF-GDO-047 — Configurar Plano de Classificação

O sistema deverá permitir configurar o plano de classificação hierárquico (classes, subclasses, séries) — perfil administrador GDO.

**Origem:**
* HU-GDO-043

**Regras relacionadas:**
* RN-GDO-004

**Prioridade:** P1

---

## RF-GDO-048 — Gerenciar Perfis de Acesso ao GDO

O sistema deverá permitir gerenciar perfis de acesso ao módulo de gestão documental (leitura, escrita, administração).

**Origem:**
* HU-GDO-044

**Regras relacionadas:**
* RN-GDO-020

**Prioridade:** P0

---

# 24. Relação com Histórias de Usuário

| Requisito | História de Usuário | Regra de Negócio |
| --- | --- | --- |
| RF-GDO-001 | HU-GDO-001 | RN-GDO-001, RN-GDO-002, RN-GDO-003 |
| RF-GDO-002 | HU-GDO-002 | RN-GDO-002 |
| RF-GDO-003 | HU-GDO-003 | RN-GDO-001, RN-GDO-003 |
| RF-GDO-004 | HU-GDO-001 | RN-GDO-001 |
| RF-GDO-005 | HU-GDO-001 | RN-GDO-002 |
| RF-GDO-006 | HU-GDO-004 | RN-GDO-004, RN-GDO-005 |
| RF-GDO-007 | HU-GDO-005 | RN-GDO-004 |
| RF-GDO-008 | HU-GDO-004 | RN-GDO-004 |
| RF-GDO-009 | HU-GDO-006 | RN-GDO-006 |
| RF-GDO-010 | HU-GDO-007 | RN-GDO-006 |
| RF-GDO-011 | HU-GDO-008 | RN-GDO-007 |
| RF-GDO-012 | HU-GDO-009 | RN-GDO-006 |
| RF-GDO-013 | HU-GDO-010 | RN-GDO-008 |
| RF-GDO-014 | HU-GDO-011 | RN-GDO-009 |
| RF-GDO-015 | HU-GDO-012 | RN-GDO-010 |
| RF-GDO-016 | HU-GDO-013 | RN-GDO-010, RN-GDO-011 |
| RF-GDO-017 | HU-GDO-014 | RN-GDO-012 |
| RF-GDO-018 | HU-GDO-015 | RN-GDO-013 |
| RF-GDO-019 | HU-GDO-016 | RN-GDO-014 |
| RF-GDO-020 | HU-GDO-017 | RN-GDO-014 |
| RF-GDO-021 | HU-GDO-018 | RN-GDO-015 |
| RF-GDO-022 | HU-GDO-019 | RN-GDO-016 |
| RF-GDO-023 | HU-GDO-020 | RN-GDO-003 |
| RF-GDO-024 | HU-GDO-021 | RN-GDO-019 |
| RF-GDO-025 | HU-GDO-022 | RN-GDO-017, RN-GDO-018 |
| RF-GDO-026 | HU-GDO-023 | RN-GDO-017 |
| RF-GDO-027 | HU-GDO-024 | RN-GDO-027, RN-GDO-028 |
| RF-GDO-028 | HU-GDO-024 | RN-GDO-027 |
| RF-GDO-029 | HU-GDO-025 | RN-GDO-019 |
| RF-GDO-030 | HU-GDO-026 | RN-GDO-019 |
| RF-GDO-031 | HU-GDO-027 | RN-GDO-005, RN-GDO-025 |
| RF-GDO-032 | HU-GDO-028 | RN-GDO-005, RN-GDO-026 |
| RF-GDO-033 | HU-GDO-029 | RN-GDO-002 |
| RF-GDO-034 | HU-GDO-030 | RN-GDO-002 |
| RF-GDO-035 | HU-GDO-031 | RN-GDO-003 |
| RF-GDO-036 | HU-GDO-032 | RN-GDO-003 |
| RF-GDO-037 | HU-GDO-033 | RN-GDO-023 |
| RF-GDO-038 | HU-GDO-034 | RN-GDO-002, RN-GDO-024 |
| RF-GDO-039 | HU-GDO-035 | RN-GDO-004, RN-GDO-022 |
| RF-GDO-040 | HU-GDO-036 | RN-GDO-021 |
| RF-GDO-041 | HU-GDO-037 | RN-GDO-003 |
| RF-GDO-042 | HU-GDO-038 | RN-GDO-004 |
| RF-GDO-043 | HU-GDO-039 | RN-GDO-014 |
| RF-GDO-044 | HU-GDO-040 | RN-GDO-019 |
| RF-GDO-045 | HU-GDO-041 | RN-GDO-019 |
| RF-GDO-046 | HU-GDO-042 | RN-GDO-019 |
| RF-GDO-047 | HU-GDO-043 | RN-GDO-004 |
| RF-GDO-048 | HU-GDO-044 | RN-GDO-020 |

---

# 25. Refinamento Futuro

Os requisitos deste documento representam a primeira decomposição das necessidades do domínio.

Durante o refinamento, um requisito poderá:

* ser dividido em vários requisitos;
* ser combinado com outro;
* ser descartado;
* ser transformado em requisito transversal;
* depender de serviço corporativo;
* gerar múltiplos critérios de aceitação.

Nenhum requisito deverá ser considerado tecnicamente implementado apenas pela sua existência neste documento.

---

# 26. Registro no Mapa Mestre

Este artefato deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

**Identificador do artefato:**

`RF-MAP-GDO-001`

**Tipo:**

Mapa de Requisitos Funcionais.

**Domínio:**

Gestão Documental.

**Versão:**

2.0.

---

# 27. Próximo Artefato

O próximo artefato recomendado é:

`009-Requisitos-Nao-Funcionais-Gestao-Documental.md`

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

# 28. Controle de Versões

| Versão | Data       | Descrição                                                                |
| ------ | ---------- | ------------------------------------------------------------------------ |
| 1.0    | 2026-08-20 | Criação do esboço inicial padronizado do artefato                        |
| 2.0    | 2026-09-02 | Conteúdo detalhado: 48 requisitos funcionais, rastreabilidade completa   |

---

**Documento:** 008-Requisitos-Funcionais-Gestao-Documental.md

**Última atualização:** 2026-09-02

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
