# 007 – Regras de Negócio – Obras e Infraestrutura

#### Regras de Negócio – Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OBR-007

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

Este artefato consolida as regras de negócio do domínio de Obras e Infraestrutura,
declarando as invariantes que a implementação deve preservar.

---

# 2. Convenção de Identificação

As regras seguem o padrão `RN-<DOMÍNIO>-<sequencial>`, onde o número é sequencial
e estável. A numeração não é reutilizada após a revogação de uma regra.

---

# 3. Classificação das Regras

| Tipo | Regras | Significado |
| --- | | --- | |
| Máquina de estados | RN-OBR-002, RN-OBR-005, RN-OBR-007 | Governa as transições permitidas entre situações. |
| Restrição | RN-OBR-001, RN-OBR-003, RN-OBR-004, RN-OBR-006, RN-OBR-008 | Limita os estados ou valores aceitos pelo domínio. |


---

# 4. Regras de Negócio

## RN-OBR-001 — Unicidade do Número da Obra

**Tipo:** Restrição

**Processo:** PRO-OBR-001

**Descrição:** O número da obra é único no cadastro municipal; número e nome são obrigatórios e o número não pode ser alterado após a identificação da obra.

**Justificativa:** O número é a chave de rastreamento da obra nos convênios, nos processos e na transparência.

**Garantia técnica:** Restrição UNIQUE em `obr.obras.numero` e validação em `Obra.validar()`.

---
## RN-OBR-002 — Ciclo de Vida da Obra

**Tipo:** Máquina de estados

**Processo:** PRO-OBR-001

**Descrição:** A obra percorre `PLANEJADA -> EM_LICITACAO -> CONTRATADA -> EM_EXECUCAO -> CONCLUIDA`, com `SUSPENSA` e `CANCELADA` disponíveis. A conclusão e o cancelamento são terminais e obra concluída não aceita alteração cadastral.

**Justificativa:** O ciclo reflete a situação real do empreendimento e preserva a memória das decisões.

**Garantia técnica:** Transições em `Obra.iniciar_execucao()`, `.suspender()`, `.concluir()` e `.cancelar()`.

---
## RN-OBR-003 — Pré-condições para Iniciar a Execução

**Tipo:** Restrição

**Processo:** PRO-OBR-001

**Descrição:** A execução só pode ser iniciada em obra contratada ou suspensa, e exige empresa contratada e data de início prevista informadas.

**Justificativa:** Sem contratação formal e prazo definido não há como aferir o andamento nem a responsável pela obra.

**Garantia técnica:** Validações em `Obra.iniciar_execucao()`.

---
## RN-OBR-004 — Coerência Físico-Financeira da Obra

**Tipo:** Restrição

**Processo:** PRO-OBR-003

**Descrição:** Os valores e percentuais são não negativos, o valor contratado não supera o valor orçado, o valor pago não supera o valor medido e **o avanço financeiro nunca ultrapassa o avanço físico**.

**Justificativa:** O município não pode desembolhar mais do que executou; a coerência entre os dois avanços é a base do controle social da obra pública.

**Garantia técnica:** Checks `ck_obr_obra_valores`, `ck_obr_obra_avanco` e `ck_obr_obra_pago`, e validação em `Obra.validar()`.

---
## RN-OBR-005 — Ciclo de Vida da Medição e Composição do Avanço

**Tipo:** Máquina de estados

**Processo:** PRO-OBR-002

**Descrição:** A medição percorre `REGISTRADA -> CONFERIDA -> APROVADA`, com `GLOSADA` e `CANCELADA` disponíveis. Apenas medição aprovada compõe o avanço da obra; a conclusão exige 100% do avanço físico; o valor medido não pode superar o contratado e o número da medição é único por obra.

**Justificativa:** Somente medição conferida e aprovada deve compor o avanço, para que o físico e o financeiro reflitam a execução real.

**Garantia técnica:** Transições em `MedicaoObra.conferir()`, `.aprovar()`, `.glosar()` e `.cancelar()`; índice único parcial `uq_obr_medicao_numero`; check `ck_obr_medicao_percentual`.

---
## RN-OBR-006 — Limite da Despesa ao Valor Medido

**Tipo:** Restrição

**Processo:** PRO-OBR-003

**Descrição:** A despesa exige valor positivo, pertence a obra contratada ou em execução e não pode superar o saldo medido e ainda não pago.

**Justificativa:** Não se paga o que não foi medido; a regra protege o erário de desembolsos antecipados sem lastro de execução.

**Garantia técnica:** Check `ck_obr_despesa_valor` e validações em `RegistrarDespesaUseCase` e `DespesaObra.validar()`.

---
## RN-OBR-007 — Ciclo de Vida da Etapa e Escala de Percentuais

**Tipo:** Máquina de estados

**Processo:** PRO-OBR-004

**Descrição:** A etapa pertence a uma obra, exige responsável e percorre `PENDENTE -> EM_EXECUCAO -> CONCLUIDA`, com `ATRASADA` e `CANCELADA` disponíveis; concluí-la exige 100% do percentual previsto. O percentual previsto é o peso da etapa na obra e o percentual realizado é a conclusão da etapa: são escalas distintas e ambos ficam na faixa de 0 a 100.

**Justificativa:** O peso previsto dimensiona a etapa no cronograma; a distinção entre as escalas permite concluir uma etapa de peso parcial sem distorcer o cronograma.

**Garantia técnica:** Transições em `EtapaObra.iniciar()` e `.concluir()`, e check `ck_obr_etapa_percentual`.

---
## RN-OBR-008 — Registro de Vistoria Fiscalizadora

**Tipo:** Restrição

**Processo:** PRO-OBR-004

**Descrição:** A vistoria pertence a uma obra existente, exige fiscal identificado e registra tipo, parecer e percentual físico verificado na faixa de 0 a 100.

**Justificativa:** A vistoria é a evidência de campo que confronta o avanço declarado com o avanço executado.

**Garantia técnica:** Check `ck_obr_vistoria_percentual` e validação em `VistoriaObra.validar()`.

---

---

# 5. Matriz de Decisão

| Regra | Processo | Garantia no banco | Testada por |
| --- | | --- | | --- | |
| RN-OBR-001 | PRO-OBR-001 | Restrição UNIQUE em `obr.obras.numero` e validação em `Obra.validar()`. | 0 teste(s) |
| RN-OBR-002 | PRO-OBR-001 | Transições em `Obra.iniciar_execucao()`, `.suspender()`, `.concluir()` e `.cancelar()`. | 0 teste(s) |
| RN-OBR-003 | PRO-OBR-001 | Validações em `Obra.iniciar_execucao()`. | 0 teste(s) |
| RN-OBR-004 | PRO-OBR-003 | Checks `ck_obr_obra_valores`, `ck_obr_obra_avanco` e `ck_obr_obra_pago`, e validação em `Obra.validar()`. | 0 teste(s) |
| RN-OBR-005 | PRO-OBR-002 | Transições em `MedicaoObra.conferir()`, `.aprovar()`, `.glosar()` e `.cancelar()`; índice único parcial `uq_obr_medicao_numero`; check `ck_obr_medicao_percentual`. | 0 teste(s) |
| RN-OBR-006 | PRO-OBR-003 | Check `ck_obr_despesa_valor` e validações em `RegistrarDespesaUseCase` e `DespesaObra.validar()`. | 0 teste(s) |
| RN-OBR-007 | PRO-OBR-004 | Transições em `EtapaObra.iniciar()` e `.concluir()`, e check `ck_obr_etapa_percentual`. | 0 teste(s) |
| RN-OBR-008 | PRO-OBR-004 | Check `ck_obr_vistoria_percentual` e validação em `VistoriaObra.validar()`. | 0 teste(s) |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 007-Regras-de-Negocio-Obras-e-Infraestrutura.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_obras`. Alterações no código devem ser
> refletidas reexecutando o gerador.
