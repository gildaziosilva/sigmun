# 026 – Modelo de Domínio – Obras e Infraestrutura

#### Modelo de Domínio – Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OBR-026

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

Este artefato descreve o modelo de domínio de Obras e Infraestrutura: entidades,
invariantes, estados e as regras que os governam.

---

# 2. Conceitos Centrais

| Entidade | Responsabilidade |
| --- | |
| Obra | Obra pública acompanhada quanto ao avanço físico e financeiro. |
| MedicaoObra | Medição físico-financeira de avanço da obra. |
| EtapaObra | Etapa de execução fisicamente verificável da obra. |
| DespesaObra | Desembolso financeiro vinculado à obra. |
| VistoriaObra | Vistoria fiscalizadora com parecer sobre o avanço verificado. |


---

# 3. Invariantes por Entidade

### Obra

Obra pública acompanhada quanto ao avanço físico e financeiro.

* **Invariantes:** Campos obrigatórios conforme o schema.
* **Estados:** —

### MedicaoObra

Medição físico-financeira de avanço da obra.

* **Invariantes:** Campos obrigatórios conforme o schema.
* **Estados:** —

### EtapaObra

Etapa de execução fisicamente verificável da obra.

* **Invariantes:** Campos obrigatórios conforme o schema.
* **Estados:** —

### DespesaObra

Desembolso financeiro vinculado à obra.

* **Invariantes:** Campos obrigatórios conforme o schema.
* **Estados:** —

### VistoriaObra

Vistoria fiscalizadora com parecer sobre o avanço verificado.

* **Invariantes:** Campos obrigatórios conforme o schema.
* **Estados:** —

---

# 4. Regras e Estados

| Regra | Tipo | Entidades afetadas | Garantia técnica |
| --- | | --- | | --- | |
| RN-OBR-001 | Restrição | — | Restrição UNIQUE em `obr.obras.numero` e validação em `Obra.validar()`. |
| RN-OBR-002 | Máquina de estados | — | Transições em `Obra.iniciar_execucao()`, `.suspender()`, `.concluir()` e `.cancelar()`. |
| RN-OBR-003 | Restrição | — | Validações em `Obra.iniciar_execucao()`. |
| RN-OBR-004 | Restrição | — | Checks `ck_obr_obra_valores`, `ck_obr_obra_avanco` e `ck_obr_obra_pago`, e validação em `Obra.validar()`. |
| RN-OBR-005 | Máquina de estados | — | Transições em `MedicaoObra.conferir()`, `.aprovar()`, `.glosar()` e `.cancelar()`; índice único parcial `uq_obr_medicao_numero`; check `ck_obr_medicao_percentual`. |
| RN-OBR-006 | Restrição | — | Check `ck_obr_despesa_valor` e validações em `RegistrarDespesaUseCase` e `DespesaObra.validar()`. |
| RN-OBR-007 | Máquina de estados | — | Transições em `EtapaObra.iniciar()` e `.concluir()`, e check `ck_obr_etapa_percentual`. |
| RN-OBR-008 | Restrição | — | Check `ck_obr_vistoria_percentual` e validação em `VistoriaObra.validar()`. |


---

# 5. Modelo Conceitual

O domínio se articula em três eixos:

* **Território:** a divisão territorial organiza o território e a malha viária.
* **Valor:** a planta genérica de valores estabelece os parâmetros que sustentam
  a apuração.
* **Fundo de terra:** o cadastro imobiliário registra o lote, sua titularidade,
  sua construção e sua geometria.

---

# 6. Limites do Modelo

* As referências entre domínios são identificadores opacos, sem FK física.
* A exclusão é lógica em todos os cadastros, preservando o histórico.
* Estados terminais, como `DEMOLIDO` e `REVOGADA`, são irreversíveis por regra.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 026-Modelo-de-Dominio-Obras-e-Infraestrutura.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_obras`. Alterações no código devem ser
> refletidas reexecutando o gerador.
