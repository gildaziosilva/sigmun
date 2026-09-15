# 023 – Plano de Treinamento – Gestão Documental

#### Plano de Treinamento – Gestão Documental

**Projeto:** SIGMUN – Sistema Integrado de Gestão Municipal

**Código:** DOM-GDO-023

**Domínio:** Gestão Documental

**Versão:** 2.0

**Status:** Concluído

**Classificação da Informação:** Pública

**Documento(s) Relacionado(s):**

- `000-Dominio-Gestao-Documental.md`
- `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md`
- `000A-Padrao-Corporativo-De-Documentacao-do-SIGMUN.md`
- `000H-MAPA-MESTRE-DE-ARTEFATOS-E-RASTREABILIDADE.md`
- `021-Checklist-De-Prontidao-De-Producao-Gestao-Documental.md`
- `024-Plano-De-Suporte-E-Operacao-Gestao-Documental.md`
- `025-Estrutura-Tecnica-Gestao-Documental.md`

---

# 1. Finalidade

O **Plano de Treinamento – Gestão Documental** define o roteiro de capacitação para operadores de protocolo e pessoal de arquivo, garantindo o uso correto do sistema SIGMUN na gestão documental do município, desde o recebimento até a destinação final dos documentos.

---

# 2. Perfis de Usuário

| Perfil | Responsabilidades | Acesso Necessário |
|--------|-------------------|-------------------|
| Operador de protocolo | Recebimento, classificação, lançamento de documentos | Criar, classificar, tramitar próprio |
| Arquivista | Arquivamento, guarda permanente, destinação | Criar, versão, arquivar, consultar |
| Gestor Documental | Aprovação de classificações, definição de temporalidades | Ler, aprovar, reportar |
| Autoridade homologadora | Homologação de eliminação, assinatura de documentos de alto risco | Assinar, homologar eliminar |
| Administrador | Configuração de usuários, permissões, sistema | Administrar |

---

# 3. Roteiro de Capacitação

## 3.1 Módulo 1: Introdução ao SIGMUN (2 horas)

- Visão geral do sistema e objetivos
- Arquitetura de gestão documental (Clean Architecture/DDD)
- Acesso ao sistema: credenciais, perfis de login
- Segurança da informação: política de senhas, uso de headers de autenticação

## 3.2 Módulo 2: Protocolo de Entrada de Documentos (3 horas)

- Fluxo de recebimento: protocolo → classificação → inserção no SIGMUN
- Seleção de tipo documental (12 categorias disponíveis)
- Aplicação de classificação documental (9 níveis de sigilo/tipo)
- Definição de temporalidade (prazos de guarda: 12M, 6M, 30D, indeterminada)
- Inspeção de hash SHA-256 de integridade
- Gravação de entrada no sistema

## 3.3 Módulo 3: Tramitação e Fluxo de Trabalho (3 horas)

- Processo de tramitação: envio, retorno, consulta de status
- Realização de assinatura digital de documentos
- Procedimento de arquivamento com definição de estado final
- Gestão de versões: criação, consulta de histórico
- Tratamento de exceções: códigos duplicados (409), payload inválido (422), hash inválido (400)

## 3.4 Módulo 4: Arquivamento e Destinação (2 horas)

- Aplicação de guarda permanente vs. temporária
- Execução de destinação conforme classificação e temporalidade
- Eliminação de documentos: requisitos de autoridade homologadora (RN-GDO-011)
- Confirmação de estado final: `arquivado` / `encerrado`
- Procedimento de certidão de eliminação

## 3.5 Módulo 5: Consultas e Relatórios (2 horas)

- Consulta de documentos por tipo, classificação, temporalidade
- Listagem de tramitações e histórico de versões
- Geração de relatórios de integridade (hash, unicidade de código)
- Acesso a logs de auditoria e trilha de mudanças

---

# 4. Metodologia

- **Carga horária total:** 12 horas (5 módulos)
- **Formato:** Presencial ou remoto (sessões de 2h cada)
- **Avaliação:** Questionário final com 80% de aprovação mínima
- **Material de apoio:** Manual operacional, atalhos de teclado, FAQ
- **Certificação:** Emissão de certificado de conclusão para participantes com aprovação ≥ 80%

---

# 5. Cronograma

| Módulo | Data | Público | Carga Horária |
|--------|------|---------|---------------|
| 1 | T+1 | Todos os usuários | 2h |
| 2 | T+2 | Operadores de protocolo | 3h |
| 3 | T+3 | Operadores de protocolo, arquivistas | 3h |
| 4 | T+4 | Arquivistas | 2h |
| 5 | T+5 | Todos os usuários | 2h |

---

# 6. Evidências e Registro

- Lista de presença por sessão
- Questionários de avaliação preenchidos
- Certificados de conclusão emitidos
- Feedback dos participantes (formulário P-GDO-009)

---

# 7. Pendências

| ID | Descrição | Impacto | Responsável |
|----|-----------|---------|-------------|
| P-GDO-009 | Treinamento executado com usuários finais | Médio | Prefeitura/Equipe |

---

# 8. Versionamento

| Versão | Data | Descrição |
|--------|------|-----------|
| 1.0 | 2026-08-20 | Esboço inicial padronizado |
| 2.0 | 2026-09-06 | Roteiro completo com módulos operacionais e valigação da homologação |

---

**Documento:** 023-Plano-de-Treinamento-Gestao-Documental.md

**Última atualização:** 2026-09-06

**Responsável:** Equipe SIGMUN

**Status da revisão:** Concluído