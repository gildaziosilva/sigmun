# 002 – Mapa de Capacidades – Gestão Documental

#### Mapa de Capacidades – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-002

**Domínio:** Gestão Documental

**Versão:** 1.0

**Status:** Em elaboração

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Documental.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

---

# 1. Finalidade

O **Mapa de Capacidades – Gestão Documental** (`DOM-GDO`) tem como finalidade mapear e descrever as capacidades funcionais que o domínio deve prover para a Administração Pública Municipal, organizando-as em níveis hierárquicos que orientem a implementação incremental, o alinhamento com os atores (`001-Mapa-de-Atores-Gestao-Documental.md`) e o rastreamento com processos, serviços e casos de uso.

Este artefato atua como ponte entre a visão estratégica do domínio (`000-Dominio-Gestao-Documental.md`) e a arquitetura corporativa (`012-Arquitetura-de-Gestao-Documental-e-Arquivistica.md`), detalhando **o que** o sistema deve ser capaz de realizar.

---

# 2. Princípios

O mapa de capacidades observa os seguintes princípios:

* **Completude** — cobre todo o ciclo de vida documental (criação → destinação);
* **Granularidade progressiva** — capacidades decompostas em três níveis (foco, processo, atividade);
* **Rastreabilidade** — cada capacidade de nível inferior rastreia para um ou mais atores, processos e serviços;
* **Reutilização** — capacidades transversais (pesquisa, assinatura, auditoria) são compartilhadas entre processos;
* **Conformidade arquivística** — alinhado aos princípios de autenticidade, integridade, disponibilidade, rastreabilidade e classificação (arquitetura corporativa §3);
* **Incrementalismo** — capacidades priorizáveis por onda de entrega (ROADMAP §11).

---

# 3. Conceito de Capacidade

Para este domínio, considera-se **capacidade** qualquer habilidade funcional que:

* o sistema deve prover a um ator;
* apoie uma fase do ciclo de vida documental;
* implemente uma regra de negócio arquivística;
* atenda a um requisito legal ou normativo;
* gere valor mensurável para a gestão documental;
* integre-se com outros domínios do SIGMUN.

---

# 4. Classificação das Capacidades

As capacidades organizam-se em três níveis:

| Nível | Denominação | Descrição | Exemplo |
| --- | --- | --- | --- |
| 1 | **Foco** | Área estratégica de alto nível | Gestão de Documentos |
| 2 | **Processo** | Conjunto de atividades correlacionadas | Captura e Registro |
| 3 | **Atividade** | Ação individual e atribuível | Digitalizar documento |

---

# 5. Capacidades de Gestão Documental (Nível 1 — Foco)

## 5.1 GDO-F01 — Gestão de Documentos

Capacidade de prover ciclo de vida completo aos documentos municipais.

**Processos associados (Nível 2):**

| Código | Capacidade | Descrição |
| --- | --- | --- |
| GDO-F01-P01 | Captura e Registro | Ingestão de documentos (digitalização, upload, importação, geração nativa) com atribuição de metadados obrigatórios |
| GDO-F01-P02 | Classificação Arquivística | Atribuição de código de classificação conforme plano de classificação hierárquico |
| GDO-F01-P03 | Versionamento | Controle imutável de versões com histórico de alterações e justificativas |
| GDO-F01-P04 | Tramitação | Encaminhamento de documentos entre unidades com fluxo configurável |
| GDO-F01-P05 | Arquivamento | Movimentação para arquivo intermediário com indexação e localização |
| GDO-F01-P06 | Destinação | Aplicação da tabela de temporalidade (eliminação ou guarda permanente) |

## 5.2 GDO-F02 — Gestão de Processos Documentais

Capacidade de estruturar e gerenciar processos administrativos compostos por documentos.

**Processos associados (Nível 2):**

| Código | Capacidade | Descrição |
| --- | --- | --- |
| GDO-F02-P01 | Abertura de Processo | Criação de processo documental com autuação, numeração única e classificação inicial |
| GDO-F02-P02 | Inclusão de Documentos | Anexação de documentos a processo existente com validação de tipos permitidos |
| GDO-F02-P03 | Tramitação de Processo | Movimentação do processo entre setores com prazos e alertas |
| GDO-F02-P04 | Despacho | Registro de manifestações (despachos, pareceres, notas) vinculadas ao processo |
| GDO-F02-P05 | Encerramento | Arquivamento ou baixa de processo com verificação de pendências |
| GDO-F02-P06 | Reabertura | Reabertura de processo arquivado com justificativa e autorização |

## 5.3 GDO-F03 — Pesquisa e Consulta

Capacidade de localizar e recuperar documentos e processos.

**Processos associados (Nível 2):**

| Código | Capacidade | Descrição |
| --- | --- | --- |
| GDO-F03-P01 | Pesquisa Textual | Busca por conteúdo (OCR) e metadados com operadores booleanos |
| GDO-F03-P02 | Pesquisa por Metadados | Filtros estruturados (tipo, autor, período, classificação, unidade) |
| GDO-F03-P03 | Consulta Pública | Disponibilização de documentos de acesso livre via Portal da Transparência |
| GDO-F03-P04 | Empréstimo Documental | Controle de retirada/devolução de documentos físicos (quando aplicável) |
| GDO-F03-P05 | Exportação | Geração de relatórios e exportação em formatos padrão (PDF/A, CSV) |

## 5.4 GDO-F04 — Assinatura e Autenticação

Capacidade de garantir autoria, integridade e validade jurídica.

**Processos associados (Nível 2):**

| Código | Capacidade | Descrição |
| --- | --- | --- |
| GDO-F04-P01 | Assinatura Eletrônica | Assinatura com credencial login/senha do DOM-IDN |
| GDO-F04-P02 | Assinatura Digital | Assinatura com certificado digital (ICP-Brasil) |
| GDO-F04-P03 | Validação de Assinatura | Verificação de validade, integridade e cadeia certificadora |
| GDO-F04-P04 | Autenticação de Cópias | Certificação de cópias autênticas (eliminação de necessidade de cópias físicas) |

## 5.5 GDO-F05 — Preservação Digital

Capacidade de garantir acessibilidade e integridade a longo prazo.

**Processos associados (Nível 2):**

| Código | Capacidade | Descrição |
| --- | --- | --- |
| GDO-F05-P01 | Armazenamento Seguro | Repositório com criptografia, redundância e backup |
| GDO-F05-P02 | Migração de Formato | Conversão para formatos preserváveis (PDF/A) |
| GDO-F05-P03 | Verificação de Integridade | Checagem periódica de hashes (SHA-256) |
| GDO-F05-P04 | Plano de Backup | Política de retenção e recuperação de desastres |

---

# 6. Capacidades de Suporte (Nível 1 — Foco)

## 6.1 GDO-F06 — Classificação e Temporalidade

Capacidade de administrar planos de classificação e tabelas de temporalidade.

**Processos associados (Nível 2):**

| Código | Capacidade | Descrição |
| --- | --- | --- |
| GDO-F06-P01 | Plano de Classificação | Configuração hierárquica de classes/subclasses com códigos |
| GDO-F06-P02 | Tabela de Temporalidade | Definição de prazos corrente/intermediário e destinação final |
| GDO-F06-P03 | Indicadores de Destinação | Alertas de documentos em fase de avaliação para eliminação ou guarda |

## 6.2 GDO-F07 — Indexação e Metadados

Capacidade de estruturar informações descritivas dos documentos.

**Processos associados (Nível 2):**

| Código | Capacidade | Descrição |
| --- | --- | --- |
| GDO-F07-P01 | Metadados Obrigatórios | Definição de campos mínimos (identificador, tipo, autor, data, unidade, classificação) |
| GDO-F07-P02 | Indexação Automática | Extração de metadados via OCR e reconhecimento de padrões |
| GDO-F07-P03 | Vocabulário Controlado | Administração de termos autorizados para indexação |

## 6.3 GDO-F08 — Digitalização e OCR

Capacidade de converter documentos físicos em digitais.

**Processos associados (Nível 2):**

| Código | Capacidade | Descrição |
| --- | --- | --- |
| GDO-F08-P01 | Captura em Lote | Digitalização de múltiplos documentos com separação automática |
| GDO-F08-P02 | Reconhecimento OCR | Extração de texto para pesquisa e indexação |
| GDO-F08-P03 | Validação de Qualidade | Verificação de resolução, legibilidade e completude |

---

# 7. Capacidades de Governança (Nível 1 — Foco)

## 7.1 GDO-F09 — Auditoria e Rastreabilidade

Capacidade de registrar e consultar o histórico de ações sobre documentos.

**Processos associados (Nível 2):**

| Código | Capacidade | Descrição |
| --- | --- | --- |
| GDO-F09-P01 | Log de Ações | Registro imutável de criação, consulta, alteração, download, impressão |
| GDO-F09-P02 | Trilha de Auditoria | Vinculação ao módulo `core.trilha_auditoria` (DOM-IDN) |
| GDO-F09-P03 | Relatórios de Auditoria | Geração de relatórios de acesso e movimentação |

## 7.2 GDO-F10 — Segurança e Acesso

Capacidade de controlar permissões conforme legislação e política interna.

**Processos associados (Nível 2):**

| Código | Capacidade | Descrição |
| --- | --- | --- |
| GDO-F10-P01 | Controle de Acesso | Perfis e permissões por documento, processo e classificação (integração DOM-IDN) |
| GDO-F10-P02 | Classificação de Sigilo | Níveis de acesso (público, restrito, sigiloso, ultrasigiloso) |
| GDO-F10-P03 | LGPD | Tratamento de dados pessoais em documentos (anonização, consentimento) |

## 7.3 GDO-F11 — Indicadores e Relatórios

Capacidade de gerar informações gerenciais para a gestão documental.

**Processos associados (Nível 2):**

| Código | Capacidade | Descrição |
| --- | --- | --- |
| GDO-F11-P01 | Indicadores Operacionais | Volume por tipo, tempo médio de tramitação, backlog de digitalização |
| GDO-F11-P02 | Indicadores de Conformidade | Documentos classificados, prazos de temporalidade cumpridos |
| GDO-F11-P03 | Painéis Gerenciais | Dashboards com filtros por unidade, período e tipo documental |

---

# 8. Relacionamento com Atores

| Capacidade (Nível 1) | Ator Principal | Ator Secundário |
| --- | --- | --- |
| GDO-F01 Gestão de Documentos | Servidor/Gestor Documental | Autoridade Homologadora |
| GDO-F02 Gestão de Processos | Servidor/Gestor Documental | Público (consulta) |
| GDO-F03 Pesquisa e Consulta | Público (consulta) | Servidor/Gestor Documental |
| GDO-F04 Assinatura | Servidor/Gestor Documental | Autoridade Homologadora |
| GDO-F05 Preservação | Administrador GDO | — |
| GDO-F06 Classificação/Temporalidade | Administrador GDO | Autoridade Homologadora |
| GDO-F07 Indexação/Metadados | Servidor/Gestor Documental | Administrador GDO |
| GDO-F08 Digitalização/OCR | Servidor/Gestor Documental | — |
| GDO-F09 Auditoria | Administrador GDO | Autoridade Homologadora |
| GDO-F10 Segurança/Acesso | Administrador GDO | — |
| GDO-F11 Indicadores | Gestor Administrativo | Administrador GDO |

---

# 9. Relacionamento com Outros Domínios

| Capacidade | Domínio Relacionado | Natureza |
| --- | --- | --- |
| GDO-F04 Assinatura | DOM-IDN (Identidade) | Consome serviço de autenticação |
| GDO-F09 Auditoria | DOM-IDN (Identidade) | Consome `core.trilha_auditoria` |
| GDO-F10 Segurança | DOM-IDN (Identidade) | Consome perfis/permissões |
| GDO-F01 Gestão de Documentos | DOM-MET (Metadados) | Compartilha modelo de metadados |
| GDO-F02 Processos | DOM-COMPRAS | Vincula `processo_documental` |
| GDO-F03 Consulta Pública | DOM-CUM (Cadastro) | Valida acesso por pessoa |
| GDO-F10 LGPD | DOM-DAD (Dados) | Alinha políticas de tratamento |

---

# 10. Relacionamento com o Ciclo de Vida Documental

| Fase do Ciclo | Capacidades Ativas |
| --- | --- |
| **Criação** | GDO-F01-P01 (Captura), GDO-F07 (Indexação), GDO-F08 (Digitalização) |
| **Uso Corrente** | GDO-F01-P02 (Classificação), GDO-F01-P03 (Versionamento), GDO-F01-P04 (Tramitação), GDO-F02 (Processos), GDO-F03 (Pesquisa), GDO-F04 (Assinatura) |
| **Arquivo Intermediário** | GDO-F01-P05 (Arquivamento), GDO-F05 (Preservação), GDO-F06 (Temporalidade) |
| **Destinação** | GDO-F01-P06 (Destinação), GDO-F06-P03 (Indicadores), GDO-F09 (Auditoria) |

---

# 11. Indicadores de Capacidade

| Indicador | Capacidade | Meta |
| --- | --- |
| % documentos digitalizados | GDO-F08 | ≥ 90% após 12 meses |
| Tempo médio de tramitação | GDO-F01-P04 | ≤ 5 dias úteis |
| % documentos classificados | GDO-F01-P02 | 100% dos documentos capturados |
| Disponibilidade do repositório | GDO-F05-P01 | ≥ 99,5% |
| % documentos com assinatura válida | GDO-F04 | 100% dos documentos oficiais |
| Conformidade com temporalidade | GDO-F06 | 100% dos prazos cumpridos |

---

# 12. Identificador do Artefato

| Atributo | Valor |
| --- | --- |
| **Identificador** | `ACT-CAP-GDO-001` |
| **Código do artefato** | `DOM-GDO-002` |
| **Versão** | 2.0 |
| **Data** | 2026-09-01 |
| **Responsável** | Equipe SIGMUN |
| **Status** | Vigente |

---

# 13. Controle de Versões

| Versão | Data | Descrição | Autor |
| --- | --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato | Equipe SIGMUN |
| 2.0 | 2026-09-01 | Conteúdo detalhado: 11 capacidades de nível 1, 42 de nível 2, relacionamentos com atores, domínios e ciclo de vida | Equipe SIGMUN |

---

**Documento:** 002-Mapa-de-Capacidades-Gestao-Documental.md

**Última atualização:** 2026-09-01

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
