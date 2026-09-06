# 009 – Requisitos Não Funcionais – Gestão Documental

#### Requisitos Não Funcionais – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-009

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
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

---

# 1. Finalidade

Este documento define os **Requisitos Não Funcionais do Domínio de Gestão Documental** do SIGMUN.

Os requisitos não funcionais estabelecem características, restrições, atributos de qualidade, condições operacionais e requisitos técnicos que deverão ser observados na implementação das funcionalidades do domínio.

Eles complementam os requisitos funcionais e estabelecem **como o sistema deverá operar**, além de definir características relacionadas a:

* segurança;
* desempenho;
* disponibilidade;
* confiabilidade;
* escalabilidade;
* usabilidade;
* acessibilidade;
* interoperabilidade;
* auditabilidade;
* rastreabilidade;
* manutenção;
* observabilidade;
* portabilidade;
* recuperação;
* continuidade;
* proteção de dados;
* operação offline.

---

# 2. Princípios

Os requisitos não funcionais deste domínio deverão observar os princípios corporativos do SIGMUN:

* Segurança por princípio.
* Privacidade e proteção de dados desde a concepção.
* Transparência por padrão.
* Classificação da informação por política.
* Aberto sempre que possível, restrito sempre que necessário.
* Interoperabilidade por padrão.
* Reutilização de serviços corporativos.
* Rastreabilidade integral.
* Auditabilidade.
* Configurabilidade.
* Evolução incremental.
* Arquitetura orientada a domínios.
* Independência tecnológica sempre que possível.

---

# 3. Convenção de Identificação

Os requisitos não funcionais utilizarão o padrão:

```text
RNF-GDO-XXX
```

Exemplo:

```text
RNF-GDO-001
```

O identificador deverá permanecer estável durante o ciclo de vida do requisito.

---

# 4. Classificação

Os requisitos não funcionais serão agrupados nas seguintes categorias:

| Código    | Categoria                       |
| --------- | ------------------------------- |
| RNF-SEG   | Segurança                       |
| RNF-PRIV  | Privacidade e Proteção de Dados |
| RNF-PERF  | Desempenho                      |
| RNF-DISP  | Disponibilidade                 |
| RNF-CONF  | Confiabilidade                  |
| RNF-ESC   | Escalabilidade                  |
| RNF-USAB  | Usabilidade                     |
| RNF-INT   | Interoperabilidade              |
| RNF-AUD   | Auditabilidade                  |
| RNF-MAN   | Manutenibilidade                |

---

# 5. Requisitos Não Funcionais — Segurança

## RNF-GDO-001 — Autenticação Obrigatória

O sistema deverá exigir autenticação via DOM-IDN para todos os endpoints da API de gestão documental.

**Categoria:** RNF-SEG

**Prioridade:** P0

---

## RNF-GDO-002 — Controle de Acesso Granular

O sistema deverá implementar controle de acesso baseado em perfis (RBAC) com permissões por documento, unidade e tipo de operação.

**Categoria:** RNF-SEG

**Prioridade:** P0

---

## RNF-GDO-003 — Criptografia em Trânsito

Todas as comunicações deverão utilizar TLS 1.2 ou superior.

**Categoria:** RNF-SEG

**Prioridade:** P0

---

## RNF-GDO-004 — Criptografia em Repouso

Documentos sigilosos deverão ser armazenados com criptografia AES-256.

**Categoria:** RNF-SEG

**Prioridade:** P1

---

## RNF-GDO-005 — Classificação de Sigilo

O sistema deverá suportar classificação de sigilo em três níveis: público, reservado e secreto, com controles específicos para cada nível.

**Categoria:** RNF-SEG

**Prioridade:** P0

---

# 6. Requisitos Não Funcionais — Privacidade e Proteção de Dados

## RNF-GDO-006 — Conformidade com LGPD

O sistema deverá estar em conformidade com a Lei Geral de Proteção de Dados (LGPD), incluindo tratamento de dados pessoais, consentimento e direito ao esquecimento.

**Categoria:** RNF-PRIV

**Prioridade:** P0

---

## RNF-GDO-007 — Mascaramento de Dados Pessoais

O sistema deverá permitir mascaramento de dados pessoais em documentos de acesso público.

**Categoria:** RNF-PRIV

**Prioridade:** P1

---

## RNF-GDO-008 — Registro de Consentimento

O sistema deverá registrar o consentimento do titular para tratamento de dados pessoais quando aplicável.

**Categoria:** RNF-PRIV

**Prioridade:** P1

---

# 7. Requisitos Não Funcionais — Desempenho

## RNF-GDO-009 — Tempo de Resposta de Consulta

Consultas de pesquisa deverão retornar resultados em até 2 segundos para até 10.000 registros.

**Categoria:** RNF-PERF

**Prioridade:** P1

---

## RNF-GDO-010 — Upload de Documentos

O sistema deverá suportar upload de documentos de até 100MB com tempo de processamento inferior a 30 segundos.

**Categoria:** RNF-PERF

**Prioridade:** P1

---

## RNF-GDO-011 — Processamento OCR

O processamento OCR de documentos digitalizados deverá ser realizado em background, com tempo máximo de 5 minutos por documento.

**Categoria:** RNF-PERF

**Prioridade:** P2

---

## RNF-GDO-012 — Indexação para Pesquisa

A indexação de documentos para pesquisa deverá ser realizada em até 1 minuto após o registro.

**Categoria:** RNF-PERF

**Prioridade:** P1

---

# 8. Requisitos Não Funcionais — Disponibilidade

## RNF-GDO-013 — Disponibilidade do Repositório

O repositório documental deverá ter disponibilidade mínima de 99,5% do tempo.

**Categoria:** RNF-DISP

**Prioridade:** P0

---

## RNF-GDO-014 — Backup Automático

O sistema deverá realizar backup automático diário dos documentos e metadados, com retenção mínima de 30 dias.

**Categoria:** RNF-DISP

**Prioridade:** P0

---

## RNF-GDO-015 — Recuperação de Desastres

O sistema deverá possuir plano de recuperação de desastres com RPO de 24 horas e RTO de 4 horas.

**Categoria:** RNF-DISP

**Prioridade:** P1

---

# 9. Requisitos Não Funcionais — Confiabilidade

## RNF-GDO-016 — Integridade de Dados

O sistema deverá garantir a integridade dos documentos armazenados por meio de verificação periódica de hash SHA-256.

**Categoria:** RNF-CONF

**Prioridade:** P0

---

## RNF-GDO-017 — Validação de Metadados

O sistema deverá validar a completude e formato dos metadados obrigatórios antes do registro do documento.

**Categoria:** RNF-CONF

**Prioridade:** P0

---

## RNF-GDO-018 — Tratamento de Erros

O sistema deverá tratar erros de forma adequada, retornando mensagens claras e registrando logs para auditoria.

**Categoria:** RNF-CONF

**Prioridade:** P1

---

# 10. Requisitos Não Funcionais — Escalabilidade

## RNF-GDO-019 — Armazenamento Escalável

O sistema deverá suportar crescimento do acervo documental sem degradação de desempenho, com capacidade mínima de 1TB.

**Categoria:** RNF-ESC

**Prioridade:** P1

---

## RNF-GDO-020 — Processamento Assíncrono

Operações pesadas (OCR, geração de relatórios, verificação de integridade) deverão ser processadas de forma assíncrona.

**Categoria:** RNF-ESC

**Prioridade:** P1

---

# 11. Requisitos Não Funcionais — Usabilidade

## RNF-GDO-021 — Interface Intuitiva

A interface do sistema deverá ser intuitiva, com tempo de treinamento inferior a 4 horas para usuários básicos.

**Categoria:** RNF-USAB

**Prioridade:** P2

---

## RNF-GDO-022 — Pesquisa Simplificada

O sistema deverá oferecer pesquisa simplificada com interface similar a buscadores web, permitindo pesquisa por palavras-chave.

**Categoria:** RNF-USAB

**Prioridade:** P1

---

## RNF-GDO-023 — Acessibilidade

O sistema deverá estar em conformidade com as diretrizes de acessibilidade WCAG 2.1 nível AA.

**Categoria:** RNF-USAB

**Prioridade:** P2

---

# 12. Requisitos Não Funcionais — Interoperabilidade

## RNF-GDO-024 — API RESTful

O sistema deverá expor funcionalidades via API RESTful, seguindo padrões corporativos do SIGMUN.

**Categoria:** RNF-INT

**Prioridade:** P0

---

## RNF-GDO-025 — Integração com DOM-IDN

O sistema deverá integrar-se ao domínio de Identidade (DOM-IDN) para autenticação e autorização.

**Categoria:** RNF-INT

**Prioridade:** P0

---

## RNF-GDO-026 — Integração com Portal da Transparência

O sistema deverá permitir publicação de documentos no portal de transparência de forma automatizada.

**Categoria:** RNF-INT

**Prioridade:** P1

---

## RNF-GDO-027 — Formatos de Documento

O sistema deverá suportar os formatos PDF, PDF/A, TIFF, XML, DOCX, ODT para documentos digitais.

**Categoria:** RNF-INT

**Prioridade:** P1

---

# 13. Requisitos Não Funcionais — Auditabilidade

## RNF-GDO-028 — Log de Auditoria Imutável

O sistema deverá registrar todas as ações em log de auditoria imutável, que não poderá ser alterado ou excluído.

**Categoria:** RNF-AUD

**Prioridade:** P0

---

## RNF-GDO-029 — Rastreabilidade Completa

O sistema deverá manter rastreabilidade completa de todas as operações realizadas sobre um documento, incluindo usuário, data/hora e IP de origem.

**Categoria:** RNF-AUD

**Prioridade:** P0

---

## RNF-GDO-030 — Retenção de Logs

Os logs de auditoria deverão ser retidos por no mínimo 5 anos, conforme legislação arquivística.

**Categoria:** RNF-AUD

**Prioridade:** P1

---

# 14. Requisitos Não Funcionais — Manutenibilidade

## RNF-GDO-031 — Documentação de API

A API deverá ser documentada automaticamente via OpenAPI/Swagger.

**Categoria:** RNF-MAN

**Prioridade:** P1

---

## RNF-GDO-032 — Configurabilidade

O sistema deverá permitir configuração de parâmetros (prazos, classificações, taxonomias) sem necessidade de alteração de código.

**Categoria:** RNF-MAN

**Prioridade:** P1

---

## RNF-GDO-033 — Observabilidade

O sistema deverá fornecer métricas, logs e traces para monitoramento operacional.

**Categoria:** RNF-MAN

**Prioridade:** P1

---

# 15. Refinamento Futuro

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

# 16. Registro no Mapa Mestre

Este artefato deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

**Identificador do artefato:**

`RNF-MAP-GDO-001`

**Tipo:**

Mapa de Requisitos Não Funcionais.

**Domínio:**

Gestão Documental.

**Versão:**

2.0.

---

# 17. Próximo Artefato

O próximo artefato recomendado é:

`010-Especificacoes-Gestao-Documental.md`

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

| Versão | Data       | Descrição                                                                |
| ------ | ---------- | ------------------------------------------------------------------------ |
| 1.0    | 2026-08-20 | Criação do esboço inicial padronizado do artefato                        |
| 2.0    | 2026-09-02 | Conteúdo detalhado: 33 requisitos não funcionais, classificação completa |

---

**Documento:** 009-Requisitos-Nao-Funcionais-Gestao-Documental.md

**Última atualização:** 2026-09-02

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
