# 026 – Modelo-de-Dominio – Cadastro Único Municipal

#### Modelo-de-Dominio – Cadastro Único Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CUM-026

**Domínio:** Cadastro Único Municipal

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Cadastro-Unico-Municipal.md`
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

Este artefato detalha **o modelo de domínio** do domínio Cadastro Único Municipal (`DOM-CUM`), com base na implementação material identificada em `src/modules/sigmun_cadastro` e no conteúdo de negócio declarado no gerador.

---

# 2. Entidades

| Tabela | Classe | Atributos |
| --- | --- | --- |
| contatos | `ContatoModel` | 11 |
| documentos | `DocumentoModel` | 14 |
| enderecos | `EnderecoModel` | 21 |
| pessoas | `PessoaModel` | 10 |
| pessoas_fisicas | `PessoaFisicaModel` | 14 |
| pessoas_juridicas | `PessoaJuridicaModel` | 12 |
| unidades_administrativas | `UnidadeAdministrativaModel` | 12 |

---

# 3. Domínios de valor

### TipoContato

| Membro | Valor |
| --- | --- |
| TELEFONE | "TEL" |
| EMAIL | "EMAIL" |
| REDES | "REDES" |
| WHATSAPP | "WHATSAPP" |
### TipoDocumento

| Membro | Valor |
| --- | --- |
| CPF | "CPF" |
| CNPJ | "CNPJ" |
| RG | "RG" |
| INSCRICAO_ESTADUAL | "INSCRICAO_ESTADUAL" |
| INSCRICAO_MUNICIPAL | "INSCRICAO_MUNICIPAL" |
| CNH | "CNH" |
| OUTRO | "OUTRO" |
### TipoEndereco

| Membro | Valor |
| --- | --- |
| RESIDENCIAL | "RESIDENCIAL" |
| COMERCIAL | "COMERCIAL" |
| COBRANCA | "COBRANCA" |
| ENTREGA | "ENTREGA" |
| OUTRO | "OUTRO" |
### TipoPessoa

| Membro | Valor |
| --- | --- |
| FISICA | "FISICA" |
| JURIDICA | "JURIDICA" |
### CategoriaPessoa

| Membro | Valor |
| --- | --- |
| CIDADAO | "CIDADAO" |
| SERVIDOR | "SERVIDOR" |
| FORNECEDOR | "FORNECEDOR" |
| AGENTE_EXTERNO | "AGENTE_EXTERNO" |
### Sexo

| Membro | Valor |
| --- | --- |
| MASCULINO | "M" |
| FEMININO | "F" |
| OUTRO | "OUTRO" |

---

# 4. Regras

| ID | Descrição |
| --- | --- |
| RN-CUM-001 | tipo {FISICA, JURIDICA} exige extensão correspondente |
| RN-CUM-004 | a unicidade de documento considera apenas registros |
| RN-CUM-005 | unicidade de endereço principal vigente por pessoa |
| RN-CUM-006 | unicidade de contato principal por tipo por pessoa |
| RN-CUM-007 | não operar sobre excluída) |
| RN-CUM-008 | o repositório valida ciclos profundos no save |
| RN-CUM-009 | unicidade (desconsiderando a própria unidade) |

---

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0 | 2026-09-30 | Artefato atualizado pelo gerador conforme o estado material e o conteúdo declarado do domínio |

---

**Documento:** 026-Cadastro-Unico-Municipal-Modelo-de-Dominio.md

**Última atualização:** 2026-09-30

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente

> Artefato gerado por `scripts/gerar_artefatos_dominio.py` a partir do
> estado material identificado e do conteúdo de negócio declarado no gerador.
> Para domínios propostos, o conteúdo representa o modelo previsto e não
> constitui evidência de implementação. Alterações no código ou no modelo
> declarado devem ser refletidas reexecutando o gerador.
