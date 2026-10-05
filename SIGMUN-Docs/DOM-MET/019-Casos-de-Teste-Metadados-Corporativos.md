# 019 – Casos-de-Teste – Metadados Corporativos

#### Casos-de-Teste – Metadados Corporativos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-MET-019

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

Este artefato detalha **os casos de teste** do domínio Metadados Corporativos (`DOM-MET`), com base na implementação material identificada em `src/modules/sigmun_met` e no conteúdo de negócio declarado no gerador.

---

# 2. Testes

| ID | Teste |
| --- | --- |
| CT-MET-001 | `TestCriarMetadadoUseCase.test_cria_metadado_com_sucesso` |
| CT-MET-002 | `TestCriarMetadadoUseCase.test_codigo_invalido_levanta_erro` |
| CT-MET-003 | `TestCriarMetadadoUseCase.test_codigo_duplicado_levanta_erro` |
| CT-MET-004 | `TestAtualizarBuscarMetadadoUseCase.test_atualiza_campos` |
| CT-MET-005 | `TestAtualizarBuscarMetadadoUseCase.test_atualizar_inexistente_levanta_erro` |
| CT-MET-006 | `TestAtualizarBuscarMetadadoUseCase.test_busca_por_id_e_codigo` |
| CT-MET-007 | `TestAtualizarBuscarMetadadoUseCase.test_buscar_inexistente_levanta_erro` |
| CT-MET-008 | `TestAtualizarBuscarMetadadoUseCase.test_listar_com_filtro_tipo` |
| CT-MET-009 | `TestAtivarDesativarDeletarMetadadoUseCase.test_desativar_e_ativar` |
| CT-MET-010 | `TestAtivarDesativarDeletarMetadadoUseCase.test_desativar_inexistente_levanta_erro` |
| CT-MET-011 | `TestAtivarDesativarDeletarMetadadoUseCase.test_deletar` |
| CT-MET-012 | `TestAtribuirValorMetadadoUseCase.test_atribui_novo_valor` |
| CT-MET-013 | `TestAtribuirValorMetadadoUseCase.test_atualiza_valor_existente` |
| CT-MET-014 | `TestAtribuirValorMetadadoUseCase.test_valor_invalido_para_tipo_numero` |
| CT-MET-015 | `TestAtribuirValorMetadadoUseCase.test_metadado_inexistente_levanta_erro` |
| CT-MET-016 | `TestAtribuirValorMetadadoUseCase.test_entidade_tipo_invalida_levanta_erro` |
| CT-MET-017 | `TestBuscarRemoverValidarValorUseCase.test_busca_por_entidade` |
| CT-MET-018 | `TestBuscarRemoverValidarValorUseCase.test_remover_valor` |
| CT-MET-019 | `TestBuscarRemoverValidarValorUseCase.test_validar_valor_valido_e_invalido` |
| CT-MET-020 | `TestClassificacaoUseCases.test_cria_classificacao` |
| CT-MET-021 | `TestClassificacaoUseCases.test_codigo_duplicado_levanta_erro` |
| CT-MET-022 | `TestClassificacaoUseCases.test_atualizar_e_buscar` |
| CT-MET-023 | `TestClassificacaoUseCases.test_buscar_inexistente_levanta_erro` |
| CT-MET-024 | `TestClassificacaoUseCases.test_deletar` |
| CT-MET-025 | `TestClassificacaoUseCases.test_listar_com_filtro_tipo` |
| CT-MET-026 | `TestTaxonomiaUseCases.test_cria_taxonomia` |
| CT-MET-027 | `TestTaxonomiaUseCases.test_codigo_duplicado_levanta_erro` |
| CT-MET-028 | `TestTaxonomiaUseCases.test_atualizar_e_buscar` |
| CT-MET-029 | `TestTaxonomiaUseCases.test_buscar_inexistente_levanta_erro` |
| CT-MET-030 | `TestTaxonomiaUseCases.test_deletar` |
| CT-MET-031 | `TestTermoUseCases.test_cria_termo_raiz_e_filho` |
| CT-MET-032 | `TestTermoUseCases.test_taxonomia_inexistente_levanta_erro` |
| CT-MET-033 | `TestTermoUseCases.test_codigo_duplicado_na_taxonomia_levanta_erro` |
| CT-MET-034 | `TestTermoUseCases.test_atualizar_termo` |
| CT-MET-035 | `TestTermoUseCases.test_buscar_filhos_e_por_taxonomia` |
| CT-MET-036 | `TestTermoUseCases.test_deletar_termo` |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 019-Metadados-Corporativos-Casos-de-Teste.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
