# 016 – Modelo de Segurança – Contabilidade Pública

#### Modelo de Segurança – Contabilidade Pública

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-CON-016

**Domínio:** Contabilidade Pública

**Versão:** 1.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Contabilidade-Publica.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000C-HIERARQUIA-DOCUMENTAL-v1.0.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
* `AUDITORIA-DOM-CON-2026-09-30.md`

---

# 1. Finalidade

Este artefato especifica o modelo de segurança do domínio de Contabilidade Pública,
abrangendo autenticação, autorização, segregação de funções, proteção de dados e
conformidade aplicável.

---

# 2. Princípios de Segurança

* **Autenticação antes de autorização:** nenhuma operação sem identidade verificada.
* **Segregação de funções:** emitir, autorizar e pagar exigem papéis distintos.
* **Privilégio mínimo:** cada papel acessa apenas o necessário.
* **Rastreabilidade:** toda operação com efeito financeiro é auditável.
* **Integridade:** registro contábil não pode ser alterado sem contrapartida.

---

# 3. Autenticação

| Aspecto | Definição |
| --- | --- |
| Mecanismo | OAuth 2.0 / JWT, gerenciado pelo DOM-IDN |
| Ponto de entrada | Middleware de autenticação da aplicação FastAPI |
| Escopo do domínio | Identificação do servidor responsável pela operação |
| Estado atual | O middleware existe na aplicação; **o domínio não consome a identidade** |

**Lacuna:** os endpoints do DOM-CON não recebem nem verificam o usuário autenticado,
razão pela qual o campo `created_by` permanece vazio (achado M-04) e a autoria não pode
ser atribuída.

---

# 4. Autorização

## 4.1 Matriz de Permissões por Papel

| Operação | Contador | Ordenador | Tesoureiro | Gestor PCASP | Conciliador | Controle | Cidadão |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Emitir empenho | ✔ | — | — | — | — | — | — |
| Liquidar | ✔ | — | — | — | — | — | — |
| Pagar | — | — | ✔ | — | — | — | — |
| Anular | ✔ | ✔ | — | — | — | — | — |
| Cancelar empenho | — | ✔ | — | — | — | — | — |
| Criar conta | — | — | — | ✔ | — | — | — |
| Desativar conta | — | — | — | ✔ | — | — | — |
| Lançar partidas | ✔ | — | — | — | — | — | — |
| Estornar lançamento | — | ✔ | — | — | — | — | — |
| Conciliar conta | — | — | — | — | ✔ | — | — |
| Justificar divergência | — | — | — | — | ✔ | — | — |
| Consultar execução | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ (resumo) |

**Estado atual:** a matriz **não é aplicada**. Os endpoints não verificam perfil, e
qualquer servidor autenticado pode executar qualquer operação (achado RNF-CON-007).

## 4.2 Segregação de Funções

A Lei 4.320/64 exige separação entre quem autoriza o empenho e quem libera o
pagamento. O domínio registra o ator em `001-Mapa-de-Atores` com essa separação, mas
**nenhum controle técnico a impõe**.

**Requisito:** o sistema deve recusar pagamento da liquidação de empenho emitido pelo
mesmo servidor, exceto quando a norma municipal dispensando expressamente a
segregação.

---

# 5. Proteção de Dados

## 5.1 Classificação

| Dado | Classificação | Fundamento |
| --- | --- | --- |
| Dados de execução da despesa | **Pública** | LC 4.320/64, art. 48 |
| Dados do plano de contas | Pública | Norma contábil aplicável |
| Identificação do favorecido | **Restrita** | LGPD, art. 5º, XVII |
| Identificação do servidor responsável | **Restrita** | LGPD, art. 5º, II |
| Credenciais e tokens | **Sigilosa** | Lei 13.874/2019 |

## 5.2 Proteções Aplicáveis

| Proteção | Aplicação ao domínio |
| --- | --- |
| Criptografia em trânsito | TLS obrigatório na exposição da API |
| Criptografia em repouso | Criptografia do volume do PostgreSQL |
| Controle de acesso | Por papel, conforme matriz da seção 4 |
| Auditoria de acesso | Registro de leitura em dados restritos |
| Minimização | Somente `favorecido_nome` é armazenado; o cadastro oficial vive no DOM-COM |
| Retenção | Preservação conforme prazo legal de guarda da documentação contábil |

**Lacuna de minimização:** o campo `favorecido_id` foi previsto no domínio para
referenciar o fornecedor sem duplicar o cadastro, **mas não possui coluna** — o
repositório persiste apenas o nome livre, que pode divergir do cadastro oficial
(achado A-01).

---

# 6. Integridade e Não Repudiação

| Garantia | Mecanismo | Estado |
| --- | --- | --- |
| Não repudiação da emissão | `created_by` e `created_at` no empenho | Parcial — `created_by` não preenchido |
| Não repudiação do lançamento | Autor e data no lançamento | **Não implementada** |
| Imutabilidade após lançamento | Estorno por contrapartida | Planejado |
| Integridade referencial | `ON DELETE RESTRICT` em FKs internas | Atendida |
| Integridade com DOM-ORC | Chave estrangeira entre schemas | **Ausente** |
| Integridade das partidas dobradas | Tabela filha com FK e trigger de balanço | **Ausente** (JSON em TEXT) |

---

# 7. Conformidade Aplicável

| Norma | Âmbito | Situação |
| --- | --- | --- |
| Lei 4.320/64 | Fases da despesa, segregação de funções | Parcial |
| Lei Complementar 101/2000 | Transparência da execução | **Não implementada** (sem consulta) |
| MCASP | Estrutura de contas e lançamentos | Parcial — falta `data_lancamento` |
| LGPD | Dados pessoais do favorecido e do servidor | Parcial — sem classificação aplicada |
| Instrução normativa do TCE | Prestação de contas | Não avaliado |

---

# 8. Threat Modeling

| Ameaça | Vetor | Mitigação atual | Lacuna |
| --- | --- | --- | --- |
| Empenho sem autorização | Servidor autenticado indevidamente | Nenhuma | Ausência de verificação de papel |
| Pagamento duplicado | Reenvio da requisição | Nenhuma | Ausência de idempotência |
| Alteração de valor lançado | Acesso direto ao banco | Exclusão lógica e `RESTRICT` | Sem trigger de imutabilidade |
| Empenho em dotação inexistente | `dotacao_id` forjado | Validação em aplicação | Sem FK |
| Lançamento desequilibrado | Inserção direta no banco | Validação em aplicação | Sem trigger no banco |
| Exposição de dados do favorecido | Endpoint público | Nenhum | Sem classificação nem filtro |

---

# 9. Plano de Segurança

| Prioridade | Ação | Referência |
| --- | --- | --- |
| 1 | Aplicar autenticação e autorização por papel nos sete serviços | RNF-CON-007 |
| 2 | Preencher `created_by` com o usuário autenticado | RNF-CON-010 |
| 3 | Impedir que o mesmo servidor emita e pague o mesmo empenho | RNF-CON-008 |
| 4 | Tornar idempotente as operações de escrita | A-02 |
| 5 | Adicionar chave estrangeira para dotação e reserva | A-03 |
| 6 | Adicionar trigger de imutabilidade do lançamento lançado | RNF-CON-009 |
| 7 | Normalizar partidas dobradas com FK e trigger de balanço | M-02 |
| 8 | Publicar a execução com classificação de dado público | RF-CON-028 |


---

Este artefato especifica o modelo de segurança do domínio de Contabilidade Pública,
abrangendo autenticação, autorização, segregação de funções, proteção de dados e
conformidade aplicável.

---

# 2. Princípios de Segurança

* **Autenticação antes de autorização:** nenhuma operação sem identidade verificada.
* **Segregação de funções:** emitir, autorizar e pagar exigem papéis distintos.
* **Privilégio mínimo:** cada papel acessa apenas o necessário.
* **Rastreabilidade:** toda operação com efeito financeiro é auditável.
* **Integridade:** registro contábil não pode ser alterado sem contrapartida.

---

# 3. Autenticação

| Aspecto | Definição |
| --- | --- |
| Mecanismo | OAuth 2.0 / JWT, gerenciado pelo DOM-IDN |
| Ponto de entrada | Middleware de autenticação da aplicação FastAPI |
| Escopo do domínio | Identificação do servidor responsável pela operação |
| Estado atual | O middleware existe na aplicação; **o domínio não consome a identidade** |

**Lacuna:** os endpoints do DOM-CON não recebem nem verificam o usuário autenticado,
razão pela qual o campo `created_by` permanece vazio (achado M-04) e a autoria não pode
ser atribuída.

---

# 4. Autorização

## 4.1 Matriz de Permissões por Papel

| Operação | Contador | Ordenador | Tesoureiro | Gestor PCASP | Conciliador | Controle | Cidadão |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Emitir empenho | ✔ | — | — | — | — | — | — |
| Liquidar | ✔ | — | — | — | — | — | — |
| Pagar | — | — | ✔ | — | — | — | — |
| Anular | ✔ | ✔ | — | — | — | — | — |
| Cancelar empenho | — | ✔ | — | — | — | — | — |
| Criar conta | — | — | — | ✔ | — | — | — |
| Desativar conta | — | — | — | ✔ | — | — | — |
| Lançar partidas | ✔ | — | — | — | — | — | — |
| Estornar lançamento | — | ✔ | — | — | — | — | — |
| Conciliar conta | — | — | — | — | ✔ | — | — |
| Justificar divergência | — | — | — | — | ✔ | — | — |
| Consultar execução | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ (resumo) |

**Estado atual:** a matriz **não é aplicada**. Os endpoints não verificam perfil, e
qualquer servidor autenticado pode executar qualquer operação (achado RNF-CON-007).

## 4.2 Segregação de Funções

A Lei 4.320/64 exige separação entre quem autoriza o empenho e quem libera o
pagamento. O domínio registra o ator em `001-Mapa-de-Atores` com essa separação, mas
**nenhum controle técnico a impõe**.

**Requisito:** o sistema deve recusar pagamento da liquidação de empenho emitido pelo
mesmo servidor, exceto quando a norma municipal dispensando expressamente a
segregação.

---

# 5. Proteção de Dados

## 5.1 Classificação

| Dado | Classificação | Fundamento |
| --- | --- | --- |
| Dados de execução da despesa | **Pública** | LC 4.320/64, art. 48 |
| Dados do plano de contas | Pública | Norma contábil aplicável |
| Identificação do favorecido | **Restrita** | LGPD, art. 5º, XVII |
| Identificação do servidor responsável | **Restrita** | LGPD, art. 5º, II |
| Credenciais e tokens | **Sigilosa** | Lei 13.874/2019 |

## 5.2 Proteções Aplicáveis

| Proteção | Aplicação ao domínio |
| --- | --- |
| Criptografia em trânsito | TLS obrigatório na exposição da API |
| Criptografia em repouso | Criptografia do volume do PostgreSQL |
| Controle de acesso | Por papel, conforme matriz da seção 4 |
| Auditoria de acesso | Registro de leitura em dados restritos |
| Minimização | Somente `favorecido_nome` é armazenado; o cadastro oficial vive no DOM-COM |
| Retenção | Preservação conforme prazo legal de guarda da documentação contábil |

**Lacuna de minimização:** o campo `favorecido_id` foi previsto no domínio para
referenciar o fornecedor sem duplicar o cadastro, **mas não possui coluna** — o
repositório persiste apenas o nome livre, que pode divergir do cadastro oficial
(achado A-01).

---

# 6. Integridade e Não Repudiação

| Garantia | Mecanismo | Estado |
| --- | --- | --- |
| Não repudiação da emissão | `created_by` e `created_at` no empenho | Parcial — `created_by` não preenchido |
| Não repudiação do lançamento | Autor e data no lançamento | **Não implementada** |
| Imutabilidade após lançamento | Estorno por contrapartida | Planejado |
| Integridade referencial | `ON DELETE RESTRICT` em FKs internas | Atendida |
| Integridade com DOM-ORC | Chave estrangeira entre schemas | **Ausente** |
| Integridade das partidas dobradas | Tabela filha com FK e trigger de balanço | **Ausente** (JSON em TEXT) |

---

# 7. Conformidade Aplicável

| Norma | Âmbito | Situação |
| --- | --- | --- |
| Lei 4.320/64 | Fases da despesa, segregação de funções | Parcial |
| Lei Complementar 101/2000 | Transparência da execução | **Não implementada** (sem consulta) |
| MCASP | Estrutura de contas e lançamentos | Parcial — falta `data_lancamento` |
| LGPD | Dados pessoais do favorecido e do servidor | Parcial — sem classificação aplicada |
| Instrução normativa do TCE | Prestação de contas | Não avaliado |

---

# 8. Threat Modeling

| Ameaça | Vetor | Mitigação atual | Lacuna |
| --- | --- | --- | --- |
| Empenho sem autorização | Servidor autenticado indevidamente | Nenhuma | Ausência de verificação de papel |
| Pagamento duplicado | Reenvio da requisição | Nenhuma | Ausência de idempotência |
| Alteração de valor lançado | Acesso direto ao banco | Exclusão lógica e `RESTRICT` | Sem trigger de imutabilidade |
| Empenho em dotação inexistente | `dotacao_id` forjado | Validação em aplicação | Sem FK |
| Lançamento desequilibrado | Inserção direta no banco | Validação em aplicação | Sem trigger no banco |
| Exposição de dados do favorecido | Endpoint público | Nenhum | Sem classificação nem filtro |

---

# 9. Plano de Segurança

| Prioridade | Ação | Referência |
| --- | --- | --- |
| 1 | Aplicar autenticação e autorização por papel nos sete serviços | RNF-CON-007 |
| 2 | Preencher `created_by` com o usuário autenticado | RNF-CON-010 |
| 3 | Impedir que o mesmo servidor emita e pague o mesmo empenho | RNF-CON-008 |
| 4 | Tornar idempotente as operações de escrita | A-02 |
| 5 | Adicionar chave estrangeira para dotação e reserva | A-03 |
| 6 | Adicionar trigger de imutabilidade do lançamento lançado | RNF-CON-009 |
| 7 | Normalizar partidas dobradas com FK e trigger de balanço | M-02 |
| 8 | Publicar a execução com classificação de dado público | RF-CON-028 |

---

# Versionamento

| Versão | Data | Descrição |
| --- | --- | --- |
| 1.0 | 2026-09-30 | Conteudo inicial derivado da auditoria do modulo `sigmun_con` e do PCASP |

---

**Documento:** 016-Modelo-de-Seguranca-Contabilidade-Publica.md
**Última atualização:** 2026-09-30
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
