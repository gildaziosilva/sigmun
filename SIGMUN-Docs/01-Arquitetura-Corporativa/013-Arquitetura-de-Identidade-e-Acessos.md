# 017 – Arquitetura de Gestão de Identidade e Acessos

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal
**Domínio:** Arquitetura Corporativa
**Versão:** 1.0
**Status:** Vigente
**Classificação da Informação:** Pública
**Documento(s) Relacionado(s):**
- 000-CONSTITUICAO-DO-PROJETO-SIGMUN.md

---

---

# 1. Objetivo

Este documento define a arquitetura de gestão de identidade e controle de acessos do SIGMUN, estabelecendo padrões para identificação, autenticação, autorização, auditoria e governança dos usuários da plataforma.

O objetivo é garantir que cada usuário possua:

* identidade única;
* acesso adequado às suas responsabilidades;
* proteção contra uso indevido;
* rastreabilidade completa.

---

# 2. Visão Geral

O SIGMUN possuirá uma camada corporativa de identidade responsável por todos os usuários da plataforma.

Modelo:

```id="w9r5ks"

Usuário

   |

Identidade Municipal

   |

Autenticação

   |

Autorização

   |

Módulos SIGMUN

```

---

# 3. Princípios de Identidade

## 3.1 Identidade Única

Cada pessoa deverá possuir uma única identidade digital no SIGMUN.

Não serão permitidos:

* usuários duplicados;
* contas compartilhadas;
* acessos sem identificação.

---

## 3.2 Menor Privilégio

O usuário terá somente os acessos necessários para sua função.

---

## 3.3 Separação de Funções

Atividades críticas deverão possuir segregação.

Exemplo:

Quem cadastra uma despesa não deve necessariamente aprovar o pagamento.

---

## 3.4 Ciclo de Vida da Identidade

Toda identidade possuirá:

* criação;
* ativação;
* alteração;
* suspensão;
* encerramento.

---

# 4. Tipos de Identidades

O SIGMUN deverá suportar diferentes categorias.

---

# 4.1 Servidores Municipais

Exemplos:

* efetivos;
* contratados;
* comissionados;
* estagiários.

Origem:

* Recursos Humanos.

---

# 4.2 Gestores

Exemplos:

* prefeito;
* secretários;
* diretores;
* coordenadores.

Possuem permissões administrativas.

---

# 4.3 Usuários Externos

Exemplos:

* cidadãos;
* contribuintes;
* fornecedores.

---

# 4.4 Sistemas

Identidades técnicas utilizadas por:

* APIs;
* integrações;
* serviços automáticos.

---

# 5. Cadastro Central de Identidades

O SIGMUN deverá possuir um cadastro corporativo.

Informações:

* nome;
* CPF/CNPJ;
* identificação;
* vínculos;
* contatos;
* situação;
* permissões.

---

# 6. Integração com Cadastro Único Municipal

A identidade deverá estar vinculada ao Cadastro Único Municipal.

Modelo:

```id="1ym9b2"

Pessoa

 |

Identidade Digital

 |

Usuários SIGMUN

```

Uma pessoa poderá possuir diferentes vínculos.

Exemplo:

* servidor;
* contribuinte;
* fornecedor.

---

# 7. Autenticação

A autenticação deverá suportar diferentes métodos.

---

## 7.1 Usuários Internos

Possibilidades:

* usuário e senha;
* MFA;
* certificado digital;
* autenticação institucional.

---

## 7.2 Cidadãos

Integração prevista:

* Gov.br.

Benefícios:

* identidade digital nacional;
* redução de cadastros duplicados;
* maior segurança.

---

## 7.3 Sistemas

Métodos:

* OAuth 2.0;
* JWT;
* certificados;
* chaves de serviço.

---

# 8. Autenticação Multifator (MFA)

Usuários privilegiados deverão utilizar MFA.

Aplicável:

* administradores;
* gestores;
* contabilidade;
* controladoria;
* jurídico;
* usuários com acesso sensível.

Métodos:

* aplicativo autenticador;
* token;
* certificado.

---

# 9. Modelo de Autorização

O SIGMUN utilizará controle baseado em:

* papéis;
* atributos;
* contexto.

---

# 10. RBAC – Controle por Papéis

Exemplo:

```id="7z9t6j"

Papel:

Secretário Municipal

Permissões:

- visualizar indicadores
- aprovar processos
- consultar relatórios

```

---

# 11. ABAC – Controle por Atributos

Permissões considerando:

* secretaria;
* unidade;
* localização;
* cargo;
* vínculo.

Exemplo:

Um médico poderá acessar pacientes somente da unidade onde atua.

---

# 12. Estrutura de Permissões

Modelo:

```id="0b2s7h"

Usuário

   |

Papel

   |

Permissões

   |

Recursos

```

---

# 13. Perfis Administrativos

Perfis iniciais:

## Administrador do Sistema

Responsável pela plataforma.

---

## Gestor Municipal

Visão estratégica.

---

## Secretário

Gestão da secretaria.

---

## Servidor Operacional

Execução diária.

---

## Auditor/Controladoria

Consulta e fiscalização.

---

## Cidadão

Serviços públicos.

---

## Fornecedor

Relacionamento comercial.

---

# 14. Delegação de Acesso

O sistema deverá permitir:

* substituição temporária;
* férias;
* afastamentos;
* delegação formal.

Exemplo:

Secretário em viagem:

Delegar aprovação ao substituto.

---

# 15. Controle de Acesso por Secretaria

O acesso deverá considerar a estrutura administrativa.

Exemplo:

```id="qz9k33"

Prefeitura

 ├── Saúde

 ├── Educação

 ├── Administração

 ├── Finanças

 └── Assistência Social

```

---

# 16. Gestão do Ciclo de Vida

Eventos:

## Entrada

Criação automática após admissão.

---

## Mudança

Alteração de cargo ou secretaria.

---

## Saída

Bloqueio automático após desligamento.

---

# 17. Integração com Recursos Humanos

O RH será fonte oficial para servidores.

Eventos:

* admissão;
* exoneração;
* alteração funcional;
* afastamento.

---

# 18. Auditoria de Acessos

Registrar:

* login;
* falhas;
* alterações de permissão;
* consultas;
* ações críticas.

---

# 19. Trilhas de Auditoria

Exemplo:

```id="p8k2k5"

Usuário:
Maria Silva

Ação:
Alterou permissão

Data:
30/07/2026

Anterior:
Consulta

Novo:
Aprovação

Responsável:
Administrador

```

---

# 20. Gestão de Usuários Externos

Cidadãos e fornecedores deverão possuir:

* cadastro próprio;
* autenticação segura;
* recuperação de acesso;
* aceite de termos.

---

# 21. Segurança de Senhas

Políticas:

* complexidade mínima;
* bloqueio após tentativas;
* expiração quando necessário;
* armazenamento seguro.

---

# 22. Contas Privilegiadas

Usuários administrativos deverão possuir controles especiais:

* MFA obrigatório;
* logs completos;
* revisão periódica;
* aprovação de acesso.

---

# 23. Revisão Periódica de Acessos

A Prefeitura deverá realizar:

* revisão de usuários ativos;
* validação de permissões;
* remoção de acessos indevidos.

---

# 24. Integrações Externas

A camada de identidade deverá integrar com:

* Gov.br;
* eSocial;
* sistemas bancários;
* serviços federais;
* APIs municipais.

---

# 25. Indicadores de Gestão de Identidade

Indicadores:

* usuários ativos;
* usuários inativos;
* acessos negados;
* permissões revisadas;
* incidentes de acesso.

---

# 26. Evolução Futura

A arquitetura deverá permitir:

* Single Sign-On (SSO);
* autenticação biométrica;
* identidade móvel;
* análise comportamental;
* governança automatizada.

---

# 27. Conclusão

A Arquitetura de Gestão de Identidade e Acessos estabelece a base de segurança operacional do SIGMUN.

Ao criar uma identidade digital única para cidadãos, servidores, gestores e sistemas, a Prefeitura terá maior controle sobre seus recursos, garantindo segurança, transparência e conformidade com a LGPD e os requisitos de auditoria pública.

---

**Documento:**013-Arquitetura-de-Identidade-e-Acessos.md
**Última atualização:** 2026-08-03
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
