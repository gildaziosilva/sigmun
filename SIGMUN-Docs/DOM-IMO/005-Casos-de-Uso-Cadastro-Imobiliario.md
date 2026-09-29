# 005 – Casos de Uso – Cadastro Imobiliário

#### Casos de Uso – Cadastro Imobiliário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IMO-005

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

Este artefato especifica os casos de uso do domínio de Cadastro Imobiliário,
relacionando cada cenário à sua implementação na camada de casos de uso.

---

# 2. Convenções

* Casos de uso descrevem **cenários de negócio**; a implementação é referenciada
  pelo nome da classe de caso de uso correspondente.
* Cenários de consulta direta ao repositório são assim identificados, pois não
  exigem lógica de negócio própria.

---

# 3. Casos de Uso

### CU-IMO-001 — Cadastrar lote

**Ator:** AT-IMO-001

**Capacidade:** CAP-IMO-001

**Pré-condições:** O logradouro e o bairro de vinculação existem no DOM-TEL.

**Fluxo principal:**

1. Selecionar o logradouro
2. o bairro é resolvido a partir dele (RN-IMO-002)
3. informar inscrição, número, tipo, áreas e ano
4. verificar a unicidade da inscrição (RN-IMO-001) e a coerência das áreas (RN-IMO-003)
5. gravar com situação ativa.

**Pós-condições:** O imóvel está cadastrado com inscrição definitiva.

**Regras aplicadas:** RN-IMO-001, RN-IMO-002, RN-IMO-003

**Caso de uso implementador:** `CadastrarImovelUseCase`
### CU-IMO-002 — Vincular titular principal

**Ator:** AT-IMO-001

**Capacidade:** CAP-IMO-002

**Pré-condições:** O imóvel existe.

**Fluxo principal:**

1. Selecionar o imóvel e informar nome e CPF ou CNPJ
2. o sistema impede titular principal duplicado e vínculo repetido (RN-IMO-006)
3. gravar o vínculo.

**Pós-condições:** O imóvel possui o titular principal vinculado.

**Regras aplicadas:** RN-IMO-006

**Caso de uso implementador:** `VincularProprietarioUseCase`
### CU-IMO-003 — Alterar situação do imóvel

**Ator:** AT-IMO-001

**Capacidade:** CAP-IMO-003

**Pré-condições:** O imóvel existe.

**Fluxo principal:**

1. Selecionar a nova situação
2. o sistema valida a transição contra a máquina de estados (RN-IMO-004)
3. transições inválidas são recusadas com HTTP 409.

**Pós-condições:** O imóvel está na situação informada, quando a transição é válida.

**Regras aplicadas:** RN-IMO-004

**Caso de uso implementador:** `AlterarSituacaoImovelUseCase`
### CU-IMO-004 — Avaliar o valor venal

**Ator:** AT-IMO-002

**Capacidade:** CAP-IMO-004

**Pré-condições:** O imóvel existe e possui áreas cadastradas.

**Fluxo principal:**

1. Consultar a planta vigente no DOM-TEL
2. calcular terreno, construção, valor venal e lançamento (RN-IMO-005)
3. o sistema recusa a reavaliação de exercício concluído
4. registrar e concluir.

**Pós-condições:** A avaliação do exercício está concluída e o valor venal apurado.

**Regras aplicadas:** RN-IMO-005

**Caso de uso implementador:** `AvaliarImovelUseCase`
### CU-IMO-005 — Consultar cadastro do imóvel

**Ator:** AT-IMO-004

**Capacidade:** CAP-IMO-005

**Pré-condições:** Não há precondição.

**Fluxo principal:**

1. Informar a inscrição imobiliária
2. o sistema exibe situação, áreas, titularidade e avaliações.

**Pós-condições:** Os dados cadastrais foram apresentados ao cidadão.

**Regras aplicadas:** RN-IMO-001, RN-IMO-005

**Caso de uso implementador:** — (consulta ao repositório) (implementado como consulta ao repositório)
### CU-IMO-006 — Georreferenciar o lote

**Ator:** AT-IMO-001

**Capacidade:** CAP-IMO-006

**Pré-condições:** O imóvel existe.

**Fluxo principal:**

1. Selecionar o imóvel e informar geometria, vértices, datum e precisão
2. o sistema valida e substitui a geometria vigente (RN-IMO-007).

**Pós-condições:** O lote possui geometria georreferenciada vigente.

**Regras aplicadas:** RN-IMO-007

**Caso de uso implementador:** `RegistrarGeometriaUseCase`

# 4. Cobertura

| Indicador | Quantidade |
| --- | |
| Casos de uso especificados | 6 |
| Casos de uso com classe implementadora | 5 |
| Histórias de usuário relacionadas | 5 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 005-Casos-de-Uso-Cadastro-Imobiliario.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_cadastro_imobiliario`. Alterações no código devem ser
> refletidas reexecutando o gerador.
