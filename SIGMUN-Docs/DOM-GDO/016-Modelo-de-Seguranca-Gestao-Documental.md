# 016 – Modelo de Segurança – Gestão Documental

#### Modelo de Segurança – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-016

**Domínio:** Gestão Documental

**Versão:** 2.0

**Status:** Vigente

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

* `000-Dominio-Gestao-Documental.md`
* `001-Mapa-de-Atores-Gestao-Documental.md`
* `002-Mapa-de-Capacidades-Gestao-Documental.md`
* `003-Mapa-de-Processos-Gestao-Documental.md`
* `004-Mapa-de-Servicos-Gestao-Documental.md`
* `005-Casos-de-Uso-Gestao-Documental.md`
* `006-Historias-de-Usuario-Gestao-Documental.md`
* `007-Regras-de-Negocio-Gestao-Documental.md`
* `008-Requisitos-Funcionais-Gestao-Documental.md`
* `009-Requisitos-Nao-Funcionais-Gestao-Documental.md`
* `010-Especificacoes-Gestao-Documental.md`
* `011-Criterios-de-Aceitacao-Gestao-Documental.md`
* `012-Matriz-de-Rastreabilidade-Gestao-Documental.md`
* `013-Modelo-de-Dados-Gestao-Documental.md`
* `014-Modelo-de-Integracao-Gestao-Documental.md`
* `015-Arquitetura-de-Servicos-Gestao-Documental.md`
* `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
* `000A-Padrao-Corporativo-de-Documentacao-do-SIGMUN.md`
* `000B-VOCABULARIO-CORPORATIVO-DO-SIGMUN.md`
* `000D-MODELO-DE-DOCUMENTO.md`
* `000G-Framework-Corporativo-de-Gestao-de-Requisitos-e-Rastreabilidade-do-SIGMUN.md`
* `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

---

# 1. Finalidade

Este documento define o **Modelo de Segurança do Domínio de Gestão Documental do SIGMUN**.

O modelo estabelece os princípios, controles, responsabilidades e mecanismos necessários para proteger informações, processos, serviços, documentos, operações e integrações relacionados ao domínio.

O modelo deverá garantir, de forma integrada:

* confidencialidade;
* integridade;
* disponibilidade;
* autenticidade;
* rastreabilidade;
* responsabilização;
* proteção de dados pessoais;
* segregação de funções;
* prevenção de alterações indevidas;
* identificação de acessos e operações.

---

# 2. Objetivos

São objetivos deste modelo:

1. proteger os dados do domínio;
2. proteger os serviços e APIs;
3. controlar o acesso às funcionalidades;
4. impedir operações não autorizadas;
5. preservar a integridade dos processos;
6. garantir rastreabilidade das operações;
7. aplicar segregação de funções;
8. proteger dados pessoais;
9. proteger documentos e evidências;
10. reduzir riscos de fraude, erro e abuso;
11. permitir auditoria;
12. apoiar conformidade com as políticas corporativas do SIGMUN;
13. permitir integração segura com outros domínios e sistemas externos.

---

# 3. Princípios de Segurança

## 3.1 Segurança por Princípio

A segurança deverá ser considerada desde a definição do processo, requisito, serviço, modelo de dados e interface.

## 3.2 Privilégio Mínimo

Cada usuário deverá possuir somente as permissões necessárias para executar suas responsabilidades.

## 3.3 Necessidade de Saber

O acesso a informações deverá considerar a necessidade efetiva de utilização.

## 3.4 Segregação de Funções

Operações incompatíveis deverão ser separadas entre diferentes responsabilidades.

Exemplo:

```text
Criar documento
    ≠
Classificar documento
    ≠
Autorizar eliminação
    ≠
Auditar operações
```

## 3.5 Defesa em Profundidade

Múltiplas camadas de segurança deverão ser aplicadas para proteger os ativos.

## 3.6 Auditoria por Padrão

Todas as operações relevantes deverão ser registradas para fins de auditoria.

---

# 4. Perfis de Acesso

## 4.1 Definição de Perfis

| Perfil | Descrição | Permissões |
| --- | --- | --- |
| PUBLICO | Cidadão sem autenticação | Consultar documentos públicos |
| USUARIO_GDO | Servidor gestor documental | CRUD documentos da unidade, tramitar, pesquisar |
| AUTORIDADE_GDO | Autoridade homologadora | Aprovar eliminação, homologar atos |
| ADMIN_GDO | Administrador do sistema | Configurar planos, temporalidade, permissões |
| AUDITOR_GDO | Auditor | Leitura completa + logs de auditoria |

## 4.2 Matriz de Permissões

| Operação | PUBLICO | USUARIO_GDO | AUTORIDADE_GDO | ADMIN_GDO | AUDITOR_GDO |
| --- | --- | --- | --- | --- | --- |
| Consultar documento público | ✅ | ✅ | ✅ | ✅ | ✅ |
| Criar documento | ❌ | ✅ | ❌ | ❌ | ❌ |
| Editar documento próprio | ❌ | ✅ | ❌ | ❌ | ❌ |
| Classificar documento | ❌ | ✅ | ❌ | ✅ | ❌ |
| Tramitar documento | ❌ | ✅ | ❌ | ❌ | ❌ |
| Receber documento | ❌ | ✅ | ❌ | ❌ | ❌ |
| Assinar documento | ❌ | ✅ | ✅ | ❌ | ❌ |
| Aprovar eliminação | ❌ | ❌ | ✅ | ❌ | ❌ |
| Configurar plano classificação | ❌ | ❌ | ❌ | ✅ | ❌ |
| Configurar temporalidade | ❌ | ❌ | ❌ | ✅ | ❌ |
| Gerenciar permissões | ❌ | ❌ | ❌ | ✅ | ❌ |
| Consultar logs auditoria | ❌ | ❌ | ❌ | ❌ | ✅ |
| Exportar relatórios | ❌ | ✅ | ✅ | ✅ | ✅ |

---

# 5. Classificação de Sigilo

## 5.1 Níveis de Sigilo

| Nível | Descrição | Controle de Acesso |
| --- | --- | --- |
| PÚBLICO | Acesso livre | Sem restrição |
| RESTRITO | Acesso limitado à unidade | Usuários da unidade |
| SIGILOSO | Acesso específico | Permissão individual |

## 5.2 Regras de Classificação

1. Todo documento deve ter classificação de sigilo definida
2. Documentos sem classificação são tratados como restritos
3. Classificação sigilosa requer justificativa formal
4. A classificação deve ser registrada em auditoria

---

# 6. Controles de Acesso

## 6.1 Autenticação

* Bearer Token (JWT) via DOM-IDN
* Validação em todas as requisições
* Suporte a certificado digital para assinaturas

## 6.2 Autorização

* Controle de acesso baseado em perfis (RBAC)
* Permissões granulares por documento
* Herança de permissões por unidade

## 6.3 Sessão

* Tempo de expiração do token: 8 horas
* Renovação automática possível
* Logout invalida token imediatamente

---

# 7. Proteção de Dados

## 7.1 Dados em Trânsito

* Criptografia: TLS 1.2 ou superior
* Certificado digital válido
* HSTS habilitado

## 7.2 Dados em Repouso

* Documentos sigilosos: AES-256
* Metadados: criptografia padrão do banco
* Backups criptografados

## 7.3 Dados Pessoais (LGPD)

* Mascaramento em consultas públicas
* Registro de consentimento quando aplicável
* Direito ao esquecimento suportado
* Relatório de impacto disponível

---

# 8. Segregação de Funções

## 8.1 Regras de Segregação

1. Quem cria não pode autorizar eliminação
2. Quem classifica não pode eliminar
3. Quem administra não pode criar documentos
4. Quem auditoria não pode modificar dados

## 8.2 Controle de Conflito de Interesse

* Verificação automática de segregação
* Alertas para operações conflitantes
* Registro em auditoria

---

# 9. Auditoria e Rastreabilidade

## 9.1 Registros de Auditoria

Toda operação relevante deve registrar:

* Identificador do usuário
* Data e hora (timestamp)
* Operação realizada
* Entidade afetada
* Registro afetado
* IP de origem
* Resultado (sucesso/erro)

## 9.2 Imutabilidade

* Registros de auditoria não podem ser alterados
* Registros de auditoria não podem ser excluídos
* Retenção mínima: 5 anos

## 9.3 Logs de Segurança

* Tentativas de acesso negado
* Operações sensíveis (eliminação, alteração de permissões)
* Alterações de classificação de sigilo
* Autenticações suspeitas

---

# 10. Segurança de Integração

## 10.1 APIs Internas

* Autenticação: Bearer Token (JWT) via DOM-IDN
* Rate limiting: 1000 req/min por serviço
* Validação de entrada em todas as requisições

## 10.2 APIs Públicas

* Autenticação: API Key (quando aplicável)
* Rate limiting: 100 req/min por IP
* CORS configurado adequadamente

## 10.3 Sistemas Externos

* mTLS ou OAuth 2.0
* Certificados digitais válidos
* Whitelist de IPs quando aplicável

---

# 11. Resiliência de Segurança

## 11.1 Proteção contra Ataques

| Ataque | Proteção |
| --- | --- |
| SQL Injection | Prepared statements, validação de entrada |
| XSS | Sanitização de saída, Content Security Policy |
| CSRF | Tokens CSRF, SameSite cookies |
| Brute Force | Rate limiting, bloqueio temporário |
| DDoS | WAF, rate limiting, CDN |

## 11.2 Monitoramento

* Alertas de segurança em tempo real
* Análise de padrões de acesso
* Detecção de anomalias

---

# 12. Resposta a Incidentes

## 12.1 Classificação de Incidentes

| Nível | Descrição | Ação |
| --- | --- | --- |
| Baixo | Tentativa de acesso não autorizada | Registrar e monitorar |
| Médio | Acesso indevido a dados restritos | Investigar e bloquear |
| Alto | Violação de dados sigilosos | Resposta imediata, notificar autoridades |

## 12.2 Procedimento de Resposta

1. Identificação do incidente
2. Contenção imediata
3. Análise de impacto
4. Erradicação da causa
5. Recuperação dos serviços
6. Lições aprendidas

---

# 13. Refinamento Futuro

O modelo deste documento representa a primeira versão da segurança do domínio.

Durante o refinamento, o modelo poderá:

* ser expandido com novos controles;
* ser ajustado conforme evolução das ameaças;
* ser integrado com SIEM corporativo;
* ser atualizado conforme novas regulamentações.

---

# 14. Registro no Mapa Mestre

Este artefato deverá ser registrado no:

`000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`

**Identificador do artefato:**

`SEG-MAP-GDO-001`

**Tipo:**

Modelo de Segurança.

**Domínio:**

Gestão Documental.

**Versão:**

2.0.

---

# 15. Próximo Artefato

O próximo artefato recomendado é:

`017-Modelo-de-Auditoria-Gestao-Documental.md`

A cadeia de detalhamento ficará:

```text
000-Domínio
      ↓
001-Atores
      ↓
002-Capacidades
      ↓
003-Processos
      ↓
004-Serviços
      ↓
005-Casos de Uso
      ↓
006-Histórias de Usuário
      ↓
007-Regras de Negócio
      ↓
008-Requisitos Funcionais
      ↓
009-Requisitos Não Funcionais
      ↓
010-Especificações
      ↓
011-Critérios de Aceitação
      ↓
012-Matriz de Rastreabilidade
      ↓
013-Modelo de Dados
      ↓
014-Modelo de Integração
      ↓
015-Arquitetura de Serviços
      ↓
016-Modelo de Segurança
      ↓
017-Modelo de Auditoria
```

---

# 16. Controle de Versões

| Versão | Data       | Descrição |
| ------ | ---------- | --------- |
| 1.0    | 2026-08-20 | Criação do esboço inicial padronizado do artefato |
| 2.0    | 2026-09-02 | Conteúdo detalhado: perfis, controles, segregação |

---

**Documento:** 016-Modelo-de-Seguranca-Gestao-Documental.md

**Última atualização:** 2026-09-02

**Responsável:** Equipe SIGMUN

**Status da revisão:** Vigente
