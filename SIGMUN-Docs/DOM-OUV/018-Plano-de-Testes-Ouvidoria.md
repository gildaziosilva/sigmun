# 018 – Plano-de-Testes – Ouvidoria

#### Plano-de-Testes – Ouvidoria

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OUV-018

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

Este artefato detalha **o plano de testes** do domínio Ouvidoria (`DOM-OUV`), com base na implementação material identificada em `src/modules/sigmun_ouvidoria` e no conteúdo de negócio declarado no gerador.

---

# 2. Suítes por classe

| Arquivo | Classe | Testes |
| --- | --- | --- |
| `tests/unit/test_sigmun_ouvidoria_domain.py` | TestProtocolo | 4 |
| `tests/unit/test_sigmun_ouvidoria_domain.py` | TestTransicoesDeStatus | 4 |
| `tests/unit/test_sigmun_ouvidoria_domain.py` | TestCalculadoraPrazo | 9 |
| `tests/unit/test_sigmun_ouvidoria_domain.py` | TestDadosCidadao | 9 |
| `tests/unit/test_sigmun_ouvidoria_domain.py` | TestValidacaoManifestacao | 7 |
| `tests/unit/test_sigmun_ouvidoria_domain.py` | TestRespostaEAvaliacao | 5 |
| `tests/unit/test_sigmun_ouvidoria_domain.py` | TestDenuncia | 6 |
| `tests/unit/test_sigmun_ouvidoria_domain.py` | TestPedidoLai | 9 |
| `tests/unit/test_sigmun_ouvidoria_domain.py` | TestValidadorManifestacao | 6 |
| `tests/unit/test_sigmun_ouvidoria_domain.py` | TestPrioridade | 1 |
| `tests/unit/test_sigmun_ouvidoria_domain.py` | TestExclusaoLogica | 1 |
| `tests/unit/test_sigmun_ouvidoria_domain.py` | TestAdicionarAnexo | 1 |
| `tests/unit/test_sigmun_ouvidoria_domain.py` | TestEnumsDeSuporte | 2 |
| `tests/unit/test_sigmun_ouvidoria_use_cases.py` | RepoProtocoloMemoria | 0 |
| `tests/unit/test_sigmun_ouvidoria_use_cases.py` | RepoAnexoMemoria | 0 |
| `tests/unit/test_sigmun_ouvidoria_use_cases.py` | RepoTramitacaoMemoria | 0 |
| `tests/unit/test_sigmun_ouvidoria_use_cases.py` | _RepoBaseMemoria | 0 |
| `tests/unit/test_sigmun_ouvidoria_use_cases.py` | TestRegistrarManifestacaoUseCase | 6 |
| `tests/unit/test_sigmun_ouvidoria_use_cases.py` | TestRegistrarDenunciaUseCase | 3 |
| `tests/unit/test_sigmun_ouvidoria_use_cases.py` | TestRegistrarPedidoLaiUseCase | 2 |
| `tests/unit/test_sigmun_ouvidoria_use_cases.py` | TestResponderManifestacaoUseCase | 5 |
| `tests/unit/test_sigmun_ouvidoria_use_cases.py` | TestAlterarStatusUseCase | 6 |
| `tests/unit/test_sigmun_ouvidoria_use_cases.py` | TestProrrogarPrazoUseCase | 4 |
| `tests/unit/test_sigmun_ouvidoria_use_cases.py` | TestAvaliarManifestacaoUseCase | 3 |
| `tests/unit/test_sigmun_ouvidoria_use_cases.py` | TestEncaminharDenunciaUseCase | 3 |
| `tests/unit/test_sigmun_ouvidoria_use_cases.py` | TestRecursoLaiUseCase | 6 |
| `tests/unit/test_sigmun_ouvidoria_use_cases.py` | TestListagemEEstatisticas | 5 |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 018-Ouvidoria-Plano-de-Testes.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
