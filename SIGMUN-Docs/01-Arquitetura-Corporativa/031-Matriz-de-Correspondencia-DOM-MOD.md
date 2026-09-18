# 031 — Matriz de Correspondência DOM ↔ MOD

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Classificação da Informação:** Pública
**Documento:** Matriz de Correspondência entre Domínios e Módulos
**Código:** 031
**Versão:** 1.2
**Status:** Revisão
**Última atualização:** 2026-09-17
**Responsável:** Equipe SIGMUN
**Domínio:** Arquitetura Corporativa
**Documento(s) Relacionado(s):**
- [Padrão corporativo](../00-Governanca/000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md)
- [Hierarquia documental](../00-Governanca/000C-HIERARQUIA-DOCUMENTAL-v1.0.md)
- [Mapa de domínios](../02-Modelo-de-Negocio/Mapa-de-Dominios.md)
- [Arquitetura de software](004-Arquitetura-de-Software.md)
- [Diagnóstico histórico de 2026-09-16](../DIAGNOSTICO-ESTADO-SISTEMA.md)

| Campo | Conteúdo |
| --- | --- |
| Projeto | SIGMUN |
| Proprietário | Arquitetura Corporativa |
| Responsável | Equipe SIGMUN |
| Versão | 1.2 |
| Status | Revisão |
| Classificação | Pública |
| Data de Criação | 16/09/2026 |
| Última Revisão | 17/09/2026 |
| Próxima Revisão | Na próxima alteração DOM ↔ módulo ou validação desta revisão |
| Aprovado por | Canonicalização autorizada no ADR-0006; aprovação integral da matriz não registrada |

> Esta revisão distingue fatos observados de propostas arquiteturais. Não registra aprovação de identificadores `MOD-*`, homologação funcional ou prontidão para produção.

---

## 1. Objetivo

Registrar a correspondência observada entre domínios corporativos (`DOM-*`) e módulos de aplicação (`sigmun_*`), distinguindo evidência técnica, proposta documental e pendência de decisão. Os identificadores `MOD-*` são propostas, não renomeações de pacotes nem decisões de aprovação.

## 2. Princípios

- Domínio organiza responsabilidades, conceitos, capacidades e requisitos de negócio.
- Módulo é uma unidade implementável da aplicação, organizada como Bounded Context.
- A presença de um diretório não comprova implementação.
- Referência textual, adoção de padrão e dependência técnica são relações diferentes.
- Uma dependência não transfere a responsabilidade funcional (ownership).
- A correspondência principal não implica exclusividade nem cobertura integral do domínio. Relações adicionais exigem evidências próprias.
- A hierarquia DOM → MOD é uma relação de navegação; não substitui a hierarquia normativa corporativa nem exige mover arquivos existentes.

## 3. Definições

### 3.1 Domínio corporativo

Unidade de conhecimento ou responsabilidade documentada. Um domínio pode existir sem módulo implementado.

### 3.2 Módulo de aplicação

Unidade técnica atualmente localizada em:

```text
src/modules/sigmun_<modulo>
```

O nome técnico existente é a identidade estável usada neste inventário. A proposta de um código `MOD-*` não significa implementação ou aprovação arquitetural.

### 3.3 Ownership

Responsabilidade funcional principal sustentada por casos de uso, entidades, APIs e persistência coerentes com o domínio. A correspondência confirmada nesta matriz limita-se ao escopo encontrado no código.

### 3.4 Dependência e referência

Dependência pressupõe utilização demonstrável de uma interface, serviço, contrato ou mecanismo. Comentários que mencionam outro domínio podem descrever somente um padrão reutilizado ou uma integração futura. Não devem ser convertidos automaticamente em dependências implementadas.

## 4. Evidências e limites da verificação

Inspeção estática em **17/09/2026**, sobre a base Git `51c82dc`, com as alterações documentais desta revisão ainda não commitadas:

- [Registro da aplicação](../../src/main.py): 14 chamadas `include_router`, provenientes de 8 módulos.
- [Módulos de aplicação](../../src/modules/): 28 diretórios `sigmun_*`.
- [Migrações](../../alembic/versions/): arquivos de persistência correspondentes aos módulos com código.
- [Testes unitários](../../tests/unit/) e [testes de integração](../../tests/integration/): artefatos disponíveis; presença não equivale a execução ou aprovação.
- [Mapa de domínios](../02-Modelo-de-Negocio/Mapa-de-Dominios.md) e documentos dos domínios: referência de negócio, com ressalvas de nomenclatura registradas abaixo.

Nos 20 módulos classificados como preparados foram encontrados 13 arquivos Python por módulo, sem instruções de implementação além de docstrings ou `pass` na análise AST. Nenhum deles possui router registrado no ponto de entrada inspecionado. Isso não declara ausência de toda capacidade relacionada em outros módulos ou no núcleo compartilhado.

Esta revisão **não executou testes funcionais, migrações ou homologação**. Não certifica completude de requisitos, segurança, operação ou prontidão para produção. O diagnóstico de 16/09/2026 é uma fotografia histórica, não substitui esta checagem. O README do código é auxiliar e seu catálogo está incompleto; metadados de empacotamento não são usados como prova de implementação.

## 5. Matriz principal DOM ↔ módulo

### 5.1 Correspondências sustentadas por implementação

“Implementação identificada” significa código, persistência e APIs registradas, não entrega integral do domínio. Os códigos MOD continuam propostos.

| Domínio documentado | Módulo de aplicação | MOD proposto | Maturidade técnica | Correspondência |
| --- | --- | --- | --- | --- |
| [DOM-COM](../DOM-COMPRAS-001/) | [sigmun_compras](../../src/modules/sigmun_compras/) | `MOD-COMPRAS` | Implementação identificada | Confirmada no escopo observado |
| [DOM-CUM](../DOM-CUM/) | [sigmun_cadastro](../../src/modules/sigmun_cadastro/) | `MOD-CUM` | Implementação identificada | Confirmada no escopo observado |
| [DOM-DAD](../DOM-DAD/) | [sigmun_dad](../../src/modules/sigmun_dad/) | `MOD-DAD` | Implementação identificada | Confirmada no escopo observado |
| [DOM-GDO](../DOM-GDO/) | [sigmun_gdo](../../src/modules/sigmun_gdo/) | `MOD-GDO` | Implementação identificada | Confirmada no escopo observado |
| [DOM-IDN](../DOM-IDN/) | [sigmun_idn](../../src/modules/sigmun_idn/) | `MOD-IDN` | Implementação identificada | Confirmada no escopo observado |
| [DOM-INT](../DOM-INT/) | [sigmun_int](../../src/modules/sigmun_int/) | `MOD-INT` | Implementação identificada | Confirmada no escopo observado |
| [DOM-MET](../DOM-MET/) | [sigmun_met](../../src/modules/sigmun_met/) | `MOD-MET` | Implementação identificada | Confirmada no escopo observado |
| [DOM-SEG](../DOM-SEG/) | [sigmun_seg](../../src/modules/sigmun_seg/) | `MOD-SEG` | Implementação identificada | Confirmada no escopo observado |

### 5.2 Correspondências candidatas preservadas da versão 1.0

As oito associações abaixo permanecem **candidatas**, não ownership tecnicamente confirmado. Foram propostas na versão 1.0; o scaffolding vazio não permite validá-las por comportamento funcional. A afinidade nominal não basta para promovê-las a confirmadas.

| Domínio candidato | Módulo de aplicação | MOD proposto | Maturidade técnica | Correspondência |
| --- | --- | --- | --- | --- |
| [DOM-ASS](../DOM-ASS/) | [sigmun_assistencia_social](../../src/modules/sigmun_assistencia_social/) | `MOD-ASS` | Preparado | Candidata; validar escopo |
| [DOM-EDU](../DOM-EDU/) | [sigmun_educacao](../../src/modules/sigmun_educacao/) | `MOD-EDU` | Preparado | Candidata; validar escopo |
| [DOM-FRO](../DOM-FRO/) | [sigmun_frotas](../../src/modules/sigmun_frotas/) | `MOD-FRO` | Preparado | Candidata; validar escopo |
| [DOM-OBR](../DOM-OBR/) | [sigmun_obras](../../src/modules/sigmun_obras/) | `MOD-OBR` | Preparado | Candidata; validar escopo |
| [DOM-OUV](../DOM-OUV/) | [sigmun_ouvidoria](../../src/modules/sigmun_ouvidoria/) | `MOD-OUV` | Preparado | Candidata; validar escopo |
| [DOM-PLA](../DOM-PLA/) | [sigmun_planejamento](../../src/modules/sigmun_planejamento/) | `MOD-PLA` | Preparado | Candidata; validar escopo |
| [DOM-SAU](../DOM-SAU/) | [sigmun_saude](../../src/modules/sigmun_saude/) | `MOD-SAU` | Preparado | Candidata; validar escopo |
| [DOM-TRI](../DOM-TRI/) | [sigmun_tributos](../../src/modules/sigmun_tributos/) | `MOD-TRI` | Preparado | Candidata; validar escopo |

### 5.3 Estruturas sem correspondência determinada

Os rótulos MOD potenciais da versão 1.0 não são adotados como identidades oficiais. Não se infere automaticamente DOM-CON para Contabilidade, DOM-PAT para Patrimônio ou DOM-PES para RH: essas associações exigem validação de fronteiras, como as demais candidatas.

| Módulo de aplicação | Maturidade técnica | Correspondência DOM | Identidade MOD |
| --- | --- | --- | --- |
| [sigmun_administracao](../../src/modules/sigmun_administracao/) | Preparado | Não determinada | Não definida |
| [sigmun_agricultura](../../src/modules/sigmun_agricultura/) | Preparado | Não determinada | Não definida |
| [sigmun_almoxarifado](../../src/modules/sigmun_almoxarifado/) | Preparado | Não determinada | Não definida |
| [sigmun_contabilidade](../../src/modules/sigmun_contabilidade/) | Preparado | Não determinada | Não definida |
| [sigmun_controladoria](../../src/modules/sigmun_controladoria/) | Preparado | Não determinada | Não definida |
| [sigmun_financas](../../src/modules/sigmun_financas/) | Preparado | Não determinada | Não definida |
| [sigmun_gabinete](../../src/modules/sigmun_gabinete/) | Preparado | Não determinada | Não definida |
| [sigmun_licitacoes](../../src/modules/sigmun_licitacoes/) | Preparado | Não determinada | Não definida |
| [sigmun_patrimonio](../../src/modules/sigmun_patrimonio/) | Preparado | Não determinada | Não definida |
| [sigmun_procuradoria](../../src/modules/sigmun_procuradoria/) | Preparado | Não determinada | Não definida |
| [sigmun_rh](../../src/modules/sigmun_rh/) | Preparado | Não determinada | Não definida |
| [sigmun_transparencia](../../src/modules/sigmun_transparencia/) | Preparado | Não determinada | Não definida |

## 6. Resumo em dois eixos independentes

| Maturidade técnica | Quantidade |
| --- | --- |
| Implementação identificada e APIs registradas | 8 |
| Preparado, sem implementação Python identificada | 20 |
| Total | 28 |

| Correspondência DOM ↔ módulo | Quantidade |
| --- | --- |
| Confirmada no escopo observado | 8 |
| Candidata, preservada da versão 1.0 | 8 |
| Não determinada | 12 |
| Total | 28 |

Há **33 diretórios de domínio**. A matriz de módulos não é um catálogo completo dos domínios: 17 diretórios não aparecem como correspondência confirmada ou candidata nas seções 5.1 e 5.2. Isso não autoriza criar módulos fictícios ou concluir ausência de capacidades compartilhadas.

## 7. Evidências específicas das correspondências confirmadas

As APIs abaixo importam casos de uso e repositórios do respectivo módulo. O registro efetivo deve ser conferido em `src/main.py`, não apenas na existência do arquivo de API.

| Domínio | API / evidência funcional | Persistência |
| --- | --- | --- |
| DOM-COM | [Compras, UC-COMPRAS-022 e RN-COMPRAS-025 a 029](../../src/modules/sigmun_compras/presentation/api/compras_router.py) | [Migração inicial de Compras](../../alembic/versions/20260820_01_core_compras.py) |
| DOM-CUM | [Pessoas, identificação DOM-CUM e regras RN-CUM](../../src/modules/sigmun_cadastro/presentation/api/pessoas_router.py) | [Endereços, documentos e contatos](../../alembic/versions/20260831_02_cum_enderecos_documentos_contatos.py) |
| DOM-DAD | [API Dados Corporativos](../../src/modules/sigmun_dad/presentation/api/__init__.py) | [Ativos, catálogo e linhagem](../../alembic/versions/20260831_04_dad_ativos_catalogo_linhagem.py) |
| DOM-GDO | [API Gestão Documental](../../src/modules/sigmun_gdo/presentation/api/__init__.py) | [Documentos, tramitações e processos](../../alembic/versions/20260901_02_gdo_documentos_tramitacoes_processos.py) |
| DOM-IDN | [API Identidade e Acesso](../../src/modules/sigmun_idn/presentation/api/__init__.py) | [Usuários, roles e sessões](../../alembic/versions/20260831_03_idn_usuarios_roles_sessoes.py) |
| DOM-INT | [API Integração](../../src/modules/sigmun_int/presentation/api/__init__.py) | [Schema de integração](../../alembic/versions/20260916_01_dom_int_schema.py) |
| DOM-MET | [API Metadados Corporativos](../../src/modules/sigmun_met/presentation/api/__init__.py) | [Metadados, classificações e taxonomias](../../alembic/versions/20260901_01_met_metadados_classificacoes_taxonomias.py) |
| DOM-SEG | [API Segurança da Informação](../../src/modules/sigmun_seg/presentation/api/__init__.py) | [Modelos de segurança](../../alembic/versions/20260901_04_dom_seg_models.py) e [correção do schema](../../alembic/versions/20260901_05_dom_seg_schema_correction.py) |

As migrações são exemplos verificáveis, não uma lista exaustiva nem prova de aplicação ao banco em execução.

## 8. Relações que não comprovam ownership ou dependência implementada

### 8.1 Integração e segurança: adoção de padrão

Os [modelos de Integração](../../src/modules/sigmun_int/infrastructure/database/models.py), linhas 11–13 na base inspecionada, dizem “Segue o padrão do DOM-SEG”. Isso descreve convenções de persistência, não consumo comprovado do módulo `sigmun_seg`. A análise de imports Python do módulo não encontrou importação direta de outro `src.modules.sigmun_*`.

Não afirmar `MOD-INT → depende de MOD-SEG` a partir desses comentários. Dependências indiretas, via núcleo, infraestrutura ou contratos externos exigem investigação específica.

### 8.2 Cadastro e identidade: integração futura/provisória

Os routers de [Pessoas](../../src/modules/sigmun_cadastro/presentation/api/pessoas_router.py) e [Unidades](../../src/modules/sigmun_cadastro/presentation/api/unidades_router.py) descrevem `X-Usuario-Id` como provisório “até o DOM-IDN”. Não comprovam integração concluída com `sigmun_idn`. A análise de imports Python também não encontrou importação direta de outro módulo de negócio.

A correspondência principal observada continua sendo DOM-CUM ↔ `sigmun_cadastro`; não se atribui a ele ownership de Identidade e Acesso.

### 8.3 Referências a Compras: padrões e histórico

Comentários em Cadastro, Dados, Gestão Documental, Identidade e Metadados mencionam DOM-COM como padrão ou contexto, após normalização conforme ADR-0006. Exemplo: [exceções de Metadados](../../src/modules/sigmun_met/domain/exceptions.py) descrevem um “espelho DOM-COM”. Cada ocorrência deve ser interpretada em seu contexto, não convertida em ownership.

Compras contém artefatos de processo documental, enquanto Gestão Documental possui módulo próprio. Essa coexistência não prova duplicação indevida nem transferência integral de responsabilidade: a fronteira entre o recorte de Compras e o serviço documental corporativo permanece um ponto de rastreabilidade a aprofundar.

## 9. Divergências documentais preexistentes

### 9.1 Identificação de Compras — decisão aplicada

Conforme [ADR-0006](../00-Governanca/ADR/ADR-0006-Compras-canonicalizacao.md), **DOM-COM é o identificador corporativo vigente de Compras e Contratações**, alinhado ao [Mapa de Domínios](../02-Modelo-de-Negocio/Mapa-de-Dominios.md).

- DOM-COMPRAS: identificação documental histórica, substituída nas referências correntes.
- DOM-COMPRAS-001: identificação histórica do piloto e localização física/documental preservada por compatibilidade.
- O [diretório documental](../DOM-COMPRAS-001/index.md), os destinos de evidências e os códigos documentais legados não são renomeados.
- O módulo técnico permanece `sigmun_compras`; RN-COMPRAS-*, UC-COMPRAS-* e ENT-COMPRAS-* permanecem inalterados.

A decisão foi aprovada pelo solicitante desta alteração; não se presume aprovação institucional adicional. Esta normalização não altera ownership, maturidade, fronteiras funcionais ou a situação proposta de MOD-COMPRAS. A auditoria anterior permanece como registro histórico.

### 9.2 Hierarquia e identidade documental

O padrão 000A e a hierarquia 000C apresentam escalas de níveis distintas. Esta matriz não resolve sua precedência nem substitui os dois documentos. A organização por índices é navegação, não mudança de autoridade normativa.

Há numeração divergente entre nomes de arquivos e títulos corporativos (por exemplo, a arquitetura de software tem arquivo 004 e título 008). Os links desta matriz apontam para os **arquivos existentes**, sem inferir renumeração oficial.

## 10. Critérios de classificação

### 10.1 Eixo técnico

- **Preparado:** scaffolding existente, sem implementação identificada na inspeção.
- **Em implementação:** comportamento parcial identificado, ainda sem evidências suficientes de integração ao ponto de entrada aplicável.
- **Implementação identificada:** código funcional reconhecível, persistência e APIs integradas ao ponto de entrada, no escopo observado. Substitui o rótulo ambíguo “Implementado” da versão 1.0; não certifica completude nem execução bem-sucedida.
- **Consolidado:** requer critérios formalizados e evidências de testes, homologação, observabilidade e operação. Nenhum módulo é certificado neste estado por esta revisão.

### 10.2 Eixo da correspondência

- **Confirmada no escopo observado:** identificação documental e responsabilidade funcional corroboradas pelo código.
- **Candidata:** associação proposta ainda sem evidência funcional suficiente.
- **Não determinada:** sem associação formalizada nesta matriz.

A maturidade documental e a aprovação de códigos MOD são independentes desses dois eixos.

## 11. Organização documental

Manter os documentos corporativos nos diretórios atuais. Organizar índices de módulos sob `05-Modulos/sigmun_<modulo>/index.md`, usando a identidade técnica existente. Isso evita criar identidades MOD oficiais por inferência.

Um índice de domínio deve listar seus documentos e apontar para módulos confirmados ou candidatos com rótulos explícitos. Um índice de módulo deve informar correspondência, maturidade, evidências, limites e retorno ao catálogo. Domínio sem associação registrada não deve receber módulo fictício.

## 12. SIGMUN-AI e RAG

A navegação pode relacionar domínio, módulo, capacidade, caso de uso e evidência. O consumidor deve preservar os qualificadores “candidato”, “não determinado”, “proposto” e “implementação identificada”. A indexação não é prova de integração RAG implementada nem deve promover relações hipotéticas a fatos.

## 13. Governança

Atualizar a matriz quando houver novo módulo, mudança de responsabilidade, API, persistência, fronteira de contexto ou documentação corporativa relevante. Registrar data, base técnica, evidências e histórico. Aprovações devem ser registradas pela instância responsável; não presumidas pela presença do documento no repositório.

## 14. Regras para os índices

- Verificar o conteúdo e o registro na aplicação, não somente nomes de diretórios.
- Usar esta matriz revisada como referência de correspondência, preservando suas ressalvas.
- Permitir índices de inventário para os 20 módulos preparados, sem declará-los implementados.
- Não atribuir código MOD oficial aos 12 módulos sem correspondência determinada.
- Verificar destinos locais e cobertura dos documentos; distinguir link válido de conteúdo validado.
- Identificar templates e documentos em elaboração quando observados, sem mudar aprovações em massa.

## 15. Estado das decisões

Confirmados por inspeção: 28 estruturas modulares, 8 com implementação identificada e 14 routers registrados. Preservadas como candidatas: 8 associações da versão 1.0. Sem correspondência determinada: 12 estruturas. Aprovação dos códigos MOD e alinhamento da hierarquia corporativa continuam pendentes. A canonicalização de Compras foi decidida no ADR-0006 e aplicada nesta revisão.

## 16. Próximas verificações

- Manter a identidade DOM-COM e a compatibilidade física do piloto conforme ADR-0006; acompanhar a auditoria de regressão.
- Validar as fronteiras dos módulos preparados e as associações candidatas.
- Ampliar o cruzamento requisito → caso de uso → implementação → teste.
- Executar testes e homologação em ambiente apropriado antes de atestar completude funcional.
- Manter os índices alinhados às mudanças desta matriz, sem alterar o roadmap como se a indexação fosse entrega de capacidades de negócio.

## 17. Histórico de alterações

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-16 | Criação da matriz formal DOM ↔ MOD com base na análise do repositório | Equipe SIGMUN |
| 1.1 | 2026-09-17 | Correção Markdown; eixos independentes; evidências locais; revisão de dependências inferidas; divergências de nomenclatura e regras de indexação. Em revisão, sem aprovação presumida | Equipe SIGMUN |
| 1.2 | 2026-09-17 | Aplicação do ADR-0006: DOM-COM vigente; histórico e localização física preservados; demais pendências mantidas | Gildazio, por autorização do solicitante |
