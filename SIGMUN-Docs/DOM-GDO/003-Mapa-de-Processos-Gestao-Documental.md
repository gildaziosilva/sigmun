# 003 – Mapa de Processos – Gestão Documental

#### Mapa de Processos – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-003

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

O **Mapa de Processos – Gestão Documental** (`DOM-GDO`) tem como finalidade mapear e descrever os processos de negócio do domínio, detalhando o fluxo documental desde a captura até a destinação final, com identificação de atividades, atores, regras de negócio, sistemas envolvidos e indicadores de desempenho.

Este artefato integra os atores (`001-Mapa-de-Atores-Gestao-Documental.md`) e capacidades (`002-Mapa-de-Capacidades-Gestao-Documental.md`) em uma visão operacional, orientando a implementação dos serviços, casos de uso e fluxos de trabalho.

---

# 2. Princípios

O mapa de processos observa os seguintes princípios:

* **Ciclo de vida completo** — cobre todas as fases: criação, uso corrente, arquivo intermediário e destinação;
* **Rastreabilidade** — cada atividade gera registro de auditoria;
* **Segregação de funções** — separa quem cria, classifica, tramita, arquiva e destina;
* **Conformidade arquivística** — alinhado à legislação e normas de gestão documental;
* **Integração** — processos conectados aos domínios DOM-IDN, DOM-MET, DOM-COMPRAS, DOM-CUM;
* **Automação progressiva** — prioriza fluxos digitais com redução de papel.

---

# 3. Conceito de Processo

Para este domínio, considera-se **processo** qualquer sequência estruturada de atividades que:

* transforme insumos (documentos físicos, dados, solicitações) em resultados (documentos classificados, tramitados, arquivados);
* envolva um ou mais atores;
* siga regras de negócio definidas;
* gere valor para a gestão documental;
* seja mensurável por indicadores de desempenho.

---

# 4. Classificação dos Processos

Os processos organizam-se em dois níveis:

| Nível | Denominação | Descrição | Exemplo |
| --- | --- | --- | --- |
| 1 | **Macroprocesso** | Conjunto de processos correlacionados | Ciclo de Vida Documental |
| 2 | **Processo** | Sequência de atividades com início, meio e fim | Captura e Registro |

---

# 5. Visão Geral do Fluxo Documental

O fluxo documental segue o ciclo de vida definido na arquitetura corporativa (§11):

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CICLO DE VIDA DOCUMENTAL (DOM-GDO)                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────┐    ┌──────────────┐    ┌────────────┐    ┌───────────────┐   │
│  │ CAPTURA  │───▶│ CLASSIFICAÇÃO│───▶│ TRAMITAÇÃO │───▶│ ARQUIVAMENTO  │   │
│  │ E        │    │ ARQUIVÍSTICA │    │            │    │               │   │
│  │ REGISTRO │    │              │    │            │    │               │   │
│  └──────────┘    └──────────────┘    └────────────┘    └───────┬───────┘   │
│       │              │                    │                    │           │
│       │              │                    │                    ▼           │
│       │              │                    │            ┌───────────────┐   │
│       │              │                    │            │  DESTINAÇÃO   │   │
│       │              │                    │            │               │   │
│       │              │                    │            │ • Eliminação  │   │
│       │              │                    │            │ • Guarda      │   │
│       │              │                    │            │   Permanente  │   │
│       │              │                    │            └───────────────┘   │
│       │              │                    │                                │
│       ▼              ▼                    ▼                                │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │              PESQUISA E CONSULTA (transversal)                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Processos transversais** (atuam em todas as fases):
* Assinatura e Autenticação
* Digitalização e OCR
* Auditoria e Rastreabilidade
* Segurança e Acesso

---

# 6. Processo 1: Captura e Registro

**Código:** `GDO-PRO-001` | **Capacidade:** GDO-F01-P01

## 6.1 Descrição

Ingestão de documentos no sistema SIGMUN, seja por digitalização de documentos físicos, upload de arquivos digitais, importação de sistemas externos ou geração nativa de documentos eletrônicos.

## 6.2 Fluxo do Processo

```text
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Origem do      │     │  Validação de    │     │  Atribuição de  │
│  Documento      │────▶│  Formato e       │────▶│  Metadados      │
│  (físico/digital)│     │  Qualidade       │     │  Obrigatórios   │
└─────────────────┘     └──────────────────┘     └────────┬────────┘
                                                           │
                                                           ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Geração de     │     │  Armazenamento   │     │  Indexação      │
│  Identificador  │◀────│  Seguro          │◀────│  Inicial        │
│  Único          │     │  (repositório)   │     │                 │
└────────┬────────┘     └──────────────────┘     └─────────────────┘
         │
         ▼
┌─────────────────┐
│  Registro de    │
│  Auditoria      │
│  (log imutável) │
└─────────────────┘
```

## 6.3 Atividades

| # | Atividade | Ator Responsável | Sistema/Ferramenta |
| --- | --- | --- | --- |
| 1 | Receber documento (físico ou digital) | Servidor/Gestor Documental | Módulo de Captura |
| 2 | Verificar formato e qualidade | Servidor/Gestor Documental | Validador de Formato |
| 3 | Digitalizar (se físico) | Servidor/Gestor Documental | Scanner/OCR |
| 4 | Atribuir metadados obrigatórios | Servidor/Gestor Documental | Formulário de Registro |
| 5 | Gerar identificador único | Sistema | Gerador de Código |
| 6 | Armazenar no repositório | Sistema | Content Storage |
| 7 | Indexar para pesquisa | Sistema | Indexador |
| 8 | Registrar log de auditoria | Sistema | Módulo de Auditoria |

## 6.4 Regras de Negócio Aplicáveis

* **RN-GDO-001** — Unicidade de código documental
* **RN-GDO-002** — Integridade obrigatória por hash (SHA-256)
* Metadados obrigatórios: tipo documental, autor, data, unidade, classificação

## 6.5 Indicadores

| Indicador | Meta |
| --- | --- |
| Tempo médio de captura | ≤ 5 minutos por documento |
| % documentos com metadados completos | 100% |
| Taxa de rejeição por qualidade | ≤ 5% |

---

# 7. Processo 2: Classificação Arquivística

**Código:** `GDO-PRO-002` | **Capacidade:** GDO-F01-P02

## 7.1 Descrição

Atribuição de código de classificação conforme plano de classificação hierárquico, definindo a organização do documento no arquivo e sua temporalidade.

## 7.2 Fluxo do Processo

```text
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Documento      │     │  Consulta ao     │     │  Atribuição de  │
│  Capturado      │────▶│  Plano de        │────▶│  Código de      │
│  (sem classe)   │     │  Classificação   │     │  Classificação  │
└─────────────────┘     └──────────────────┘     └────────┬────────┘
                                                           │
                                                           ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Vinculação     │     │  Validação de    │     │  Definição da   │
│  à Temporalidade│◀────│  Classificação   │◀────│  Destinação     │
│                 │     │                  │     │  Prevista       │
└────────┬────────┘     └──────────────────┘     └─────────────────┘
         │
         ▼
┌─────────────────┐
│  Registro de    │
│  Auditoria      │
└─────────────────┘
```

## 7.3 Atividades

| # | Atividade | Ator Responsável | Sistema/Ferramenta |
| --- | --- | --- | --- |
| 1 | Identificar natureza do documento | Servidor/Gestor Documental | Análise Documental |
| 2 | Consultar plano de classificação | Servidor/Gestor Documental | Catálogo de Classes |
| 3 | Atribuir código de classificação | Servidor/Gestor Documental | Formulário de Classificação |
| 4 | Validar classificação (dupla) | Gestor Documental | Validação de Classe |
| 5 | Definir destinação prevista | Sistema | Tabela de Temporalidade |
| 6 | Vincular à temporalidade | Sistema | Vinculador |
| 7 | Registrar log de auditoria | Sistema | Módulo de Auditoria |

## 7.4 Regras de Negócio Aplicáveis

* **RN-GDO-004** — Temporalidade define destinação
* Classificação deve seguir hierarquia: Classe → Subclasse → Série

## 7.5 Indicadores

| Indicador | Meta |
| --- | --- |
| % documentos classificados | 100% |
| Tempo médio de classificação | ≤ 2 dias úteis |
| Taxa de reclassificação | ≤ 2% |

---

# 8. Processo 3: Tramitação

**Código:** `GDO-PRO-003` | **Capacidade:** GDO-F01-P04

## 8.1 Descrição

Encaminhamento de documentos entre unidades organizacionais com fluxo configurável, permitindo despachos, pareceres e acompanhamento de prazos.

## 8.2 Fluxo do Processo

```text
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Documento      │     │  Definição do    │     │  Envio para     │
│  Classificado   │────▶│  Destinatário    │────▶│  Unidade        │
│                 │     │  (unidade/pessoa)│     │  Destino        │
└─────────────────┘     └──────────────────┘     └────────┬────────┘
                                                           │
                                                           ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Recebimento    │     │  Análise e       │     │  Registro de    │
│  e Ciência      │◀────│  Despacho        │◀────│  Despacho       │
│                 │     │  (opcional)      │     │                 │
└────────┬────────┘     └──────────────────┘     └─────────────────┘
         │
         ▼
┌─────────────────┐     ┌──────────────────┐
│  Próxima        │     │  Registro de     │
│  Tramitação ou  │────▶│  Auditoria       │
│  Arquivamento   │     │                  │
└─────────────────┘     └──────────────────┘
```

## 8.3 Atividades

| # | Atividade | Ator Responsável | Sistema/Ferramenta |
| --- | --- | --- | --- |
| 1 | Identificar destinatário | Servidor/Gestor Documental | Catálogo de Unidades |
| 2 | Definir prazo de resposta | Servidor/Gestor Documental | Configurador de Fluxo |
| 3 | Enviar documento | Sistema | Motor de Workflow |
| 4 | Notificar destinatário | Sistema | Notificador |
| 5 | Registrar recebimento | Destinatário | Confirmação de Ciência |
| 6 | Analisar e despachar | Destinatário | Editor de Despacho |
| 7 | Encaminhar ou arquivar | Destinatário | Botão de Ação |
| 8 | Registrar log de auditoria | Sistema | Módulo de Auditoria |

## 8.4 Regras de Negócio Aplicáveis

* **RN-GDO-003** — Não eliminar documento em fase corrente sem autorização
* Prazos devem ser configuráveis por tipo documental
* Alertas automáticos de vencimento

## 8.5 Indicadores

| Indicador | Meta |
| --- | --- |
| Tempo médio de tramitação | ≤ 5 dias úteis |
| % documentos dentro do prazo | ≥ 90% |
| Taxa de documentos parados (>30 dias) | ≤ 5% |

---

# 9. Processo 4: Arquivamento

**Código:** `GDO-PRO-004` | **Capacidade:** GDO-F01-P05

## 9.1 Descrição

Movimentação de documentos para arquivo intermediário, com indexação e localização para preservação e consulta futura.

## 9.2 Fluxo do Processo

```text
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Documento      │     │  Verificação     │     │  Indexação      │
│  Tramitado      │────▶│  de Pendências   │────▶│  para           │
│  (fase corrente)│     │                  │     │  Arquivo        │
└─────────────────┘     └──────────────────┘     └────────┬────────┘
                                                           │
                                                           ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Disponibilização│     │  Armazenamento   │     │  Definição de  │
│  para Consulta  │◀────│  no Arquivo      │◀────│  Localização   │
│                 │     │  Intermediário   │     │  Física/Lógica │
└────────┬────────┘     └──────────────────┘     └─────────────────┘
         │
         ▼
┌─────────────────┐
│  Registro de    │
│  Auditoria      │
└─────────────────┘
```

## 9.3 Atividades

| # | Atividade | Ator Responsável | Sistema/Ferramenta |
| --- | --- | --- | --- |
| 1 | Verificar pendências | Sistema | Validador de Pendências |
| 2 | Confirmar arquivamento | Servidor/Gestor Documental | Botão de Arquivamento |
| 3 | Definir localização | Sistema | Indexador de Arquivo |
| 4 | Mover para arquivo intermediário | Sistema | Motor de Arquivamento |
| 5 | Atualizar índice de consulta | Sistema | Indexador |
| 6 | Registrar log de auditoria | Sistema | Módulo de Auditoria |

## 9.4 Indicadores

| Indicador | Meta |
| --- | --- |
| Tempo de arquivamento | ≤ 1 dia útil |
| % documentos arquivados sem pendências | 100% |

---

# 10. Processo 5: Destinação

**Código:** `GDO-PRO-005` | **Capacidade:** GDO-F01-P06

## 10.1 Descrição

Aplicação da tabela de temporalidade, decidindo entre eliminação ou guarda permanente dos documentos.

## 10.2 Fluxo do Processo

```text
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Documento      │     │  Consulta à      │     │  Avaliação      │
│  Arquivado      │────▶│  Tabela de       │────▶│  de             │
│  (prazo vencido)│     │  Temporalidade   │     │  Destinação     │
└─────────────────┘     └──────────────────┘     └────────┬────────┘
                                                           │
                              ┌────────────────────────────┼────────────────┐
                              │                            │                │
                              ▼                            ▼                ▼
                     ┌─────────────────┐          ┌─────────────────┐  ┌─────────────────┐
                     │  ELIMINAÇÃO     │          │  GUARDA         │  │  PRORROGAÇÃO    │
                     │  (descarte)     │          │  PERMANENTE     │  │  (reavaliação)  │
                     └────────┬────────┘          └────────┬────────┘  └────────┬────────┘
                              │                            │                │
                              ▼                            ▼                ▼
                     ┌─────────────────┐          ┌─────────────────┐  ┌─────────────────┐
                     │  Registro de    │          │  Transferência  │  │  Atualização    │
                     │  Eliminação     │          │  para Guarda     │  │  de Prazo       │
                     └────────┬────────┘          └────────┬────────┘  └────────┬────────┘
                              │                            │                │
                              └────────────────────────────┴────────────────┘
                                                           │
                                                           ▼
                                                  ┌─────────────────┐
                                                  │  Registro de    │
                                                  │  Auditoria      │
                                                  └─────────────────┘
```

## 10.3 Atividades

| # | Atividade | Ator Responsável | Sistema/Ferramenta |
| --- | --- | --- | --- |
| 1 | Identificar documentos com prazo vencido | Sistema | Alerta de Temporalidade |
| 2 | Consultar tabela de temporalidade | Sistema | Catálogo de Temporalidade |
| 3 | Avaliar destinação | Autoridade Homologadora | Formulário de Avaliação |
| 4a | Eliminar (se aplicável) | Autoridade Homologadora | Botão de Eliminação |
| 4b | Transferir para guarda permanente | Autoridade Homologadora | Botão de Transferência |
| 4c | Prorrogar prazo (com justificativa) | Autoridade Homologadora | Formulário de Prorrogação |
| 5 | Registrar termo de eliminação/guarda | Sistema | Gerador de Termo |
| 6 | Registrar log de auditoria | Sistema | Módulo de Auditoria |

## 10.4 Regras de Negócio Aplicáveis

* **RN-GDO-003** — Não eliminar documento em fase corrente sem autorização
* **RN-GDO-004** — Temporalidade define destinação
* Eliminação requer autoridade homologadora

## 10.5 Indicadores

| Indicador | Meta |
| --- | --- |
| % documentos destinação correta | 100% |
| Tempo de destinação após prazo | ≤ 30 dias |
| Taxa de prorrogação indevida | ≤ 1% |

---

# 11. Processo 6: Gestão de Processos Documentais

**Código:** `GDO-PRO-006` | **Capacidade:** GDO-F02

## 11.1 Descrição

Gestão do ciclo de vida de processos administrativos, desde a abertura até o encerramento, com inclusão de documentos, tramitação, despachos e reabertura.

## 11.2 Atividades Principais

| # | Atividade | Ator Responsável | Sistema/Ferramenta |
| --- | --- | --- | --- |
| 1 | Abrir processo (autuação, numeração única) | Servidor/Gestor Documental | Módulo de Processos |
| 2 | Incluir documentos no processo | Servidor/Gestor Documental | Anexador de Documentos |
| 3 | Tramitar processo entre setores | Servidor/Gestor Documental | Motor de Workflow |
| 4 | Registrar despachos e pareceres | Servidor/Gestor Documental | Editor de Despacho |
| 5 | Encerrar processo (arquivamento/baixa) | Servidor/Gestor Documental | Botão de Encerramento |
| 6 | Reabrir processo (com justificativa) | Servidor/Gestor Documental | Formulário de Reabertura |

## 11.3 Indicadores

| Indicador | Meta |
| --- | --- |
| Tempo médio de tramitação de processo | ≤ 15 dias úteis |
| % processos encerrados sem pendências | 100% |

---

# 12. Processo 7: Pesquisa e Consulta

**Código:** `GDO-PRO-007` | **Capacidade:** GDO-F03

## 12.1 Descrição

Localização e recuperação de documentos e processos por pesquisa textual (OCR), metadados ou consulta pública.

## 12.2 Atividades Principais

| # | Atividade | Ator Responsável | Sistema/Ferramenta |
| --- | --- | --- | --- |
| 1 | Pesquisar por conteúdo textual | Público/Servidor | Motor de Busca |
| 2 | Pesquisar por metadados | Servidor/Gestor Documental | Filtros Estruturados |
| 3 | Consultar documentos públicos | Público | Portal da Transparência |
| 4 | Solicitar empréstimo documental | Servidor | Formulário de Empréstimo |
| 5 | Exportar relatórios | Servidor/Gestor Documental | Exportador |

## 12.3 Indicadores

| Indicador | Meta |
| --- | --- |
| Tempo de resposta da pesquisa | ≤ 3 segundos |
| % satisfação do usuário | ≥ 85% |

---

# 13. Processo 8: Assinatura e Autenticação

**Código:** `GDO-PRO-008` | **Capacidade:** GDO-F04

## 13.1 Descrição

Assinatura eletrônica e digital de documentos, com validação de integridade e cadeia certificadora.

## 13.2 Atividades Principais

| # | Atividade | Ator Responsável | Sistema/Ferramenta |
| --- | --- | --- | --- |
| 1 | Assinar documento eletronicamente | Servidor/Gestor Documental | Assinador Eletrônico (DOM-IDN) |
| 2 | Assinar documento digitalmente | Servidor/Gestor Documental | Assinador Digital (ICP-Brasil) |
| 3 | Validar assinatura | Sistema/Servidor | Validador de Assinatura |
| 4 | Autenticar cópias | Sistema | Certificador de Cópias |

## 13.3 Indicadores

| Indicador | Meta |
| --- | --- |
| % documentos oficiais assinados | 100% |
| Taxa de invalidação de assinatura | 0% |

---

# 14. Processo 9: Digitalização e OCR

**Código:** `GDO-PRO-009` | **Capacidade:** GDO-F08

## 14.1 Descrição

Conversão de documentos físicos em digitais, com reconhecimento óptico de caracteres para indexação e pesquisa.

## 14.2 Atividades Principais

| # | Atividade | Ator Responsável | Sistema/Ferramenta |
| --- | --- | --- | --- |
| 1 | Capturar documentos em lote | Servidor/Gestor Documental | Scanner |
| 2 | Aplicar OCR | Sistema | Motor de OCR |
| 3 | Validar qualidade | Servidor/Gestor Documental | Validador de Qualidade |

## 14.3 Indicadores

| Indicador | Meta |
| --- | --- |
| Volume mensal digitalizado | ≥ 6.000 páginas |
| Taxa de reconhecimento OCR | ≥ 95% |

---

# 15. Processo 10: Auditoria e Rastreabilidade

**Código:** `GDO-PRO-010` | **Capacidade:** GDO-F09

## 15.1 Descrição

Registro e consulta do histórico de ações sobre documentos e processos, com geração de relatórios de auditoria.

## 15.2 Atividades Principais

| # | Atividade | Ator Responsável | Sistema/Ferramenta |
| --- | --- | --- | --- |
| 1 | Registrar log de ações | Sistema | Módulo de Auditoria |
| 2 | Vincular à trilha de auditoria (DOM-IDN) | Sistema | Integrador de Auditoria |
| 3 | Gerar relatórios de auditoria | Administrador/Gestor | Relatórios |

## 15.3 Indicadores

| Indicador | Meta |
| --- | --- |
| % ações registradas | 100% |
| Tempo de geração de relatório | ≤ 5 minutos |

---

# 16. Processo 11: Segurança e Acesso

**Código:** `GDO-PRO-011` | **Capacidade:** GDO-F10

## 16.1 Descrição

Controle de permissões de acesso a documentos e processos, com classificação de sigilo e conformidade LGPD.

## 16.2 Atividades Principais

| # | Atividade | Ator Responsável | Sistema/Ferramenta |
| --- | --- | --- | --- |
| 1 | Configurar perfis de acesso | Administrador GDO | Módulo de Segurança (DOM-IDN) |
| 2 | Classificar sigilo | Servidor/Gestor Documental | Classificador de Sigilo |
| 3 | Tratar dados pessoais (LGPD) | Administrador GDO | Módulo de LGPD |

## 16.3 Indicadores

| Indicador | Meta |
| --- | --- |
| % documentos com acesso controlado | 100% |
| Taxa de incidentes de segurança | 0% |

---

# 17. Relacionamento com Atores

| Processo | Ator Principal | Ator Secundário |
| --- | --- | --- |
| GDO-PRO-001 Captura e Registro | Servidor/Gestor Documental | — |
| GDO-PRO-002 Classificação | Servidor/Gestor Documental | Gestor Documental |
| GDO-PRO-003 Tramitação | Servidor/Gestor Documental | Destinatário |
| GDO-PRO-004 Arquivamento | Servidor/Gestor Documental | — |
| GDO-PRO-005 Destinação | Autoridade Homologadora | — |
| GDO-PRO-006 Gestão de Processos | Servidor/Gestor Documental | — |
| GDO-PRO-007 Pesquisa e Consulta | Público (consulta) | Servidor/Gestor Documental |
| GDO-PRO-008 Assinatura | Servidor/Gestor Documental | Autoridade Homologadora |
| GDO-PRO-009 Digitalização/OCR | Servidor/Gestor Documental | — |
| GDO-PRO-010 Auditoria | Administrador GDO | Autoridade Homologadora |
| GDO-PRO-011 Segurança/Acesso | Administrador GDO | — |

---

# 18. Relacionamento com Capacidades

| Processo | Capacidade (Nível 1) | Capacidade (Nível 2) |
| --- | --- | --- |
| GDO-PRO-001 | GDO-F01 Gestão de Documentos | GDO-F01-P01 Captura e Registro |
| GDO-PRO-002 | GDO-F01 Gestão de Documentos | GDO-F01-P02 Classificação Arquivística |
| GDO-PRO-003 | GDO-F01 Gestão de Documentos | GDO-F01-P04 Tramitação |
| GDO-PRO-004 | GDO-F01 Gestão de Documentos | GDO-F01-P05 Arquivamento |
| GDO-PRO-005 | GDO-F01 Gestão de Documentos | GDO-F01-P06 Destinação |
| GDO-PRO-006 | GDO-F02 Gestão de Processos | GDO-F02-P01 a P06 |
| GDO-PRO-007 | GDO-F03 Pesquisa e Consulta | GDO-F03-P01 a P05 |
| GDO-PRO-008 | GDO-F04 Assinatura | GDO-F04-P01 a P04 |
| GDO-PRO-009 | GDO-F08 Digitalização/OCR | GDO-F08-P01 a P03 |
| GDO-PRO-010 | GDO-F09 Auditoria | GDO-F09-P01 a P03 |
| GDO-PRO-011 | GDO-F10 Segurança/Acesso | GDO-F10-P01 a P03 |

---

# 19. Relacionamento com Outros Domínios

| Processo | Domínio Relacionado | Natureza |
| --- | --- | --- |
| GDO-PRO-008 Assinatura | DOM-IDN (Identidade) | Consome serviço de autenticação |
| GDO-PRO-010 Auditoria | DOM-IDN (Identidade) | Consome `core.trilha_auditoria` |
| GDO-PRO-011 Segurança | DOM-IDN (Identidade) | Consome perfis/permissões |
| GDO-PRO-001 Captura | DOM-MET (Metadados) | Compartilha modelo de metadados |
| GDO-PRO-006 Processos | DOM-COMPRAS | Vincula `processo_documental` |
| GDO-PRO-007 Consulta Pública | DOM-CUM (Cadastro) | Valida acesso por pessoa |
| GDO-PRO-011 LGPD | DOM-DAD (Dados) | Alinha políticas de tratamento |

---

# 20. Identificador do Artefato

| Atributo | Valor |
| --- | --- |
| **Identificador** | `ACT-PRO-GDO-001` |
| **Código do artefato** | `DOM-GDO-003` |
| **Versão** | 2.0 |
| **Data** | 2026-09-01 |
| **Responsável** | Equipe SIGMUN |
| **Status** | Vigente |

---

# 21. Controle de Versões

| Versão | Data | Descrição | Autor |
| --- | --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato | Equipe SIGMUN |
| 2.0 | 2026-09-01 | Conteúdo detalhado: 11 processos, fluxos de trabalho, atividades, regras de negócio, indicadores, relacionamentos | Equipe SIGMUN |

---

**Documento:** 003-Mapa-de-Processos-Gestao-Documental.md

**Última atualização:** 2026-09-01

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
