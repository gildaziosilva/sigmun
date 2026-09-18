# Catálogo dos módulos de aplicação

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Domínio:** Módulos de aplicação
**Versão:** 1.1
**Status:** Em elaboração
**Classificação da Informação:** Pública
**Última atualização:** 2026-09-17
**Responsável:** Equipe SIGMUN

| Campo | Conteúdo |
| --- | --- |
| Projeto | SIGMUN |
| Proprietário | Módulos de aplicação |
| Responsável | Equipe SIGMUN |
| Versão | 1.1 |
| Status | Em elaboração; validação editorial pendente |
| Classificação | Pública |
| Data de Criação | 17/09/2026 |
| Última Revisão | 17/09/2026 |
| Próxima Revisão | Ao alterar os documentos ou evidências relacionados |
| Aprovado por | Aprovação não registrada |

**Documento(s) Relacionado(s):** [Documentação geral](../index.md) · [Matriz DOM ↔ módulo](../01-Arquitetura-Corporativa/031-Matriz-de-Correspondencia-DOM-MOD.md) · [Auditoria documental](../00-Governanca/AUDITORIA-DOCUMENTAL-2026-09-17.md)

> Identidade corporativa vigente: **DOM-COM — Compras e Contratações**, conforme [ADR-0006](../00-Governanca/ADR/ADR-0006-Compras-canonicalizacao.md). DOM-COMPRAS é identificação documental histórica; DOM-COMPRAS-001 é identificação histórica do piloto e localização física preservada por compatibilidade. A decisão não aprova códigos MOD nem certifica completude funcional.

## Como interpretar

Este catálogo cobre os 28 diretórios técnicos existentes. São 8 módulos com implementação identificada e 20 preparados. A correspondência é um eixo independente: 8 confirmadas no escopo observado, 8 candidatas e 12 não determinadas. Nenhum código MOD proposto é apresentado como aprovado.

Índices usam o nome técnico `sigmun_*`, sem mover código ou documentos de domínio. O diretório `modelo` é um template, não um 29º módulo.

| Módulo | Domínio | MOD proposto | Maturidade técnica | Correspondência |
| --- | --- | --- | --- | --- |
| [sigmun_administracao](sigmun_administracao/index.md) | Não determinado | Não definido | Preparado | Não determinada |
| [sigmun_agricultura](sigmun_agricultura/index.md) | Não determinado | Não definido | Preparado | Não determinada |
| [sigmun_almoxarifado](sigmun_almoxarifado/index.md) | Não determinado | Não definido | Preparado | Não determinada |
| [sigmun_assistencia_social](sigmun_assistencia_social/index.md) | [DOM-ASS](../DOM-ASS/index.md) | `MOD-ASS` | Preparado | Candidata; validar escopo |
| [sigmun_cadastro](sigmun_cadastro/index.md) | [DOM-CUM](../DOM-CUM/index.md) | `MOD-CUM` | Implementação identificada | Confirmada no escopo observado |
| [sigmun_compras](sigmun_compras/index.md) | [DOM-COM](../DOM-COMPRAS-001/index.md) | `MOD-COMPRAS` | Implementação identificada | Confirmada no escopo observado |
| [sigmun_contabilidade](sigmun_contabilidade/index.md) | Não determinado | Não definido | Preparado | Não determinada |
| [sigmun_controladoria](sigmun_controladoria/index.md) | Não determinado | Não definido | Preparado | Não determinada |
| [sigmun_dad](sigmun_dad/index.md) | [DOM-DAD](../DOM-DAD/index.md) | `MOD-DAD` | Implementação identificada | Confirmada no escopo observado |
| [sigmun_educacao](sigmun_educacao/index.md) | [DOM-EDU](../DOM-EDU/index.md) | `MOD-EDU` | Preparado | Candidata; validar escopo |
| [sigmun_financas](sigmun_financas/index.md) | Não determinado | Não definido | Preparado | Não determinada |
| [sigmun_frotas](sigmun_frotas/index.md) | [DOM-FRO](../DOM-FRO/index.md) | `MOD-FRO` | Preparado | Candidata; validar escopo |
| [sigmun_gabinete](sigmun_gabinete/index.md) | Não determinado | Não definido | Preparado | Não determinada |
| [sigmun_gdo](sigmun_gdo/index.md) | [DOM-GDO](../DOM-GDO/index.md) | `MOD-GDO` | Implementação identificada | Confirmada no escopo observado |
| [sigmun_idn](sigmun_idn/index.md) | [DOM-IDN](../DOM-IDN/index.md) | `MOD-IDN` | Implementação identificada | Confirmada no escopo observado |
| [sigmun_int](sigmun_int/index.md) | [DOM-INT](../DOM-INT/index.md) | `MOD-INT` | Implementação identificada | Confirmada no escopo observado |
| [sigmun_licitacoes](sigmun_licitacoes/index.md) | Não determinado | Não definido | Preparado | Não determinada |
| [sigmun_met](sigmun_met/index.md) | [DOM-MET](../DOM-MET/index.md) | `MOD-MET` | Implementação identificada | Confirmada no escopo observado |
| [sigmun_obras](sigmun_obras/index.md) | [DOM-OBR](../DOM-OBR/index.md) | `MOD-OBR` | Preparado | Candidata; validar escopo |
| [sigmun_ouvidoria](sigmun_ouvidoria/index.md) | [DOM-OUV](../DOM-OUV/index.md) | `MOD-OUV` | Preparado | Candidata; validar escopo |
| [sigmun_patrimonio](sigmun_patrimonio/index.md) | Não determinado | Não definido | Preparado | Não determinada |
| [sigmun_planejamento](sigmun_planejamento/index.md) | [DOM-PLA](../DOM-PLA/index.md) | `MOD-PLA` | Preparado | Candidata; validar escopo |
| [sigmun_procuradoria](sigmun_procuradoria/index.md) | Não determinado | Não definido | Preparado | Não determinada |
| [sigmun_rh](sigmun_rh/index.md) | Não determinado | Não definido | Preparado | Não determinada |
| [sigmun_saude](sigmun_saude/index.md) | [DOM-SAU](../DOM-SAU/index.md) | `MOD-SAU` | Preparado | Candidata; validar escopo |
| [sigmun_seg](sigmun_seg/index.md) | [DOM-SEG](../DOM-SEG/index.md) | `MOD-SEG` | Implementação identificada | Confirmada no escopo observado |
| [sigmun_transparencia](sigmun_transparencia/index.md) | Não determinado | Não definido | Preparado | Não determinada |
| [sigmun_tributos](sigmun_tributos/index.md) | [DOM-TRI](../DOM-TRI/index.md) | `MOD-TRI` | Preparado | Candidata; validar escopo |

## Modelo documental preexistente

Os arquivos abaixo são templates; seus status declarados não comprovam conteúdo concluído.

- [APIs.md](modelo/APIs.md)
- [Banco-de-dados.md](modelo/Banco-de-dados.md)
- [Casos-de-Uso.md](modelo/Casos-de-Uso.md)
- [Documentacao.md](modelo/Documentacao.md)
- [Modelo-de-Negocio.md](modelo/Modelo-de-Negocio.md)
- [README.md](modelo/README.md)
- [Requisitos.md](modelo/Requisitos.md)
- [Testes.md](modelo/Testes.md)
- [UX.md](modelo/UX.md)

## Histórico

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 2026-09-17 | Criação do inventário e navegação; aprovação não presumida | Equipe SIGMUN |
| 1.1 | 2026-09-17 | Regeneração seletiva de Compras conforme ADR-0006; destinos físicos e demais qualificadores preservados | Cline, por autorização do solicitante |
