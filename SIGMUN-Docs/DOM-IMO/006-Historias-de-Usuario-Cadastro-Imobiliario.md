# 006 – Histórias de Usuário – Cadastro Imobiliário

#### Histórias de Usuário – Cadastro Imobiliário

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-IMO-006

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

Este artefato expressa as necessidades do domínio de Cadastro Imobiliário em histórias
de usuário, com critérios de aceitação verificáveis.

---

# 2. Convenções

* O padrão é *Como / Quero / Para*, com critérios no formato
  **Dado** / **Quando** / **Então**.
* Cada critério referencia a regra de negócio que ele exercita.

---

# 3. Histórias de Usuário

### HU-IMO-001 — Cadastrar e manter lotes

**Como** como técnico de cadastro imobiliário,
**quero** cadastrar lotes com inscrição definitiva e áreas consistentes,
**para** manter a base do cadastro imobiliário municipal.

**Capacidade:** CAP-IMO-001

**Regras relacionadas:** RN-IMO-001, RN-IMO-002, RN-IMO-003

**Critérios de aceitação:**

1. Dado um logradouro existente no DOM-TEL, quando o técnico cadastra o lote, então o imóvel é criado com o bairro resolvido
2. Dado uma inscrição já cadastrada, quando o técnico tenta cadastrar, então o sistema recusa com HTTP 409 (RN-IMO-001)
3. Dado uma área negativa, quando o técnico cadastra, então o sistema recusa (RN-IMO-003).
### HU-IMO-002 — Controlar a titularidade do imóvel

**Como** como técnico de cadastro imobiliário,
**quero** vincular o titular principal e demais parceiros,
**para** notificar corretamente o cidadão e orientar a cobrança.

**Capacidade:** CAP-IMO-002

**Regras relacionadas:** RN-IMO-006

**Critérios de aceitação:**

1. Dado um imóvel sem titular, quando o técnico vincula um titular principal, então o vínculo é criado
2. Dado um imóvel que já possui titular principal, quando o técnico tenta vincular outro principal, então o sistema recusa com HTTP 409 (RN-IMO-006)
3. Dado um CPF ou CNPJ com comprimento inválido, quando o técnico vincula, então o sistema recusa (RN-IMO-006)
4. Dado a mesma pessoa já vinculada, quando o técnico vincula novamente, então o sistema recusa (RN-IMO-006).
### HU-IMO-003 — Controlar o ciclo de vida do imóvel

**Como** como técnico de cadastro imobiliário,
**quero** alterar a situação cadastral do imóvel,
**para** refletir a realidade do imóvel e sustentar a avaliação.

**Capacidade:** CAP-IMO-003

**Regras relacionadas:** RN-IMO-004

**Critérios de aceitação:**

1. Dado um imóvel ativo, quando o técnico marca em obra, então a situação é alterada (RN-IMO-004)
2. Dado um imóvel demolido, quando o técnico tenta reativar, então o sistema recusa com HTTP 409 (RN-IMO-004)
3. Dado um imóvel inativo, quando o técnico marca desocupado sem reativar, então o sistema recusa (RN-IMO-004).
### HU-IMO-004 — Avaliar o valor venal do imóvel

**Como** como avaliador fiscal,
**quero** apurar o valor venal com base na planta genérica de valores vigente,
**para** fundamentar o lançamento do tributo municipal.

**Capacidade:** CAP-IMO-004

**Regras relacionadas:** RN-IMO-005

**Critérios de aceitação:**

1. Dado um imóvel de 200 m² de terreno e 120 m² de construção, quando a avaliação usa R$ 180/m² e R$ 950/m², então o valor venal é de R$ 150.000,00 (RN-IMO-005)
2. Dado um exercício já avaliado e concluído, quando o avaliador tenta reavaliar, então o sistema recusa com HTTP 409 (RN-IMO-005)
3. Dado um imóvel sem áreas, quando o avaliador tenta avaliar, então o sistema recusa (RN-IMO-005).
### HU-IMO-005 — Georreferenciar o lote

**Como** como técnico de cadastro imobiliário,
**quero** registrar a geometria georreferenciada do lote,
**para** apoiar o georreferenciamento legal e a produção cartográfica.

**Capacidade:** CAP-IMO-006

**Regras relacionadas:** RN-IMO-007

**Critérios de aceitação:**

1. Dado um imóvel existente, quando o técnico registra um polígono com vértices válidos, então a geometria é gravada
2. Dado um polígono com menos de 3 vértices, quando o técnico registra, então o sistema recusa (RN-IMO-007)
3. Dado um datum não suportado, quando o técnico registra, então o sistema recusa (RN-IMO-007).

# 4. Rastreabilidade às Capacidades

| História | Capacidade | Regras |
| --- | | --- | |
| HU-IMO-001 — Cadastrar e manter lotes | CAP-IMO-001 | RN-IMO-001, RN-IMO-002, RN-IMO-003 |
| HU-IMO-002 — Controlar a titularidade do imóvel | CAP-IMO-002 | RN-IMO-006 |
| HU-IMO-003 — Controlar o ciclo de vida do imóvel | CAP-IMO-003 | RN-IMO-004 |
| HU-IMO-004 — Avaliar o valor venal do imóvel | CAP-IMO-004 | RN-IMO-005 |
| HU-IMO-005 — Georreferenciar o lote | CAP-IMO-006 | RN-IMO-007 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 006-Historias-de-Usuario-Cadastro-Imobiliario.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_cadastro_imobiliario`. Alterações no código devem ser
> refletidas reexecutando o gerador.
