# 001 – Mapa de Atores – Gestão Documental

#### Mapa de Atores – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-001

**Domínio:** Gestão Documental

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Documental.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000C-HIERARQUIA-DOCUMENTAL.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `030-Roadmap-de-Implementacao-dos-Dominios.md`
* `Mapa-de-Dominios.md`
* `Modelo-Conceitual.md`
* `Modelo-Logico.md`
* `Modelo-Fisico.md`
* `Dicionario-de-dados.md`

---

# 1. Finalidade

O **Mapa de Atores – Gestão Documental** (`DOM-GDO-001`) identifica as pessoas, unidades organizacionais, funções, entidades externas e demais participantes que interagem direta ou indiretamente com os processos e serviços do domínio de Gestão Documental.

O objetivo é estabelecer uma visão estruturada de:

* quem participa;
* qual é o papel de cada participante;
* quais responsabilidades possui;
* com quais processos interage;
* quais informações produz ou consome;
* quais decisões pode tomar;
* quais sistemas ou serviços utiliza;
* quais relações de dependência existem.

Este documento servirá de base para a elaboração dos processos, serviços, casos de uso, histórias de usuário, regras de negócio, requisitos e controles de acesso do domínio.

---

# 2. Princípios

O mapeamento dos atores deverá observar os seguintes princípios:

* **Atores representam papéis, não necessariamente pessoas específicas.**
* **Uma mesma pessoa poderá exercer mais de um papel**, conforme suas atribuições.
* **Um ator poderá representar uma unidade organizacional**, quando a interação ocorrer institucionalmente.
* **Atores externos deverão ser identificados quando influenciarem ou participarem dos processos.**
* **Responsabilidade não deverá ser confundida com permissão de sistema.**
* **Permissões deverão ser derivadas posteriormente das responsabilidades e regras de negócio.**
* **Atores deverão ser relacionados aos processos e serviços nos quais efetivamente participam.**

---

# 3. Conceito de Ator

Para este domínio, considera-se ator qualquer pessoa, papel, unidade organizacional, organização ou sistema externo que:

* participe de um processo documental;
* forneça documento ou informação;
* consuma documento ou informação;
* execute uma atividade de gestão documental;
* tome decisão sobre classificação, arquivamento ou destinação;
* aprove ou rejeite eliminação ou guarda permanente;
* assine ou autentique documento;
* fiscalize o cumprimento da política documental;
* forneça serviço de apoio (jurídico, TI, arquivo);
* receba resultado de consulta ou publicação;
* integre-se com o SIGMUN.

---

# 4. Classificação dos Atores

Os atores serão classificados em:

```text
Atores Internos
Atores Externos
Atores Institucionais
Atores de Controle
Atores de Apoio
Sistemas Externos
```

---

# 5. Atores Internos — Identificação

São os participantes pertencentes à estrutura administrativa municipal ou que atuam institucionalmente dentro da Prefeitura.

## 5.1 Atores principais

| Identificador | Ator | Descrição |
|---|---|---|
| `ACT-GDO-001` | **Servidor / Gestor Documental** | Servidor responsável pela criação, classificação, versionamento e tramitação de documentos no âmbito de sua unidade. |
| `ACT-GDO-002` | **Autoridade Homologadora** | Autoridade competente (Secretário Municipal, Presidente de Comissão, Procurador ou equivalente) responsável por autorizar eliminação, guarda permanente e homologar atos documentais. |
| `ACT-GDO-003` | **Administrador GDO** | Administrador do sistema de Gestão Documental, responsável pela configuração de taxonomias, planos de classificação, tabelas de temporalidade e parametrização técnica do módulo. |

## 5.2 Atores institucionais internos

| Identificador | Ator | Descrição |
|---|---|---|
| `ACT-GDO-004` | Unidade Administrativa (Órgão/Secretaria) | Unidade organizacional que produz, recebe e arquiva documentos. Representa o destino institucional do acervo. |
| `ACT-GDO-005` | Setor de Protocolo / Arquivo | Unidade responsável pelo recebimento, registro, distribuição e guarda física/intermediária de documentos. |
| `ACT-GDO-006` | Setor Jurídico | Unidade responsável por pareceres jurídicos, validação de autenticidade e consultoria em legislação arquivística. |

# 001 – Mapa de Atores – Gestão Documental

#### Mapa de Atores – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-001

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

# 6. Atores Externos

São participantes fora da estrutura administrativa municipal que interagem com o domínio.

| Identificador | Ator | Descrição |
|---|---|---|
| `ACT-GDO-007` | **Público (consulta)** | Cidadão, empresa ou entidade que consulta documentos públicos, atas, legislação e demais documentos de acesso livre via Portal da Transparência ou consulta pública. |
| `ACT-GDO-008` | Órgão Externo / Outro Ente | Outro órgão público (Tribunais, Assembleia, Ministério Público) que recebe ou fornece documentos oficiais por meio de ofícios e comunicações oficiais. |
| `ACT-GDO-009` | Fornecedor / Contratado | Pessoa jurídica que apresenta documentos contratuais, certidões e comprovantes no âmbito de processos de compras e contratações. |

---

# 7. Atores Institucionais

Representam entidades com as quais a Prefeitura mantém relação formal no âmbito documental.

* **Tribunais de Contas (TCU/TCE):** recebem documentação fiscalizada, determinam adequação de arquivamento e eliminação;
* **Arquivo Nacional / Sistema de Gestão de Documentos do Estado (SIGE/arquivo estadual):** define normas arquivísticas de interoperabilidade e preservação;
* **Conselhos de Administração:** podem determinar guarda permanente de documentos históricos.

---

# 8. Atores de Controle

Atores responsáveis pela fiscalização e conformidade:

* **Controladoria Municipal:** verifica conformidade da gestão documental com normas internas e legislação;
* **Auditoria Interna:** audita processos de eliminação, integridade documental e segregação de funções;
* **Comissão de Avaliação Documental (CAD):** comissão temporária ou permanente que avalia e propõe eliminação ou guarda permanente de documentos.

---

# 9. Atores de Apoio

* **Setor de Tecnologia da Informação:** mantém infraestrutura, storage, backup e disponibilidade do repositório documental;
* **Assessoria de Comunicação:** publica documentos oficiais, diários oficiais e comunicados;
* **Gabinete do Prefeito:** produz e recebe atos oficiais de alta hierarquia (decretos, portarias, leis).

---

# 10. Sistemas Externos

| Identificador | Sistema | Interação |
|---|---|---|
| `SYS-EXT-001` | Portal da Transparência | Publicação de documentos de acesso público |
| `SYS-EXT-002` | Sistema Eletrônico do Município (novo/legado) | Intercâmbio de documentos de processo eletrônico |
| `SYS-EXT-003` | Certificador Digital (ICP-Brasil) | Validação de assinaturas digitais e certificados |
| `SYS-EXT-004` | Diário Oficial eletrônico | Publicação de atos oficiais |

---

# 11. Relacionamento entre Atores e Fases do Ciclo de Vida Documental

| Fase | Ator principal | Ator de apoio |
|---|---|---|
| Criação / Captura | Servidor / Gestor Documental | Setor de Protocolo |
| Classificação | Servidor / Gestor Documental | Administrador GDO |
| Versionamento | Servidor / Gestor Documental | Setor de TI |
| Tramitação | Servidor / Gestor Documental | Setor de Protocolo |
| Arquivamento (corrente/intermediário) | Setor de Arquivo | Unidade Administrativa |
| Avaliação / Temporalidade | Administrador GDO | Comissão de Avaliação |
| Eliminação | Autoridade Homologadora | Setor Jurídico |
| Guarda Permanente | Autoridade Homologadora | Setor de Arquivo |
| Consulta / Publicação | Público (consulta) | Setor de Comunicação |
| Auditoria / Controle | Auditoria Interna | Controladoria |

---

# 12. Segregação de Funções

| Ator | Pode criar | Pode classificar | Pode arquivar | Pode eliminar | Pode auditar |
|---|---|---|---|---|---|
| Servidor / Gestor Documental | ✅ | ✅ | ✅ (corrente) | ❌ | ❌ |
| Autoridade Homologadora | ❌ | ❌ | ❌ | ✅ (autoriza) | ❌ |
| Administrador GDO | ❌ | ✅ (configura) | ❌ | ❌ | ❌ |
| Auditoria Interna | ❌ | ❌ | ❌ | ❌ | ✅ |
| Público (consulta) | ❌ | ❌ | ❌ | ❌ | ❌ |

---

# 13. Relacionamento com Perfis de Acesso (DOM-IDN)

| Ator | Perfil mínimo (DOM-IDN) | Permissões esperadas |
|---|---|---|
| Servidor / Gestor Documental | `USUARIO_GDO` | CRUD de documentos da unidade; upload de versões |
| Autoridade Homologadora | `AUTORIDADE_GDO` | Aprovar/rejeitar eliminação; homologar atos |
| Administrador GDO | `ADMIN_GDO` | Configurar planos de classificação, temporalidade, taxonomias |
| Público (consulta) | `PUBLICO` | Leitura de documentos públicos |
| Auditoria Interna | `AUDITOR_GDO` | Leitura completa + logs de auditoria |

---

# 14. Identificador do Artefato

Este documento deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

Identificador do artefato:

`ACT-MAP-GDO-001`

Relações principais:

```text
DOM-GDO-000
       ↓
ACT-MAP-GDO-001
       ↓
PROC-GDO-001... (processos)
       ↓
SERV-GDO-001... (serviços)
       ↓
UC-GDO-001... (casos de uso)
```

---

# 15. Controle de Versões

| Versão | Data | Descrição |
|---|---|---|
| 1.0 | 2026-09-01 | Criação do Mapa de Atores do Domínio de Gestão Documental |

---

**Documento:** 001-Mapa-de-Atores-Gestao-Documental.md

**Última atualização:** 2026-09-01

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
