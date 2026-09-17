# Auditoria de regressão — canonicalização de Compras

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Domínio:** DOM-COM — Compras e Contratações
**Versão:** 1.0
**Data:** 2026-09-17
**Status:** Executada; resultados e limites registrados
**Classificação da Informação:** Pública
**Responsável pela execução:** Cline, por autorização explícita do solicitante
**Decisão:** [ADR-0006](ADR/ADR-0006-Compras-canonicalizacao.md)

## 1. Resultado

DOM-COM é o identificador corporativo vigente. DOM-COMPRAS é identificação documental histórica, substituída nas referências correntes. DOM-COMPRAS-001 é identificação histórica do piloto e nome físico/documental preservado por compatibilidade.

A aprovação registrada no ADR é a instrução explícita do solicitante; não se alega ata ou aprovação institucional adicional. Não há renomeação de diretório, pacote, banco ou requisitos.

## 2. Execução

1. Criado ADR-0006, após conferir a numeração existente.
2. Revisada a compatibilidade e registrada a aprovação do solicitante.
3. Normalizadas seletivamente referências correntes em Compras, Gestão Documental, planejamento, código e rótulos operacionais.
4. Regenerados os quatro índices afetados: geral, catálogo de módulos, módulo de Compras e domínio; preservados destinos e qualificadores. Índice de ADRs atualizado.
5. Matriz 031 atualizada para versão 1.2, sem promover maturidade, ownership ou códigos MOD.
6. Executados testes e auditoria comparativa contra snapshot anterior à intervenção, incluindo arquivos não versionados preexistentes.

## 3. Verificações e resultados

| Verificação | Resultado |
| --- | --- |
| Suíte unitária existente antes dos novos testes | 480 aprovados; 5 avisos |
| Suíte unitária incluindo quatro testes de identidade | 484 aprovados; 5 avisos; 1,30 s |
| OpenAPI | Teste confirma DOM-COM na descrição pública e ausência das formas históricas nessa descrição |
| Índices | Rótulos DOM-COM, destinos no diretório histórico; nenhum diretório substituto criado |
| Links Markdown | 570 destinos examinados nos arquivos alterados, sem links quebrados, após inclusão do teste e do relatório; links do ADR também verificados |
| Higiene do diff e shell | git diff --check e bash -n concluídos com código 0 |
| Estrutura Python | AST comparada após normalização somente das strings de identidade; sem mudança estrutural executável |
| Identificadores de artefatos | Sequências numeradas RN/UC/ENT/RF/HU/CAP/PROC/SERV/RNF/ESP/CA/TST-COMPRAS preservadas nos arquivos existentes |
| Conteúdo protegido | Hashes preservados para módulo sigmun_compras, migrações, testes preexistentes, evidências, auditoria anterior e listagens temporárias |
| Arquivos existentes alterados | 45 em relação ao snapshot local anterior; não confundir com diff contra HEAD |
| Formas históricas residuais | 101 linhas classificadas na passagem anterior ao relatório; nenhuma sem justificativa |

Os testes novos estão em [test_compras_identidade_corporativa.py](../../tests/unit/test_compras_identidade_corporativa.py). Não importam scripts de deploy/monitoramento: inspecionam seus caminhos via AST.

## 4. Classificação das formas históricas preservadas

- Evidências e log do piloto: integridade histórica, sem reescrita.
- Auditoria documental anterior: registro do achado à época, não declaração de pendência vigente após ADR-0006.
- Checklist de produção e item de homologação do roadmap: gates datados e caminhos de evidências; suas alegações não foram recertificadas.
- Plano de Trabalho: colunas de localização física, árvore documental e marcos históricos; nota explícita distingue identidade e localização.
- Modelo Conceitual: proveniência histórica do template do piloto.
- Scripts de deploy e monitoramento: EVIDENCE_DIR preservado.
- Scripts de setup: referências ao template, exclusões e seletores físicos preservados. Não foram executados os geradores antigos que escrevem documentos de outros domínios.
- Matriz 012: código documental composto DOM-COMPRAS-001-012 preservado como legado; raiz de domínio normalizada.
- ADR, matriz e índices: menções explicativas às formas históricas e destinos de links, não identidade corrente concorrente.
- Listagens temporárias: preservadas como cópias de inventário, sem autoridade normativa.

## 5. Limites e reprodução

Comando executado a partir da raiz do projeto:

```sh
PYTHONDONTWRITEBYTECODE=1 LOG_FILE=/tmp/sigmun-compras-canonicalizacao-20260917/test-app.log .venv/bin/python -m pytest tests/unit -q -p no:cacheprovider
```

Cinco avisos de depreciação do TestClient/HTTPX e FastAPI on_event já estavam presentes na primeira execução; não foram corrigidos nesta alteração de identidade.

Não foram executados deploy, migrações, homologação operacional ou suíte de integração PostgreSQL. A suíte unitária importa a aplicação e inclui o teste de health existente; esse teste pode verificar conectividade, sem migração ou escrita de dados por esta tarefa. Aprovação dos testes não equivale a homologação de produção.

Os diffs, inventário residual por arquivo/linha, hashes e logs desta execução estão em `/tmp/sigmun-compras-canonicalizacao-20260917`; são evidências locais temporárias, não substituem este registro versionável. Nenhum commit foi criado e as alterações locais anteriores foram preservadas.
