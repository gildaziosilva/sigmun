# SIGMUN — documentação geral

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Domínio:** Governança documental
**Versão:** 1.1
**Status:** Em elaboração
**Classificação da Informação:** Pública
**Última atualização:** 2026-09-17
**Responsável:** Equipe SIGMUN

| Campo | Conteúdo |
| --- | --- |
| Projeto | SIGMUN |
| Proprietário | Governança documental |
| Responsável | Equipe SIGMUN |
| Versão | 1.1 |
| Status | Em elaboração; validação editorial pendente |
| Classificação | Pública |
| Data de Criação | 17/09/2026 |
| Última Revisão | 17/09/2026 |
| Próxima Revisão | Ao alterar os documentos ou evidências relacionados |
| Aprovado por | Aprovação não registrada |

**Documento(s) Relacionado(s):** [Catálogo de módulos](05-Modulos/index.md) · [Matriz DOM ↔ módulo](01-Arquitetura-Corporativa/031-Matriz-de-Correspondencia-DOM-MOD.md) · [Auditoria documental](00-Governanca/AUDITORIA-DOCUMENTAL-2026-09-17.md)

> Identidade corporativa vigente: **DOM-COM — Compras e Contratações**, conforme [ADR-0006](00-Governanca/ADR/ADR-0006-Compras-canonicalizacao.md). DOM-COMPRAS é identificação documental histórica; DOM-COMPRAS-001 é identificação histórica do piloto e localização física preservada por compatibilidade. A decisão não aprova códigos MOD nem certifica completude funcional.

## Comece por aqui

Este índice é a entrada da documentação corporativa. Preserva a organização existente e distingue planejamento, documentação e implementação. Não altera a precedência normativa: as diferenças entre 000A e 000C constam na auditoria.

- [Constituição do projeto](000-CONSTITUICAO-DO-PROJETO-SIGMUN.md)
- [Padrão corporativo](00-Governanca/000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md)
- [Hierarquia documental](00-Governanca/000C-HIERARQUIA-DOCUMENTAL-v1.0.md)
- [Mapa de domínios](02-Modelo-de-Negocio/Mapa-de-Dominios.md)
- [Roadmap](ROADMAP.md)
- [Diagnóstico histórico de 16/09/2026](DIAGNOSTICO-ESTADO-SISTEMA.md)

## Situação verificada em 17/09/2026

- [Auditoria de regressão da canonicalização de Compras](00-Governanca/AUDITORIA-REGRESSAO-COMPRAS-2026-09-17.md)

- 33 diretórios de domínio documentados; existência de documentos não significa implementação.
- 28 módulos técnicos: 8 com implementação identificada e 20 preparados.
- 14 routers registrados, distribuídos pelos 8 módulos com código.
- 8 correspondências DOM confirmadas no escopo observado, 8 candidatas e 12 módulos sem correspondência determinada.
- Aprovação dos códigos MOD e harmonização da hierarquia continuam pendentes. A identidade de Compras foi definida no ADR-0006.

Consulte a matriz e a auditoria antes de interpretar “Vigente” como conteúdo completo ou “implementação identificada” como homologação. O inventário cobre os 1.097 Markdown preexistentes; a auditoria semântica integral continua pendente.

## Domínios

| Domínio | Nome documental | Situação da correspondência |
| --- | --- | --- |
| [DOM-ANA](DOM-ANA/index.md) | Analytics e Inteligência | Sem associação registrada na matriz |
| [DOM-ASS](DOM-ASS/index.md) | Assistência Social | Candidata; validar escopo |
| [DOM-ATE](DOM-ATE/index.md) | Atendimento ao Cidadão | Sem associação registrada na matriz |
| [DOM-COM](DOM-COMPRAS-001/index.md) | Gestão de Compras e Contratações | Confirmada no escopo observado |
| [DOM-CON](DOM-CON/index.md) | Contabilidade Pública | Sem associação registrada na matriz |
| [DOM-CPT](DOM-CPT/index.md) | Gestão de Competências | Sem associação registrada na matriz |
| [DOM-CUM](DOM-CUM/index.md) | Cadastro Único Municipal | Confirmada no escopo observado |
| [DOM-DAD](DOM-DAD/index.md) | Dados Corporativos | Confirmada no escopo observado |
| [DOM-DEC](DOM-DEC/index.md) | Desenvolvimento Econômico | Sem associação registrada na matriz |
| [DOM-DIA](DOM-DIA/index.md) | Gestão de Diárias, Viagens e Deslocamentos | Sem associação registrada na matriz |
| [DOM-EDU](DOM-EDU/index.md) | Educação Pública | Candidata; validar escopo |
| [DOM-FRO](DOM-FRO/index.md) | Gestão de Frota | Candidata; validar escopo |
| [DOM-GDO](DOM-GDO/index.md) | Gestão Documental | Confirmada no escopo observado |
| [DOM-GEO](DOM-GEO/index.md) | Geoinformação Municipal | Sem associação registrada na matriz |
| [DOM-GOV](DOM-GOV/index.md) | Governança Municipal | Sem associação registrada na matriz |
| [DOM-IDN](DOM-IDN/index.md) | Identidade e Acesso | Confirmada no escopo observado |
| [DOM-IMO](DOM-IMO/index.md) | Cadastro Imobiliário | Sem associação registrada na matriz |
| [DOM-IND](DOM-IND/index.md) | Indicadores e Desempenho | Sem associação registrada na matriz |
| [DOM-INF](DOM-INF/index.md) | Infraestrutura Tecnológica | Sem associação registrada na matriz |
| [DOM-INT](DOM-INT/index.md) | Integração e Interoperabilidade | Confirmada no escopo observado |
| [DOM-MAM](DOM-MAM/index.md) | Meio Ambiente | Sem associação registrada na matriz |
| [DOM-MET](DOM-MET/index.md) | Metadados Corporativos | Confirmada no escopo observado |
| [DOM-MOB](DOM-MOB/index.md) | Mobilidade e Serviços de Campo | Sem associação registrada na matriz |
| [DOM-OBR](DOM-OBR/index.md) | Obras e Infraestrutura | Candidata; validar escopo |
| [DOM-ORC](DOM-ORC/index.md) | Orçamento Público | Sem associação registrada na matriz |
| [DOM-OUV](DOM-OUV/index.md) | Ouvidoria | Candidata; validar escopo |
| [DOM-PAT](DOM-PAT/index.md) | Gestão Patrimonial | Sem associação registrada na matriz |
| [DOM-PES](DOM-PES/index.md) | Gestão de Pessoas | Sem associação registrada na matriz |
| [DOM-PLA](DOM-PLA/index.md) | Planejamento Governamental | Candidata; validar escopo |
| [DOM-SAU](DOM-SAU/index.md) | Saúde Pública | Candidata; validar escopo |
| [DOM-SEG](DOM-SEG/index.md) | Segurança da Informação | Confirmada no escopo observado |
| [DOM-TEL](DOM-TEL/index.md) | Gestão Territorial | Sem associação registrada na matriz |
| [DOM-TRI](DOM-TRI/index.md) | Administração Tributária | Candidata; validar escopo |

## Módulos

[Catálogo dos 28 módulos e seus índices](05-Modulos/index.md). Os módulos preparados possuem índices de inventário, não documentação de capacidades entregues.

## Documentação geral e corporativa

Lista dos documentos fora dos diretórios DOM. Caminhos e nomes existentes são preservados, inclusive quando o título interno tem outra numeração. Consulte a auditoria para essas divergências.

### 00-Governanca

- [00-Governanca/00.1-Estrutura-de-Governanca/001-Termo-de-Abertura.md](00-Governanca/00.1-Estrutura-de-Governanca/001-Termo-de-Abertura.md)
- [00-Governanca/00.1-Estrutura-de-Governanca/002-Visao-do-Projeto.md](00-Governanca/00.1-Estrutura-de-Governanca/002-Visao-do-Projeto.md)
- [00-Governanca/00.1-Estrutura-de-Governanca/003-Objetivos-Estrategicos.md](00-Governanca/00.1-Estrutura-de-Governanca/003-Objetivos-Estrategicos.md)
- [00-Governanca/00.1-Estrutura-de-Governanca/004-Modelo-de-Governanca.md](00-Governanca/00.1-Estrutura-de-Governanca/004-Modelo-de-Governanca.md)
- [00-Governanca/00.1-Estrutura-de-Governanca/005-Governanca-Corporativa.md](00-Governanca/00.1-Estrutura-de-Governanca/005-Governanca-Corporativa.md)
- [00-Governanca/00.1-Estrutura-de-Governanca/007-Gestao-de-Riscos.md](00-Governanca/00.1-Estrutura-de-Governanca/007-Gestao-de-Riscos.md)
- [00-Governanca/00.1-Estrutura-de-Governanca/008-Gestao-do-Portfolio.md](00-Governanca/00.1-Estrutura-de-Governanca/008-Gestao-do-Portfolio.md)
- [00-Governanca/00.1-Estrutura-de-Governanca/009-Governanca-da-Arquitetura.md](00-Governanca/00.1-Estrutura-de-Governanca/009-Governanca-da-Arquitetura.md)
- [00-Governanca/00.1-Estrutura-de-Governanca/010-Etica-Integridade-e-Compliance.md](00-Governanca/00.1-Estrutura-de-Governanca/010-Etica-Integridade-e-Compliance.md)
- [00-Governanca/00.2-Governanca-Organizacional/010-Plano-de-Comunicacao.md](00-Governanca/00.2-Governanca-Organizacional/010-Plano-de-Comunicacao.md)
- [00-Governanca/00.2-Governanca-Organizacional/011-Plano-de-Gestao-das-Partes-Interessadas.md](00-Governanca/00.2-Governanca-Organizacional/011-Plano-de-Gestao-das-Partes-Interessadas.md)
- [00-Governanca/00.2-Governanca-Organizacional/012-Plano-de-Gestao-de-Mudancas.md](00-Governanca/00.2-Governanca-Organizacional/012-Plano-de-Gestao-de-Mudancas.md)
- [00-Governanca/00.3-Governanca-da-Informacao/013-Plano-de-Governanca-de-Dados.md](00-Governanca/00.3-Governanca-da-Informacao/013-Plano-de-Governanca-de-Dados.md)
- [00-Governanca/00.3-Governanca-da-Informacao/014-Plano-de-Governanca-de-Indicadores.md](00-Governanca/00.3-Governanca-da-Informacao/014-Plano-de-Governanca-de-Indicadores.md)
- [00-Governanca/00.4-Governanca-Institucional/015-Plano-de-Auditoria.md](00-Governanca/00.4-Governanca-Institucional/015-Plano-de-Auditoria.md)
- [00-Governanca/00.4-Governanca-Institucional/016-Plano-de-Gestao-de-Conformidade.md](00-Governanca/00.4-Governanca-Institucional/016-Plano-de-Gestao-de-Conformidade.md)
- [00-Governanca/00.4-Governanca-Institucional/017-Plano-de-Continuidade-de-Negocios-e-Recuperacao-de-Desastres.md](00-Governanca/00.4-Governanca-Institucional/017-Plano-de-Continuidade-de-Negocios-e-Recuperacao-de-Desastres.md)
- [00-Governanca/00.4-Governanca-Institucional/018-Plano-de-Gestao-de-Crises.md](00-Governanca/00.4-Governanca-Institucional/018-Plano-de-Gestao-de-Crises.md)
- [00-Governanca/00.4-Governanca-Institucional/019-Plano-de-Comunicacao-Engajamento-e-Colaboracao-da-Comunidade-SIGMUN.md](00-Governanca/00.4-Governanca-Institucional/019-Plano-de-Comunicacao-Engajamento-e-Colaboracao-da-Comunidade-SIGMUN.md)
- [00-Governanca/00.4-Governanca-Institucional/020-Politica-de-Classificacao-da-Informacao-e- Publicacao-de-Artefatos.md](00-Governanca/00.4-Governanca-Institucional/020-Politica-de-Classificacao-da-Informacao-e-%20Publicacao-de-Artefatos.md)
- [00-Governanca/00.5-Politicas-Corporativas/019-Politica-de-Governanca-Digital.md](00-Governanca/00.5-Politicas-Corporativas/019-Politica-de-Governanca-Digital.md)
- [00-Governanca/00.5-Politicas-Corporativas/020-Politica-de-Qualidade.md](00-Governanca/00.5-Politicas-Corporativas/020-Politica-de-Qualidade.md)
- [00-Governanca/00.5-Politicas-Corporativas/021-Politica-de-Seguranca.md](00-Governanca/00.5-Politicas-Corporativas/021-Politica-de-Seguranca.md)
- [00-Governanca/00.5-Politicas-Corporativas/022-Politica-de-Gestao-Documental.md](00-Governanca/00.5-Politicas-Corporativas/022-Politica-de-Gestao-Documental.md)
- [00-Governanca/00.5-Politicas-Corporativas/023-Politica-de-Retencao-e-Descarte-de-Documentos.md](00-Governanca/00.5-Politicas-Corporativas/023-Politica-de-Retencao-e-Descarte-de-Documentos.md)
- [00-Governanca/00.5-Politicas-Corporativas/024-Politica-de-Gestao-de-Riscos.md](00-Governanca/00.5-Politicas-Corporativas/024-Politica-de-Gestao-de-Riscos.md)
- [00-Governanca/00.5-Politicas-Corporativas/025-Politica-de-Protecao-de-Dados-Pessoais.md](00-Governanca/00.5-Politicas-Corporativas/025-Politica-de-Protecao-de-Dados-Pessoais.md)
- [00-Governanca/00.5-Politicas-Corporativas/026-Manual-de-Governanca-do-SIGMUN.md](00-Governanca/00.5-Politicas-Corporativas/026-Manual-de-Governanca-do-SIGMUN.md)
- [00-Governanca/00.6-Colaboracao/Engenharia-de-Software/Guia-do-Colaborador.md](00-Governanca/00.6-Colaboracao/Engenharia-de-Software/Guia-do-Colaborador.md)
- [00-Governanca/000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md](00-Governanca/000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md)
- [00-Governanca/000B-Base-de-Conhecimento/CHANGELOG.md](00-Governanca/000B-Base-de-Conhecimento/CHANGELOG.md)
- [00-Governanca/000B-Base-de-Conhecimento/CONVENCOES.md](00-Governanca/000B-Base-de-Conhecimento/CONVENCOES.md)
- [00-Governanca/000B-Base-de-Conhecimento/INDEX.md](00-Governanca/000B-Base-de-Conhecimento/INDEX.md)
- [00-Governanca/000B-Base-de-Conhecimento/ONTOLOGIA.md](00-Governanca/000B-Base-de-Conhecimento/ONTOLOGIA.md)
- [00-Governanca/000B-Base-de-Conhecimento/README.md](00-Governanca/000B-Base-de-Conhecimento/README.md)
- [00-Governanca/000B-Base-de-Conhecimento/SIGLAS.md](00-Governanca/000B-Base-de-Conhecimento/SIGLAS.md)
- [00-Governanca/000B-Base-de-Conhecimento/TAXONOMIA.md](00-Governanca/000B-Base-de-Conhecimento/TAXONOMIA.md)
- [00-Governanca/000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md](00-Governanca/000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md)
- [00-Governanca/000C-HIERARQUIA-DOCUMENTAL-v1.0.md](00-Governanca/000C-HIERARQUIA-DOCUMENTAL-v1.0.md)
- [00-Governanca/000D-MODELO-DE-DOCUMENTO.md](00-Governanca/000D-MODELO-DE-DOCUMENTO.md)
- [00-Governanca/000E-GUIA-DE-CONTRIBUICAO.md](00-Governanca/000E-GUIA-DE-CONTRIBUICAO.md)
- [00-Governanca/000F-Registro-de-Decisoes-Arquiteturais(ADR-Arqhiteture-Decision-Records).md](00-Governanca/000F-Registro-de-Decisoes-Arquiteturais%28ADR-Arqhiteture-Decision-Records%29.md)
- [00-Governanca/000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md](00-Governanca/000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md)
- [00-Governanca/000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md](00-Governanca/000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md)
- [00-Governanca/ADR/0001-adopt-apache-2.0-license.md](00-Governanca/ADR/0001-adopt-apache-2.0-license.md)
- [00-Governanca/ADR/ADR-0001-Arquitetura-Modular.md](00-Governanca/ADR/ADR-0001-Arquitetura-Modular.md)
- [00-Governanca/ADR/ADR-0002-Offline-First.md](00-Governanca/ADR/ADR-0002-Offline-First.md)
- [00-Governanca/ADR/ADR-0003-APIs-REST.md](00-Governanca/ADR/ADR-0003-APIs-REST.md)
- [00-Governanca/ADR/ADR-0004-Neutralidade-Tecnologica.md](00-Governanca/ADR/ADR-0004-Neutralidade-Tecnologica.md)
- [00-Governanca/ADR/ADR-0005-Cadastro-Unico-Municipal.md](00-Governanca/ADR/ADR-0005-Cadastro-Unico-Municipal.md)
- [00-Governanca/ADR/ADR-0006-Compras-canonicalizacao.md](00-Governanca/ADR/ADR-0006-Compras-canonicalizacao.md)
- [00-Governanca/ADR/ADR-INDEX.md](00-Governanca/ADR/ADR-INDEX.md)
- [00-Governanca/ADR/README.md](00-Governanca/ADR/README.md)
- [00-Governanca/ADR/templates/ADR-TEMPLATE.md](00-Governanca/ADR/templates/ADR-TEMPLATE.md)

### 01-Arquitetura-Corporativa

- [01-Arquitetura-Corporativa/001-Principios-de-Arquitetura.md](01-Arquitetura-Corporativa/001-Principios-de-Arquitetura.md)
- [01-Arquitetura-Corporativa/002-Arquitetura-de-Negocio.md](01-Arquitetura-Corporativa/002-Arquitetura-de-Negocio.md)
- [01-Arquitetura-Corporativa/003-Cadastro-Unico-Municipal.md](01-Arquitetura-Corporativa/003-Cadastro-Unico-Municipal.md)
- [01-Arquitetura-Corporativa/004-Arquitetura-de-Software.md](01-Arquitetura-Corporativa/004-Arquitetura-de-Software.md)
- [01-Arquitetura-Corporativa/005-Arquitetura-de-Dados.md](01-Arquitetura-Corporativa/005-Arquitetura-de-Dados.md)
- [01-Arquitetura-Corporativa/006-Arquitetura-de-Integracao.md](01-Arquitetura-Corporativa/006-Arquitetura-de-Integracao.md)
- [01-Arquitetura-Corporativa/007-Arquitetura-de-Seguranca.md](01-Arquitetura-Corporativa/007-Arquitetura-de-Seguranca.md)
- [01-Arquitetura-Corporativa/008-Arquitetura-de-Implantacao-e-Infraestrutura.md](01-Arquitetura-Corporativa/008-Arquitetura-de-Implantacao-e-Infraestrutura.md)
- [01-Arquitetura-Corporativa/009-Arquitetura-de-Experiencia-do-Usuario-e-Acessibilidade.md](01-Arquitetura-Corporativa/009-Arquitetura-de-Experiencia-do-Usuario-e-Acessibilidade.md)
- [01-Arquitetura-Corporativa/010-Arquitetura-de-Processos-e-Workflow.md](01-Arquitetura-Corporativa/010-Arquitetura-de-Processos-e-Workflow.md)
- [01-Arquitetura-Corporativa/011-Arquitetura-de-Relatorios-Indicadores-e-BI.md](01-Arquitetura-Corporativa/011-Arquitetura-de-Relatorios-Indicadores-e-BI.md)
- [01-Arquitetura-Corporativa/012-Arquitetura-de-Gestao-Documental-e-Arquivistica.md](01-Arquitetura-Corporativa/012-Arquitetura-de-Gestao-Documental-e-Arquivistica.md)
- [01-Arquitetura-Corporativa/013-Arquitetura-de-Identidade-e-Acessos.md](01-Arquitetura-Corporativa/013-Arquitetura-de-Identidade-e-Acessos.md)
- [01-Arquitetura-Corporativa/014-Arquitetura-de-Notificacoes-e-Comunicacao.md](01-Arquitetura-Corporativa/014-Arquitetura-de-Notificacoes-e-Comunicacao.md)
- [01-Arquitetura-Corporativa/015-Arquitetura-de-Dispositivos-Moveis-e-Servicos-de-Campo.md](01-Arquitetura-Corporativa/015-Arquitetura-de-Dispositivos-Moveis-e-Servicos-de-Campo.md)
- [01-Arquitetura-Corporativa/016-Arquitetura-de-Observabilidade-e-Operacoes-DevSecOps.md](01-Arquitetura-Corporativa/016-Arquitetura-de-Observabilidade-e-Operacoes-DevSecOps.md)
- [01-Arquitetura-Corporativa/017-Arquitetura-de-Governaca-de-Dados.md](01-Arquitetura-Corporativa/017-Arquitetura-de-Governaca-de-Dados.md)
- [01-Arquitetura-Corporativa/018-Arquitetura-de-BI-Analytcs-e-Inteligencia-Artificial.md](01-Arquitetura-Corporativa/018-Arquitetura-de-BI-Analytcs-e-Inteligencia-Artificial.md)
- [01-Arquitetura-Corporativa/019-Arquitetura-de-Gestao-de-Configuracao-e-versionamento.md](01-Arquitetura-Corporativa/019-Arquitetura-de-Gestao-de-Configuracao-e-versionamento.md)
- [01-Arquitetura-Corporativa/020-Arquitetura-de-Gestao-do-Ciclo-de-Vida.md](01-Arquitetura-Corporativa/020-Arquitetura-de-Gestao-do-Ciclo-de-Vida.md)
- [01-Arquitetura-Corporativa/021-Arquitetura-de-Continuidade-e-Evolucao-Tecnologica.md](01-Arquitetura-Corporativa/021-Arquitetura-de-Continuidade-e-Evolucao-Tecnologica.md)
- [01-Arquitetura-Corporativa/022-Arquitetura-de-Gestao-da-Qualidade-Corporativa.md](01-Arquitetura-Corporativa/022-Arquitetura-de-Gestao-da-Qualidade-Corporativa.md)
- [01-Arquitetura-Corporativa/023-Arquitetura-de-Gestao-da-Inovacao-e-Transformacao-Digital.md](01-Arquitetura-Corporativa/023-Arquitetura-de-Gestao-da-Inovacao-e-Transformacao-Digital.md)
- [01-Arquitetura-Corporativa/024-Arquitetura-de-Gestao-do-Conhecimento-e-Aprendizagem-Organizacional.md](01-Arquitetura-Corporativa/024-Arquitetura-de-Gestao-do-Conhecimento-e-Aprendizagem-Organizacional.md)
- [01-Arquitetura-Corporativa/025-Arquitetura-de-Gestao-de-Competencias-e-Desenvolvimento-de-Pessoas.md](01-Arquitetura-Corporativa/025-Arquitetura-de-Gestao-de-Competencias-e-Desenvolvimento-de-Pessoas.md)
- [01-Arquitetura-Corporativa/026-Arquitetura-de-Gestao-da-Mudanca-Organizacional.md](01-Arquitetura-Corporativa/026-Arquitetura-de-Gestao-da-Mudanca-Organizacional.md)
- [01-Arquitetura-Corporativa/027-Arquitetura-de-Excelencia-Operacional-e-Melhoria-Continua.md](01-Arquitetura-Corporativa/027-Arquitetura-de-Excelencia-Operacional-e-Melhoria-Continua.md)
- [01-Arquitetura-Corporativa/028-Arquitetura-de-Gestao-da-Sustentabilidade-e-Responsabilidade-Socioambiental.md](01-Arquitetura-Corporativa/028-Arquitetura-de-Gestao-da-Sustentabilidade-e-Responsabilidade-Socioambiental.md)
- [01-Arquitetura-Corporativa/029-Arquitetura-do-Observatorio-Municipal-Inteligente.md](01-Arquitetura-Corporativa/029-Arquitetura-do-Observatorio-Municipal-Inteligente.md)
- [01-Arquitetura-Corporativa/030-Roadmap-de-Implementacao-dos-Dominios.md](01-Arquitetura-Corporativa/030-Roadmap-de-Implementacao-dos-Dominios.md)
- [01-Arquitetura-Corporativa/031-Matriz-de-Correspondencia-DOM-MOD.md](01-Arquitetura-Corporativa/031-Matriz-de-Correspondencia-DOM-MOD.md)
- [01-Arquitetura-Corporativa/04-Conhecimento-Corporativo/000-CATALOGO-CORPORATIVO-DO-CONHECIMENTO.md](01-Arquitetura-Corporativa/04-Conhecimento-Corporativo/000-CATALOGO-CORPORATIVO-DO-CONHECIMENTO.md)

### 02-Modelo-de-Negocio

- [02-Modelo-de-Negocio/Cadeia-de-Valor-v1.0.md](02-Modelo-de-Negocio/Cadeia-de-Valor-v1.0.md)
- [02-Modelo-de-Negocio/Cadeia-de-Valor-v1.1.md](02-Modelo-de-Negocio/Cadeia-de-Valor-v1.1.md)
- [02-Modelo-de-Negocio/Glossario-de-Negocio.md](02-Modelo-de-Negocio/Glossario-de-Negocio.md)
- [02-Modelo-de-Negocio/Mapa-de-Atores.md](02-Modelo-de-Negocio/Mapa-de-Atores.md)
- [02-Modelo-de-Negocio/Mapa-de-Capacidades.md](02-Modelo-de-Negocio/Mapa-de-Capacidades.md)
- [02-Modelo-de-Negocio/Mapa-de-Dominios.md](02-Modelo-de-Negocio/Mapa-de-Dominios.md)
- [02-Modelo-de-Negocio/Mapa-de-Processos.md](02-Modelo-de-Negocio/Mapa-de-Processos.md)
- [02-Modelo-de-Negocio/Mapa-de-Secretarias.md](02-Modelo-de-Negocio/Mapa-de-Secretarias.md)
- [02-Modelo-de-Negocio/Mapa-de-Servicos.md](02-Modelo-de-Negocio/Mapa-de-Servicos.md)
- [02-Modelo-de-Negocio/Modelo-de-Competencias.md](02-Modelo-de-Negocio/Modelo-de-Competencias.md)
- [02-Modelo-de-Negocio/Modelo-de-Governanca-Administrativa.md](02-Modelo-de-Negocio/Modelo-de-Governanca-Administrativa.md)

### 03-Requisitos

- [03-Requisitos/Casos-de-Uso.md](03-Requisitos/Casos-de-Uso.md)
- [03-Requisitos/Criterios-de-Aceitacao.md](03-Requisitos/Criterios-de-Aceitacao.md)
- [03-Requisitos/Especificacoes-v1.0.md](03-Requisitos/Especificacoes-v1.0.md)
- [03-Requisitos/Historias-de-Usuario-v1.0.md](03-Requisitos/Historias-de-Usuario-v1.0.md)
- [03-Requisitos/Matriz-de-Rastreabilidade-v1.md](03-Requisitos/Matriz-de-Rastreabilidade-v1.md)
- [03-Requisitos/Regras-de-Negocio-v1.0.md](03-Requisitos/Regras-de-Negocio-v1.0.md)
- [03-Requisitos/Requisitos-Funcionais-v1.0.md](03-Requisitos/Requisitos-Funcionais-v1.0.md)
- [03-Requisitos/Requisitos-Nao-Funcionais-v1.0.md](03-Requisitos/Requisitos-Nao-Funcionais-v1.0.md)

### 04-Modelo-de-Dados

- [04-Modelo-de-Dados/Cadastro-Unico.md](04-Modelo-de-Dados/Cadastro-Unico.md)
- [04-Modelo-de-Dados/Dicionario-de-dados.md](04-Modelo-de-Dados/Dicionario-de-dados.md)
- [04-Modelo-de-Dados/MER.md](04-Modelo-de-Dados/MER.md)
- [04-Modelo-de-Dados/Modelo-Conceitual.md](04-Modelo-de-Dados/Modelo-Conceitual.md)
- [04-Modelo-de-Dados/Modelo-Fisico.md](04-Modelo-de-Dados/Modelo-Fisico.md)
- [04-Modelo-de-Dados/Modelo-Logico.md](04-Modelo-de-Dados/Modelo-Logico.md)
- [04-Modelo-de-Dados/Modelos-SQL.md](04-Modelo-de-Dados/Modelos-SQL.md)
- [04-Modelo-de-Dados/Procedures.md](04-Modelo-de-Dados/Procedures.md)
- [04-Modelo-de-Dados/Seeds.md](04-Modelo-de-Dados/Seeds.md)
- [04-Modelo-de-Dados/Views.md](04-Modelo-de-Dados/Views.md)

### 05-Modulos

- [05-Modulos/modelo/APIs.md](05-Modulos/modelo/APIs.md)
- [05-Modulos/modelo/Banco-de-dados.md](05-Modulos/modelo/Banco-de-dados.md)
- [05-Modulos/modelo/Casos-de-Uso.md](05-Modulos/modelo/Casos-de-Uso.md)
- [05-Modulos/modelo/Documentacao.md](05-Modulos/modelo/Documentacao.md)
- [05-Modulos/modelo/Modelo-de-Negocio.md](05-Modulos/modelo/Modelo-de-Negocio.md)
- [05-Modulos/modelo/README.md](05-Modulos/modelo/README.md)
- [05-Modulos/modelo/Requisitos.md](05-Modulos/modelo/Requisitos.md)
- [05-Modulos/modelo/Testes.md](05-Modulos/modelo/Testes.md)
- [05-Modulos/modelo/UX.md](05-Modulos/modelo/UX.md)

### 06-Integracoes

- [06-Integracoes/APIs.md](06-Integracoes/APIs.md)
- [06-Integracoes/Bancos.md](06-Integracoes/Bancos.md)
- [06-Integracoes/Correios.md](06-Integracoes/Correios.md)
- [06-Integracoes/ESUS.md](06-Integracoes/ESUS.md)
- [06-Integracoes/GovBR.md](06-Integracoes/GovBR.md)
- [06-Integracoes/Receita.md](06-Integracoes/Receita.md)
- [06-Integracoes/SIASUS.md](06-Integracoes/SIASUS.md)
- [06-Integracoes/TCM-BA.md](06-Integracoes/TCM-BA.md)
- [06-Integracoes/eSocial.md](06-Integracoes/eSocial.md)

### 07-LGPD-e-Seguranca

- [07-LGPD-e-Seguranca/Auditoria.md](07-LGPD-e-Seguranca/Auditoria.md)
- [07-LGPD-e-Seguranca/Backup.md](07-LGPD-e-Seguranca/Backup.md)
- [07-LGPD-e-Seguranca/Classificacao.md](07-LGPD-e-Seguranca/Classificacao.md)
- [07-LGPD-e-Seguranca/Continuidade.md](07-LGPD-e-Seguranca/Continuidade.md)
- [07-LGPD-e-Seguranca/Criptografia.md](07-LGPD-e-Seguranca/Criptografia.md)
- [07-LGPD-e-Seguranca/Incidentes.md](07-LGPD-e-Seguranca/Incidentes.md)
- [07-LGPD-e-Seguranca/LGPD.md](07-LGPD-e-Seguranca/LGPD.md)
- [07-LGPD-e-Seguranca/Logs.md](07-LGPD-e-Seguranca/Logs.md)

### 08-Migracao

- [08-Migracao/ETL.md](08-Migracao/ETL.md)
- [08-Migracao/Firebird.md](08-Migracao/Firebird.md)
- [08-Migracao/Qualidade.md](08-Migracao/Qualidade.md)
- [08-Migracao/SQLServer.md](08-Migracao/SQLServer.md)
- [08-Migracao/Validacao.md](08-Migracao/Validacao.md)

### 09-UX

- [09-UX/Acessibilidade.md](09-UX/Acessibilidade.md)
- [09-UX/Componentes.md](09-UX/Componentes.md)
- [09-UX/DesignSystem.md](09-UX/DesignSystem.md)
- [09-UX/Prototipos.md](09-UX/Prototipos.md)
- [09-UX/Wireframes.md](09-UX/Wireframes.md)

### 10-Testes

- [10-Testes/Homologacao.md](10-Testes/Homologacao.md)
- [10-Testes/Integracao.md](10-Testes/Integracao.md)
- [10-Testes/Performance.md](10-Testes/Performance.md)
- [10-Testes/Seguranca.md](10-Testes/Seguranca.md)
- [10-Testes/Unitarios.md](10-Testes/Unitarios.md)

### 11-Implantacao

- [11-Implantacao/Ambientes.md](11-Implantacao/Ambientes.md)
- [11-Implantacao/CI-CD.md](11-Implantacao/CI-CD.md)
- [11-Implantacao/Docker.md](11-Implantacao/Docker.md)
- [11-Implantacao/Kubernets.md](11-Implantacao/Kubernets.md)
- [11-Implantacao/Operacao.md](11-Implantacao/Operacao.md)

### 96-Sustentabilidade

- [96-Sustentabilidade/000-Modelo-de-Sustentabilidade-do-Ecossistema-SIGMUN.md](96-Sustentabilidade/000-Modelo-de-Sustentabilidade-do-Ecossistema-SIGMUN.md)
- [96-Sustentabilidade/001-Plano-de-Captacao-de-Recursos.md](96-Sustentabilidade/001-Plano-de-Captacao-de-Recursos.md)
- [96-Sustentabilidade/002-Programa-Nacional-de-Colaboradores.md](96-Sustentabilidade/002-Programa-Nacional-de-Colaboradores.md)
- [96-Sustentabilidade/003-Modelo-de-Bolsas-e-Incentivos.md](96-Sustentabilidade/003-Modelo-de-Bolsas-e-Incentivos.md)
- [96-Sustentabilidade/004-Programa-de-Municipios-Mantenedores.md](96-Sustentabilidade/004-Programa-de-Municipios-Mantenedores.md)
- [96-Sustentabilidade/005-Modelo-de-Certificacao-e-Servicos.md](96-Sustentabilidade/005-Modelo-de-Certificacao-e-Servicos.md)
- [96-Sustentabilidade/006-Plano-de-Marketing-Institucional.md](96-Sustentabilidade/006-Plano-de-Marketing-Institucional.md)
- [96-Sustentabilidade/007-Modelo-de-Governanca-do-Instituto-SIGMUN.md](96-Sustentabilidade/007-Modelo-de-Governanca-do-Instituto-SIGMUN.md)

### 97-Estudos-e-Pesquisas

- [97-Estudos-e-Pesquisas/001-Estudo-Nacional-da-Transformacao-Digital-dos-Municipios-Brasileiros.md](97-Estudos-e-Pesquisas/001-Estudo-Nacional-da-Transformacao-Digital-dos-Municipios-Brasileiros.md)
- [97-Estudos-e-Pesquisas/002-Metodologia-de-Coleta-de-Dados.md](97-Estudos-e-Pesquisas/002-Metodologia-de-Coleta-de-Dados.md)
- [97-Estudos-e-Pesquisas/003-Dicionario-de-Dados-da-Pesquisa.md](97-Estudos-e-Pesquisas/003-Dicionario-de-Dados-da-Pesquisa.md)
- [97-Estudos-e-Pesquisas/004-Plano-de-Coleta-Nacional.md](97-Estudos-e-Pesquisas/004-Plano-de-Coleta-Nacional.md)
- [97-Estudos-e-Pesquisas/005-Modelo-de-Questionario.md](97-Estudos-e-Pesquisas/005-Modelo-de-Questionario.md)
- [97-Estudos-e-Pesquisas/006-Metodologia-de-Indicadores.md](97-Estudos-e-Pesquisas/006-Metodologia-de-Indicadores.md)
- [97-Estudos-e-Pesquisas/007-Framework-Nacional-de-Avaliacao-da-Maturidade-Digital-Municipal.md](97-Estudos-e-Pesquisas/007-Framework-Nacional-de-Avaliacao-da-Maturidade-Digital-Municipal.md)
- [97-Estudos-e-Pesquisas/008-Metodologia-do-INMDM.md](97-Estudos-e-Pesquisas/008-Metodologia-do-INMDM.md)
- [97-Estudos-e-Pesquisas/009-Metodologia-do-IGDM.md](97-Estudos-e-Pesquisas/009-Metodologia-do-IGDM.md)
- [97-Estudos-e-Pesquisas/010-Metodologia-do-IDDM.md](97-Estudos-e-Pesquisas/010-Metodologia-do-IDDM.md)
- [97-Estudos-e-Pesquisas/011-Metodologia-do-ISDM.md](97-Estudos-e-Pesquisas/011-Metodologia-do-ISDM.md)
- [97-Estudos-e-Pesquisas/012-Modelo-de-Diagnostico-e-Plano-de-Evolucao.md](97-Estudos-e-Pesquisas/012-Modelo-de-Diagnostico-e-Plano-de-Evolucao.md)
- [97-Estudos-e-Pesquisas/013-Modelo-de-Certificacao-da-Maturidade-Digital-Municipal.md](97-Estudos-e-Pesquisas/013-Modelo-de-Certificacao-da-Maturidade-Digital-Municipal.md)

### 98-Comunidade-SIGMUN

- [98-Comunidade-SIGMUN/Codigo-de-Conduta.md](98-Comunidade-SIGMUN/Codigo-de-Conduta.md)
- [98-Comunidade-SIGMUN/Criar-documentos-da-comunidade.md](98-Comunidade-SIGMUN/Criar-documentos-da-comunidade.md)
- [98-Comunidade-SIGMUN/FAQ-SIGMUN.md](98-Comunidade-SIGMUN/FAQ-SIGMUN.md)
- [98-Comunidade-SIGMUN/Kit-de-Comunicacao-SIGMUN.md](98-Comunidade-SIGMUN/Kit-de-Comunicacao-SIGMUN.md)
- [98-Comunidade-SIGMUN/Modelo-de-Governanca-da-Comunidade.md](98-Comunidade-SIGMUN/Modelo-de-Governanca-da-Comunidade.md)
- [98-Comunidade-SIGMUN/Programa-de-Embaixadores.md](98-Comunidade-SIGMUN/Programa-de-Embaixadores.md)
- [98-Comunidade-SIGMUN/Programa-de-Municipios-Piloto.md](98-Comunidade-SIGMUN/Programa-de-Municipios-Piloto.md)
- [98-Comunidade-SIGMUN/TEMPLATES-DE-EVENTOS-E-WEBINARS.md](98-Comunidade-SIGMUN/TEMPLATES-DE-EVENTOS-E-WEBINARS.md)

### 99-Anexos

- [99-Anexos/Estudos/Estrutura-da-Constituicao-SIGMUN.md](99-Anexos/Estudos/Estrutura-da-Constituicao-SIGMUN.md)

### Documentos da raiz

- [000-CONSTITUICAO-DO-PROJETO-SIGMUN.md](000-CONSTITUICAO-DO-PROJETO-SIGMUN.md)
- [CHANGELOG.md](CHANGELOG.md)
- [DECISOES-ARQUITETURAIS.md](DECISOES-ARQUITETURAIS.md)
- [DIAGNOSTICO-ESTADO-SISTEMA.md](DIAGNOSTICO-ESTADO-SISTEMA.md)
- [Plano-de-Trabalho.md](Plano-de-Trabalho.md)
- [REFERENCIAS.md](REFERENCIAS.md)
- [ROADMAP.md](ROADMAP.md)
- [SIGMUN-DEV-AGENT.md](SIGMUN-DEV-AGENT.md)

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-17 | Criação do inventário e navegação; aprovação não presumida | Equipe SIGMUN |
| 1.1 | 2026-09-17 | Regeneração seletiva de Compras conforme ADR-0006; destinos físicos e demais qualificadores preservados | Cline, por autorização do solicitante |
