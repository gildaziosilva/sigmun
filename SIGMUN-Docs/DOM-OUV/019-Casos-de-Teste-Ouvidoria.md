# 019 – Casos-de-Teste – Ouvidoria

#### Casos-de-Teste – Ouvidoria

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OUV-019

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

Este artefato detalha **os casos de teste** do domínio Ouvidoria (`DOM-OUV`), com base na implementação material identificada em `src/modules/sigmun_ouvidoria` e no conteúdo de negócio declarado no gerador.

---

# 2. Testes

| ID | Teste |
| --- | --- |
| CT-OU-001 | `TestProtocolo.test_gerar_formata_com_seis_digitos` |
| CT-OU-002 | `TestProtocolo.test_numero_invalido_rejeitado` |
| CT-OU-003 | `TestProtocolo.test_numero_vazio_rejeitado` |
| CT-OU-004 | `TestProtocolo.test_str_retorna_codigo` |
| CT-OU-005 | `TestTransicoesDeStatus.test_transicao_valida_permitida` |
| CT-OU-006 | `TestTransicoesDeStatus.test_transicao_invalida_proibida` |
| CT-OU-007 | `TestTransicoesDeStatus.test_alterar_status_atualiza_campos_de_auditoria` |
| CT-OU-008 | `TestTransicoesDeStatus.test_alterar_status_invalido_lanca_erro` |
| CT-OU-009 | `TestCalculadoraPrazo.test_prazo_por_tipo` |
| CT-OU-010 | `TestCalculadoraPrazo.test_prorrogacao_soma_dez_dias` |
| CT-OU-011 | `TestCalculadoraPrazo.test_calcular_prorrogacao_avanca_dez_dias` |
| CT-OU-012 | `TestCalculadoraPrazo.test_prorrogacao_duplicada_rejeitada` |
| CT-OU-013 | `TestCalculadoraPrazo.test_vencimento` |
| CT-OU-014 | `TestCalculadoraPrazo.test_prorrogar_prazo_na_entidade` |
| CT-OU-015 | `TestCalculadoraPrazo.test_prorrogar_sem_prazo_rejeitado` |
| CT-OU-016 | `TestCalculadoraPrazo.test_prorrogar_duas_vezes_rejeitado` |
| CT-OU-017 | `TestCalculadoraPrazo.test_verificar_prazo_sem_prazo_nao_vence` |
| CT-OU-018 | `TestDadosCidadao.test_cpf_invalido_rejeitado` |
| CT-OU-019 | `TestDadosCidadao.test_email_invalido_rejeitado` |
| CT-OU-020 | `TestDadosCidadao.test_nome_obrigatorio_quando_identificado` |
| CT-OU-021 | `TestDadosCidadao.test_anonimo_nao_exige_nome` |
| CT-OU-022 | `TestDadosCidadao.test_mascaramento_cpf_e_email` |
| CT-OU-023 | `TestDadosCidadao.test_exibicao_anonima_nao_traz_identificacao` |
| CT-OU-024 | `TestDadosCidadao.test_servico_lgpd_mascara` |
| CT-OU-025 | `TestDadosCidadao.test_servico_lgpd_anonimiza` |
| CT-OU-026 | `TestDadosCidadao.test_acesso_a_dados_sensiveis_por_papel` |
| CT-OU-027 | `TestValidacaoManifestacao.test_manifestacao_valida_nao_lanca` |
| CT-OU-028 | `TestValidacaoManifestacao.test_campos_obrigatorios` |
| CT-OU-029 | `TestValidacaoManifestacao.test_manifestacao_anonima_sem_identificacao_rejeitada` |
| CT-OU-030 | `TestValidacaoManifestacao.test_manifestacao_sem_cidadao_rejeitada` |
| CT-OU-031 | `TestValidacaoManifestacao.test_denuncia_anonima_e_aceita` |
| CT-OU-032 | `TestValidacaoManifestacao.test_denuncia_sem_local_rejeitada` |
| CT-OU-033 | `TestValidacaoManifestacao.test_denuncia_sem_data_rejeitada` |
| CT-OU-034 | `TestRespostaEAvaliacao.test_responde_somente_em_tratamento` |
| CT-OU-035 | `TestRespostaEAvaliacao.test_resposta_muda_status_para_respondida` |
| CT-OU-036 | `TestRespostaEAvaliacao.test_avaliacao_exige_status_respondida` |
| CT-OU-037 | `TestRespostaEAvaliacao.test_avaliacao_fora_da_faixa_rejeitada` |
| CT-OU-038 | `TestRespostaEAvaliacao.test_avaliacao_valida_conclui_manifestacao` |
| CT-OU-039 | `TestDenuncia.test_encaminhar_marca_orgao_correspondente` |
| CT-OU-040 | `TestDenuncia.test_encaminhar_aceita_minusculo` |
| CT-OU-041 | `TestDenuncia.test_dados_sigilosos_negados_a_nao_autorizado` |
| CT-OU-042 | `TestDenuncia.test_dados_sigilosos_mascarados_para_autorizado` |
| CT-OU-043 | `TestDenuncia.test_dados_sigilosos_vazio_sem_cidadao` |
| CT-OU-044 | `TestDenuncia.test_concluir_investigacao` |
| CT-OU-045 | `TestPedidoLai.test_valido_ajusta_o_tipo` |
| CT-OU-046 | `TestPedidoLai.test_sem_informacao_solicitada_rejeitado` |
| CT-OU-047 | `TestPedidoLai.test_sem_fundamentacao_rejeitado` |
| CT-OU-048 | `TestPedidoLai.test_sigilo_nao_publico_exige_fundamentacao` |
| CT-OU-049 | `TestPedidoLai.test_classificar_sigilo` |
| CT-OU-050 | `TestPedidoLai.test_interpor_recurso_cria_novo_pedido_vinculado` |
| CT-OU-051 | `TestPedidoLai.test_decidir_recurso_deferido_conclui` |
| CT-OU-052 | `TestPedidoLai.test_decidir_recurso_indeferido_arquiva` |
| CT-OU-053 | `TestPedidoLai.test_decidir_pedido_que_nao_e_recurso_rejeitado` |
| CT-OU-054 | `TestValidadorManifestacao.test_avisa_ausencia_de_prazo` |
| CT-OU-055 | `TestValidadorManifestacao.test_avisa_denuncia_identificada` |
| CT-OU-056 | `TestValidadorManifestacao.test_manifestacao_completa_sem_avisos` |
| CT-OU-057 | `TestValidadorManifestacao.test_validar_resposta_bloqueia_status_invalido` |
| CT-OU-058 | `TestValidadorManifestacao.test_validar_resposta_permite_em_tratamento` |
| CT-OU-059 | `TestValidadorManifestacao.test_validar_transicao_bloqueia_pulo_de_etapa` |
| CT-OU-060 | `TestPrioridade.test_rotulos` |
| CT-OU-061 | `TestExclusaoLogica.test_excluir_marca_is_deleted` |
| CT-OU-062 | `TestAdicionarAnexo.test_anexo_e_adicionado` |
| CT-OU-063 | `TestEnumsDeSuporte.test_canais_falabr` |
| CT-OU-064 | `TestEnumsDeSuporte.test_prazos_de_sigilo_conforme_lai` |
| CT-OU-065 | `TestRegistrarManifestacaoUseCase.test_registra_com_protocolo_sequencial` |
| CT-OU-066 | `TestRegistrarManifestacaoUseCase.test_segundo_registro_incrementa_sequencial` |
| CT-OU-067 | `TestRegistrarManifestacaoUseCase.test_gera_prazo_conforme_tipo` |
| CT-OU-068 | `TestRegistrarManifestacaoUseCase.test_anexos_sao_convertidos` |
| CT-OU-069 | `TestRegistrarManifestacaoUseCase.test_tipo_com_use_case_proprio_rejeitado` |
| CT-OU-070 | `TestRegistrarManifestacaoUseCase.test_manifestacao_anonima_rejeitada` |
| CT-OU-071 | `TestRegistrarDenunciaUseCase.test_registra_denuncia_anonima` |
| CT-OU-072 | `TestRegistrarDenunciaUseCase.test_denuncia_com_privilegio_alta` |
| CT-OU-073 | `TestRegistrarDenunciaUseCase.test_denuncia_sem_local_rejeitada` |
| CT-OU-074 | `TestRegistrarPedidoLaiUseCase.test_registra_pedido_com_prazo_de_20_dias` |
| CT-OU-075 | `TestRegistrarPedidoLaiUseCase.test_sem_fundamentacao_rejeitado` |
| CT-OU-076 | `TestResponderManifestacaoUseCase.test_responde_manifestacao_em_tratamento` |
| CT-OU-077 | `TestResponderManifestacaoUseCase.test_responde_denuncia` |
| CT-OU-078 | `TestResponderManifestacaoUseCase.test_responde_pedido_lai` |
| CT-OU-079 | `TestResponderManifestacaoUseCase.test_manifestacao_inexistente` |
| CT-OU-080 | `TestResponderManifestacaoUseCase.test_status_invalido_para_responder` |
| CT-OU-081 | `TestAlterarStatusUseCase.test_altera_status_manifestacao` |
| CT-OU-082 | `TestAlterarStatusUseCase.test_transicao_invalida_rejeitada` |
| CT-OU-083 | `TestAlterarStatusUseCase.test_altera_status_denuncia` |
| CT-OU-084 | `TestAlterarStatusUseCase.test_altera_status_pedido_lai` |
| CT-OU-085 | `TestAlterarStatusUseCase.test_inexistente` |
| CT-OU-086 | `TestAlterarStatusUseCase.test_status_invalido_rejeitado` |
| CT-OU-087 | `TestProrrogarPrazoUseCase.test_prorroga_manifestacao` |
| CT-OU-088 | `TestProrrogarPrazoUseCase.test_prorroga_denuncia` |
| CT-OU-089 | `TestProrrogarPrazoUseCase.test_prorroga_pedido_lai` |
| CT-OU-090 | `TestProrrogarPrazoUseCase.test_inexistente` |
| CT-OU-091 | `TestAvaliarManifestacaoUseCase.test_avalia_e_conclui` |
| CT-OU-092 | `TestAvaliarManifestacaoUseCase.test_nota_fora_da_faixa_rejeitada` |
| CT-OU-093 | `TestAvaliarManifestacaoUseCase.test_manifestacao_inexistente` |
| CT-OU-094 | `TestEncaminharDenunciaUseCase.test_encaminha_para_mp` |
| CT-OU-095 | `TestEncaminharDenunciaUseCase.test_orgao_desconhecido_rejeitado` |
| CT-OU-096 | `TestEncaminharDenunciaUseCase.test_denuncia_inexistente` |
| CT-OU-097 | `TestRecursoLaiUseCase.test_interpoe_recurso_de_pedido_arquivado` |
| CT-OU-098 | `TestRecursoLaiUseCase.test_pedido_nao_arquivado_rejeita_recurso` |
| CT-OU-099 | `TestRecursoLaiUseCase.test_interpor_recurso_pedido_inexistente` |
| CT-OU-100 | `TestRecursoLaiUseCase.test_decide_recurso` |
| CT-OU-101 | `TestRecursoLaiUseCase.test_decidir_pedido_que_nao_e_recurso` |
| CT-OU-102 | `TestRecursoLaiUseCase.test_decidir_recurso_inexistente` |
| CT-OU-103 | `TestListagemEEstatisticas.test_lista_com_paginacao` |
| CT-OU-104 | `TestListagemEEstatisticas.test_lista_vazia` |
| CT-OU-105 | `TestListagemEEstatisticas.test_consulta_por_id` |
| CT-OU-106 | `TestListagemEEstatisticas.test_consulta_inexistente` |
| CT-OU-107 | `TestListagemEEstatisticas.test_indicadores_agregam_os_tres_tipos` |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 019-Ouvidoria-Casos-de-Teste.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
