# 019 – Casos de Teste – Obras e Infraestrutura

#### Casos de Teste – Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OBR-019

**Domínio:** Obras e Infraestrutura

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Obras-e-Infraestrutura.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000C-HIERARQUIA-DOCUMENTAL.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `030-Roadmap-de-Implementacao-dos-Dominios.md`
* `Mapa-de-Dominios.md`
* `Modelo-Logico.md`
* `Modelo-Fisico.md`
* `Dicionario-de-dados.md`

---

# 1. Finalidade

Este artefato cataloga os casos de teste implementados para o domínio de
Obras e Infraestrutura, vinculando cada um às regras de negócio exercitadas.

---

# 2. Convenções

* O nome do caso de teste descreve o comportamento esperado e referencia a regra
  exercitada, quando aplicável.
* Casos sem referência explícita exercitam regras de estrutura da entidade.

---

# 3. Casos de Teste

### TestEtapas

**Arquivo:** `tests/unit/test_obr_acompanhamento_use_cases.py` · **Testes:** 11

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_cadastra_etapa` | estrutura da entidade |
| 2 | `test_cadastra_etapa_em_obra_inexistente` | estrutura da entidade |
| 3 | `test_responsavel_da_etapa_obrigatorio` | estrutura da entidade |
| 4 | `test_etapa_de_peso_parcial_aceita_100_de_conclusao` | estrutura da entidade |
| 5 | `test_percentual_realizado_fora_de_faixa_rejeitado` | estrutura da entidade |
| 6 | `test_atualiza_avanco_da_etapa` | estrutura da entidade |
| 7 | `test_atualiza_etapa_inexistente` | estrutura da entidade |
| 8 | `test_atualiza_etapa_com_situacao_invalida` | regra de situação |
| 9 | `test_conclui_etapa_com_100_realizado` | estrutura da entidade |
| 10 | `test_conclui_etapa_incompleta_rejeitado` | estrutura da entidade |
| 11 | `test_conclui_etapa_inexistente` | estrutura da entidade |
### TestVistorias

**Arquivo:** `tests/unit/test_obr_acompanhamento_use_cases.py` · **Testes:** 5

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_registra_vistoria_periodica` | estrutura da entidade |
| 2 | `test_registra_vistoria_reprovada` | estrutura da entidade |
| 3 | `test_registra_vistoria_em_obra_inexistente` | estrutura da entidade |
| 4 | `test_fiscal_obrigatorio` | estrutura da entidade |
| 5 | `test_percentual_verificado_fora_de_faixa_rejeitado` | estrutura da entidade |
### TestRegistroMedicao

**Arquivo:** `tests/unit/test_obr_medicao_use_cases.py` · **Testes:** 7

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_registra_medicao_em_obra_em_execucao` | estrutura da entidade |
| 2 | `test_registra_medicao_em_obra_planejada_rejeitado` | estrutura da entidade |
| 3 | `test_obra_inexistente_rejeitada` | estrutura da entidade |
| 4 | `test_numero_de_medicao_duplicado_rejeitado` | estrutura da entidade |
| 5 | `test_valor_acima_do_contratado_rejeitado` | estrutura da entidade |
| 6 | `test_percentual_acima_de_100_rejeitado` | estrutura da entidade |
| 7 | `test_responsavel_tecnico_obrigatorio` | estrutura da entidade |
### TestCicloMedicao

**Arquivo:** `tests/unit/test_obr_medicao_use_cases.py` · **Testes:** 6

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_aprova_medicao_e_recompoe_avanco_da_obra` | estrutura da entidade |
| 2 | `test_avanco_financeiro_limitado_ao_fisico` | estrutura da entidade |
| 3 | `test_glosa_medicao_exige_justificativa` | estrutura da entidade |
| 4 | `test_glosa_medicao_conferida` | estrutura da entidade |
| 5 | `test_medicao_aprovada_nao_e_cancelada` | estrutura da entidade |
| 6 | `test_medicao_inexistente` | estrutura da entidade |
### TestDespesas

**Arquivo:** `tests/unit/test_obr_medicao_use_cases.py` · **Testes:** 6

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_registra_despesa_ate_o_saldo_mediado` | estrutura da entidade |
| 2 | `test_despesa_acima_do_saldo_mediado_rejeitada` | estrutura da entidade |
| 3 | `test_despesa_sem_saldo_mediado_rejeitada` | estrutura da entidade |
| 4 | `test_despesa_em_obra_planejada_rejeitada` | estrutura da entidade |
| 5 | `test_exclui_despesa_e_recompoe_avanco` | estrutura da entidade |
| 6 | `test_exclui_despesa_inexistente` | estrutura da entidade |
### TestCadastroObra

**Arquivo:** `tests/unit/test_obr_obra_use_cases.py` · **Testes:** 5

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_cadastra_obra_planejada` | estrutura da entidade |
| 2 | `test_numero_duplicado_rejeitado` | estrutura da entidade |
| 3 | `test_valor_contratado_acima_do_orcado_rejeitado` | estrutura da entidade |
| 4 | `test_valor_negativo_rejeitado` | estrutura da entidade |
| 5 | `test_datas_previstas_invertidas_rejeitadas` | estrutura da entidade |
### TestCicloVidaObra

**Arquivo:** `tests/unit/test_obr_obra_use_cases.py` · **Testes:** 9

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_inicia_execucao` | estrutura da entidade |
| 2 | `test_inicia_execucao_sem_empresa_rejeitado` | estrutura da entidade |
| 3 | `test_inicia_execucao_de_obra_planejada_rejeitado` | estrutura da entidade |
| 4 | `test_suspende_obra_em_execucao` | estrutura da entidade |
| 5 | `test_conclui_obra_com_100_fisico` | estrutura da entidade |
| 6 | `test_conclui_obra_incompleta_rejeitado` | estrutura da entidade |
| 7 | `test_obra_concluida_nao_retorna_a_execucao` | estrutura da entidade |
| 8 | `test_cancela_obra_planejada` | estrutura da entidade |
| 9 | `test_obra_inexistente_no_ciclo` | estrutura da entidade |
### TestAtualizacaoEExclusaoObra

**Arquivo:** `tests/unit/test_obr_obra_use_cases.py` · **Testes:** 6

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_atualiza_obra` | estrutura da entidade |
| 2 | `test_atualiza_obra_inexistente` | estrutura da entidade |
| 3 | `test_obra_concluida_nao_aceita_alteracao` | estrutura da entidade |
| 4 | `test_exclui_obra_sem_dependencias` | estrutura da entidade |
| 5 | `test_exclui_obra_com_mediacao_rejeitado` | estrutura da entidade |
| 6 | `test_exclui_obra_com_despesa_rejeitado` | estrutura da entidade |

# 4. Totais

| Indicador | Quantidade |
| --- | |
| Arquivos de teste unitário | 3 |
| Classes de teste | 8 |
| Casos de teste | 55 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 019-Casos-de-Teste-Obras-e-Infraestrutura.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_obras`. Alterações no código devem ser
> refletidas reexecutando o gerador.
