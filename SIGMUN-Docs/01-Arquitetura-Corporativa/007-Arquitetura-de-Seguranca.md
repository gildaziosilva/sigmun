# 011 – Arquitetura de Segurança

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

Este documento estabelece a arquitetura de segurança da informação do SIGMUN, definindo princípios, controles, padrões técnicos e processos necessários para proteger os dados, aplicações, integrações e infraestrutura da plataforma.

A arquitetura de segurança tem como objetivos:

* proteger informações públicas e dados pessoais;
* garantir confidencialidade, integridade e disponibilidade;
* atender requisitos legais;
* permitir auditoria completa;
* reduzir riscos operacionais;
* garantir continuidade dos serviços municipais.

---

# 2. Princípios de Segurança

A segurança do SIGMUN será baseada nos seguintes princípios:

---

## 2.1 Security by Design

A segurança deverá ser incorporada desde a concepção das funcionalidades.

Nenhum módulo deverá ser desenvolvido sem considerar:

* controle de acesso;
* proteção de dados;
* auditoria;
* validação;
* tratamento de riscos.

---

## 2.2 Privacy by Design

A proteção de dados pessoais deverá ser considerada desde o desenho dos processos.

Aplicação dos princípios:

* finalidade;
* adequação;
* necessidade;
* transparência;
* segurança;
* prevenção.

---

## 2.3 Defesa em Profundidade

A proteção será realizada em múltiplas camadas.

Exemplo:

```
Usuário
   |
Autenticação
   |
Aplicação
   |
API Gateway
   |
Banco de Dados
   |
Infraestrutura
```

Uma falha em uma camada não deverá comprometer todo o sistema.

---

## 2.4 Menor Privilégio

Usuários terão somente os acessos necessários para suas funções.

Nenhum usuário deverá possuir permissões excessivas.

---

## 2.5 Zero Trust

Nenhuma comunicação deverá ser considerada confiável automaticamente.

Toda solicitação deverá ser:

* autenticada;
* autorizada;
* registrada.

---

# 3. Modelo de Segurança

A arquitetura será organizada em cinco pilares:

1. Identidade e acesso;
2. Proteção de dados;
3. Segurança de aplicações;
4. Segurança de infraestrutura;
5. Monitoramento e resposta.

---

# 4. Gestão de Identidade e Acesso (IAM)

O SIGMUN deverá possuir um sistema centralizado de identidade.

Tipos de usuários:

* servidores municipais;
* gestores;
* controladoria;
* jurídico;
* contadores;
* fornecedores;
* contribuintes;
* cidadãos;
* sistemas externos.

---

# 5. Autenticação

Métodos previstos:

## Usuários internos

Possibilidades:

* usuário e senha;
* autenticação multifator (MFA);
* certificado digital;
* integração institucional.

---

## Cidadãos

Integração prevista:

* Gov.br;
* identidade digital.

---

## Sistemas

Autenticação por:

* OAuth 2.0;
* certificados;
* tokens;
* chaves de integração.

---

# 6. Autorização

O modelo de autorização deverá utilizar:

## RBAC – Role Based Access Control

Permissões baseadas em papéis.

Exemplos:

```
Secretário Municipal
    |
    ├── visualizar relatórios
    ├── aprovar processos
    └── consultar indicadores
```

---

## Possível evolução para ABAC

Controle baseado em atributos:

Exemplo:

Usuário:

* Secretaria = Saúde
* Cargo = Médico
* Localidade = Unidade X

Permissão:

* acessar pacientes daquela unidade.

---

# 7. Modelo de Permissões

As permissões deverão considerar:

* usuário;
* órgão;
* secretaria;
* unidade administrativa;
* função;
* módulo;
* operação.

Operações:

* consultar;
* criar;
* alterar;
* excluir;
* aprovar;
* publicar;
* exportar.

---

# 8. Proteção de Dados Pessoais

O SIGMUN deverá classificar informações conforme sensibilidade.

---

## Dados Públicos

Exemplo:

* informações institucionais;
* dados publicados no Portal da Transparência.

---

## Dados Internos

Exemplo:

* documentos administrativos;
* relatórios internos.

---

## Dados Pessoais

Exemplo:

* CPF;
* endereço;
* telefone;
* dados funcionais.

---

## Dados Sensíveis

Exemplo:

* informações de saúde;
* dados socioassistenciais;
* informações familiares.

---

# 9. Criptografia

## Dados em trânsito

Obrigatório:

* HTTPS;
* TLS atualizado.

---

## Dados armazenados

Aplicação de criptografia para informações sensíveis.

Exemplos:

* documentos pessoais;
* dados médicos;
* informações protegidas pela LGPD.

---

# 10. Segurança do Banco de Dados

Controles:

* usuários separados por ambiente;
* privilégios mínimos;
* registros de acesso;
* backups protegidos;
* criptografia;
* auditoria.

---

# 11. Segurança das Aplicações

O desenvolvimento deverá considerar:

* OWASP Top 10;
* validação de entrada;
* proteção contra SQL Injection;
* proteção contra XSS;
* proteção contra CSRF;
* controle de sessão;
* tratamento seguro de arquivos.

---

# 12. Segurança das APIs

Todas as APIs deverão possuir:

* autenticação;
* autorização;
* controle de versão;
* limitação de requisições;
* validação de dados;
* logs.

Controles:

* API Gateway;
* rate limiting;
* tokens;
* certificados.

---

# 13. Auditoria e Trilhas de Acesso

Atendimento aos requisitos:

* SIAFIC;
* TCE/BA;
* LGPD;
* Controle Interno.

Deverão ser registrados:

* login;
* logout;
* consultas;
* alterações;
* exclusões;
* aprovações;
* exportações;
* integrações.

---

## Exemplo

```
Usuário:
João Silva

Data:
30/07/2026 14:35

Ação:
Alteração cadastral

Registro:
Pessoa 54892

Valor anterior:
Rua A

Valor novo:
Rua B
```

---

# 14. Gestão de Logs

Os logs deverão ser:

* centralizados;
* protegidos contra alteração;
* pesquisáveis;
* armazenados conforme legislação.

Tipos:

* aplicação;
* segurança;
* auditoria;
* integração;
* infraestrutura.

---

# 15. Segurança da Infraestrutura

Ambiente previsto:

* AWS.

Controles:

* redes privadas;
* grupos de segurança;
* firewall;
* segregação de ambientes;
* controle de acesso administrativo;
* monitoramento.

---

# 16. Gestão de Segredos

Credenciais não deverão existir em código fonte.

Utilizar:

* cofres de senha;
* variáveis protegidas;
* rotação de chaves.

---

# 17. Backup e Recuperação

A política deverá contemplar:

* backups automáticos;
* cópias externas;
* criptografia;
* testes de restauração.

Objetivos:

RPO:

* perda máxima aceitável de dados.

RTO:

* tempo máximo para recuperação.

Valores deverão ser definidos na fase de implantação.

---

# 18. Continuidade de Negócio

O SIGMUN deverá possuir:

* plano de continuidade;
* procedimentos de contingência;
* responsáveis definidos;
* testes periódicos.

---

# 19. Gestão de Incidentes

Deverá existir processo para:

* identificação;
* classificação;
* contenção;
* investigação;
* recuperação;
* comunicação.

Exemplos:

* vazamento de dados;
* acesso indevido;
* indisponibilidade;
* comprometimento de credenciais.

---

# 20. Monitoramento de Segurança

Indicadores:

* tentativas de acesso inválidas;
* usuários bloqueados;
* alterações críticas;
* falhas de integração;
* comportamento anormal.

---

# 21. Segurança no Desenvolvimento

O ciclo de desenvolvimento deverá incluir:

* análise de código;
* revisão;
* testes automatizados;
* testes de segurança;
* análise de dependências.

---

# 22. Conformidade Legal

A arquitetura deverá atender:

* LGPD;
* Lei 14.129/2021;
* Lei 14.133/2021;
* LC 101/2000;
* SIAFIC;
* PCASP;
* eSocial;
* requisitos TCE/BA.

---

# 23. Modelo de Maturidade de Segurança

A evolução seguirá níveis:

## Nível 1 – Básico

* autenticação;
* backups;
* logs.

## Nível 2 – Controlado

* MFA;
* auditoria;
* gestão de acessos.

## Nível 3 – Gerenciado

* monitoramento;
* resposta a incidentes;
* testes.

## Nível 4 – Avançado

* inteligência de segurança;
* análise comportamental;
* automação.

---

# 24. Conclusão

A Arquitetura de Segurança estabelece os fundamentos para que o SIGMUN seja uma plataforma confiável, segura e adequada ao ambiente da administração pública.

A proteção dos dados municipais será tratada como requisito estrutural do sistema, garantindo que a digitalização dos processos aumente a eficiência sem comprometer a privacidade, a transparência e a confiança dos cidadãos.

---

**Documento:**007-Arquitetura-de-Segurança.md
**Última atualização:** 2026-08-03
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
