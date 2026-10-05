# 026 – Modelo-de-Dominio – Mobilidade e Serviços de Campo

#### Modelo-de-Dominio – Mobilidade e Serviços de Campo

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-MOB-026

**Domínio:** Mobilidade e Serviços de Campo

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Mobilidade-e-Servicos-de-Campo.md`
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

Este artefato descreve **o modelo de domínio** do domínio Mobilidade e Serviços de Campo (`DOM-MOB`) em caráter **proposto**. O conteúdo técnico e de negócio deverá ser validado antes da implementação.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| dispositivos_moveis | `` | 13 |
| evidencias_campo | `` | 14 |
| ordens_campo | `` | 15 |
| sincronizacoes | `` | 12 |

---

# 3. Domínios de valor

### TipoOrdemCampo

| Membro | Valor |
| --- | --- |
| VISTORIA | 'vistoria' |
| COLETA | 'coleta' |
| MANUTENCAO | 'manutencao' |
| LEVANTAMENTO | 'levantamento' |
| OUTRO | 'outro' |
### SituacaoOrdemCampo

| Membro | Valor |
| --- | --- |
| ABERTA | 'aberta' |
| ASSINADA | 'assinada' |
| EM_CAMPO | 'em_campo' |
| CONCLUIDA | 'concluida' |
| CANCELADA | 'cancelada' |
### SituacaoSincronizacao

| Membro | Valor |
| --- | --- |
| EM_ANDAMENTO | 'em_andamento' |
| CONCLUIDA | 'concluida' |
| COM_CONFLITO | 'com_conflito' |
| FALHA | 'falha' |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-MOB-001 | o dispositivo é vinculado a pessoa e mantém a última sincronização. |
| RN-MOB-002 | a ordem executa offline e só conclui após sincronizar. |
| RN-MOB-003 | a evidência preserva data de captura, geolocalização e integridade do arquivo. |
| RN-MOB-004 | conflito de sincronização não sobrescreve dado sem decisão. |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Mobilidade-e-Servicos-de-Campo-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
