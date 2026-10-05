# 018 – Plano-de-Testes – Integração e Interoperabilidade

#### Plano-de-Testes – Integração e Interoperabilidade

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-INT-018

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

Este artefato detalha **o plano de testes** do domínio Integração e Interoperabilidade (`DOM-INT`), com base na implementação material identificada em `src/modules/sigmun_int` e no conteúdo de negócio declarado no gerador.

---

# 2. Suítes por classe

| Arquivo | Classe | Testes |
| --- | --- | --- |
| `tests/unit/test_dom_int_use_cases.py` | _RepoMixin | 0 |
| `tests/unit/test_dom_int_use_cases.py` | FakeOutboxSource | 0 |
| `tests/unit/test_dom_int_use_cases.py` | TestWebhookEntity | 6 |
| `tests/unit/test_dom_int_use_cases.py` | TestEntregaWebhook | 10 |
| `tests/unit/test_dom_int_use_cases.py` | TestEntidadesBasicas | 4 |
| `tests/unit/test_dom_int_use_cases.py` | TestConectorUseCases | 14 |
| `tests/unit/test_dom_int_use_cases.py` | TestApiUseCases | 12 |
| `tests/unit/test_dom_int_use_cases.py` | TestContratoUseCases | 14 |
| `tests/unit/test_dom_int_use_cases.py` | TestWebhookUseCases | 17 |
| `tests/unit/test_dom_int_use_cases.py` | TestEntregaUseCases | 9 |
| `tests/unit/test_dom_int_use_cases.py` | TestBusUseCases | 12 |
| `tests/integration/test_dom_int_sqlalchemy_repositories.py` | TestSqlAlchemyApiExternaRepository | 5 |
| `tests/integration/test_dom_int_sqlalchemy_repositories.py` | TestSqlAlchemyContratoIntegracaoRepository | 4 |
| `tests/integration/test_dom_int_sqlalchemy_repositories.py` | TestSqlAlchemyConectorRepository | 3 |
| `tests/integration/test_dom_int_sqlalchemy_repositories.py` | TestSqlAlchemyWebhookRepository | 2 |
| `tests/integration/test_dom_int_sqlalchemy_repositories.py` | TestSqlAlchemyEntregaWebhookRepository | 5 |
| `tests/integration/test_dom_int_sqlalchemy_repositories.py` | TestSqlAlchemyEventoProcessadoRepository | 6 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 018-Integracao-e-Interoperabilidade-Plano-de-Testes.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
