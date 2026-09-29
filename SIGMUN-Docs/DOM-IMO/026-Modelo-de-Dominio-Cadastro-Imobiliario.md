# 026 – Modelo de Domínio – Cadastro Imobiliário

#### Modelo de Domínio – Cadastro Imobiliário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IMO-026

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

Este artefato descreve o modelo de domínio de Cadastro Imobiliário: entidades,
invariantes, estados e as regras que os governam.

---

# 2. Conceitos Centrais

| Entidade | Responsabilidade |
| --- | |
| Imovel | Unidade imobiliária (lote) com inscrição definitiva. |
| ProprietarioImovel | Vínculo de titularidade entre pessoa e imóvel. |
| AvaliacaoImovel | Avaliação do valor venal para um exercício. |
| CaracteristicaImovel | Característica construtiva do imóvel. |
| GeometriaImovel | Geometria georreferenciada do lote. |


---

# 3. Invariantes por Entidade

### Imovel

Unidade imobiliária (lote) com inscrição definitiva.

* **Invariantes:** Inscrição única; logradouro e divisão obrigatórios; áreas não negativas; situação válida.
* **Estados:** `ativo`, `inativo`, `em_obra`, `desocupado`, `demolido` (terminal)

### ProprietarioImovel

Vínculo de titularidade entre pessoa e imóvel.

* **Invariantes:** Imóvel e nome obrigatórios; documento com 11 (CPF) ou 14 (CNPJ) dígitos.
* **Estados:** Vínculo vigente ou removido logicamente

### AvaliacaoImovel

Avaliação do valor venal para um exercício.

* **Invariantes:** Exercício entre 1900 e 2200; valores unitários não negativos; conclusão única.
* **Estados:** `rascunho`, `concluida`, `cancelada`

### CaracteristicaImovel

Característica construtiva do imóvel.

* **Invariantes:** Imóvel obrigatório; ao menos um pavimento.
* **Estados:** Vigente, substituída a cada novo registro

### GeometriaImovel

Geometria georreferenciada do lote.

* **Invariantes:** Imóvel obrigatório; datum suportado; vértices compatíveis com a geometria.
* **Estados:** Vigente, substituída a cada levantamento

---

# 4. Regras e Estados

| Regra | Tipo | Entidades afetadas | Garantia técnica |
| --- | | --- | | --- | |
| RN-IMO-001 | Restrição | Imovel | Restrição UNIQUE em `imo.imoveis.inscricao_imobiliaria` e validação em `Imovel.validar()`. |
| RN-IMO-002 | Restrição | Imovel | Validação de `logradouro_id` e `bairro_id` em `Imovel.validar()`. |
| RN-IMO-003 | Restrição | Imovel | Validação em `Imovel.validar()` e faixas restritivas nos schemas Pydantic. |
| RN-IMO-004 | Máquina de estados | Imovel | Tabela `_TRANSICOES_SITUACAO` e validação em `Imovel.mudar_situacao()`. |
| RN-IMO-005 | Cálculo | AvaliacaoImovel | Propriedades calculadas em `AvaliacaoImovel` e índice único `uq_imo_avaliacao_exercicio`. |
| RN-IMO-006 | Restrição | ProprietarioImovel | Índice único parcial `uq_imo_titular_principal` e validação em `ProprietarioImovel.validar()`. |
| RN-IMO-007 | Restrição | GeometriaImovel | Validação em `GeometriaImovel.validar()` e índice único `uq_imo_geometria_lote`. |


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

**Documento:** 026-Modelo-de-Dominio-Cadastro-Imobiliario.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_cadastro_imobiliario`. Alterações no código devem ser
> refletidas reexecutando o gerador.
