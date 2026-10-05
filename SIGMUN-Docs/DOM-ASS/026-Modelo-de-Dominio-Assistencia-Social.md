# 026 – Modelo-de-Dominio – Assistência Social

#### Modelo-de-Dominio – Assistência Social

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-ASS-026

**Domínio:** Assistência Social

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Assistencia-Social.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `030-Roadmap-de-Implementacao-dos-Dominios.md`
* `Mapa-de-Dominios.md`

---


# 1. Finalidade

Este artefato detalha **o modelo de domínio** do domínio Assistência Social (`DOM-ASS`), com base na implementação material identificada em `src/modules/sigmun_assistencia_social` e no conteúdo de negócio declarado no gerador.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| atendimentos_sociais | `AtendimentoSocialModel` | 10 |
| beneficios_eventuais | `BeneficioEventualModel` | 15 |
| familias_cadunico | `FamiliaCadUnicoModel` | 13 |
| pessoas_cadunico | `PessoaCadUnicoModel` | 15 |
| unidades_assistencia | `UnidadeAssistenciaModel` | 13 |

---

# 3. Domínios de valor

### Sexo

| Membro | Valor |
| --- | --- |
| MASCULINO | "masculino" |
| FEMININO | "feminino" |
| IGNORADO | "ignorado" |
### StatusFamilia

| Membro | Valor |
| --- | --- |
| ATIVA | "ativa" |
| INATIVA | "inativa" |
| EXCLUIDA | "excluida" |
### TipoBeneficio

| Membro | Valor |
| --- | --- |
| ALIMENTACAO | "alimentacao" |
| ALUGUEL | "aluguel" |
| MEDICAMENTO | "medicamento" |
| FUNERAL | "funeral" |
| NATALIDADE | "natalidade" |
| CALAMIDADE | "calamidade" |
| OUTRO | "outro" |
### StatusBeneficio

| Membro | Valor |
| --- | --- |
| SOLICITADO | "solicitado" |
| APROVADO | "aprovado" |
| NEGADO | "negado" |
| ENTREGUE | "entregue" |
| CANCELADO | "cancelado" |
### TipoUnidade

| Membro | Valor |
| --- | --- |
| CRAS | "cras" |
| CREAS | "creas" |
| CENTRO_POP | "centro_pop" |
| ABRIGO | "abrigo" |
| OUTRO | "outro" |
### StatusUnidade

| Membro | Valor |
| --- | --- |
| ATIVA | "ativa" |
| INATIVA | "inativa" |
| MANUTENCAO | "manutencao" |
### TipoAtendimento

| Membro | Valor |
| --- | --- |
| ACOLHIMENTO | "acolhimento" |
| ORIENTACAO | "orientacao" |
| ENCAMINHAMENTO | "encaminhamento" |
| VISITA_DOMICILIAR | "visita_domiciliar" |
| GRUPO_CONVIVENCIA | "grupo_convivencia" |
| BENEFICIO_EVENTUAL | "beneficio_eventual" |
| OUTRO | "outro" |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-ASS-001 | o NIS da família é único no cadastro municipal |
| RN-ASS-002 | o CPF da pessoa é único no cadastro municipal |
| RN-ASS-003 | o benefício eventual obedece à máquina de estados |
| RN-ASS-004 | atendimentos são registrados por unidade CRAS/CREAS |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Assistencia-Social-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
