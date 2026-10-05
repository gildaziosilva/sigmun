# 019 – Casos-de-Teste – Integração e Interoperabilidade

#### Casos-de-Teste – Integração e Interoperabilidade

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-INT-019

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

Este artefato detalha **os casos de teste** do domínio Integração e Interoperabilidade (`DOM-INT`), com base na implementação material identificada em `src/modules/sigmun_int` e no conteúdo de negócio declarado no gerador.

---

# 2. Testes

| ID | Teste |
| --- | --- |
| CT-INT-001 | `TestWebhookEntity.test_inscrito_em_wildcard` |
| CT-INT-002 | `TestWebhookEntity.test_inscrito_em_topico_exacto` |
| CT-INT-003 | `TestWebhookEntity.test_inscrito_em_lista_multiple` |
| CT-INT-004 | `TestWebhookEntity.test_inscrito_em_vacia` |
| CT-INT-005 | `TestWebhookEntity.test_esta_ativo` |
| CT-INT-006 | `TestWebhookEntity.test_is_active` |
| CT-INT-007 | `TestEntregaWebhook.test_pendente_para_retry_sem_proximo` |
| CT-INT-008 | `TestEntregaWebhook.test_pendente_para_retry_com_fecha_futura` |
| CT-INT-009 | `TestEntregaWebhook.test_pendente_para_retry_estado_no_pendente` |
| CT-INT-010 | `TestEntregaWebhook.test_pendente_para_retry_estado_fallido` |
| CT-INT-011 | `TestEntregaWebhook.test_registrar_sucesso` |
| CT-INT-012 | `TestEntregaWebhook.test_registrar_falha_no_agoto_tentativas` |
| CT-INT-013 | `TestEntregaWebhook.test_registrar_falha_agota_tentativas_cola_muerta` |
| CT-INT-014 | `TestEntregaWebhook.test_calcular_proximo_retry_backoff_exponencial` |
| CT-INT-015 | `TestEntregaWebhook.test_eh_sucesso` |
| CT-INT-016 | `TestEntregaWebhook.test_en_cola_muerta` |
| CT-INT-017 | `TestEntidadesBasicas.test_api_eh_consumivel` |
| CT-INT-018 | `TestEntidadesBasicas.test_contrato_eh_vigente` |
| CT-INT-019 | `TestEntidadesBasicas.test_conector_esta_ativo` |
| CT-INT-020 | `TestEntidadesBasicas.test_evento_processado_is_active` |
| CT-INT-021 | `TestConectorUseCases.test_conectores_oficiales_constante` |
| CT-INT-022 | `TestConectorUseCases.test_criar_conector_oficial_completa_dados` |
| CT-INT-023 | `TestConectorUseCases.test_criar_conector_personalizado` |
| CT-INT-024 | `TestConectorUseCases.test_criar_conector_codigo_invalido` |
| CT-INT-025 | `TestConectorUseCases.test_criar_conector_duplicado` |
| CT-INT-026 | `TestConectorUseCases.test_buscar_conector_por_id` |
| CT-INT-027 | `TestConectorUseCases.test_buscar_conector_nao_encontrado` |
| CT-INT-028 | `TestConectorUseCases.test_atualizar_conector` |
| CT-INT-029 | `TestConectorUseCases.test_cambiar_estado_conector_sin_configuracion` |
| CT-INT-030 | `TestConectorUseCases.test_cambiar_estado_conector_con_configuracion` |
| CT-INT-031 | `TestConectorUseCases.test_cambiar_estado_conector_nao_encontrado` |
| CT-INT-032 | `TestConectorUseCases.test_eliminar_conector` |
| CT-INT-033 | `TestConectorUseCases.test_eliminar_conector_nao_encontrado` |
| CT-INT-034 | `TestConectorUseCases.test_listar_conectores` |
| CT-INT-035 | `TestApiUseCases.test_criar_api_valida` |
| CT-INT-036 | `TestApiUseCases.test_criar_api_codigo_invalido` |
| CT-INT-037 | `TestApiUseCases.test_criar_api_url_invalida` |
| CT-INT-038 | `TestApiUseCases.test_criar_api_duplicada` |
| CT-INT-039 | `TestApiUseCases.test_buscar_api_por_id` |
| CT-INT-040 | `TestApiUseCases.test_buscar_api_nao_encontrada` |
| CT-INT-041 | `TestApiUseCases.test_atualizar_api` |
| CT-INT-042 | `TestApiUseCases.test_mudar_estado_api` |
| CT-INT-043 | `TestApiUseCases.test_mudar_estado_api_nao_encontrada` |
| CT-INT-044 | `TestApiUseCases.test_deletar_api` |
| CT-INT-045 | `TestApiUseCases.test_deletar_api_nao_encontrada` |
| CT-INT-046 | `TestApiUseCases.test_listar_apis` |
| CT-INT-047 | `TestContratoUseCases.test_criar_contrato_com_api` |
| CT-INT-048 | `TestContratoUseCases.test_criar_contrato_api_inexistente` |
| CT-INT-049 | `TestContratoUseCases.test_criar_contrato_sin_api` |
| CT-INT-050 | `TestContratoUseCases.test_criar_contrato_duplicado` |
| CT-INT-051 | `TestContratoUseCases.test_criar_contrato_codigo_invalido` |
| CT-INT-052 | `TestContratoUseCases.test_approbar_contrato` |
| CT-INT-053 | `TestContratoUseCases.test_approbar_contrato_nao_encontrado` |
| CT-INT-054 | `TestContratoUseCases.test_retirar_contrato` |
| CT-INT-055 | `TestContratoUseCases.test_retirar_contrato_nao_encontrado` |
| CT-INT-056 | `TestContratoUseCases.test_atualizar_contrato` |
| CT-INT-057 | `TestContratoUseCases.test_atualizar_contrato_nao_encontrado` |
| CT-INT-058 | `TestContratoUseCases.test_buscar_contrato_nao_encontrado` |
| CT-INT-059 | `TestContratoUseCases.test_deletar_contrato` |
| CT-INT-060 | `TestContratoUseCases.test_deletar_contrato_nao_encontrado` |
| CT-INT-061 | `TestWebhookUseCases.test_registrar_webhook_valido` |
| CT-INT-062 | `TestWebhookUseCases.test_registrar_webhook_url_invalida` |
| CT-INT-063 | `TestWebhookUseCases.test_registrar_webhook_url_vacia` |
| CT-INT-064 | `TestWebhookUseCases.test_registrar_webhook_nome_corto` |
| CT-INT-065 | `TestWebhookUseCases.test_registrar_webhook_topicos_vacios` |
| CT-INT-066 | `TestWebhookUseCases.test_registrar_webhook_duplicado` |
| CT-INT-067 | `TestWebhookUseCases.test_registrar_webhook_max_tentativas_invalido` |
| CT-INT-068 | `TestWebhookUseCases.test_registrar_webhook_backoff_negativo` |
| CT-INT-069 | `TestWebhookUseCases.test_buscar_webhook` |
| CT-INT-070 | `TestWebhookUseCases.test_buscar_webhook_nao_encontrado` |
| CT-INT-071 | `TestWebhookUseCases.test_atualizar_webhook` |
| CT-INT-072 | `TestWebhookUseCases.test_atualizar_webhook_nao_encontrado` |
| CT-INT-073 | `TestWebhookUseCases.test_mudar_estado_webhook` |
| CT-INT-074 | `TestWebhookUseCases.test_mudar_estado_webhook_nao_encontrado` |
| CT-INT-075 | `TestWebhookUseCases.test_deletar_webhook` |
| CT-INT-076 | `TestWebhookUseCases.test_deletar_webhook_nao_encontrado` |
| CT-INT-077 | `TestWebhookUseCases.test_listar_webhooks` |
| CT-INT-078 | `TestEntregaUseCases.test_get_by_id` |
| CT-INT-079 | `TestEntregaUseCases.test_get_by_id_nao_encontrado` |
| CT-INT-080 | `TestEntregaUseCases.test_reenfileirar_entrega_bem_sucedida` |
| CT-INT-081 | `TestEntregaUseCases.test_reenfileirar_entrega_nao_encontrada` |
| CT-INT-082 | `TestEntregaUseCases.test_reenfileirar_entrega_ja_bem_sucedida` |
| CT-INT-083 | `TestEntregaUseCases.test_reenfileirar_entrega_ja_pendente` |
| CT-INT-084 | `TestEntregaUseCases.test_cancelar_entrega` |
| CT-INT-085 | `TestEntregaUseCases.test_cancelar_entrega_ya_sucessosa` |
| CT-INT-086 | `TestEntregaUseCases.test_listar_entregas` |
| CT-INT-087 | `TestBusUseCases.test_fontes_validas` |
| CT-INT-088 | `TestBusUseCases.test_consumir_outbox_fonte_invalida` |
| CT-INT-089 | `TestBusUseCases.test_consumir_outbox_cria_entregas_para_webhooks_inscritos` |
| CT-INT-090 | `TestBusUseCases.test_consumir_outbox_sin_webhooks_inscritos` |
| CT-INT-091 | `TestBusUseCases.test_consumir_outbox_webhook_wildcard` |
| CT-INT-092 | `TestBusUseCases.test_consumir_outbox_webhook_desativado_no_recebe` |
| CT-INT-093 | `TestBusUseCases.test_consumir_outbox_multiple_webhooks` |
| CT-INT-094 | `TestBusUseCases.test_despachar_webhooks_sucesso` |
| CT-INT-095 | `TestBusUseCases.test_despachar_webhooks_falha_sem_esgotar` |
| CT-INT-096 | `TestBusUseCases.test_despachar_webhooks_falha_esgota_fila_morta` |
| CT-INT-097 | `TestBusUseCases.test_despachar_webhooks_sem_pendentes` |
| CT-INT-098 | `TestBusUseCases.test_despachar_webhooks_payload_envelope` |
| CT-INT-099 | `TestSqlAlchemyApiExternaRepository.test_save_get_codigo_exists_e_list` |
| CT-INT-100 | `TestSqlAlchemyApiExternaRepository.test_update_persiste_alteracoes` |
| CT-INT-101 | `TestSqlAlchemyApiExternaRepository.test_filtros_estado_tipo_e_paginacao` |
| CT-INT-102 | `TestSqlAlchemyApiExternaRepository.test_delete_e_soft_delete` |
| CT-INT-103 | `TestSqlAlchemyApiExternaRepository.test_delete_inexistente_retorna_false` |
| CT-INT-104 | `TestSqlAlchemyContratoIntegracaoRepository.test_save_get_codigo_exists_e_list_por_api` |
| CT-INT-105 | `TestSqlAlchemyContratoIntegracaoRepository.test_update_e_filtro_por_estado` |
| CT-INT-106 | `TestSqlAlchemyContratoIntegracaoRepository.test_delete_e_soft_delete` |
| CT-INT-107 | `TestSqlAlchemyContratoIntegracaoRepository.test_fk_api_externa_rejeita_id_inexistente` |
| CT-INT-108 | `TestSqlAlchemyConectorRepository.test_save_get_codigo_exists_e_list` |
| CT-INT-109 | `TestSqlAlchemyConectorRepository.test_filtro_estado_e_paginacao` |
| CT-INT-110 | `TestSqlAlchemyConectorRepository.test_update_e_delete` |
| CT-INT-111 | `TestSqlAlchemyWebhookRepository.test_save_get_nome_exists_list_e_ativos` |
| CT-INT-112 | `TestSqlAlchemyWebhookRepository.test_update_e_delete` |
| CT-INT-113 | `TestSqlAlchemyEntregaWebhookRepository.test_save_get_e_list_by_webhook` |
| CT-INT-114 | `TestSqlAlchemyEntregaWebhookRepository.test_list_pendentes_para_retry_respeita_janela` |
| CT-INT-115 | `TestSqlAlchemyEntregaWebhookRepository.test_list_pendentes_respeita_lote_e_estado` |
| CT-INT-116 | `TestSqlAlchemyEntregaWebhookRepository.test_fk_webhook_rejeita_id_inexistente` |
| CT-INT-117 | `TestSqlAlchemyEntregaWebhookRepository.test_update_e_delete` |
| CT-INT-118 | `TestSqlAlchemyEventoProcessadoRepository.test_save_get_exists_e_list` |
| CT-INT-119 | `TestSqlAlchemyEventoProcessadoRepository.test_delete_remove_evento_da_consulta_logica` |
| CT-INT-120 | `TestSqlAlchemyEventoProcessadoRepository.test_constraint_idempotencia_fonte_evento` |
| CT-INT-121 | `TestSqlAlchemyEventoProcessadoRepository.test_mesmo_id_em_fontes_diferentes_e_permitido` |
| CT-INT-122 | `TestSqlAlchemyEventoProcessadoRepository.test_paginacao_e_filtro_por_fonte` |
| CT-INT-123 | `TestSqlAlchemyEventoProcessadoRepository.test_delete_inexistente_retorna_false` |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 019-Integracao-e-Interoperabilidade-Casos-de-Teste.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
