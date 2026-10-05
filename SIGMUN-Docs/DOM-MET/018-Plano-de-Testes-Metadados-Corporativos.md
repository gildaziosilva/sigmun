# 018 – Plano-de-Testes – Metadados Corporativos

#### Plano-de-Testes – Metadados Corporativos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-MET-018

**Domínio:** Metadados Corporativos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Metadados-Corporativos.md`
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

Este artefato detalha **o plano de testes** do domínio Metadados Corporativos (`DOM-MET`), com base na implementação material identificada em `src/modules/sigmun_met` e no conteúdo de negócio declarado no gerador.

---

# 2. Suítes por classe

| Arquivo | Classe | Testes |
| --- | --- | --- |
| `tests/unit/test_met_use_cases.py` | _FakeBaseRepository | 0 |
| `tests/unit/test_met_use_cases.py` | TestCriarMetadadoUseCase | 3 |
| `tests/unit/test_met_use_cases.py` | TestAtualizarBuscarMetadadoUseCase | 5 |
| `tests/unit/test_met_use_cases.py` | TestAtivarDesativarDeletarMetadadoUseCase | 3 |
| `tests/unit/test_met_use_cases.py` | TestAtribuirValorMetadadoUseCase | 5 |
| `tests/unit/test_met_use_cases.py` | TestBuscarRemoverValidarValorUseCase | 3 |
| `tests/unit/test_met_use_cases.py` | TestClassificacaoUseCases | 6 |
| `tests/unit/test_met_use_cases.py` | TestTaxonomiaUseCases | 5 |
| `tests/unit/test_met_use_cases.py` | TestTermoUseCases | 6 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 018-Metadados-Corporativos-Plano-de-Testes.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
