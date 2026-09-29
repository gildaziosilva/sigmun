# 006 – Histórias de Usuário – Gestão Territorial

#### Histórias de Usuário – Gestão Territorial

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-TEL-006

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

Este artefato expressa as necessidades do domínio de Gestão Territorial em histórias
de usuário, com critérios de aceitação verificáveis.

---

# 2. Convenções

* O padrão é *Como / Quero / Para*, com critérios no formato
  **Dado** / **Quando** / **Então**.
* Cada critério referencia a regra de negócio que ele exercita.

---

# 3. Histórias de Usuário

### HU-TEL-001 — Manter o cadastro de divisões territoriais

**Como** como técnico de cadastro imobiliário,
**quero** cadastrar e manter bairros, distritos, setores e zonas rurais,
**para** dispor da malha territorial codificada e consistente.

**Capacidade:** CAP-TEL-001

**Regras relacionadas:** RN-TEL-001, RN-TEL-006

**Critérios de aceitação:**

1. Dado um código inexistente, quando o técnico cadastra a divisão, então a divisão é criada e fica ativa
2. Dado um código já cadastrado, quando o técnico tenta cadastrar, então o sistema recusa com HTTP 409 (RN-TEL-001)
3. Dado uma divisão com logradouros ativos, quando o técnico tenta excluir, então o sistema recusa com HTTP 409 (RN-TEL-006).
### HU-TEL-002 — Manter a malha de logradouros

**Como** como técnico de cadastro imobiliário,
**quero** cadastrar logradouros vinculados à divisão territorial correspondente,
**para** identificar univocamente cada endereço do município.

**Capacidade:** CAP-TEL-002

**Regras relacionadas:** RN-TEL-002

**Critérios de aceitação:**

1. Dado um bairro existente, quando o técnico cadastra o logradouro, então o logradouro fica vinculado ao bairro
2. Dado um bairro inexistente, quando o técnico cadastra o logradouro, então o sistema recusa com HTTP 404 (RN-TEL-002)
3. Dado um código de logradouro já cadastrado, quando o técnico cadastra, então o sistema recusa com HTTP 409 (RN-TEL-002).
### HU-TEL-003 — Elaborar e aprovar a planta de valores do exercício

**Como** como membro da comissão de valores da planta,
**quero** elaborar, ativar e revogar plantas genéricas de valores,
**para** estabelecer os valores unitários que sustentam o valor venal.

**Capacidade:** CAP-TEL-003

**Regras relacionadas:** RN-TEL-003, RN-TEL-004

**Critérios de aceitação:**

1. Dado uma planta em rascunho, quando a comissão ativa e não há conflito, então a planta passa a vigente
2. Dado que já existe planta vigente para a mesma combinação, quando a comissão ativa outra, então o sistema recusa com HTTP 409 (RN-TEL-003)
3. Dado uma planta vigente, quando a comissão revoga com justificativa, então a planta passa a revogada (RN-TEL-004)
4. Dado uma planta sem justificativa, quando a comissão tenta revogar, então o sistema recusa (RN-TEL-004)
5. Dado uma planta vigente ou revogada, quando se tenta editar valores, então o sistema recusa (RN-TEL-004).
### HU-TEL-004 — Consultar a planta de valores vigente

**Como** como fiscal de tributos,
**quero** consultar os valores unitários vigentes por ano, divisão e ocupação,
**para** instruir lançamentos e contestações com base na tabela oficial.

**Capacidade:** CAP-TEL-004

**Regras relacionadas:** RN-TEL-003

**Critérios de aceitação:**

1. Dado uma planta vigente para a combinação, quando o fiscal consulta, então os valores unitários e a alíquota são retornados
2. Dado que não há planta vigente para a combinação, quando o fiscal consulta, então o sistema responde HTTP 404.
### HU-TEL-005 — Registrar a georreferência do território

**Como** como técnico de georreferenciamento,
**quero** registrar a posição geográfica de divisões e logradouros,
**para** apoiar o georreferenciamento legal e a produção cartográfica.

**Capacidade:** CAP-TEL-005

**Regras relacionadas:** RN-TEL-005

**Critérios de aceitação:**

1. Dado uma divisão existente, quando o técnico registra um polígono com ao menos 3 vértices válidos, então a georreferência é criada
2. Dado que nenhum ou ambos os vínculos são informados, quando o técnico registra, então o sistema recusa (RN-TEL-005)
3. Dado um polígono com menos de 3 vértices, quando o técnico registra, então o sistema recusa com HTTP 409 (RN-TEL-005)
4. Dado uma coordenada fora da faixa do datum, quando o técnico registra, então o sistema recusa (RN-TEL-005).

# 4. Rastreabilidade às Capacidades

| História | Capacidade | Regras |
| --- | | --- | |
| HU-TEL-001 — Manter o cadastro de divisões territoriais | CAP-TEL-001 | RN-TEL-001, RN-TEL-006 |
| HU-TEL-002 — Manter a malha de logradouros | CAP-TEL-002 | RN-TEL-002 |
| HU-TEL-003 — Elaborar e aprovar a planta de valores do exercício | CAP-TEL-003 | RN-TEL-003, RN-TEL-004 |
| HU-TEL-004 — Consultar a planta de valores vigente | CAP-TEL-004 | RN-TEL-003 |
| HU-TEL-005 — Registrar a georreferência do território | CAP-TEL-005 | RN-TEL-005 |


---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 006-Historias-de-Usuario-Gestao-Territorial.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_territorial`. Alterações no código devem ser
> refletidas reexecutando o gerador.
