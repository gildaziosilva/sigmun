# 017 – Modelo de Auditoria – Obras e Infraestrutura

#### Modelo de Auditoria – Obras e Infraestrutura

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-OBR-017

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

Este artefato define como o domínio de Obras e Infraestrutura assegura a rastreabilidade
das alterações sobre seus dados.

---

# 2. Campos de Auditoria

| Campo | Tipo | Significado |
| --- | --- | --- |
| `created_at` | `timestamptz` | Momento da criação do registro |
| `created_by` | `text` | Identificador do usuário que criou o registro |
| `updated_at` | `timestamptz` | Momento da última alteração |
| `is_deleted` | `boolean` | Marcação de exclusão lógica |

---

# 3. Abrangência

| Tabela | created_at | created_by | updated_at | is_deleted |
| --- | | --- | | --- | | --- | |
| `obr.obras` | ✔ | ✔ | ✔ | ✔ |
| `obr.medicoes_obras` | ✔ | ✔ | ✔ | ✔ |
| `obr.etapas_obras` | ✔ | ✔ | ✔ | ✔ |
| `obr.despesas_obras` | ✔ | ✔ | — | ✔ |
| `obr.vistorias_obras` | ✔ | ✔ | — | ✔ |


---

# 4. Princípios

* **Imutabilidade do histórico:** a exclusão é lógica; o registro permanece
  consultável para fins fiscais e fundiários.
* **Autoria:** o campo `created_by` existe em todas as tabelas e é persistido,
  mas **não é preenchido a partir de uma sessão autenticada**, porque as rotas
  não exigem autenticação. Até que PB-01/PB-04 do artefato 021 sejam resolvidos,
  a autoria registrada não identifica um usuário autenticado.
* **Rastreabilidade de regra:** as mensagens de erro identificam a regra
  violada, permitindo correlação entre incidente e requisito.

---

# 5. Trilha de Auditoria de Negócio

Além da auditoria técnica, o domínio mantém, na própria entidade:

| Entidade | Evidência preservada |
| --- | |
| PlantaGenericaValores | Legislação e justificativa de revogação |
| AvaliacaoImovel | Valores unitários aplicados e data da avaliação |
| Imovel | Inscrição, áreas e situação ao longo do tempo |


---

# 6. Relato de Incidentes

Eventos de recusa por violação de regra são identificáveis pelo par
(identificador da regra, mensagem), permitindo a construção de indicadores de
conformidade por regra.

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-29 | Artefato detailado a partir da implementação verificada do domínio |

---

**Documento:** 017-Modelo-de-Auditoria-Obras-e-Infraestrutura.md

**Última atualização:** 2026-09-29

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_territoriais.py` a partir da
> implementação em `src/modules/sigmun_obras`. Alterações no código devem ser
> refletidas reexecutando o gerador.
