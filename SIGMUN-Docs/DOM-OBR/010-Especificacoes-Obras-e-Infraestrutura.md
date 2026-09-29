# 010 – Especificações – Obras e Infraestrutura

#### Especificações – Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OBR-010

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

Este artefato detalha as especificações de interface do domínio de
Obras e Infraestrutura: contrato REST, esquema de persistência e convenções de
identificação.

---

# 2. Contrato de Interface

* **Base:** `/api/v1/obr`
* **Formato:** JSON sobre HTTP
* **Autenticação:** **não aplicada** — as rotas deste domínio não exigem token;
  a lacuna está registrada no artefato 016 (verifique antes de expor em produção)
* **Erros de negócio:** `409 Conflict` com mensagem descritiva
* **Recurso inexistente:** `404 Not Found`
* **Validação de entrada:** `422 Unprocessable Entity`
* **Listagem:** `page` (a partir de 1) e `page_size` (1 a 100)

---

# 3. Operações

| Método | Caminho | Finalidade |
| --- | | --- | |
| GET | /api/v1/obr/obras/{obra_id}/acompanhamento | Consultar obras por identificador |
| POST | /api/v1/obr/medicoes | Registrar ação sobre medicoes |
| GET | /api/v1/obr/obras/{obra_id}/medicoes | Consultar obras por identificador |
| POST | /api/v1/obr/medicoes/{medicao_id}/aprovar | Registrar ação sobre medicoes |
| POST | /api/v1/obr/medicoes/{medicao_id}/glosar | Registrar ação sobre medicoes |
| POST | /api/v1/obr/medicoes/{medicao_id}/cancelar | Registrar ação sobre medicoes |
| POST | /api/v1/obr/despesas | Registrar ação sobre despesas |
| GET | /api/v1/obr/obras/{obra_id}/despesas | Consultar obras por identificador |
| DELETE | /api/v1/obr/despesas/{despesa_id} | Excluir despesas (exclusão lógica) |
| POST | /api/v1/obr/etapas | Registrar ação sobre etapas |
| GET | /api/v1/obr/obras/{obra_id}/etapas | Consultar obras por identificador |
| PATCH | /api/v1/obr/etapas/{etapa_id} | Atualizar etapas |
| POST | /api/v1/obr/etapas/{etapa_id}/concluir | Registrar ação sobre etapas |
| POST | /api/v1/obr/vistorias | Registrar ação sobre vistorias |
| GET | /api/v1/obr/obras/{obra_id}/vistorias | Consultar obras por identificador |
| GET | /api/v1/obr/obras | Listar ou consultar obras |
| POST | /api/v1/obr/obras | Registrar ação sobre obras |
| DELETE | /api/v1/obr/obras/{obra_id} | Excluir obras (exclusão lógica) |
| GET | /api/v1/obr/obras/{obra_id} | Consultar obras por identificador |
| PATCH | /api/v1/obr/obras/{obra_id} | Atualizar obras |
| POST | /api/v1/obr/obras/{obra_id}/iniciar-execucao | Registrar ação sobre obras |
| POST | /api/v1/obr/obras/{obra_id}/suspender | Registrar ação sobre obras |
| POST | /api/v1/obr/obras/{obra_id}/concluir | Registrar ação sobre obras |
| POST | /api/v1/obr/obras/{obra_id}/cancelar | Registrar ação sobre obras |


---

# 4. Modelo de Persistência

| Schema | Tabela | Colunas | Chave natural / restrição |
| --- | | --- | | --- | |
| `obr` | `obras` | 28 | numero |
| `obr` | `medicoes_obras` | 14 | — |
| `obr` | `etapas_obras` | 16 | — |
| `obr` | `despesas_obras` | 13 | — |
| `obr` | `vistorias_obras` | 11 | — |


---

# 5. Convenções de Identificação

* **Identificador interno:** UUID v4, gerado pela aplicação.
* **Chave natural:** código cadastral, textual e estável.
* **Exclusão:** lógica, por meio do campo `is_deleted`, preservando o histórico
  fiscal e fundiário.

---

# 6. Regras Aplicadas na Interface

| Regra | Efeito observável na API |
| --- | |
| RN-OBR-001 | O número da obra é único no cadastro municipal; número e nome são obrigatórios e o número não pode ser alterado após a identificação da obra. |
| RN-OBR-002 | A obra percorre `PLANEJADA -> EM_LICITACAO -> CONTRATADA -> EM_EXECUCAO -> CONCLUIDA`, com `SUSPENSA` e `CANCELADA` disponíveis. A conclusão e o cancelamento são terminais e obra concluída não aceita alteração cadastral. |
| RN-OBR-003 | A execução só pode ser iniciada em obra contratada ou suspensa, e exige empresa contratada e data de início prevista informadas. |
| RN-OBR-004 | Os valores e percentuais são não negativos, o valor contratado não supera o valor orçado, o valor pago não supera o valor medido e **o avanço financeiro nunca ultrapassa o avanço físico**. |
| RN-OBR-005 | A medição percorre `REGISTRADA -> CONFERIDA -> APROVADA`, com `GLOSADA` e `CANCELADA` disponíveis. Apenas medição aprovada compõe o avanço da obra; a conclusão exige 100% do avanço físico; o valor medido não pode superar o contratado e o número da medição é único por obra. |
| RN-OBR-006 | A despesa exige valor positivo, pertence a obra contratada ou em execução e não pode superar o saldo medido e ainda não pago. |
| RN-OBR-007 | A etapa pertence a uma obra, exige responsável e percorre `PENDENTE -> EM_EXECUCAO -> CONCLUIDA`, com `ATRASADA` e `CANCELADA` disponíveis; concluí-la exige 100% do percentual previsto. O percentual previsto é o peso da etapa na obra e o percentual realizado é a conclusão da etapa: são escalas distintas e ambos ficam na faixa de 0 a 100. |
| RN-OBR-008 | A vistoria pertence a uma obra existente, exige fiscal identificado e registra tipo, parecer e percentual físico verificado na faixa de 0 a 100. |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 010-Especificacoes-Obras-e-Infraestrutura.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_obras`. Alterações no código devem ser
> refletidas reexecutando o gerador.
