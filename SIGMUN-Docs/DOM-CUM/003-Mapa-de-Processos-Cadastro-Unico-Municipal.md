# 003 – Mapa de Processos – Cadastro Único Municipal

#### Mapa de Processos – Cadastro Único Municipal

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CUM-003

**Domínio:** Cadastro Único Municipal

**Versão:** 1.0

**Status:** Vigente

**Mapa de Processos Implementados:**
Os 11 processos mapeados refletem as operações críticas do Cadastro Único:

1. **Cadastro Inicial** (RN-CUM-001): Recebimento e validação de dados do beneficiário (CPF/CNPJ)
2. **Atualização Cadastral** (RN-CUM-008): Atualização de informações a cada 24 meses ou evento mudança
3. **Inclusão de Endereço** (RN-CUM-005): Registro de endereço principal e/ou alternativo ao agregado
4. **Inclusão de Documento** (RN-CUM-002/003/006): Emissão e validção de CPF/CNPJ e outros documentos
5. **Inclusão de Contato** (RN-CUM-006): Registro de meios de comunicação (telefone, e-mail)
6. **Consulta de Beneficiário** (RN-CUM-010): Busca por CPF/CNPJ, nome, unidade administrativa
7. **Exclusão Lógica** (RN-CUM-011): Marcação de registro como excluído preservando histórico
8. **Agrupamento Familiar** (RN-CUM-012): Vinculação entre pessoas Físicas e Jurídicas do mesmo núcleo
9. **Consulta por CPF/CNPJ com Validade** (RN-CUM-013): Verificação de status ativo/inativo do cadastro
10. **Geração de Relatório** (RN-CUM-014): Produção de relatórios de cadastro para órgãos federais
11. **Atualização de Grupo Familiar** (RN-CUM-015): Atualização das relações de parentesco e dependência

**Fluxo de Trabalho:**
- Captura → Validação → Classificação → Inclusão → Consulta → Atualização → Exclusão (se necessário)
- Cada etapa possui regras de negócio (RN-CUM) e indicadores de qualidade associados
- Integração com fluxos de DOM-GDO (gestão documental) para protocolo e arquivamento

**Indicadores Associados:**
- Tempo médio de cadastro
- Taxa de validação de documentos
- Percentual de atualizações dentro do prazo
- Consistencia entre CPF/CNPJ e dados cadastrais

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

O **Mapa de Processos – Cadastro Único Municipal** (`DOM-CUM`) tem como finalidade mapear e definir mapa de processos do domínio.

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

**Documento:** 003-Mapa-de-Processos-Cadastro-Unico-Municipal.md

**Última atualização:** 2026-08-20

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
