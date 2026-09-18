# Auditoria documental — 17/09/2026

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Domínio:** Governança documental
**Versão:** 1.0
**Status:** Em elaboração
**Classificação da Informação:** Pública
**Última atualização:** 2026-09-17
**Responsável:** Equipe SIGMUN

| Campo | Conteúdo |
| --- | --- |
| Projeto | SIGMUN |
| Proprietário | Governança documental |
| Responsável | Equipe SIGMUN |
| Versão | 1.0 |
| Status | Em elaboração; validação editorial pendente |
| Classificação | Pública |
| Data de Criação | 17/09/2026 |
| Última Revisão | 17/09/2026 |
| Próxima Revisão | Ao alterar os documentos ou evidências relacionados |
| Aprovado por | Aprovação não registrada |

**Documento(s) Relacionado(s):** [Documentação geral](../index.md) · [Catálogo de módulos](../05-Modulos/index.md) · [Matriz DOM ↔ módulo](../01-Arquitetura-Corporativa/031-Matriz-de-Correspondencia-DOM-MOD.md)

## Escopo e método

Base Git inspecionada: `51c82dc`, com a revisão documental desta auditoria ainda não commitada. Inventário anterior aos novos índices: **1097 arquivos Markdown, 33 diretórios DOM e 28 módulos de código**. A matriz 031 já estava corrigida ao executar a varredura abaixo.

Inspeção estática de arquivos, sintaxe Python (AST), registro de routers, documentação arquitetural e amostras de APIs. Varredura de todos os Markdown para blocos cercados por crases/til, numeração inicial do título, combinação exata de status com texto-padrão e destinos de links inline fora desses blocos.

**Limites:** não houve leitura semântica integral dos 1.097 documentos, testes funcionais, aplicação de migrações, homologação, requisições externas ou validação de segurança. Links por referência, HTML, âncoras e citações em texto simples não são integralmente cobertos pela varredura de links. Ausência de erro no link não significa correção do conteúdo. Blocos aninhados em listas e exemplos podem exigir revisão manual.

## Síntese e prioridade

| Achado | Prioridade | Estado / encaminhamento |
| --- | --- | --- |
| AUD-001 — 031 com bloco aberto e tabelas em texto | Alta | Corrigido; títulos, tabelas e links locais verificados |
| AUD-002 — maturidade técnica misturada com correspondência | Alta | Corrigido na 031: 8 com implementação identificada, 20 preparados; 8 correspondências confirmadas, 8 candidatas, 12 não determinadas |
| AUD-003 — dependências inferidas de comentários | Alta | Corrigido na 031: INT/SEG é adoção de padrão; Cadastro/IDN descreve mecanismo provisório, não integração concluída |
| AUD-004 — códigos divergentes para Compras | Alta | Pendente: decidir identidade canônica e compatibilidade histórica; não renomear por inferência |
| AUD-005 — hierarquias 000A/000C distintas | Alta | Pendente: explicitar equivalência/precedência; índices não redefinem autoridade |
| AUD-006 — numeração arquivo/título divergente | Média | 30 ocorrências listadas; confirmar política antes de renumerar |
| AUD-007 — Vigente com texto-padrão de elaboração | Média | 72 ocorrências listadas; revisar conteúdo e aprovação, não mudar status em massa |
| AUD-008 — blocos sem fechamento reconhecido | Média | 22 ocorrências para revisão contextual |
| AUD-009 — catálogo técnico incompleto | Média | README de código lista 21 de 28 módulos; mantém scaffolding como disponível sem qualificação |
| AUD-010 — ausência de índices | Média | Tratada com 1 índice geral, 33 de domínio, 28 de módulo e 1 catálogo de módulos |

Nenhum destino inexistente foi encontrado nos links inline locais reconhecidos na documentação SIGMUN-Docs após a correção da matriz. Isso **não** cobre as referências nominais antigas, nem os links do README de código descritos abaixo.

## Evidências dos achados transversais

- [02-Modelo-de-Negocio/Mapa-de-Dominios.md](../02-Modelo-de-Negocio/Mapa-de-Dominios.md): Seção 12 e resumo usam DOM-COM; referências citam arquiteturas com numeração antiga.
- [DOM-COMPRAS-001/000-Dominio-Gestao-de-Compras-e-Contratacoes.md](../DOM-COMPRAS-001/000-Dominio-Gestao-de-Compras-e-Contratacoes.md): Cadeia de rastreabilidade usa DOM-COMPRAS; diretório e código usam DOM-COMPRAS-001. Equivalência oficial pendente.
- [00-Governanca/000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md](000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md): Seção 4 define níveis 1–12, com Constituição no nível 1.
- [00-Governanca/000C-HIERARQUIA-DOCUMENTAL-v1.0.md](000C-HIERARQUIA-DOCUMENTAL-v1.0.md): Seção 3 define níveis 0–12, com Constituição no nível 0; não explicita equivalência com a escala do 000A.
- [05-Modulos/modelo/README.md](../05-Modulos/modelo/README.md): Modelo ainda contém texto-padrão; não foi usado como evidência de módulo implementado.
- [README do código](../../src/README.md): seção “Módulos Disponíveis” omite cadastro, dad, gdo, idn, int, met e seg; os três links SIGMUN-Docs são relativos a src, onde esse diretório não existe. Fora do escopo de edição desta entrega.

## AUD-008 — blocos a revisar

| Documento | Linha | Evidência |
| --- | --- | --- |
| [01-Arquitetura-Corporativa/030-Roadmap-de-Implementacao-dos-Dominios.md](../01-Arquitetura-Corporativa/030-Roadmap-de-Implementacao-dos-Dominios.md) | 614 | Bloco de código sem fechamento reconhecido |
| [98-Comunidade-SIGMUN/Codigo-de-Conduta.md](../98-Comunidade-SIGMUN/Codigo-de-Conduta.md) | 250 | Bloco de código sem fechamento reconhecido |
| [98-Comunidade-SIGMUN/FAQ-SIGMUN.md](../98-Comunidade-SIGMUN/FAQ-SIGMUN.md) | 486 | Bloco de código sem fechamento reconhecido |
| [98-Comunidade-SIGMUN/Kit-de-Comunicacao-SIGMUN.md](../98-Comunidade-SIGMUN/Kit-de-Comunicacao-SIGMUN.md) | 210 | Bloco de código sem fechamento reconhecido |
| [98-Comunidade-SIGMUN/Modelo-de-Governanca-da-Comunidade.md](../98-Comunidade-SIGMUN/Modelo-de-Governanca-da-Comunidade.md) | 123 | Bloco de código sem fechamento reconhecido |
| [98-Comunidade-SIGMUN/Programa-de-Embaixadores.md](../98-Comunidade-SIGMUN/Programa-de-Embaixadores.md) | 203 | Bloco de código sem fechamento reconhecido |
| [98-Comunidade-SIGMUN/Programa-de-Municipios-Piloto.md](../98-Comunidade-SIGMUN/Programa-de-Municipios-Piloto.md) | 172 | Bloco de código sem fechamento reconhecido |
| [98-Comunidade-SIGMUN/TEMPLATES-DE-EVENTOS-E-WEBINARS.md](../98-Comunidade-SIGMUN/TEMPLATES-DE-EVENTOS-E-WEBINARS.md) | 136 | Bloco de código sem fechamento reconhecido |
| [DOM-COMPRAS-001/012-Matriz-de-Rastreabilidade-Gestao-de-Compras-e-Contratacoes.md](../DOM-COMPRAS-001/012-Matriz-de-Rastreabilidade-Gestao-de-Compras-e-Contratacoes.md) | 57 | Bloco de código sem fechamento reconhecido |
| [DOM-COMPRAS-001/015-Arquitetura-de-Servicos-Gestao-de-Compras-e-Contratacoes.md](../DOM-COMPRAS-001/015-Arquitetura-de-Servicos-Gestao-de-Compras-e-Contratacoes.md) | 143 | Bloco de código sem fechamento reconhecido |
| [DOM-COMPRAS-001/016-Modelo-de-Seguranca-Gestao-de-Compras-e-Contratacoes.md](../DOM-COMPRAS-001/016-Modelo-de-Seguranca-Gestao-de-Compras-e-Contratacoes.md) | 108 | Bloco de código sem fechamento reconhecido |
| [DOM-COMPRAS-001/017-Modelo-de-Auditoria-Gestao-de-Compras-e-Contratacoes.md](../DOM-COMPRAS-001/017-Modelo-de-Auditoria-Gestao-de-Compras-e-Contratacoes.md) | 65 | Bloco de código sem fechamento reconhecido |
| [DOM-COMPRAS-001/019-Casos-de-Teste-Gestao-de-Compras-e-Contratacoes.md](../DOM-COMPRAS-001/019-Casos-de-Teste-Gestao-de-Compras-e-Contratacoes.md) | 84 | Bloco de código sem fechamento reconhecido |
| [DOM-COMPRAS-001/020-Plano-de-Implantacao-Gestao-de-Compras-e-Contratacoes.md](../DOM-COMPRAS-001/020-Plano-de-Implantacao-Gestao-de-Compras-e-Contratacoes.md) | 151 | Bloco de código sem fechamento reconhecido |
| [DOM-COMPRAS-001/021-Checklist-de-Prontidao-para-Producao-Gestao-de-Compras-e-Contratacoes.md](../DOM-COMPRAS-001/021-Checklist-de-Prontidao-para-Producao-Gestao-de-Compras-e-Contratacoes.md) | 83 | Bloco de código sem fechamento reconhecido |
| [DOM-COMPRAS-001/022-Plano-de-Migracao-de-Dados-Gestao-de-Compras-e-Contratacoes.md](../DOM-COMPRAS-001/022-Plano-de-Migracao-de-Dados-Gestao-de-Compras-e-Contratacoes.md) | 153 | Bloco de código sem fechamento reconhecido |
| [DOM-COMPRAS-001/023-Plano-de-Treinamento-Gestao-de-Compras-e-Contratacoes.md](../DOM-COMPRAS-001/023-Plano-de-Treinamento-Gestao-de-Compras-e-Contratacoes.md) | 245 | Bloco de código sem fechamento reconhecido |
| [DOM-COMPRAS-001/024-Plano-de-Suporte-e-Operacao-Gestao-de-Compras-e-Contratacoes.md](../DOM-COMPRAS-001/024-Plano-de-Suporte-e-Operacao-Gestao-de-Compras-e-Contratacoes.md) | 112 | Bloco de código sem fechamento reconhecido |
| [DOM-COMPRAS-001/025-Estrutura-Tecnica-Gestao-de-Compras-e-Contratacoes.md](../DOM-COMPRAS-001/025-Estrutura-Tecnica-Gestao-de-Compras-e-Contratacoes.md) | 104 | Bloco de código sem fechamento reconhecido |
| [DOM-COMPRAS-001/026-Modelo-de-Dominio-Gestao-de-Compras-e-Contratacoes.md](../DOM-COMPRAS-001/026-Modelo-de-Dominio-Gestao-de-Compras-e-Contratacoes.md) | 47 | Bloco de código sem fechamento reconhecido |
| [ROADMAP.md](../ROADMAP.md) | 715 | Bloco de código sem fechamento reconhecido |
| [SIGMUN-DEV-AGENT.md](../SIGMUN-DEV-AGENT.md) | 142 | Bloco de código sem fechamento reconhecido |

## AUD-006 — numeração divergente

| Documento | Linha | Evidência |
| --- | --- | --- |
| [00-Governanca/00.1-Estrutura-de-Governanca/004-Modelo-de-Governanca.md](00.1-Estrutura-de-Governanca/004-Modelo-de-Governanca.md) | 1 | Arquivo 004; título 007 |
| [00-Governanca/00.1-Estrutura-de-Governanca/007-Gestao-de-Riscos.md](00.1-Estrutura-de-Governanca/007-Gestao-de-Riscos.md) | 1 | Arquivo 007; título 025 |
| [00-Governanca/00.1-Estrutura-de-Governanca/008-Gestao-do-Portfolio.md](00.1-Estrutura-de-Governanca/008-Gestao-do-Portfolio.md) | 1 | Arquivo 008; título 024 |
| [00-Governanca/00.4-Governanca-Institucional/017-Plano-de-Continuidade-de-Negocios-e-Recuperacao-de-Desastres.md](00.4-Governanca-Institucional/017-Plano-de-Continuidade-de-Negocios-e-Recuperacao-de-Desastres.md) | 1 | Arquivo 017; título 016 |
| [01-Arquitetura-Corporativa/001-Principios-de-Arquitetura.md](../01-Arquitetura-Corporativa/001-Principios-de-Arquitetura.md) | 1 | Arquivo 001; título 004 |
| [01-Arquitetura-Corporativa/002-Arquitetura-de-Negocio.md](../01-Arquitetura-Corporativa/002-Arquitetura-de-Negocio.md) | 1 | Arquivo 002; título 003 |
| [01-Arquitetura-Corporativa/003-Cadastro-Unico-Municipal.md](../01-Arquitetura-Corporativa/003-Cadastro-Unico-Municipal.md) | 1 | Arquivo 003; título 006 |
| [01-Arquitetura-Corporativa/004-Arquitetura-de-Software.md](../01-Arquitetura-Corporativa/004-Arquitetura-de-Software.md) | 1 | Arquivo 004; título 008 |
| [01-Arquitetura-Corporativa/005-Arquitetura-de-Dados.md](../01-Arquitetura-Corporativa/005-Arquitetura-de-Dados.md) | 1 | Arquivo 005; título 009 |
| [01-Arquitetura-Corporativa/006-Arquitetura-de-Integracao.md](../01-Arquitetura-Corporativa/006-Arquitetura-de-Integracao.md) | 1 | Arquivo 006; título 010 |
| [01-Arquitetura-Corporativa/007-Arquitetura-de-Seguranca.md](../01-Arquitetura-Corporativa/007-Arquitetura-de-Seguranca.md) | 1 | Arquivo 007; título 011 |
| [01-Arquitetura-Corporativa/008-Arquitetura-de-Implantacao-e-Infraestrutura.md](../01-Arquitetura-Corporativa/008-Arquitetura-de-Implantacao-e-Infraestrutura.md) | 1 | Arquivo 008; título 012 |
| [01-Arquitetura-Corporativa/009-Arquitetura-de-Experiencia-do-Usuario-e-Acessibilidade.md](../01-Arquitetura-Corporativa/009-Arquitetura-de-Experiencia-do-Usuario-e-Acessibilidade.md) | 1 | Arquivo 009; título 013 |
| [01-Arquitetura-Corporativa/010-Arquitetura-de-Processos-e-Workflow.md](../01-Arquitetura-Corporativa/010-Arquitetura-de-Processos-e-Workflow.md) | 1 | Arquivo 010; título 014 |
| [01-Arquitetura-Corporativa/011-Arquitetura-de-Relatorios-Indicadores-e-BI.md](../01-Arquitetura-Corporativa/011-Arquitetura-de-Relatorios-Indicadores-e-BI.md) | 1 | Arquivo 011; título 015 |
| [01-Arquitetura-Corporativa/012-Arquitetura-de-Gestao-Documental-e-Arquivistica.md](../01-Arquitetura-Corporativa/012-Arquitetura-de-Gestao-Documental-e-Arquivistica.md) | 1 | Arquivo 012; título 016 |
| [01-Arquitetura-Corporativa/013-Arquitetura-de-Identidade-e-Acessos.md](../01-Arquitetura-Corporativa/013-Arquitetura-de-Identidade-e-Acessos.md) | 1 | Arquivo 013; título 017 |
| [01-Arquitetura-Corporativa/014-Arquitetura-de-Notificacoes-e-Comunicacao.md](../01-Arquitetura-Corporativa/014-Arquitetura-de-Notificacoes-e-Comunicacao.md) | 1 | Arquivo 014; título 018 |
| [01-Arquitetura-Corporativa/015-Arquitetura-de-Dispositivos-Moveis-e-Servicos-de-Campo.md](../01-Arquitetura-Corporativa/015-Arquitetura-de-Dispositivos-Moveis-e-Servicos-de-Campo.md) | 1 | Arquivo 015; título 019 |
| [01-Arquitetura-Corporativa/016-Arquitetura-de-Observabilidade-e-Operacoes-DevSecOps.md](../01-Arquitetura-Corporativa/016-Arquitetura-de-Observabilidade-e-Operacoes-DevSecOps.md) | 1 | Arquivo 016; título 020 |
| [01-Arquitetura-Corporativa/019-Arquitetura-de-Gestao-de-Configuracao-e-versionamento.md](../01-Arquitetura-Corporativa/019-Arquitetura-de-Gestao-de-Configuracao-e-versionamento.md) | 1 | Arquivo 019; título 027 |
| [01-Arquitetura-Corporativa/020-Arquitetura-de-Gestao-do-Ciclo-de-Vida.md](../01-Arquitetura-Corporativa/020-Arquitetura-de-Gestao-do-Ciclo-de-Vida.md) | 1 | Arquivo 020; título 028 |
| [01-Arquitetura-Corporativa/021-Arquitetura-de-Continuidade-e-Evolucao-Tecnologica.md](../01-Arquitetura-Corporativa/021-Arquitetura-de-Continuidade-e-Evolucao-Tecnologica.md) | 1 | Arquivo 021; título 029 |
| [01-Arquitetura-Corporativa/022-Arquitetura-de-Gestao-da-Qualidade-Corporativa.md](../01-Arquitetura-Corporativa/022-Arquitetura-de-Gestao-da-Qualidade-Corporativa.md) | 1 | Arquivo 022; título 030 |
| [01-Arquitetura-Corporativa/023-Arquitetura-de-Gestao-da-Inovacao-e-Transformacao-Digital.md](../01-Arquitetura-Corporativa/023-Arquitetura-de-Gestao-da-Inovacao-e-Transformacao-Digital.md) | 1 | Arquivo 023; título 031 |
| [01-Arquitetura-Corporativa/024-Arquitetura-de-Gestao-do-Conhecimento-e-Aprendizagem-Organizacional.md](../01-Arquitetura-Corporativa/024-Arquitetura-de-Gestao-do-Conhecimento-e-Aprendizagem-Organizacional.md) | 1 | Arquivo 024; título 032 |
| [01-Arquitetura-Corporativa/025-Arquitetura-de-Gestao-de-Competencias-e-Desenvolvimento-de-Pessoas.md](../01-Arquitetura-Corporativa/025-Arquitetura-de-Gestao-de-Competencias-e-Desenvolvimento-de-Pessoas.md) | 1 | Arquivo 025; título 033 |
| [01-Arquitetura-Corporativa/026-Arquitetura-de-Gestao-da-Mudanca-Organizacional.md](../01-Arquitetura-Corporativa/026-Arquitetura-de-Gestao-da-Mudanca-Organizacional.md) | 1 | Arquivo 026; título 034 |
| [01-Arquitetura-Corporativa/027-Arquitetura-de-Excelencia-Operacional-e-Melhoria-Continua.md](../01-Arquitetura-Corporativa/027-Arquitetura-de-Excelencia-Operacional-e-Melhoria-Continua.md) | 1 | Arquivo 027; título 035 |
| [01-Arquitetura-Corporativa/028-Arquitetura-de-Gestao-da-Sustentabilidade-e-Responsabilidade-Socioambiental.md](../01-Arquitetura-Corporativa/028-Arquitetura-de-Gestao-da-Sustentabilidade-e-Responsabilidade-Socioambiental.md) | 1 | Arquivo 028; título 036 |

## AUD-007 — status e texto de elaboração

| Documento | Linha | Evidência |
| --- | --- | --- |
| [00-Governanca/00.5-Politicas-Corporativas/019-Politica-de-Governanca-Digital.md](00.5-Politicas-Corporativas/019-Politica-de-Governanca-Digital.md) | 33 | Vigente + texto-padrão de elaboração |
| [00-Governanca/00.5-Politicas-Corporativas/020-Politica-de-Qualidade.md](00.5-Politicas-Corporativas/020-Politica-de-Qualidade.md) | 33 | Vigente + texto-padrão de elaboração |
| [00-Governanca/00.5-Politicas-Corporativas/021-Politica-de-Seguranca.md](00.5-Politicas-Corporativas/021-Politica-de-Seguranca.md) | 33 | Vigente + texto-padrão de elaboração |
| [00-Governanca/00.5-Politicas-Corporativas/022-Politica-de-Gestao-Documental.md](00.5-Politicas-Corporativas/022-Politica-de-Gestao-Documental.md) | 33 | Vigente + texto-padrão de elaboração |
| [00-Governanca/00.5-Politicas-Corporativas/023-Politica-de-Retencao-e-Descarte-de-Documentos.md](00.5-Politicas-Corporativas/023-Politica-de-Retencao-e-Descarte-de-Documentos.md) | 33 | Vigente + texto-padrão de elaboração |
| [00-Governanca/00.5-Politicas-Corporativas/024-Politica-de-Gestao-de-Riscos.md](00.5-Politicas-Corporativas/024-Politica-de-Gestao-de-Riscos.md) | 33 | Vigente + texto-padrão de elaboração |
| [00-Governanca/00.5-Politicas-Corporativas/025-Politica-de-Protecao-de-Dados-Pessoais.md](00.5-Politicas-Corporativas/025-Politica-de-Protecao-de-Dados-Pessoais.md) | 33 | Vigente + texto-padrão de elaboração |
| [00-Governanca/00.5-Politicas-Corporativas/026-Manual-de-Governanca-do-SIGMUN.md](00.5-Politicas-Corporativas/026-Manual-de-Governanca-do-SIGMUN.md) | 33 | Vigente + texto-padrão de elaboração |
| [00-Governanca/000D-MODELO-DE-DOCUMENTO.md](000D-MODELO-DE-DOCUMENTO.md) | 33 | Vigente + texto-padrão de elaboração |
| [00-Governanca/ADR/ADR-0001-Arquitetura-Modular.md](ADR/ADR-0001-Arquitetura-Modular.md) | 33 | Vigente + texto-padrão de elaboração |
| [00-Governanca/ADR/ADR-0002-Offline-First.md](ADR/ADR-0002-Offline-First.md) | 33 | Vigente + texto-padrão de elaboração |
| [00-Governanca/ADR/ADR-0003-APIs-REST.md](ADR/ADR-0003-APIs-REST.md) | 33 | Vigente + texto-padrão de elaboração |
| [00-Governanca/ADR/ADR-0004-Neutralidade-Tecnologica.md](ADR/ADR-0004-Neutralidade-Tecnologica.md) | 33 | Vigente + texto-padrão de elaboração |
| [00-Governanca/ADR/ADR-0005-Cadastro-Unico-Municipal.md](ADR/ADR-0005-Cadastro-Unico-Municipal.md) | 33 | Vigente + texto-padrão de elaboração |
| [00-Governanca/ADR/ADR-INDEX.md](ADR/ADR-INDEX.md) | 33 | Vigente + texto-padrão de elaboração |
| [00-Governanca/ADR/README.md](ADR/README.md) | 33 | Vigente + texto-padrão de elaboração |
| [00-Governanca/ADR/templates/ADR-TEMPLATE.md](ADR/templates/ADR-TEMPLATE.md) | 33 | Vigente + texto-padrão de elaboração |
| [04-Modelo-de-Dados/Cadastro-Unico.md](../04-Modelo-de-Dados/Cadastro-Unico.md) | 33 | Vigente + texto-padrão de elaboração |
| [04-Modelo-de-Dados/MER.md](../04-Modelo-de-Dados/MER.md) | 25 | Vigente + texto-padrão de elaboração |
| [04-Modelo-de-Dados/Modelos-SQL.md](../04-Modelo-de-Dados/Modelos-SQL.md) | 33 | Vigente + texto-padrão de elaboração |
| [04-Modelo-de-Dados/Procedures.md](../04-Modelo-de-Dados/Procedures.md) | 33 | Vigente + texto-padrão de elaboração |
| [04-Modelo-de-Dados/Seeds.md](../04-Modelo-de-Dados/Seeds.md) | 33 | Vigente + texto-padrão de elaboração |
| [04-Modelo-de-Dados/Views.md](../04-Modelo-de-Dados/Views.md) | 33 | Vigente + texto-padrão de elaboração |
| [05-Modulos/modelo/APIs.md](../05-Modulos/modelo/APIs.md) | 33 | Vigente + texto-padrão de elaboração |
| [05-Modulos/modelo/Banco-de-dados.md](../05-Modulos/modelo/Banco-de-dados.md) | 33 | Vigente + texto-padrão de elaboração |
| [05-Modulos/modelo/Casos-de-Uso.md](../05-Modulos/modelo/Casos-de-Uso.md) | 33 | Vigente + texto-padrão de elaboração |
| [05-Modulos/modelo/Documentacao.md](../05-Modulos/modelo/Documentacao.md) | 33 | Vigente + texto-padrão de elaboração |
| [05-Modulos/modelo/Modelo-de-Negocio.md](../05-Modulos/modelo/Modelo-de-Negocio.md) | 33 | Vigente + texto-padrão de elaboração |
| [05-Modulos/modelo/README.md](../05-Modulos/modelo/README.md) | 33 | Vigente + texto-padrão de elaboração |
| [05-Modulos/modelo/Requisitos.md](../05-Modulos/modelo/Requisitos.md) | 33 | Vigente + texto-padrão de elaboração |
| [05-Modulos/modelo/Testes.md](../05-Modulos/modelo/Testes.md) | 33 | Vigente + texto-padrão de elaboração |
| [05-Modulos/modelo/UX.md](../05-Modulos/modelo/UX.md) | 33 | Vigente + texto-padrão de elaboração |
| [06-Integracoes/APIs.md](../06-Integracoes/APIs.md) | 33 | Vigente + texto-padrão de elaboração |
| [06-Integracoes/Bancos.md](../06-Integracoes/Bancos.md) | 33 | Vigente + texto-padrão de elaboração |
| [06-Integracoes/Correios.md](../06-Integracoes/Correios.md) | 33 | Vigente + texto-padrão de elaboração |
| [06-Integracoes/ESUS.md](../06-Integracoes/ESUS.md) | 33 | Vigente + texto-padrão de elaboração |
| [06-Integracoes/GovBR.md](../06-Integracoes/GovBR.md) | 33 | Vigente + texto-padrão de elaboração |
| [06-Integracoes/Receita.md](../06-Integracoes/Receita.md) | 33 | Vigente + texto-padrão de elaboração |
| [06-Integracoes/SIASUS.md](../06-Integracoes/SIASUS.md) | 33 | Vigente + texto-padrão de elaboração |
| [06-Integracoes/TCM-BA.md](../06-Integracoes/TCM-BA.md) | 33 | Vigente + texto-padrão de elaboração |
| [06-Integracoes/eSocial.md](../06-Integracoes/eSocial.md) | 33 | Vigente + texto-padrão de elaboração |
| [07-LGPD-e-Seguranca/Auditoria.md](../07-LGPD-e-Seguranca/Auditoria.md) | 33 | Vigente + texto-padrão de elaboração |
| [07-LGPD-e-Seguranca/Backup.md](../07-LGPD-e-Seguranca/Backup.md) | 33 | Vigente + texto-padrão de elaboração |
| [07-LGPD-e-Seguranca/Classificacao.md](../07-LGPD-e-Seguranca/Classificacao.md) | 33 | Vigente + texto-padrão de elaboração |
| [07-LGPD-e-Seguranca/Continuidade.md](../07-LGPD-e-Seguranca/Continuidade.md) | 33 | Vigente + texto-padrão de elaboração |
| [07-LGPD-e-Seguranca/Criptografia.md](../07-LGPD-e-Seguranca/Criptografia.md) | 33 | Vigente + texto-padrão de elaboração |
| [07-LGPD-e-Seguranca/Incidentes.md](../07-LGPD-e-Seguranca/Incidentes.md) | 33 | Vigente + texto-padrão de elaboração |
| [07-LGPD-e-Seguranca/LGPD.md](../07-LGPD-e-Seguranca/LGPD.md) | 33 | Vigente + texto-padrão de elaboração |
| [07-LGPD-e-Seguranca/Logs.md](../07-LGPD-e-Seguranca/Logs.md) | 33 | Vigente + texto-padrão de elaboração |
| [08-Migracao/ETL.md](../08-Migracao/ETL.md) | 33 | Vigente + texto-padrão de elaboração |
| [08-Migracao/Firebird.md](../08-Migracao/Firebird.md) | 33 | Vigente + texto-padrão de elaboração |
| [08-Migracao/Qualidade.md](../08-Migracao/Qualidade.md) | 33 | Vigente + texto-padrão de elaboração |
| [08-Migracao/SQLServer.md](../08-Migracao/SQLServer.md) | 33 | Vigente + texto-padrão de elaboração |
| [08-Migracao/Validacao.md](../08-Migracao/Validacao.md) | 33 | Vigente + texto-padrão de elaboração |
| [09-UX/Acessibilidade.md](../09-UX/Acessibilidade.md) | 33 | Vigente + texto-padrão de elaboração |
| [09-UX/Componentes.md](../09-UX/Componentes.md) | 33 | Vigente + texto-padrão de elaboração |
| [09-UX/DesignSystem.md](../09-UX/DesignSystem.md) | 33 | Vigente + texto-padrão de elaboração |
| [09-UX/Prototipos.md](../09-UX/Prototipos.md) | 33 | Vigente + texto-padrão de elaboração |
| [09-UX/Wireframes.md](../09-UX/Wireframes.md) | 33 | Vigente + texto-padrão de elaboração |
| [10-Testes/Homologacao.md](../10-Testes/Homologacao.md) | 33 | Vigente + texto-padrão de elaboração |
| [10-Testes/Integracao.md](../10-Testes/Integracao.md) | 33 | Vigente + texto-padrão de elaboração |
| [10-Testes/Performance.md](../10-Testes/Performance.md) | 33 | Vigente + texto-padrão de elaboração |
| [10-Testes/Seguranca.md](../10-Testes/Seguranca.md) | 33 | Vigente + texto-padrão de elaboração |
| [10-Testes/Unitarios.md](../10-Testes/Unitarios.md) | 33 | Vigente + texto-padrão de elaboração |
| [11-Implantacao/Ambientes.md](../11-Implantacao/Ambientes.md) | 33 | Vigente + texto-padrão de elaboração |
| [11-Implantacao/CI-CD.md](../11-Implantacao/CI-CD.md) | 33 | Vigente + texto-padrão de elaboração |
| [11-Implantacao/Docker.md](../11-Implantacao/Docker.md) | 33 | Vigente + texto-padrão de elaboração |
| [11-Implantacao/Kubernets.md](../11-Implantacao/Kubernets.md) | 33 | Vigente + texto-padrão de elaboração |
| [11-Implantacao/Operacao.md](../11-Implantacao/Operacao.md) | 33 | Vigente + texto-padrão de elaboração |
| [CHANGELOG.md](../CHANGELOG.md) | 33 | Vigente + texto-padrão de elaboração |
| [DECISOES-ARQUITETURAIS.md](../DECISOES-ARQUITETURAIS.md) | 33 | Vigente + texto-padrão de elaboração |
| [REFERENCIAS.md](../REFERENCIAS.md) | 33 | Vigente + texto-padrão de elaboração |

## Pendências e critérios de encerramento

1. Decidir a nomenclatura de Compras e documentar aliases históricos, se aprovados.
2. Alinhar a hierarquia 000A/000C e a numeração corporativa antes de correções em lote.
3. Revisar os 22 blocos sinalizados em contexto; não inserir fechamentos automaticamente no fim dos documentos.
4. Revisar os 72 documentos com texto-padrão e verificar aprovação/conteúdo efetivo.
5. Atualizar o README técnico em mudança documental específica.
6. Auditar semântica e rastreabilidade por domínio, começando pelos oito com implementação identificada e pela fronteira Compras/GDO.

Os 33 domínios possuem documentos numerados 000–026. A presença dessa sequência não comprova conteúdo completo: os índices mostram o status declarado e alertas detectados. Os demais artefatos, inclusive evidências, também foram incluídos na navegação.

## Validação dos artefatos desta entrega

Índices construídos a partir do inventário real, nomes dos domínios extraídos das capas e correspondências extraídas da matriz 031 revisada. Os 28 módulos são confrontados com a AST e os 14 routers do ponto de entrada. Testes são relacionados somente quando seus arquivos mencionam o nome técnico do módulo; isso não representa cobertura integral nem resultado de execução.

Antes da publicação, verificar todos os destinos locais gerados, blocos de código, cobertura dos arquivos Markdown preexistentes e correspondência de cada índice de módulo com sua classificação. Não há certificação de aplicação funcional nesta entrega.

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-17 | Criação do inventário e navegação; aprovação não presumida | Equipe SIGMUN |
