# 007 – Regras de Negócio – Cadastro Imobiliário

#### Regras de Negócio – Cadastro Imobiliário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IMO-007

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

Este artefato consolida as regras de negócio do domínio de Cadastro Imobiliário,
declarando as invariantes que a implementação deve preservar.

---

# 2. Convenção de Identificação

As regras seguem o padrão `RN-<DOMÍNIO>-<sequencial>`, onde o número é sequencial
e estável. A numeração não é reutilizada após a revogação de uma regra.

---

# 3. Classificação das Regras

| Tipo | Regras | Significado |
| --- | | --- | |
| Cálculo | RN-IMO-005 | Define fórmula determinística de apuração. |
| Máquina de estados | RN-IMO-004 | Governa as transições permitidas entre situações. |
| Restrição | RN-IMO-001, RN-IMO-002, RN-IMO-003, RN-IMO-006, RN-IMO-007 | Limita os estados ou valores aceitos pelo domínio. |


---

# 4. Regras de Negócio

## RN-IMO-001 — Unicidade da Inscrição Imobiliária

**Tipo:** Restrição

**Processo:** PRO-IMO-001

**Descrição:** A inscrição imobiliária é única no município e obrigatória; a alteração posterior mantém o mesmo identificador.

**Justificativa:** A inscrição é a chave de endereçamento do imóvel e o meio de citação de lançamento junto ao cidadão.

**Garantia técnica:** Restrição UNIQUE em `imo.imoveis.inscricao_imobiliaria` e validação em `Imovel.validar()`.

---
## RN-IMO-002 — Vinculação Obrigatória ao Território

**Tipo:** Restrição

**Processo:** PRO-IMO-001

**Descrição:** O imóvel exige logradouro e divisão territorial vinculados; o bairro é resolvido a partir do logradouro.

**Justificativa:** Sem o vínculo territorial não há endereço válido nem aplicação possível da planta de valores.

**Garantia técnica:** Validação de `logradouro_id` e `bairro_id` em `Imovel.validar()`.

---
## RN-IMO-003 — Coerência das Áreas

**Tipo:** Restrição

**Processo:** PRO-IMO-001

**Descrição:** As áreas do terreno e da construção não podem ser negativas e o ano de construção deve ser coerente.

**Justificativa:** Áreas negativas produziriam valor venal incorreto e urbanismo inválido.

**Garantia técnica:** Validação em `Imovel.validar()` e faixas restritivas nos schemas Pydantic.

---
## RN-IMO-004 — Máquina de Estados da Situação do Imóvel

**Tipo:** Máquina de estados

**Processo:** PRO-IMO-003

**Descrição:** As transições são `ATIVO -> INATIVO | EM_OBRA | DESOCUPADO | DEMOLIDO`, `INATIVO -> ATIVO`, `EM_OBRA -> ATIVO | DEMOLIDO` e `DESOCUPADO -> ATIVO | INATIVO`; `DEMOLIDO` é terminal.

**Justificativa:** Impede situações incoerentes, como imóvel demolido reativado, e preserva o histórico fiscal.

**Garantia técnica:** Tabela `_TRANSICOES_SITUACAO` e validação em `Imovel.mudar_situacao()`.

---
## RN-IMO-005 — Apuração do Valor Venal

**Tipo:** Cálculo

**Processo:** PRO-IMO-004

**Descrição:** `valor_terreno = área_terreno_m2 × Vt`, `valor_construção = área_construida_m2 × Vc`, `valor_venal = valor_terreno + valor_construcao` e `valor_lançamento = valor_venal × alíquota / 100`; um exercício já concluído não pode ser reavaliado.

**Justificativa:** Garante a rastreabilidade do valor aplicado e impede índices contraditórios no mesmo exercício.

**Garantia técnica:** Propriedades calculadas em `AvaliacaoImovel` e índice único `uq_imo_avaliacao_exercicio`.

---
## RN-IMO-006 — Titularidade Principal Única

**Tipo:** Restrição

**Processo:** PRO-IMO-002

**Descrição:** Cada imóvel admite no máximo um proprietário titular principal, a mesma pessoa não é vinculada duas vezes ao mesmo imóvel e o documento é CPF (11 dígitos) ou CNPJ (14 dígitos).

**Justificativa:** A titularidade principal é a base da notificação de lançamento e da cobrança.

**Garantia técnica:** Índice único parcial `uq_imo_titular_principal` e validação em `ProprietarioImovel.validar()`.

---
## RN-IMO-007 — Integridade da Geometria do Lote

**Tipo:** Restrição

**Processo:** PRO-IMO-006

**Descrição:** A geometria exige datum suportado, coordenadas no intervalo admissível e vértices compatíveis com o tipo de geometria; cada lote admite uma geometria vigente.

**Justificativa:** Assegura a fidelidade do desenho fundiário e o georreferenciamento legal.

**Garantia técnica:** Validação em `GeometriaImovel.validar()` e índice único `uq_imo_geometria_lote`.

---

---

# 5. Matriz de Decisão

| Regra | Processo | Garantia no banco | Testada por |
| --- | | --- | | --- | |
| RN-IMO-001 | PRO-IMO-001 | Restrição UNIQUE em `imo.imoveis.inscricao_imobiliaria` e validação em `Imovel.validar()`. | 0 teste(s) |
| RN-IMO-002 | PRO-IMO-001 | Validação de `logradouro_id` e `bairro_id` em `Imovel.validar()`. | 0 teste(s) |
| RN-IMO-003 | PRO-IMO-001 | Validação em `Imovel.validar()` e faixas restritivas nos schemas Pydantic. | 0 teste(s) |
| RN-IMO-004 | PRO-IMO-003 | Tabela `_TRANSICOES_SITUACAO` e validação em `Imovel.mudar_situacao()`. | 0 teste(s) |
| RN-IMO-005 | PRO-IMO-004 | Propriedades calculadas em `AvaliacaoImovel` e índice único `uq_imo_avaliacao_exercicio`. | 0 teste(s) |
| RN-IMO-006 | PRO-IMO-002 | Índice único parcial `uq_imo_titular_principal` e validação em `ProprietarioImovel.validar()`. | 0 teste(s) |
| RN-IMO-007 | PRO-IMO-006 | Validação em `GeometriaImovel.validar()` e índice único `uq_imo_geometria_lote`. | 0 teste(s) |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 007-Regras-de-Negocio-Cadastro-Imobiliario.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_cadastro_imobiliario`. Alterações no código devem ser
> refletidas reexecutando o gerador.
