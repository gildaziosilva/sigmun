# 026 – Modelo-de-Dominio – Integração e Interoperabilidade

#### Modelo-de-Dominio – Integração e Interoperabilidade

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-INT-026

**Domínio:** Integração e Interoperabilidade

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Integracao-e-Interoperabilidade.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `030-Roadmap-de-Implementacao-dos-Dominios.md`
* `Mapa-de-Dominios.md`

---


# 1. Finalidade

Este artefato detalha **o modelo de domínio** do domínio Integração e Interoperabilidade (`DOM-INT`), com base na implementação material identificada em `src/modules/sigmun_int` e no conteúdo de negócio declarado no gerador.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| apis_externas | `ApiExternaModel` | 15 |
| conectores | `ConectorModel` | 12 |
| contratos_integracao | `ContratoIntegracaoModel` | 11 |
| entregas_webhook | `EntregaWebhookModel` | 20 |
| eventos_processados | `EventoProcessadoModel` | 10 |
| webhooks | `WebhookModel` | 12 |

---

# 3. Domínios de valor

### EstadoApi

| Membro | Valor |
| --- | --- |
| RASCUNHO | "rascunho" |
| TESTES | "testes" |
| ATIVA | "ativa" |
| INATIVA | "inativa" |
| RETIRADA | "retirada" |
### TipoApi

| Membro | Valor |
| --- | --- |
| REST | "rest" |
| SOAP | "soap" |
| GRAPHQL | "graphql" |
### AutenticacaoApi

| Membro | Valor |
| --- | --- |
| NENHUMA | "nenhuma" |
| API_KEY | "api_key" |
| BASIC | "basic" |
| OAUTH2 | "oauth2" |
| MTLS | "mtls" |
### EstadoContrato

| Membro | Valor |
| --- | --- |
| RASCUNHO | "rascunho" |
| VIGENTE | "vigente" |
| OBSOLETO | "obsoleto" |
| RETIRADO | "retirado" |
### EstadoConector

| Membro | Valor |
| --- | --- |
| SEM_CONFIGURACAO | "sem_configuracao" |
| CONFIGURADO | "configurado" |
| TESTES | "testes" |
| ATIVO | "ativo" |
| INATIVO | "inativo" |
### EstadoInscricao

| Membro | Valor |
| --- | --- |
| ATIVA | "ativa" |
| DESATIVADA | "desativada" |
### EstadoEntrega

| Membro | Valor |
| --- | --- |
| PENDENTE | "pendente" |
| SUCESSO | "sucesso" |
| FALHOU | "falhou" |
| FILA_MORTA | "fila_morta" |
| CANCELADO | "cancelado" |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-INT-001 | API externa só opera quando o contrato está publicado. |
| RN-INT-002 | o contrato deve referenciar uma API existente do catálogo |
| RN-INT-004 | para passar a `ativo` o conector deve ter configuração |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Integracao-e-Interoperabilidade-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
