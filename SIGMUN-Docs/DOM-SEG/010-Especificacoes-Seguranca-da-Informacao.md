# 010 – Especificacoes – Segurança da Informação

#### Especificacoes – Segurança da Informação

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-SEG-010

**Domínio:** Segurança da Informação

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Seguranca-da-Informacao.md`
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

Este artefato detalha **as especificações** do domínio Segurança da Informação (`DOM-SEG`), com base na implementação material identificada em `src/modules/sigmun_seg` e no conteúdo de negócio declarado no gerador.

---

# 2. Contratos publicados

| Método | Caminho | Recurso | Corpo |
| --- | --- | --- | --- |
| GET | `/api/v1/seg/chaves` | chaves | JSON (payload do domínio) |
| POST | `/api/v1/seg/chaves` | chaves | JSON (payload do domínio) |
| DELETE | `/api/v1/seg/chaves/{chave_id}` | chaves | JSON (payload do domínio) |
| GET | `/api/v1/seg/chaves/{chave_id}` | chaves | JSON (payload do domínio) |
| POST | `/api/v1/seg/chaves/{chave_id}/expirar` | chaves | JSON (payload do domínio) |
| POST | `/api/v1/seg/chaves/{chave_id}/revogar` | chaves | JSON (payload do domínio) |
| GET | `/api/v1/seg/controles` | controles | JSON (payload do domínio) |
| POST | `/api/v1/seg/controles` | controles | JSON (payload do domínio) |
| DELETE | `/api/v1/seg/controles/{controle_id}` | controles | JSON (payload do domínio) |
| GET | `/api/v1/seg/controles/{controle_id}` | controles | JSON (payload do domínio) |
| PUT | `/api/v1/seg/controles/{controle_id}` | controles | JSON (payload do domínio) |
| POST | `/api/v1/seg/controles/{controle_id}/implementar` | controles | JSON (payload do domínio) |
| POST | `/api/v1/seg/controles/{controle_id}/parcial` | controles | JSON (payload do domínio) |
| GET | `/api/v1/seg/credenciais` | credenciais | JSON (payload do domínio) |
| POST | `/api/v1/seg/credenciais` | credenciais | JSON (payload do domínio) |
| GET | `/api/v1/seg/credenciais/{credencial_id}` | credenciais | JSON (payload do domínio) |
| POST | `/api/v1/seg/credenciais/{credencial_id}/revogar` | credenciais | JSON (payload do domínio) |
| POST | `/api/v1/seg/credenciais/{credencial_id}/suspender` | credenciais | JSON (payload do domínio) |
| GET | `/api/v1/seg/incidentes` | incidentes | JSON (payload do domínio) |
| POST | `/api/v1/seg/incidentes` | incidentes | JSON (payload do domínio) |
| DELETE | `/api/v1/seg/incidentes/{incidente_id}` | incidentes | JSON (payload do domínio) |
| GET | `/api/v1/seg/incidentes/{incidente_id}` | incidentes | JSON (payload do domínio) |
| POST | `/api/v1/seg/incidentes/{incidente_id}/encerrar` | incidentes | JSON (payload do domínio) |
| POST | `/api/v1/seg/incidentes/{incidente_id}/escalar` | incidentes | JSON (payload do domínio) |
| POST | `/api/v1/seg/incidentes/{incidente_id}/mitigar` | incidentes | JSON (payload do domínio) |
| POST | `/api/v1/seg/incidentes/{incidente_id}/resolver` | incidentes | JSON (payload do domínio) |
| GET | `/api/v1/seg/politicas` | politicas | JSON (payload do domínio) |
| POST | `/api/v1/seg/politicas` | politicas | JSON (payload do domínio) |
| DELETE | `/api/v1/seg/politicas/{politica_id}` | politicas | JSON (payload do domínio) |
| GET | `/api/v1/seg/politicas/{politica_id}` | politicas | JSON (payload do domínio) |
| PUT | `/api/v1/seg/politicas/{politica_id}` | politicas | JSON (payload do domínio) |
| POST | `/api/v1/seg/politicas/{politica_id}/aprovar` | politicas | JSON (payload do domínio) |

---

# 3. Validações aplicadas

| Regra | Validação |
| --- | --- |
| RN-SEG-001 | credencial revogada ou expirada é recusada pelo autenticação. |
| RN-SEG-002 | chave criptográfica revogada não pode voltar a valer. |
| RN-SEG-003 | incidente exige classificação de severidade antes do tratamento. |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 010-Seguranca-da-Informacao-Especificacoes.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
