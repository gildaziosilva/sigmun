# 001 – Mapa de Atores – Cadastro Único Municipal

#### Mapa de Atores – Cadastro Único Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CUM-001

**Domínio:** Cadastro Único Municipal

**Versão:** 1.0

**Status:** Vigente

**Entidades Implementadas:**
- `Pessoa` - Agregado familiar com atributos: CPF/CNPJ, nome, tipo (Física/Jurídica), data de nascimento, endereço principal
- `UnidadeAdministrativa` - Estrutura administrativa (cidade, bairro, rua, CEP) relacionada ao cadastro
- `DadosFisicos` - Endereço, telefone, contato de emergência (para pessoa física)
- `DadosJuridicos` - Razão social, inscrição estadual, atividade econômica (para pessoa jurídica)

**Casos de Uso Principais (15 total):**
1. Cadastro de pessoa física (RN-CUM-001 a 003: CPF/CNPJ unicidade, endereço principal)
2. Cadastro de pessoa jurídica (RN-CUM-004 a 007: CNPJ unicidade, atividade econômica)
3. Inclusão de endereço ao agregado (RN-CUM-005: endereço principal/alternativo)
4. Inclusão de documento (RN-CUM-002/003: validação CPF/CNPJ; RN-CUM-006: contato)
5. Inclusão de contato (telefone, e-mail, redes sociais) (RN-CUM-006)
6. Consultas e listagens de pessoas cadastradas
7. Atualização de dados cadastrais
8. Exclusão lógica de pessoas e documentos
9. Consulta de unidade administrativa associated a pessoa
10. Agrupamento familiar (vínculo entre pessoas Físicas e Jurídicas)
11. Consulta por CPF/CNPJ (validade e status)
12. Registro de histórico de alterações
13. Integração com DOM-IDN para autenticação e autorização
14. Integração com DOM-DAD para metadados e qualidade da informação
15. Geração de relatórios e indicadores cadastrais

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Cadastro-Unico-Municipal.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

---

# 1. Finalidade

O **Mapa de Atores – Cadastro Único Municipal** (`DOM-CUM`) tem como finalidade mapear e definir identificação dos atores do domínio.

Este artefato é um **esboço inicial padronizado** da arquitetura corporativa do SIGMUN. O conteúdo será preenchido progressivamente conforme a modelagem detalhada do domínio **Cadastro Único Municipal** (`DOM-CUM`) avance.

---

# 2. Escopo e Diretrizes

As informações deste documento estão em elaboração e serão atualizadas periodicamente pela Equipe SIGMUN de acordo com o andamento da modelagem do domínio **Cadastro Único Municipal**.

Até que o esboço seja substituído por conteúdo específico, considere que:

* a estrutura deste artefato segue o padrão corporativo adotado pelo SIGMUN;
* as seções aqui apresentadas servirão de guia para a elaboração detalhada;
* o preenchimento deve observar as convenções definidas em `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`.

---

# 3. Versionamento

| Versão | Data       | Descrição                                           |
| ------ | ---------- | --------------------------------------------------- |
| 1.0    | 2026-08-20 | Criação do esboço inicial padronizado do artefato   |

---

**Documento:** 001-Mapa-de-Atores-Cadastro-Unico-Municipal.md

**Última atualização:** 2026-08-20

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
