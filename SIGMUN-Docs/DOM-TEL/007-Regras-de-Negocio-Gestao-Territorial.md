# 007 – Regras de Negócio – Gestão Territorial

#### Regras de Negócio – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-007

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

Este artefato consolida as regras de negócio do domínio de Gestão Territorial,
declarando as invariantes que a implementação deve preservar.

---

# 2. Convenção de Identificação

As regras seguem o padrão `RN-<DOMÍNIO>-<sequencial>`, onde o número é sequencial
e estável. A numeração não é reutilizada após a revogação de uma regra.

---

# 3. Classificação das Regras

| Tipo | Regras | Significado |
| --- | | --- | |
| Máquina de estados | RN-TEL-004 | Governa as transições permitidas entre situações. |
| Restrição | RN-TEL-001, RN-TEL-002, RN-TEL-003, RN-TEL-005, RN-TEL-006 | Limita os estados ou valores aceitos pelo domínio. |


---

# 4. Regras de Negócio

## RN-TEL-001 — Unicidade do Código da Divisão Territorial

**Tipo:** Restrição

**Processo:** PRO-TEL-001

**Descrição:** O código da divisão territorial é único no cadastro municipal; código e nome são obrigatórios.

**Justificativa:** O código é a chave natural usada pelo cadastro imobiliário e pelas bases cartográficas.

**Garantia técnica:** Restrição UNIQUE em `tel.bairros.codigo` e validação em `Bairro.validar()`.

---
## RN-TEL-002 — Unicidade do Logradouro e Vinculação Territorial

**Tipo:** Restrição

**Processo:** PRO-TEL-002

**Descrição:** O código do logradouro é único e todo logradouro pertence a uma divisão territorial cadastrada.

**Justificativa:** A malha viária é referenciada pelo cadastro imobiliário e pelo georreferenciamento.

**Garantia técnica:** Restrição UNIQUE em `tel.logradouros.codigo` e validação de `bairro_id`.

---
## RN-TEL-003 — Unicidade da Planta Vigente

**Tipo:** Restrição

**Processo:** PRO-TEL-003

**Descrição:** Existe no máximo uma planta vigente para cada combinação de ano, divisão e ocupação.

**Justificativa:** Garante que o cálculo do valor venal tenha referência única e determinística.

**Garantia técnica:** Índice único parcial `uq_tel_planta_vigente` e verificação na ativação.

---
## RN-TEL-004 — Ciclo de Vida da Planta Genérica de Valores

**Tipo:** Máquina de estados

**Processo:** PRO-TEL-003

**Descrição:** A planta percorre `RASCUNHO -> VIGENTE -> REVOGADA`, sem retorno a partir de `REVOGADA`; a revogação exige justificativa e somente plantas em rascunho podem ser editadas.

**Justificativa:** Preserva a memória histórica dos valores aplicados a cada exercício.

**Garantia técnica:** Transições em `PlantaGenericaValores.ativar()` e `.revogar()`.

---
## RN-TEL-005 — Integridade da Georreferência

**Tipo:** Restrição

**Processo:** PRO-TEL-005

**Descrição:** A georreferência exige datum suportado, está vinculada a uma divisão **ou** a um logradouro (nunca a ambos), e seus vértices são validados quanto à faixa de coordenadas e à quantidade mínima do tipo de geometria.

**Justificativa:** Coordenadas inválidas ou referências ambíguas corromperiam a base cartográfica.

**Garantia técnica:** Check `ck_tel_geo_referencia` e validação em `Georreferencia.validar()`.

---
## RN-TEL-006 — Proteção contra Exclusão com Dependências

**Tipo:** Restrição

**Processo:** PRO-TEL-001

**Descrição:** Uma divisão territorial com logradouros ativos não pode ser excluída.

**Justificativa:** A exclusão deixaria logradouros órfãos e quebraria o cadastro imobiliário.

**Garantia técnica:** Verificação de dependências em `ExcluirBairroUseCase`.

---

---

# 5. Matriz de Decisão

| Regra | Processo | Garantia no banco | Testada por |
| --- | | --- | | --- | |
| RN-TEL-001 | PRO-TEL-001 | Restrição UNIQUE em `tel.bairros.codigo` e validação em `Bairro.validar()`. | 0 teste(s) |
| RN-TEL-002 | PRO-TEL-002 | Restrição UNIQUE em `tel.logradouros.codigo` e validação de `bairro_id`. | 0 teste(s) |
| RN-TEL-003 | PRO-TEL-003 | Índice único parcial `uq_tel_planta_vigente` e verificação na ativação. | 0 teste(s) |
| RN-TEL-004 | PRO-TEL-003 | Transições em `PlantaGenericaValores.ativar()` e `.revogar()`. | 0 teste(s) |
| RN-TEL-005 | PRO-TEL-005 | Check `ck_tel_geo_referencia` e validação em `Georreferencia.validar()`. | 0 teste(s) |
| RN-TEL-006 | PRO-TEL-001 | Verificação de dependências em `ExcluirBairroUseCase`. | 0 teste(s) |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 007-Regras-de-Negocio-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
