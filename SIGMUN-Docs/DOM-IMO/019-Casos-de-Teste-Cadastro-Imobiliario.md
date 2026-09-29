# 019 – Casos de Teste – Cadastro Imobiliário

#### Casos de Teste – Cadastro Imobiliário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IMO-019

**Domínio:** Cadastro Imobiliário

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Cadastro-Imobiliario.md`
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
Cadastro Imobiliário, vinculando cada um às regras de negócio exercitadas.

---

# 2. Convenções

* O nome do caso de teste descreve o comportamento esperado e referencia a regra
  exercitada, quando aplicável.
* Casos sem referência explícita exercitam regras de estrutura da entidade.

---

# 3. Casos de Teste

### TestAvaliacao

**Arquivo:** `tests/unit/test_imo_avaliacao_use_cases.py` · **Testes:** 14

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_calcula_valor_venal` | regra de valor venal |
| 2 | `test_avaliacao_em_rascunho` | estrutura da entidade |
| 3 | `test_exige_imovel_existente` | estrutura da entidade |
| 4 | `test_nao_reavalia_exercicio_concluido` | estrutura da entidade |
| 5 | `test_imovel_sem_area_nao_e_avaliado` | estrutura da entidade |
| 6 | `test_valores_unitarios_negativos_rejeitados` | estrutura da entidade |
| 7 | `test_aliquota_fora_de_faixa_rejeitada` | regra de valor venal |
| 8 | `test_ano_invalido_rejeitado` | estrutura da entidade |
| 9 | `test_conclui_avaliacao_rascunho` | estrutura da entidade |
| 10 | `test_nao_conclui_avaliacao_ja_concluida` | estrutura da entidade |
| 11 | `test_conclui_avaliacao_inexistente` | estrutura da entidade |
| 12 | `test_cancela_avaliacao_rascunho` | estrutura da entidade |
| 13 | `test_nao_cancela_avaliacao_concluida` | estrutura da entidade |
| 14 | `test_cancela_avaliacao_inexistente` | estrutura da entidade |
### TestOcupacao

**Arquivo:** `tests/unit/test_imo_avaliacao_use_cases.py` · **Testes:** 1

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_resolve_ocupacao` | estrutura da entidade |
### TestGeometria

**Arquivo:** `tests/unit/test_imo_geometria_use_cases.py` · **Testes:** 11

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_registra_poligono_do_lote` | estrutura da entidade |
| 2 | `test_ponto_adota_vertice_como_coordenada` | regra de geometria |
| 3 | `test_substitui_geometria_anterior` | regra de geometria |
| 4 | `test_exige_imovel_existente` | estrutura da entidade |
| 5 | `test_poligono_exige_tres_vertices` | regra de geometria |
| 6 | `test_linha_exige_dois_vertices` | regra de geometria |
| 7 | `test_geometria_invalida_rejeitada` | regra de geometria |
| 8 | `test_datum_invalido_rejeitado` | regra de geometria |
| 9 | `test_coordenada_fora_de_faixa_rejeitada` | estrutura da entidade |
| 10 | `test_vertice_fora_de_faixa_rejeitado` | regra de geometria |
| 11 | `test_precisao_negativa_rejeitada` | estrutura da entidade |
### TestCaracteristica

**Arquivo:** `tests/unit/test_imo_geometria_use_cases.py` · **Testes:** 5

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_registra_caracteristica` | estrutura da entidade |
| 2 | `test_exige_imovel_existente` | estrutura da entidade |
| 3 | `test_obra_invalida_rejeitada` | estrutura da entidade |
| 4 | `test_pavimentos_invalidos_rejeitados` | estrutura da entidade |
| 5 | `test_ano_renovacao_invalido_rejeitado` | estrutura da entidade |
### TestImovel

**Arquivo:** `tests/unit/test_imo_imoveis_use_cases.py` · **Testes:** 17

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_cadastra_imovel` | estrutura da entidade |
| 2 | `test_nao_duplica_inscricao` | estrutura da entidade |
| 3 | `test_exige_inscricao` | estrutura da entidade |
| 4 | `test_exige_logradouro_e_bairro` | estrutura da entidade |
| 5 | `test_areas_negativas_rejeitadas` | regra de áreas |
| 6 | `test_tipo_invalido_rejeitado` | estrutura da entidade |
| 7 | `test_ano_construcao_invalido` | estrutura da entidade |
| 8 | `test_atualiza_campos` | estrutura da entidade |
| 9 | `test_atualiza_tipo_invalido` | estrutura da entidade |
| 10 | `test_atualiza_imovel_inexistente` | estrutura da entidade |
| 11 | `test_altera_situacao_permitida` | regra de situação |
| 12 | `test_inativo_nao_vai_direto_para_desocupado` | estrutura da entidade |
| 13 | `test_demolicao_e_irreversivel` | estrutura da entidade |
| 14 | `test_situacao_invalida_rejeitada` | regra de situação |
| 15 | `test_altera_situacao_imovel_inexistente` | regra de situação |
| 16 | `test_exclui_logicamente` | estrutura da entidade |
| 17 | `test_exclui_imovel_inexistente` | regra de exclusão |
### TestProprietario

**Arquivo:** `tests/unit/test_imo_imoveis_use_cases.py` · **Testes:** 10

| # | Caso de teste | Regras exercitadas |
| --- | --- | --- |
| 1 | `test_vincula_titular_principal` | regra de titularidade |
| 2 | `test_exige_imovel_existente` | estrutura da entidade |
| 3 | `test_nao_duplica_pessoa_no_imovel` | estrutura da entidade |
| 4 | `test_recusa_segundo_titular_principal` | regra de titularidade |
| 5 | `test_nao_torna_principal_vinculo_nao_titular` | estrutura da entidade |
| 6 | `test_cpf_invalido_rejeitado` | regra de titularidade |
| 7 | `test_nome_obrigatorio` | estrutura da entidade |
| 8 | `test_vinculo_invalido_rejeitado` | estrutura da entidade |
| 9 | `test_remove_vinculo_logicamente` | estrutura da entidade |
| 10 | `test_remove_vinculo_inexistente` | estrutura da entidade |

# 4. Totais

| Indicador | Quantidade |
| --- | |
| Arquivos de teste unitário | 3 |
| Classes de teste | 6 |
| Casos de teste | 58 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 019-Casos-de-Teste-Cadastro-Imobiliario.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_cadastro_imobiliario`. Alterações no código devem ser
> refletidas reexecutando o gerador.
