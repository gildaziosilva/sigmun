# ADR-0006 — Canonicalização de Compras e Contratações

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Domínio:** Governança / DOM-COM
**Identificador:** ADR-0006
**Versão:** 1.0
**Data:** 2026-09-17
**Status:** Aprovado pelo solicitante nesta conversa; vigente para esta normalização
**Classificação da Informação:** Pública
**Autor:** Gildazio, com decisão e autorização explícitas do solicitante
**Revisão:** Análise técnica documental e de compatibilidade em 17/09/2026
**Aprovado por:** Solicitante da tarefa, por instrução explícita de execução. Não se presume ata, assinatura ou aprovação adicional de comitê institucional.

## 1. Contexto e evidências

O [Mapa de Domínios](../../02-Modelo-de-Negocio/Mapa-de-Dominios.md), seção 12 e tabela consolidada, identifica Compras e Contratações como DOM-COM. A definição do piloto utilizava DOM-COMPRAS na cadeia de rastreabilidade; documentos, scripts e a descrição da API utilizavam DOM-COMPRAS-001. A auditoria prévia encontrou 291 ocorrências exatas em 61 arquivos, incluindo 96 ocorrências em três listagens temporárias. A contagem não inclui identificadores compostos, como o código documental DOM-COMPRAS-001-012.

O [módulo implementado](../../../src/modules/sigmun_compras) usa o pacote sigmun_compras, os schemas core/compras e identificadores RN-COMPRAS-*, UC-COMPRAS-* e ENT-COMPRAS-*. Os scripts de deploy e monitoramento dependem da pasta física do piloto. Não foi encontrada necessidade técnica de renomear pacotes, tabelas ou contratos para resolver a identidade corporativa.

## 2. Decisão

**DOM-COM é o identificador corporativo vigente do domínio Compras e Contratações.**

DOM-COMPRAS e DOM-COMPRAS-001 são formas históricas encontradas na documentação e nos artefatos do projeto, associadas ao mesmo escopo funcional, devendo ser preservadas somente quando necessárias à integridade histórica, compatibilidade ou localização física.

| Forma | Tratamento |
| --- | --- |
| DOM-COM | Identidade corporativa vigente; obrigatória em referências correntes |
| DOM-COMPRAS | Identificação documental histórica; substituir em referências correntes |
| DOM-COMPRAS-001 | Identificação histórica do piloto e nome físico/documental preservado por compatibilidade |

O nome técnico sigmun_compras e o namespace COMPRAS dos artefatos permanecem inalterados. As formas históricas não designam novos domínios, versões corporativas ou subdomínios. O sufixo 001 não recebe significado novo por esta decisão.

## 3. Alternativas avaliadas

- Canonicalizar como DOM-COMPRAS: rejeitado por divergir do identificador explícito no mapa corporativo.
- Canonicalizar como DOM-COMPRAS-001: rejeitado por confundir identidade corporativa com identificação do piloto/localização física.
- Substituição global e renomeação da pasta: rejeitadas pelo risco de quebra de caminhos e reescrita de evidências históricas.
- DOM-COM com preservação seletiva das formas históricas: adotado; alinha o catálogo sem alterar contratos funcionais.

## 4. Execução e compatibilidade

1. Normalizar identidade corrente, raízes de rastreabilidade, referências de Gestão Documental e descrição pública da API.
2. Preservar destinos de links, pasta física, exclusões e seletores dos geradores, códigos documentais compostos e registros históricos datados.
3. Manter íntegros os logs e arquivos de evidências, a auditoria anterior e as listagens temporárias.
4. Regenerar os índices afetados com rótulo DOM-COM e destino físico existente; atualizar a matriz 031 sem alterar maturidade, ownership ou aprovação de códigos MOD.
5. Auditar referências residuais, links, sintaxe Python, contratos e testes. Não executar deploy, migrações ou homologação operacional como parte desta alteração.

## 5. Consequências, riscos e limites

A identidade lógica difere deliberadamente da localização física. Consumidores não devem construir caminhos concatenando o código corporativo. Evidências históricas permanecem legíveis por meio deste mapeamento. Não há migração de dados nem mudança de rotas, permissões, eventos ou regras de negócio.

Esta aprovação limita-se à canonicalização autorizada. Não certifica completude funcional, produção, hierarquia documental, códigos MOD ou a validade de outras aprovações preexistentes.

## 6. Revisão e aprovação

A decisão foi revisada contra o Mapa de Domínios, a implementação e as dependências de caminho. O solicitante determinou explicitamente DOM-COM como identidade vigente e autorizou os seis passos de execução, incluindo revisão/aprovação do ADR. Esse é o registro de aprovação disponível; nenhuma aprovação institucional adicional é alegada.

## 7. Verificação e reversão

Critérios: nenhuma referência corrente ambígua; caminhos e evidências preservados; índices coerentes; nenhuma alteração em identificadores RN/UC/ENT, imports, schemas ou rotas; regressão registrada em relatório separado. A reversão deve restaurar somente os diffs desta normalização, preservando as alterações locais anteriores; não utilizar reset global.

## 8. Referências

- [Definição do domínio](../../DOM-COMPRAS-001/000-Dominio-Gestao-de-Compras-e-Contratacoes.md)
- [Matriz 031](../../01-Arquitetura-Corporativa/031-Matriz-de-Correspondencia-DOM-MOD.md)
- [Auditoria anterior preservada](../AUDITORIA-DOCUMENTAL-2026-09-17.md)

## 9. Histórico

| Versão | Data | Alteração |
| --- | --- | --- |
| 1.0 | 2026-09-17 | Decisão, revisão de compatibilidade e aprovação explícita do solicitante; normalização seletiva autorizada |
