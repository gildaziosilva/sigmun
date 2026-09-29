# 026 – Modelo de Domínio – Gestão Territorial

#### Modelo de Domínio – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-026

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

Este artefato descreve o modelo de domínio de Gestão Territorial: entidades,
invariantes, estados e as regras que os governam.

---

# 2. Conceitos Centrais

| Entidade | Responsabilidade |
| --- | |
| Bairro | Divisão territorial (bairro, distrito, setor ou zona rural). |
| Logradouro | Logradouro público vinculado a uma divisão territorial. |
| PlantaGenericaValores | Valores unitários por ano, divisão e ocupação. |
| Georreferencia | Georreferência de bairro ou logradouro. |


---

# 3. Invariantes por Entidade

### Bairro

Divisão territorial (bairro, distrito, setor ou zona rural).

* **Invariantes:** Código único e obrigatório; código e nome preservados.
* **Estados:** `ativo`, `inativo`

### Logradouro

Logradouro público vinculado a uma divisão territorial.

* **Invariantes:** Código único; vínculo obrigatório com a divisão territorial; numeração final não inferior à inicial.
* **Estados:** `ativo`, `em_obra`, `inativo`

### PlantaGenericaValores

Valores unitários por ano, divisão e ocupação.

* **Invariantes:** Valores unitários não negativos; alíquota entre 0 e 100; ciclo RASCUNHO → VIGENTE → REVOGADA.
* **Estados:** `rascunho`, `vigente`, `revogada` (irreversível)

### Georreferencia

Georreferência de bairro ou logradouro.

* **Invariantes:** Vinculada a uma divisão OU a um logradouro; vértices compatíveis; datum suportado.
* **Estados:** Vigente ou excluída logicamente

---

# 4. Regras e Estados

| Regra | Tipo | Entidades afetadas | Garantia técnica |
| --- | | --- | | --- | |
| RN-TEL-001 | Restrição | Bairro | Restrição UNIQUE em `tel.bairros.codigo` e validação em `Bairro.validar()`. |
| RN-TEL-002 | Restrição | Logradouro | Restrição UNIQUE em `tel.logradouros.codigo` e validação de `bairro_id`. |
| RN-TEL-003 | Restrição | PlantaGenericaValores | Índice único parcial `uq_tel_planta_vigente` e verificação na ativação. |
| RN-TEL-004 | Máquina de estados | PlantaGenericaValores | Transições em `PlantaGenericaValores.ativar()` e `.revogar()`. |
| RN-TEL-005 | Restrição | Georreferencia | Check `ck_tel_geo_referencia` e validação em `Georreferencia.validar()`. |
| RN-TEL-006 | Restrição | Bairro, Logradouro | Verificação de dependências em `ExcluirBairroUseCase`. |


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

**Documento:** 026-Modelo-de-Dominio-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
