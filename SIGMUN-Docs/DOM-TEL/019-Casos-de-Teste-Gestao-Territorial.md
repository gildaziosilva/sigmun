# 019 – Casos de Teste – Gestão Territorial

#### Casos de Teste – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-019

**Domínio:** Gestão Territorial

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Territorial.md`
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
Gestão Territorial, vinculando cada um às regras de negócio exercitadas.

---

# 2. Convenções

* O nome do caso de teste descreve o comportamento esperado e referencia a regra
  exercitada, quando aplicável.
* Casos sem referência explícita exercitam regras de estrutura da entidade.

---

# 3. Casos de Teste

### TestBairro

**Arquivo:** `tests/unit/test_tel_bairro_use_cases.py` · **Testes:** 14

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_cadastra_bairro` | estrutura da entidade |
| 2 | `test_nao_duplica_codigo` | regra de código |
| 3 | `test_codigo_e_nome_obrigatorios` | regra de código |
| 4 | `test_tipo_invalido_rejeitado` | estrutura da entidade |
| 5 | `test_area_negativa_rejeitada` | regra de áreas |
| 6 | `test_atualiza_campos` | estrutura da entidade |
| 7 | `test_atualiza_situacao_inativa_e_ativa` | regra de situação |
| 8 | `test_atualiza_tipo_invalido` | estrutura da entidade |
| 9 | `test_atualiza_codigo_duplicado` | estrutura da entidade |
| 10 | `test_atualiza_bairro_inexistente` | estrutura da entidade |
| 11 | `test_exclui_logicamente` | estrutura da entidade |
| 12 | `test_bairro_com_logradouro_ativo_bloqueia_exclusao` | regra de exclusão |
| 13 | `test_bairro_com_logradouro_inativo_pode_ser_excluido` | regra de exclusão |
| 14 | `test_exclui_bairro_inexistente` | regra de exclusão |
### TestGeorreferencia

**Arquivo:** `tests/unit/test_tel_geo_use_cases.py` · **Testes:** 17

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_registra_ponto_de_bairro` | estrutura da entidade |
| 2 | `test_registra_poligono_de_logradouro` | estrutura da entidade |
| 3 | `test_ponto_adota_primeiro_vertice_como_coordenada` | regra de geometria |
| 4 | `test_exige_bairro_ou_logradouro` | regra de vínculo |
| 5 | `test_recusa_bairro_e_logradouro_simultaneos` | estrutura da entidade |
| 6 | `test_exige_bairro_existente` | regra de vínculo |
| 7 | `test_exige_logradouro_existente` | estrutura da entidade |
| 8 | `test_latitude_fora_de_faixa_rejeitada` | estrutura da entidade |
| 9 | `test_longitude_fora_de_faixa_rejeitada` | estrutura da entidade |
| 10 | `test_vertice_fora_de_faixa_rejeitado` | regra de geometria |
| 11 | `test_poligono_exige_tres_vertices` | regra de geometria |
| 12 | `test_vertice_invalido_rejeitado` | regra de geometria |
| 13 | `test_geometria_invalida_rejeitada` | regra de geometria |
| 14 | `test_datum_invalido_rejeitado` | regra de geometria |
| 15 | `test_precisao_negativa_rejeitada` | estrutura da entidade |
| 16 | `test_exclui_logicamente` | estrutura da entidade |
| 17 | `test_exclui_georreferencia_inexistente` | regra de georreferência |
### TestLogradouro

**Arquivo:** `tests/unit/test_tel_logradouro_use_cases.py` · **Testes:** 12

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_cadastra_logradouro` | estrutura da entidade |
| 2 | `test_nao_duplica_codigo` | regra de código |
| 3 | `test_exige_bairro_existente` | regra de vínculo |
| 4 | `test_codigo_e_nome_obrigatorios` | regra de código |
| 5 | `test_tipo_invalido_rejeitado` | estrutura da entidade |
| 6 | `test_numero_final_menor_que_inicial_rejeitado` | regra de numeração |
| 7 | `test_atualiza_campos` | estrutura da entidade |
| 8 | `test_atualiza_situacao_em_obra` | regra de situação |
| 9 | `test_atualiza_tipo_invalido` | estrutura da entidade |
| 10 | `test_atualiza_logradouro_inexistente` | estrutura da entidade |
| 11 | `test_exclui_logicamente` | estrutura da entidade |
| 12 | `test_exclui_logradouro_inexistente` | estrutura da entidade |
### TestPlantaValores

**Arquivo:** `tests/unit/test_tel_planta_use_cases.py` · **Testes:** 19

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_cadastra_planta_rascunho` | regra de planta |
| 2 | `test_cadastra_ja_vigente` | estrutura da entidade |
| 3 | `test_nao_duplica_planta_vigente` | regra de planta |
| 4 | `test_exige_bairro` | regra de vínculo |
| 5 | `test_exige_bairro_existente` | regra de vínculo |
| 6 | `test_ocupacao_invalida_rejeitada` | estrutura da entidade |
| 7 | `test_ano_invalido_rejeitado` | estrutura da entidade |
| 8 | `test_valor_negativo_rejeitado` | estrutura da entidade |
| 9 | `test_aliquota_fora_de_faixa_rejeitada` | regra de valor venal |
| 10 | `test_ativa_planta` | regra de planta |
| 11 | `test_planta_inexistente_nao_ativa` | regra de planta |
| 12 | `test_nao_ativa_planta_ja_vigente` | regra de planta |
| 13 | `test_revoga_planta_com_justificativa` | regra de planta |
| 14 | `test_revogacao_exige_motivo` | estrutura da entidade |
| 15 | `test_nao_revoga_planta_rascunho` | regra de planta |
| 16 | `test_atualiza_planta_rascunho` | regra de planta |
| 17 | `test_nao_atualiza_planta_vigente` | regra de planta |
| 18 | `test_atualiza_valor_negativo_rejeitado` | estrutura da entidade |
| 19 | `test_atualiza_planta_inexistente` | regra de planta |

# 4. Totais

| Indicador | Quantidade |
| --- | |
| Arquivos de teste unitário | 4 |
| Classes de teste | 4 |
| Casos de teste | 62 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 019-Casos-de-Teste-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
