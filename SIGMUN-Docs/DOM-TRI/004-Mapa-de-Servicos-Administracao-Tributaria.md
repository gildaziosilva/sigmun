# 004 – Mapa-de-Servicos – Administração Tributária

#### Mapa-de-Servicos – Administração Tributária

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TRI-004

**Domínio:** Administração Tributária

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Administracao-Tributaria.md`
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

Este artefato detalha **o mapa de serviços** do domínio Administração Tributária (`DOM-TRI`), com base na implementação material identificada em `src/modules/sigmun_tributos` e no conteúdo de negócio declarado no gerador.

---

# 2. Operações publicadas em `/api/v1/tri`

| Método | Caminho | Recurso | Resumo |
| --- | --- | --- | --- |
| POST | `/api/v1/tri/certidoes` | certidoes | Emitir Certidao |
| GET | `/api/v1/tri/certidoes/{certidao_id}` | certidoes | Obter Certidao |
| GET | `/api/v1/tri/contribuintes` | contribuintes | Listar Contribuintes |
| POST | `/api/v1/tri/contribuintes` | contribuintes | Cadastrar Contribuinte |
| GET | `/api/v1/tri/contribuintes/{contribuinte_id}` | contribuintes | Obter Contribuinte |
| GET | `/api/v1/tri/divida-ativa` | divida-ativa | Listar Divida Ativa |
| GET | `/api/v1/tri/divida-ativa/{inscricao_id}` | divida-ativa | Obter Divida Ativa |
| POST | `/api/v1/tri/divida-ativa/{inscricao_id}/baixar` | divida-ativa | Baixar Divida Ativa |
| GET | `/api/v1/tri/imoveis` | imoveis | Listar Imoveis |
| POST | `/api/v1/tri/imoveis` | imoveis | Cadastrar Imovel |
| GET | `/api/v1/tri/imoveis/{imovel_id}` | imoveis | Obter Imovel |
| GET | `/api/v1/tri/lancamentos` | lancamentos | Listar Lancamentos |
| POST | `/api/v1/tri/lancamentos` | lancamentos | Lancar Tributo |
| GET | `/api/v1/tri/lancamentos/{lancamento_id}` | lancamentos | Obter Lancamento |
| POST | `/api/v1/tri/lancamentos/{lancamento_id}/inscrever-divida-ativa` | lancamentos | Inscrever Divida Ativa |
| POST | `/api/v1/tri/lancamentos/{lancamento_id}/pagar` | lancamentos | Pagar Lancamento |

---

# 3. Recursos publicados

| Recurso | Operações |
| --- | --- |
| certidoes | 2 |
| contribuintes | 3 |
| divida-ativa | 3 |
| imoveis | 3 |
| lancamentos | 5 |

---

# 4. Lacunas a validar

* Definir o convênio de cobrança com o banco BV ou tributário.
* Definir a regra de atualização de valores da dívida ativa.

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 004-Administracao-Tributaria-Mapa-de-Servicos.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
