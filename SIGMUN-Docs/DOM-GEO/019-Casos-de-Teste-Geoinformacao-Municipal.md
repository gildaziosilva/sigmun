# 019 – Casos de Teste – Geoinformação Municipal

#### Casos de Teste – Geoinformação Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GEO-019

**Domínio:** Geoinformação Municipal

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Geoinformacao-Municipal.md`
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
Geoinformação Municipal, vinculando cada um às regras de negócio exercitadas.

---

# 2. Convenções

* O nome do caso de teste descreve o comportamento esperado e referencia a regra
  exercitada, quando aplicável.
* Casos sem referência explícita exercitam regras de estrutura da entidade.

---

# 3. Casos de Teste

### TestCadastroCamada

**Arquivo:** `tests/unit/test_geo_camada_use_cases.py` · **Testes:** 5

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_cadastra_camada_em_rascunho` | estrutura da entidade |
| 2 | `test_codigo_duplicado_rejeitado` | estrutura da entidade |
| 3 | `test_tipo_invalido_rejeitado` | estrutura da entidade |
| 4 | `test_zoom_invertido_rejeitado` | estrutura da entidade |
| 5 | `test_zoom_fora_de_faixa_rejeitado` | estrutura da entidade |
### TestCicloCamada

**Arquivo:** `tests/unit/test_geo_camada_use_cases.py` · **Testes:** 5

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_ativa_camada` | estrutura da entidade |
| 2 | `test_ativar_camada_inexistente` | estrutura da entidade |
| 3 | `test_desativa_camada` | estrutura da entidade |
| 4 | `test_camada_desativada_nao_e_reativada` | estrutura da entidade |
| 5 | `test_camada_de_servico_ativa_exige_url` | estrutura da entidade |
### TestAtualizacaoCamada

**Arquivo:** `tests/unit/test_geo_camada_use_cases.py` · **Testes:** 3

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_atualiza_campos` | estrutura da entidade |
| 2 | `test_atualiza_camada_inexistente` | estrutura da entidade |
| 3 | `test_codigo_duplicado_na_atualizacao_rejeitado` | estrutura da entidade |
### TestExclusaoCamada

**Arquivo:** `tests/unit/test_geo_camada_use_cases.py` · **Testes:** 4

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_exclui_camada_sem_mapa_publicado` | estrutura da entidade |
| 2 | `test_exclui_camada_inexistente` | estrutura da entidade |
| 3 | `test_camada_de_mapa_publicado_nao_pode_ser_excluida` | estrutura da entidade |
| 4 | `test_camada_de_mapa_rascunho_pode_ser_excluida` | estrutura da entidade |
### TestElementosGeoespaciais

**Arquivo:** `tests/unit/test_geo_feature_servico_use_cases.py` · **Testes:** 10

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_registra_ponto_de_interesse` | estrutura da entidade |
| 2 | `test_ponto_adota_primeiro_vertice_como_coordenada` | regra de geometria |
| 3 | `test_registra_poligono` | estrutura da entidade |
| 4 | `test_poligono_com_vertices_insuficientes_rejeitado` | regra de geometria |
| 5 | `test_elemento_exige_camada` | estrutura da entidade |
| 6 | `test_elemento_em_camada_inexistente` | estrutura da entidade |
| 7 | `test_codigo_duplicado_na_camada_rejeitado` | estrutura da entidade |
| 8 | `test_latitude_fora_de_faixa_rejeitada` | estrutura da entidade |
| 9 | `test_exclui_elemento` | estrutura da entidade |
| 10 | `test_exclui_elemento_inexistente` | estrutura da entidade |
### TestServicosGeoespaciais

**Arquivo:** `tests/unit/test_geo_feature_servico_use_cases.py` · **Testes:** 11

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_cadastra_servico_wms` | estrutura da entidade |
| 2 | `test_codigo_duplicado_rejeitado` | estrutura da entidade |
| 3 | `test_servico_ativo_sem_url_rejeitado` | estrutura da entidade |
| 4 | `test_servico_com_url_invalida_rejeitado` | estrutura da entidade |
| 5 | `test_wms_sem_nome_de_camada_rejeitado` | estrutura da entidade |
| 6 | `test_tipo_invalido_rejeitado` | estrutura da entidade |
| 7 | `test_zoom_invertido_rejeitado` | estrutura da entidade |
| 8 | `test_atualiza_servico` | estrutura da entidade |
| 9 | `test_atualiza_servico_inexistente` | estrutura da entidade |
| 10 | `test_inativa_servico` | estrutura da entidade |
| 11 | `test_exclui_servico` | estrutura da entidade |
### TestCadastroMapa

**Arquivo:** `tests/unit/test_geo_mapa_use_cases.py` · **Testes:** 4

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_cadastra_mapa_em_rascunho` | estrutura da entidade |
| 2 | `test_codigo_duplicado_rejeitado` | estrutura da entidade |
| 3 | `test_zoom_inicial_fora_dos_limites_rejeitado` | estrutura da entidade |
| 4 | `test_extensao_invertida_rejeitada` | estrutura da entidade |
### TestComposicao

**Arquivo:** `tests/unit/test_geo_mapa_use_cases.py` · **Testes:** 7

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_compõe_camada_ativa` | estrutura da entidade |
| 2 | `test_compõe_camada_inexistente` | estrutura da entidade |
| 3 | `test_camada_rascunho_nao_compoe_mapa` | estrutura da entidade |
| 4 | `test_mapa_publicado_nao_aceita_nova_composicao` | estrutura da entidade |
| 5 | `test_opacidade_fora_de_faixa_rejeitada` | estrutura da entidade |
| 6 | `test_remove_composicao_de_mapa_rascunho` | estrutura da entidade |
| 7 | `test_remove_composicao_de_mapa_publicado_rejeitado` | estrutura da entidade |
### TestPublicacaoMapa

**Arquivo:** `tests/unit/test_geo_mapa_use_cases.py` · **Testes:** 7

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_publica_mapa_com_camada_ativa` | estrutura da entidade |
| 2 | `test_publica_mapa_sem_camadas_rejeitado` | estrutura da entidade |
| 3 | `test_publica_mapa_com_camada_rascunho_rejeitado` | estrutura da entidade |
| 4 | `test_publica_mapa_inexistente` | estrutura da entidade |
| 5 | `test_arquiva_mapa_publicado` | estrutura da entidade |
| 6 | `test_arquiva_mapa_rascunho_rejeitado` | estrutura da entidade |
| 7 | `test_arquivado_nao_e_publicado_novamente` | estrutura da entidade |
### TestAtualizacaoEExclusaoMapa

**Arquivo:** `tests/unit/test_geo_mapa_use_cases.py` · **Testes:** 5

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_atualiza_mapa` | estrutura da entidade |
| 2 | `test_atualiza_mapa_inexistente` | estrutura da entidade |
| 3 | `test_codigo_de_mapa_publicado_e_imutavel` | estrutura da entidade |
| 4 | `test_exclui_mapa_rascunho` | estrutura da entidade |
| 5 | `test_exclui_mapa_publicado_rejeitado` | estrutura da entidade |

# 4. Totais

| Indicador | Quantidade |
| --- | |
| Arquivos de teste unitário | 3 |
| Classes de teste | 10 |
| Casos de teste | 61 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 019-Casos-de-Teste-Geoinformacao-Municipal.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_geoinformacao`. Alterações no código devem ser
> refletidas reexecutando o gerador.
