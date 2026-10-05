# 004 – Mapa-de-Servicos – Orçamento Público

#### Mapa-de-Servicos – Orçamento Público

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ORC-004

**Domínio:** Orçamento Público

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Orcamento-Publico.md`
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

Este artefato detalha **o mapa de serviços** do domínio Orçamento Público (`DOM-ORC`), com base na implementação material identificada em `src/modules/sigmun_orc` e no conteúdo de negócio declarado no gerador.

---

# 2. Operações publicadas em `/api/v1/orc`

| Método | Caminho | Recurso | Resumo |
| --- | --- | --- | --- |
| POST | `/api/v1/orc/dotacoes` | dotacoes | Criar Dotacao |
| POST | `/api/v1/orc/dotacoes/{dotacao_id}/anular` | dotacoes | Anular |
| GET | `/api/v1/orc/dotacoes/{dotacao_id}/saldo` | dotacoes | Saldo |
| POST | `/api/v1/orc/dotacoes/{dotacao_id}/suplementar` | dotacoes | Suplementar |
| POST | `/api/v1/orc/ldos` | ldos | Criar Ldo |
| POST | `/api/v1/orc/ldos/{ldo_id}/sancionar` | ldos | Sancionar Ldo |
| POST | `/api/v1/orc/loas` | loas | Criar Loa |
| POST | `/api/v1/orc/loas/{loa_id}/publicar` | loas | Publicar Loa |
| POST | `/api/v1/orc/ppas` | ppas | Criar Ppa |
| POST | `/api/v1/orc/ppas/{ppa_id}/publicar` | ppas | Publicar Ppa |
| POST | `/api/v1/orc/reservas` | reservas | Reservar |
| POST | `/api/v1/orc/reservas/{reserva_id}/cancelar` | reservas | Cancelar Reserva |

---

# 3. Recursos publicados

| Recurso | Operações |
| --- | --- |
| dotacoes | 4 |
| ldos | 2 |
| loas | 2 |
| ppas | 2 |
| reservas | 2 |

---

# 4. Lacunas a validar

* API registrada em src/main.py (resolvido): 12 operações expostas em /api/v1/orc.
* Definir a integração com o sistema de SIMEOR de orçamento.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 004-Orcamento-Publico-Mapa-de-Servicos.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
