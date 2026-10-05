# 019 – Casos-de-Teste – Dados Corporativos

#### Casos-de-Teste – Dados Corporativos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-DAD-019

**Domínio:** Dados Corporativos

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Dados-Corporativos.md`
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

Este artefato detalha **os casos de teste** do domínio Dados Corporativos (`DOM-DAD`), com base na implementação material identificada em `src/modules/sigmun_dad` e no conteúdo de negócio declarado no gerador.

---

# 2. Testes

| ID | Teste |
| --- | --- |
| CT-DAD-001 | `TestCriarAtivoUseCase.test_criar_ativo_sucesso` |
| CT-DAD-002 | `TestCriarAtivoUseCase.test_criar_ativo_nome_duplicado_lanca_erro` |
| CT-DAD-003 | `TestCriarAtivoUseCase.test_criar_ativo_nome_invalido_lanca_erro` |
| CT-DAD-004 | `TestAtivarAtivoUseCase.test_ativar_ativo_sucesso` |
| CT-DAD-005 | `TestAtivarAtivoUseCase.test_ativar_ativo_inexistente_lanca_erro` |
| CT-DAD-006 | `TestDesativarAtivoUseCase.test_desativar_ativo_sucesso` |
| CT-DAD-007 | `TestArquivarAtivoUseCase.test_arquivar_ativo_sucesso` |
| CT-DAD-008 | `TestBuscarAtivoUseCase.test_buscar_ativo_por_id` |
| CT-DAD-009 | `TestBuscarAtivoUseCase.test_buscar_ativo_inexistente_lanca_erro` |
| CT-DAD-010 | `TestBuscarAtivoUseCase.test_listar_ativos` |
| CT-DAD-011 | `TestCriarCatalogoUseCase.test_criar_catalogo_sucesso` |
| CT-DAD-012 | `TestCriarCatalogoUseCase.test_criar_catalogo_nome_duplicado_lanca_erro` |
| CT-DAD-013 | `TestBuscarCatalogoUseCase.test_buscar_catalogo_por_id` |
| CT-DAD-014 | `TestBuscarCatalogoUseCase.test_buscar_catalogo_inexistente_lanca_erro` |
| CT-DAD-015 | `TestDeletarCatalogoUseCase.test_deletar_catalogo_sucesso` |
| CT-DAD-016 | `TestDeletarCatalogoUseCase.test_deletar_catalogo_inexistente_lanca_erro` |
| CT-DAD-017 | `TestCriarLinhagemUseCase.test_criar_linhagem_sucesso` |
| CT-DAD-018 | `TestCriarLinhagemUseCase.test_criar_linhagem_duplicada_lanca_erro` |
| CT-DAD-019 | `TestCriarLinhagemUseCase.test_criar_linhagem_mesmo_ativo_lanca_erro` |
| CT-DAD-020 | `TestBuscarLinhagemUseCase.test_buscar_linhagem_por_id` |
| CT-DAD-021 | `TestBuscarLinhagemUseCase.test_buscar_linhagem_inexistente_lanca_erro` |
| CT-DAD-022 | `TestDeletarLinhagemUseCase.test_deletar_linhagem_sucesso` |
| CT-DAD-023 | `TestDeletarLinhagemUseCase.test_deletar_linhagem_inexistente_lanca_erro` |
| CT-DAD-024 | `TestCriarPoliticaUseCase.test_criar_politica_sucesso` |
| CT-DAD-025 | `TestCriarPoliticaUseCase.test_criar_politica_codigo_duplicado_lanca_erro` |
| CT-DAD-026 | `TestBuscarPoliticaUseCase.test_buscar_politica_por_id` |
| CT-DAD-027 | `TestBuscarPoliticaUseCase.test_buscar_politica_por_codigo` |
| CT-DAD-028 | `TestBuscarPoliticaUseCase.test_buscar_politica_inexistente_lanca_erro` |
| CT-DAD-029 | `TestDeletarPoliticaUseCase.test_deletar_politica_sucesso` |
| CT-DAD-030 | `TestDeletarPoliticaUseCase.test_deletar_politica_inexistente_lanca_erro` |
| CT-DAD-031 | `TestAvaliarQualidadeUseCase.test_avaliar_qualidade_sucesso` |
| CT-DAD-032 | `TestAvaliarQualidadeUseCase.test_avaliar_qualidade_score_invalido_lanca_erro` |
| CT-DAD-033 | `TestBuscarQualidadeUseCase.test_buscar_qualidade_por_id` |
| CT-DAD-034 | `TestBuscarQualidadeUseCase.test_buscar_qualidade_por_ativo` |
| CT-DAD-035 | `TestBuscarQualidadeUseCase.test_buscar_qualidade_inexistente_lanca_erro` |
| CT-DAD-036 | `TestDeletarQualidadeUseCase.test_deletar_qualidade_sucesso` |
| CT-DAD-037 | `TestDeletarQualidadeUseCase.test_deletar_qualidade_inexistente_lanca_erro` |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 019-Dados-Corporativos-Casos-de-Teste.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
