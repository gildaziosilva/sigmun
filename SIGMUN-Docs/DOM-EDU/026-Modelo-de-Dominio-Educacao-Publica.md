# 026 – Modelo-de-Dominio – Educação Pública

#### Modelo-de-Dominio – Educação Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-EDU-026

**Domínio:** Educação Pública

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Educacao-Publica.md`
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

Este artefato detalha **o modelo de domínio** do domínio Educação Pública (`DOM-EDU`), com base na implementação material identificada em `src/modules/sigmun_educacao` e no conteúdo de negócio declarado no gerador.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| alunos | `AlunoModel` | 13 |
| distribuicoes_merenda | `DistribuicaoMerendaModel` | 8 |
| itens_merenda | `ItemMerendaModel` | 9 |
| lancamentos_diario | `LancamentoDiarioModel` | 8 |
| matriculas | `MatriculaModel` | 13 |
| passagens_transporte | `PassagemTransporteModel` | 6 |
| rotas_transporte | `RotaTransporteModel` | 10 |

---

# 3. Domínios de valor

### Sexo

| Membro | Valor |
| --- | --- |
| MASCULINO | "masculino" |
| FEMININO | "feminino" |
| IGNORADO | "ignorado" |
### StatusAluno

| Membro | Valor |
| --- | --- |
| ATIVO | "ativo" |
| INATIVO | "inativo" |
### StatusMatricula

| Membro | Valor |
| --- | --- |
| ATIVA | "ativa" |
| TRANSFERIDA | "transferida" |
| CANCELADA | "cancelada" |
| CONCLUIDA | "concluida" |
### StatusRota

| Membro | Valor |
| --- | --- |
| ATIVA | "ativa" |
| INATIVA | "inativa" |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-EDU-001 | o CPF do aluno, quando informado, tem 11 dígitos e é único |
| RN-EDU-002 | a transferência exige matrícula concluída na origem. |
| RN-EDU-003 | o lançamento no diário referencia a matrícula ativa. |
| RN-EDU-010 | o aluno possui no máximo UMA matrícula ``ativa`` por vez; |
| RN-EDU-020 | o lançamento exige matrícula ativa vinculada; a nota, quando |
| RN-EDU-030 | passagem exige rota ``ativa``, matrícula ativa e vaga |
| RN-EDU-040 | distribuição exige estoque suficiente; a baixa é atômica no |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Educacao-Publica-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
