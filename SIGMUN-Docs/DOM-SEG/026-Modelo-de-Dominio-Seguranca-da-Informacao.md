# 026 – Modelo-de-Dominio – Segurança da Informação

#### Modelo-de-Dominio – Segurança da Informação

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-SEG-026

**Domínio:** Segurança da Informação

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Seguranca-da-Informacao.md`
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

Este artefato detalha **o modelo de domínio** do domínio Segurança da Informação (`DOM-SEG`), com base na implementação material identificada em `src/modules/sigmun_seg` e no conteúdo de negócio declarado no gerador.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| chaves_criptograficas | `ChaveCriptograficaModel` | 11 |
| controles_seguranca | `ControleSegurancaModel` | 12 |
| credenciais | `CredencialModel` | 11 |
| incidentes_seguranca | `IncidenteSegurancaModel` | 13 |
| politicas_seguranca | `PoliticaSegurancaModel` | 12 |

---

# 3. Domínios de valor

### TipoControle

| Membro | Valor |
| --- | --- |
| FISICO | "fisico" |
| TECNICO | "tecnico" |
| ADMINISTRATIVO | "administrativo" |
### CategoriaControle

| Membro | Valor |
| --- | --- |
| ACESSO | "acesso" |
| CRIPTOGRAFIA | "criptografia" |
| INCIDENTE | "incidente" |
| CONTINUIDADE | "continuidade" |
| CONFORMIDADE | "conformidade" |
### StatusControle

| Membro | Valor |
| --- | --- |
| IMPLEMENTADO | "implementado" |
| PARCIAL | "parcial" |
| PLANEJADO | "planejado" |
### SeveridadeIncidente

| Membro | Valor |
| --- | --- |
| BAIXA | "baixa" |
| MEDIA | "media" |
| ALTA | "alta" |
| CRITICA | "critica" |
### StatusIncidente

| Membro | Valor |
| --- | --- |
| ABERTO | "aberto" |
| EM_ANALISE | "em_analise" |
| EM_MITIGACAO | "em_mitigacao" |
| RESOLVIDO | "resolvido" |
| ENCERRADO | "encerrado" |
### StatusCredencial

| Membro | Valor |
| --- | --- |
| ATIVA | "ativa" |
| SUSPENSA | "suspensa" |
| REVOGADA | "revogada" |
| EXPIRADA | "expirada" |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-SEG-001 | credencial revogada ou expirada é recusada pelo autenticação. |
| RN-SEG-002 | chave criptográfica revogada não pode voltar a valer. |
| RN-SEG-003 | incidente exige classificação de severidade antes do tratamento. |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Seguranca-da-Informacao-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
