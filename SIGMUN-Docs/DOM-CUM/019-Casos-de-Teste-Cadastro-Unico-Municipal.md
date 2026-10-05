# 019 – Casos-de-Teste – Cadastro Único Municipal

#### Casos-de-Teste – Cadastro Único Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CUM-019

**Domínio:** Cadastro Único Municipal

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Cadastro-Unico-Municipal.md`
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

Este artefato detalha **os casos de teste** do domínio Cadastro Único Municipal (`DOM-CUM`), com base na implementação material identificada em `src/modules/sigmun_cadastro` e no conteúdo de negócio declarado no gerador.

---

# 2. Testes

| ID | Teste |
| --- | --- |
| CT-CUM-001 | `TestCPF.test_aceita_cpf_valido_com_mascara` |
| CT-CUM-002 | `TestCPF.test_aceita_cpf_valido_sem_mascara` |
| CT-CUM-003 | `TestCPF.test_formatado` |
| CT-CUM-004 | `TestCPF.test_rejeita_quantidade_errada_de_digitos` |
| CT-CUM-005 | `TestCPF.test_rejeita_digitos_repetidos` |
| CT-CUM-006 | `TestCPF.test_rejeita_digito_verificador_invalido` |
| CT-CUM-007 | `TestCPF.test_igualdade_e_hash` |
| CT-CUM-008 | `TestCPF.test_str_retorna_digitos` |
| CT-CUM-009 | `TestCNPJ.test_aceita_cnpj_valido_com_mascara` |
| CT-CUM-010 | `TestCNPJ.test_aceita_cnpj_valido_sem_mascara` |
| CT-CUM-011 | `TestCNPJ.test_formatado` |
| CT-CUM-012 | `TestCNPJ.test_rejeita_quantidade_errada_de_digitos` |
| CT-CUM-013 | `TestCNPJ.test_rejeita_digitos_repetidos` |
| CT-CUM-014 | `TestCNPJ.test_rejeita_digito_verificador_invalido` |
| CT-CUM-015 | `TestCNPJ.test_igualdade_e_hash` |
| CT-CUM-016 | `TestListarPessoas.test_listagem_responde_200` |
| CT-CUM-017 | `TestListarPessoas.test_listagem_respeita_page_size` |
| CT-CUM-018 | `TestListarPessoas.test_listagem_pagina_2_nao_reparte_a_1` |
| CT-CUM-019 | `TestListarPessoas.test_consulta_por_id_responde_200` |
| CT-CUM-020 | `TestListarPessoas.test_parametros_invalidos_respondem_422` |
| CT-CUM-021 | `TestListarDesatualizadas.test_repositorio_e_instanciavel` |
| CT-CUM-022 | `TestListarDesatualizadas.test_retorna_lista_de_uuid` |
| CT-CUM-023 | `TestListarDesatualizadas.test_respeita_limite` |
| CT-CUM-024 | `TestListarDesatualizadas.test_corte_no_futuro_traz_todas_as_vivas` |
| CT-CUM-025 | `TestListarDesatualizadas.test_corte_anterior_ao_cadastro_nao_traz_nada` |
| CT-CUM-026 | `TestListarDesatualizadas.test_use_case_revisao_consome_o_metodo` |
| CT-CUM-027 | `TestSqlAlchemyPessoaRepository.test_save_e_get_by_id_roundtrip_pf` |
| CT-CUM-028 | `TestSqlAlchemyPessoaRepository.test_save_e_get_by_id_roundtrip_pj` |
| CT-CUM-029 | `TestSqlAlchemyPessoaRepository.test_update_extensao_e_subrecursos` |
| CT-CUM-030 | `TestSqlAlchemyPessoaRepository.test_lista_com_filtros_e_paginacao` |
| CT-CUM-031 | `TestSqlAlchemyPessoaRepository.test_delete_cascade_soft_delete` |
| CT-CUM-032 | `TestSqlAlchemyPessoaRepository.test_delete_idempotente_para_inexistente` |
| CT-CUM-033 | `TestSqlAlchemyPessoaRepository.test_exists_documento` |
| CT-CUM-034 | `TestSqlAlchemyPessoaRepository.test_exists_documento_ignora_excluidos` |
| CT-CUM-035 | `TestSqlAlchemyUnidadeAdministrativaRepository.test_save_e_get_by_id_roundtrip` |
| CT-CUM-036 | `TestSqlAlchemyUnidadeAdministrativaRepository.test_update_campos` |
| CT-CUM-037 | `TestSqlAlchemyUnidadeAdministrativaRepository.test_lista_com_paginacao` |
| CT-CUM-038 | `TestSqlAlchemyUnidadeAdministrativaRepository.test_hierarquia_e_ancestrais` |
| CT-CUM-039 | `TestSqlAlchemyUnidadeAdministrativaRepository.test_save_rejeita_ciclo` |
| CT-CUM-040 | `TestSqlAlchemyUnidadeAdministrativaRepository.test_save_rejeita_auto_paternidade` |
| CT-CUM-041 | `TestSqlAlchemyUnidadeAdministrativaRepository.test_delete_soft_delete` |
| CT-CUM-042 | `TestSqlAlchemyUnidadeAdministrativaRepository.test_tem_filhas_ativas` |
| CT-CUM-043 | `TestSqlAlchemyUnidadeAdministrativaRepository.test_exists_sigla_com_exclude` |
| CT-CUM-044 | `TestSqlAlchemyUnidadeAdministrativaRepository.test_exists_sigla_inclui_excluidos` |
| CT-CUM-045 | `TestSqlAlchemyUnidadeAdministrativaRepository.test_exists_codigos_ibge_e_siafi` |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 019-Cadastro-Unico-Municipal-Casos-de-Teste.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
