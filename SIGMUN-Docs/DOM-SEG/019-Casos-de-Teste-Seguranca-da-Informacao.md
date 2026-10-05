# 019 – Casos-de-Teste – Segurança da Informação

#### Casos-de-Teste – Segurança da Informação

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-SEG-019

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

Este artefato detalha **os casos de teste** do domínio Segurança da Informação (`DOM-SEG`), com base na implementação material identificada em `src/modules/sigmun_seg` e no conteúdo de negócio declarado no gerador.

---

# 2. Testes

| ID | Teste |
| --- | --- |
| CT-SEG-001 | `TestCriarChaveUseCase.test_criar_chave_valida` |
| CT-SEG-002 | `TestCriarChaveUseCase.test_criar_chave_sem_nome_lanca_erro` |
| CT-SEG-003 | `TestCriarChaveUseCase.test_criar_chave_nome_duplicado_lanca_erro` |
| CT-SEG-004 | `TestCriarChaveUseCase.test_criar_chave_tamanho_bits_invalido` |
| CT-SEG-005 | `TestBuscarChaveUseCase.test_buscar_por_id` |
| CT-SEG-006 | `TestBuscarChaveUseCase.test_buscar_por_nome` |
| CT-SEG-007 | `TestBuscarChaveUseCase.test_buscar_inexistente_lanca_erro` |
| CT-SEG-008 | `TestBuscarChaveUseCase.test_listar_vazio` |
| CT-SEG-009 | `TestFluxoChave.test_revogar_chave` |
| CT-SEG-010 | `TestFluxoChave.test_revogar_ja_revogada_lanca_erro` |
| CT-SEG-011 | `TestFluxoChave.test_expirar_chave` |
| CT-SEG-012 | `TestFluxoChave.test_atualizar_chave` |
| CT-SEG-013 | `TestFluxoChave.test_deletar_chave_soft_delete` |
| CT-SEG-014 | `TestCriarCredencialUseCase.test_criar_credencial_valida` |
| CT-SEG-015 | `TestCriarCredencialUseCase.test_criar_credencial_sem_usuario_lanca_erro` |
| CT-SEG-016 | `TestCriarCredencialUseCase.test_criar_credencial_sem_identificador_lanca_erro` |
| CT-SEG-017 | `TestBuscarCredencialUseCase.test_buscar_por_id` |
| CT-SEG-018 | `TestBuscarCredencialUseCase.test_buscar_por_usuario` |
| CT-SEG-019 | `TestBuscarCredencialUseCase.test_buscar_inexistente_lanca_erro` |
| CT-SEG-020 | `TestBuscarCredencialUseCase.test_listar` |
| CT-SEG-021 | `TestFluxoCredencial.test_suspender_credencial` |
| CT-SEG-022 | `TestFluxoCredencial.test_revogar_credencial` |
| CT-SEG-023 | `TestFluxoCredencial.test_revogar_ja_revogada_lanca_erro` |
| CT-SEG-024 | `TestFluxoCredencial.test_registrar_falha_incrementa_tentativas` |
| CT-SEG-025 | `TestFluxoCredencial.test_registrar_uso_zera_tentativas` |
| CT-SEG-026 | `TestFluxoCredencial.test_deletar_credencial_soft_delete` |
| CT-SEG-027 | `TestCriarControleSegurancaUseCase.test_criar_controle_valido` |
| CT-SEG-028 | `TestCriarControleSegurancaUseCase.test_criar_controle_duplicado_lanca_erro` |
| CT-SEG-029 | `TestCriarControleSegurancaUseCase.test_codigo_invalido_lanca_value_error` |
| CT-SEG-030 | `TestCriarControleSegurancaUseCase.test_nivel_risco_invalido_lanca_erro` |
| CT-SEG-031 | `TestBuscarControleSegurancaUseCase.test_buscar_por_id` |
| CT-SEG-032 | `TestBuscarControleSegurancaUseCase.test_buscar_inexistente_lanca_erro` |
| CT-SEG-033 | `TestBuscarControleSegurancaUseCase.test_listar_vazio` |
| CT-SEG-034 | `TestBuscarControleSegurancaUseCase.test_listar_com_registros` |
| CT-SEG-035 | `TestAtualizarControleSegurancaUseCase.test_atualizar_nome_e_descricao` |
| CT-SEG-036 | `TestAtualizarControleSegurancaUseCase.test_atualizar_inexistente_lanca_erro` |
| CT-SEG-037 | `TestFluxoControleImplementacao.test_implementar_controle` |
| CT-SEG-038 | `TestFluxoControleImplementacao.test_marcar_parcialmente_implementado` |
| CT-SEG-039 | `TestFluxoControleImplementacao.test_deletar_controle_soft_delete` |
| CT-SEG-040 | `TestFluxoControleImplementacao.test_deletar_inexistente_retorna_falso` |
| CT-SEG-041 | `TestCriarPoliticaSegurancaUseCase.test_criar_politica_valida` |
| CT-SEG-042 | `TestCriarPoliticaSegurancaUseCase.test_criar_politica_duplicada_lanca_erro` |
| CT-SEG-043 | `TestCriarPoliticaSegurancaUseCase.test_criar_politica_sem_titulo_lanca_value_error` |
| CT-SEG-044 | `TestBuscarPoliticaSegurancaUseCase.test_buscar_por_id` |
| CT-SEG-045 | `TestBuscarPoliticaSegurancaUseCase.test_buscar_inexistente_lanca_erro` |
| CT-SEG-046 | `TestBuscarPoliticaSegurancaUseCase.test_listar_politicas` |
| CT-SEG-047 | `TestAtualizarPoliticaSegurancaUseCase.test_atualizar_titulo_e_versao` |
| CT-SEG-048 | `TestAtualizarPoliticaSegurancaUseCase.test_atualizar_inexistente_lanca_erro` |
| CT-SEG-049 | `TestFluxoPoliticaAprovacao.test_aprovar_politica` |
| CT-SEG-050 | `TestFluxoPoliticaAprovacao.test_deletar_politica` |
| CT-SEG-051 | `TestRegistrarIncidenteSegurancaUseCase.test_registrar_incidente_valido` |
| CT-SEG-052 | `TestRegistrarIncidenteSegurancaUseCase.test_registrar_sem_titulo_lanca_value_error` |
| CT-SEG-053 | `TestRegistrarIncidenteSegurancaUseCase.test_registrar_severidade_invalida_lanca_erro` |
| CT-SEG-054 | `TestBuscarIncidenteSegurancaUseCase.test_buscar_por_id` |
| CT-SEG-055 | `TestBuscarIncidenteSegurancaUseCase.test_buscar_inexistente_lanca_erro` |
| CT-SEG-056 | `TestBuscarIncidenteSegurancaUseCase.test_listar_incidentes` |
| CT-SEG-057 | `TestFluxoIncidente.test_escalar_incidente` |
| CT-SEG-058 | `TestFluxoIncidente.test_mitigar_incidente` |
| CT-SEG-059 | `TestFluxoIncidente.test_resolver_incidente` |
| CT-SEG-060 | `TestFluxoIncidente.test_resolver_ja_resolvido_lanca_erro` |
| CT-SEG-061 | `TestFluxoIncidente.test_encerrar_incidente` |
| CT-SEG-062 | `TestFluxoIncidente.test_deletar_incidente` |
| CT-SEG-063 | `TestEntidades.test_controle_is_active_reflete_status` |
| CT-SEG-064 | `TestEntidades.test_chave_criptografica_revogada` |
| CT-SEG-065 | `TestEntidades.test_severidade_incidente_enum` |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 019-Seguranca-da-Informacao-Casos-de-Teste.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
