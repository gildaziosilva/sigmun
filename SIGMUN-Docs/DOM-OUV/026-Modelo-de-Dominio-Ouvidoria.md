# 026 – Modelo-de-Dominio – Ouvidoria

#### Modelo-de-Dominio – Ouvidoria

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OUV-026

**Domínio:** Ouvidoria

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Ouvidoria.md`
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

Este artefato detalha **o modelo de domínio** do domínio Ouvidoria (`DOM-OUV`), com base na implementação material identificada em `src/modules/sigmun_ouvidoria` e no conteúdo de negócio declarado no gerador.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| — | — | — |

---

# 3. Domínios de valor

### Prioridade

| Membro | Valor |
| --- | --- |
| BAIXA | "baixa" |
| NORMAL | "normal" |
| ALTA | "alta" |
| URGENTE | "urgente" |
### TipoEventoOuv

| Membro | Valor |
| --- | --- |
| MANIFESTACAO_REGISTRADA | "manifestacao_registrada" |
| MANIFESTACAO_ENCAMINHADA | "manifestacao_encaminhada" |
| MANIFESTACAO_RESPONDIDA | "manifestacao_respondida" |
| MANIFESTACAO_CONCLUIDA | "manifestacao_concluida" |
| MANIFESTACAO_ARQUIVADA | "manifestacao_arquivada" |
| MANIFESTACAO_CANCELADA | "manifestacao_cancelada" |
| DENUNCIA_REGISTRADA | "denuncia_registrada" |
| DENUNCIA_ENCAMINHADA_MP | "denuncia_encaminhada_mp" |
| DENUNCIA_ENCAMINHADA_PF | "denuncia_encaminhada_pf" |
| DENUNCIA_ENCAMINHADA_TCE | "denuncia_encaminhada_tce" |
| DENUNCIA_CONCLUIDA | "denuncia_concluida" |
| PEDIDO_LAI_REGISTRADO | "pedido_lai_registrado" |
| PEDIDO_LAI_CLASSIFICADO_SIGILO | "pedido_lai_classificado_sigilo" |
| PEDIDO_LAI_RESPONDIDO | "pedido_lai_respondido" |
| PEDIDO_LAI_RECURSO_INTERPOSTO | "pedido_lai_recurso_interposto" |
| PEDIDO_LAI_RECURSO_DECIDIDO | "pedido_lai_recurso_decidido" |
| PRAZO_VENCENDO | "prazo_vencendo" |
| PRAZO_VENCIDO | "prazo_vencido" |
| PRAZO_PRORROGADO | "prazo_prorrogado" |
### TipoManifestacao

| Membro | Valor |
| --- | --- |
| SUGESTAO | "sugestao" |
| ELOGIO | "elogio" |
| RECLAMACAO | "reclamacao" |
| SOLICITACAO | "solicitacao" |
| DENUNCIA | "denuncia" |
| PEDIDO_ACESSO_INFORMACAO | "pedido_acesso_informacao" |
### StatusManifestacao

| Membro | Valor |
| --- | --- |
| REGISTRADA | "registrada" |
| EM_ANALISE | "em_analise" |
| ENCAMINHADA | "encaminhada" |
| EM_TRATAMENTO | "em_tratamento" |
| AGUARDANDO_COMPLEMENTACAO | "aguardando_complementacao" |
| RESPONDIDA | "respondida" |
| CONCLUIDA | "concluida" |
| ARQUIVADA | "arquivada" |
| CANCELADA | "cancelada" |
| transicoes | { |
### NivelSigilo

| Membro | Valor |
| --- | --- |
| PUBLICO | "publico" |
| RESTRITO | "restrito" |
| SIGILOSO | "sigiloso" |
| ULTRA_SIGILOSO | "ultra_sigiloso" |
### CanalRecebimento

| Membro | Valor |
| --- | --- |
| PORTAL_CIDADAO | "portal_cidadao" |
| PRESENCIAL | "presencial" |
| TELEFONE | "telefone" |
| EMAIL | "email" |
| CORREIOS | "correios" |
| APLICATIVO | "aplicativo" |
| OUTRO | "outro" |
### TipoDenuncia

| Membro | Valor |
| --- | --- |
| CORRUPAO | "corrupcao" |
| IMPROBIDADE | "improbidade" |
| ASSEDIO | "assedio" |
| DESVIO_VERBA | "desvio_verba" |
| NEPOTISMO | "nepotismo" |
| FRAUDE_LICITACAO | "fraude_licitacao" |
| OUTRO | "outro" |
### FormaResposta

| Membro | Valor |
| --- | --- |
| PORTAL | "portal" |
| EMAIL | "email" |
| CORREIOS | "correios" |
| PRESENCIAL | "presencial" |
| TELEFONE | "telefone" |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-OU-001 | toda manifestação recebe protocolo e prazo. |
| RN-OU-002 | a denúncia admite proteção de identidade. |
| RN-OU-003 | o pedido de informação segue prazo próprio e admite recurso. |
| RN-OU-004 | o encerramento não apaga o histórico da manifestação. |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Ouvidoria-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
