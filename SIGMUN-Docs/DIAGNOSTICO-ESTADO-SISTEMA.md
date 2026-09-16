# Diagnóstico de Estado do Sistema — SIGMUN

**Data da checagem:** 2026-09-16  
**Branch:** `main`  
**HEAD:** `5fda72a`  
**Working tree:** limpo no momento da checagem  
**Objetivo:** levantar o estado real do repositório antes de qualquer decisão de implementação ou correção, cruzando código, migrações, APIs, testes e documentação.

---

## 1. Visão geral

O repositório está em um estado intermediário coerente com um projeto em Onda 2 de implementação:

- existe um Backend operacional com diversos domínios implementados,
- existe um núcleo de documentação corporativa avançada,
- alguns domínios têm implementação completa, outros têm implementação emergente,
- muitos domínios estão documentados com código ainda não materializado.

Isso cria uma realidade comum em projetos DDD grandes: documentação avançada e implementação concentrada em menos domínios.

---

## 2. Estado do `src/main.py` e das APIs

### 2.1 Registro de routers

`src/main.py` registra 14 routers:

- `fornecedores_router`
- `itens_compras_router`
- `compras_router`
- `processo_documental_router`
- `contratos_router`
- `auditoria_router`
- `pessoas_router`
- `unidades_router`
- `idn_router`
- `seg_router`
- `dad_router`
- `met_router`
- `gdo_router`
- `int_router`

### 2.2 Implicação

A API expõe rotas para os domínios que já têm implementação de backend.  
DOM-GOV e DOM-IND **não** têm router registrado, porque não há módulo correspondente em `src/modules/`.

---

## 3. Módulos em `src/modules/`

### 3.1 Módulos com implementação expressiva

Com base em arquivos `.py` e estrutura de subpastas, os módulos mais implementados são:

- `sigmun_compras`
- `sigmun_gdo`
- `sigmun_int`
- `sigmun_seg`
- `sigmun_idn`
- `sigmun_dad`
- `sigmun_cadastro`
- `sigmun_met`

Esses módulos costumam ter estrutura de domínio, aplicação, infraestrutura e apresentação.

### 3.2 Módulos com aparência de scaffolding

Existem muitos módulos com estrutura mínima/placeholder, como:

- `sigmun_rh`
- `sigmun_tributos`
- `sigmun_contabilidade`
- `sigmun_financas`
- `sigmun_administracao`
- `sigmun_agricultura`
- `sigmun_almoxarifado`
- `sigmun_assistencia_social`
- `sigmun_educacao`
- `sigmun_frotas`
- `sigmun_gabinete`
- `sigmun_licitacoes`
- `sigmun_obras`
- `sigmun_ouvidoria`
- `sigmun_patrimonio`
- `sigmun_planejamento`
- `sigmun_procuradoria`
- `sigmun_saude`
- `sigmun_transparencia`

### 3.3 Ausências diretas para este diagnóstico

Os seguintes módulos **não existem** em `src/modules/`:

- `sigmun_gov`
- `sigmun_ind`

---

## 4. DOM-GOV e DOM-IND: documento × código

### 4.1 DOM-GOV

**Documentação:**
- pasta completa `SIGMUN-Docs/DOM-GOV/` (000 a 026)

**Conteúdo:**
- capa `000` com “Vigente”
- `005-Casos-de-Uso-Governanca-Municipal.md` e artefatos detalhados (modelo de dados, modelo de integração, arquitetura de serviços, estrutura técnica) estão como “Em elaboração” e são basicamente templates

**Código:**
- não existe `sigmun_gov` em `src/modules/`
- não há migração óbvia de governança
- não há router de governança no `main.py`

**Conclusão:** DOM-GOV está documentado/planejado, sem materialização no backend.

### 4.2 DOM-IND

**Documentação:**
- pasta completa `SIGMUN-Docs/DOM-IND/` (000 a 026)

**Conteúdo:**
- capa `000` com “Vigente”
- artefatos detalhados (modelo de dados, modelo de integração, arquitetura de serviços, estrutura técnica) estão como “Em elaboração” e são basicamente templates

**Código:**
- não existe `sigmun_ind` em `src/modules/`
- não há migração óbvia de indicadores
- não há router `ind` no `main.py`

**Conclusão:** DOM-IND está documentado/planejado, sem materialização no backend.

---

## 5. DOM-INT: o que existe de real

- módulo `sigmun_int` existe
- estrutura: domain, application, infrastructure, presentation
- migração existe (`dom_int_schema`)
- router `/api/v1/int` registrado no `main.py`
- código recente inclui: contratos de integração, conectores, APIs externas, webhooks, entregas, eventos processados, consumo de outbox

**Ainda parece não estar totalmente consolidado:**
- event bus, catálogo de APIs/webhooks completos e dependências futuras conforme TODO

Ou seja: DOM-INT deixou de ser “scaffolding vazio” e está em andamento avançado, mas não totalmente finalizado.

---

## 6. Migrações

O repositório tem migrações nomeadas por domínio/ataque.

Head: `20260916_01 (head)`

Exemplos de versões existentes:

- `20260820_01_core_compras.py`
- `20260821_01_integracao_compra_contrato.py`
- `20260822_01_trilha_auditoria.py`
- `20260823_01_pendencias_impeditivas.py`
- `20260831_01_contratos_situacao.py`
- `20260831_02_cum_enderecos_documentos_contatos.py`
- `20260831_03_idn_usuarios_roles_sessoes.py`
- `20260831_04_dad_ativos_catalogo_linhagem.py`
- `20260901_01_met_metadados_classificacoes_taxonomias.py`
- `20260901_02_gdo_documentos_tramitacoes_processos.py`
- `20260901_03_gdo_tipos_documentais_eventos.py`
- `20260901_04_dom_seg_models.py`
- `20260901_05_dom_seg_schema_correction.py`
- `20260916_01_dom_int_schema.py`

**Ausência relevante:** não há migração óbvia de governança ou indicadores, coerente com a ausência dos módulos.

---

## 7. Testes

- lint: **falha**, 5 violações (3 fixáveis automaticamente)
- type-check: **ok** (Success: no issues found in 652 source files)
- unit: **480 passed** (5 warnings, sem falhas)

### 7.1 Cobertura observada

- compras/contratos/itens
- cadastro (CPF/CNPJ e value objects)
- GDO (use cases, eventos)
- DAD, MET
- SEG (chave/credencial)
- INT (use cases e repositórios)

### 7.2 Lacunas

- sem testes para GOV/IND (coerente)
- integração não executada neste diagnóstico; parece depender de banco
- warnings de deprecated FastAPI (`on_event`)

---

## 8. Qualidade de código

- mypy ok
- unit ok
- lint com pequenos erros concentrados em:
  - linha longa em `src/modules/sigmun_int/presentation/api/__init__.py`
  - imports longos em `tests/integration/test_dom_int_sqlalchemy_repositories.py`
  - nested `with` simplificável em testes de integração

Código tipado e testado, com pequena dívida de formato/estilo.

---

## 9. Síntese final

- **DOM-GOV:** documento/planejamento existe, backend inexistente, migração inexistente, API inexistente.
- **DOM-IND:** documento/planejamento existe, backend inexistente, migração inexistente, API inexistente.
- **DOM-INT:** backend real avançado, migração existe, API existe, mas ainda não totalmente consolidado.
- **Demais domínios implementados:** código/migração/testes compatíveis com entrega real.
- **Demais domínios documentados sem código:** muitos, com estrutura padronizada.

---

*Documento de diagnóstico interno. Não é backlog. Não altera TODO.md ou ROADMAP.md. Serve para embasar decisões futuras.*


