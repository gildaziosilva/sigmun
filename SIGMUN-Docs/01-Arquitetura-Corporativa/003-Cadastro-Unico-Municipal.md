# 006 – Cadastro Único Municipal

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

Este documento define a arquitetura conceitual, as regras de negócio e os princípios de governança do **Cadastro Único Municipal (CUM)** do SIGMUN.

O Cadastro Único Municipal será o componente corporativo responsável pela criação, manutenção, identificação e compartilhamento das principais entidades utilizadas por todos os órgãos e secretarias da Prefeitura Municipal de Camacan.

Seu objetivo principal é garantir que uma mesma informação exista uma única vez no ambiente municipal, evitando duplicidades, inconsistências e divergências entre sistemas.

---

# 2. Visão Geral

O Cadastro Único Municipal funcionará como a base de referência corporativa do SIGMUN.

Todos os módulos deverão consumir os dados mestres do CUM, incluindo:

* Recursos Humanos;
* Tributação;
* Contabilidade;
* Saúde;
* Educação;
* Assistência Social;
* Compras;
* Licitações;
* Patrimônio;
* Almoxarifado;
* Frota;
* Portal da Transparência;
* Controle Interno;
* Procuradoria.

O CUM será responsável apenas pelos dados corporativos comuns.

Cada domínio manterá suas informações específicas.

Exemplo:

Um cidadão possui um único cadastro de pessoa no CUM.

O módulo Saúde adicionará informações específicas de atendimento.

O módulo Tributação adicionará informações fiscais.

O módulo Educação adicionará informações escolares.

Nenhum módulo deverá criar um novo cadastro independente da mesma pessoa.

---

# 3. Princípios do Cadastro Único

## 3.1 Identidade Única

Cada entidade deverá possuir um identificador único dentro do SIGMUN.

Exemplos:

* Pessoa → ID SIGMUN
* Empresa → ID SIGMUN
* Imóvel → ID SIGMUN
* Unidade Administrativa → ID SIGMUN

---

## 3.2 Fonte Oficial dos Dados

O CUM será a fonte oficial das informações corporativas.

Alterações deverão ocorrer no domínio responsável.

---

## 3.3 Histórico e Rastreabilidade

Nenhuma alteração relevante deverá apagar informações anteriores.

O sistema deverá manter:

* usuário responsável;
* data e hora;
* valor anterior;
* valor atualizado;
* origem da alteração;
* justificativa quando aplicável.

---

## 3.4 Qualidade dos Dados

O cadastro deverá possuir mecanismos para:

* validação;
* padronização;
* deduplicação;
* correção;
* enriquecimento;
* auditoria.

---

# 4. Domínios do Cadastro Único Municipal

O CUM será organizado nos seguintes domínios principais:

---

# 4.1 Cadastro de Pessoas

Representa pessoas físicas relacionadas ao município.

Abrange:

* cidadãos;
* servidores;
* contribuintes;
* pacientes;
* alunos;
* responsáveis familiares;
* fornecedores pessoa física;
* representantes legais.

---

## Dados Principais

Identificação:

* nome completo;
* nome social;
* CPF;
* RG;
* órgão emissor;
* data de nascimento;
* sexo;
* nacionalidade;
* naturalidade;
* estado civil.

Documentação:

* CPF;
* RG;
* CNH;
* CTPS;
* PIS/PASEP/NIS;
* CNS;
* título eleitoral.

Contato:

* telefone;
* e-mail;
* endereço;
* meios de comunicação autorizados.

---

# 4.2 Cadastro de Pessoas Jurídicas

Representa empresas e organizações.

Inclui:

* fornecedores;
* prestadores de serviço;
* empresas contribuintes;
* associações;
* entidades conveniadas.

---

## Dados Principais

* CNPJ;
* razão social;
* nome fantasia;
* natureza jurídica;
* inscrição estadual;
* inscrição municipal;
* CNAE;
* representantes legais.

---

## Compatibilidade com CNPJ Alfanumérico

O modelo deverá estar preparado para o novo padrão de CNPJ alfanumérico.

O campo identificador deverá aceitar:

* caracteres numéricos;
* caracteres alfanuméricos;
* validações futuras conforme Receita Federal.

---

# 4.3 Cadastro de Endereços

Responsável pela padronização dos endereços municipais.

---

## Dados Principais

* CEP;
* logradouro;
* número;
* complemento;
* bairro;
* distrito;
* município;
* UF;
* país;
* coordenadas geográficas.

---

## Integrações

Preparado para integração com:

* Correios;
* serviços de CEP;
* geolocalização.

---

# 4.4 Cadastro Territorial

Responsável pelos elementos físicos do território municipal.

Inclui:

* imóveis;
* terrenos;
* lotes;
* edificações;
* logradouros;
* bairros;
* distritos.

Relacionamentos:

Pessoa → Imóvel
Empresa → Imóvel
Imóvel → Tributos
Imóvel → Obras
Imóvel → Licenciamento

---

# 4.5 Cadastro Organizacional

Representa a estrutura administrativa municipal.

Inclui:

* Prefeitura;
* secretarias;
* órgãos;
* departamentos;
* setores;
* unidades administrativas;
* fundos municipais.

---

## Dados Principais

* código;
* nome;
* responsável;
* hierarquia;
* endereço;
* contatos;
* centro de custo.

---

# 4.6 Cadastro de Servidores

Responsável pelo vínculo institucional dos servidores.

Integração principal:

* Recursos Humanos.

Dados:

* matrícula;
* cargo;
* função;
* lotação;
* vínculo;
* situação funcional.

---

# 4.7 Cadastro de Fornecedores

Integração com:

* Compras;
* Licitações;
* Contratos;
* Contabilidade.

Dados:

* cadastro empresarial;
* documentos fiscais;
* dados bancários;
* certidões;
* contratos relacionados.

---

# 5. Identificadores Corporativos

Todas as entidades possuirão:

## Identificador Interno

Gerado pelo SIGMUN.

Exemplo:

```
Pessoa:
UUID: 550e8400-e29b-41d4-a716-446655440000
```

---

## Identificadores Externos

Quando aplicável:

* CPF;
* CNPJ;
* CNS;
* NIS;
* matrícula;
* código INEP;
* código CNES;
* código IBGE.

---

# 6. Regras de Deduplicação

Antes da criação de qualquer cadastro, o sistema deverá verificar existência prévia.

Critérios:

Pessoa Física:

* CPF;
* nome;
* data nascimento;
* nome da mãe.

Pessoa Jurídica:

* CNPJ;
* razão social.

Endereço:

* CEP;
* logradouro;
* número;
* complemento.

---

# 7. Governança do Cadastro

Cada entidade possuirá:

## Proprietário do Dado

Responsável institucional pela qualidade.

Exemplo:

| Dado     | Responsável                     |
| -------- | ------------------------------- |
| Pessoa   | Administração/Cadastro Geral    |
| Servidor | RH                              |
| Empresa  | Tributação/Compras              |
| Imóvel   | Tributação/Cadastro Territorial |
| Contrato | Compras/Contratos               |

---

# 8. Integrações Previstas

O CUM deverá permitir integração com:

* Receita Federal;
* Gov.br;
* Correios;
* CADSUS;
* eSocial;
* INEP;
* sistemas estaduais;
* sistemas internos.

---

# 9. Segurança e Privacidade

O tratamento dos dados deverá observar:

* LGPD;
* princípio da necessidade;
* controle de acesso;
* classificação da informação;
* criptografia;
* auditoria.

Dados sensíveis deverão possuir controles adicionais.

---

# 10. Requisitos Funcionais

RF-CUM-001
Permitir cadastro único de pessoas.

RF-CUM-002
Permitir cadastro único de empresas.

RF-CUM-003
Permitir consulta corporativa pelos módulos autorizados.

RF-CUM-004
Registrar histórico de alterações.

RF-CUM-005
Detectar possíveis duplicidades.

RF-CUM-006
Permitir integração com fontes externas.

RF-CUM-007
Controlar permissões de alteração.

RF-CUM-008
Disponibilizar APIs corporativas.

---

# 11. Requisitos Não Funcionais

RNF-CUM-001
Alta disponibilidade.

RNF-CUM-002
Auditoria completa.

RNF-CUM-003
Escalabilidade para milhares de usuários.

RNF-CUM-004
Conformidade LGPD.

RNF-CUM-005
Tempo de resposta adequado para consultas corporativas.

---

# 12. Evolução Futura

O Cadastro Único Municipal deverá evoluir para uma plataforma completa de:

* Master Data Management;
* qualidade de dados;
* inteligência analítica;
* integração automática;
* enriquecimento cadastral;
* identificação de inconsistências;
* apoio à decisão.

---

# 13. Conclusão

O Cadastro Único Municipal constitui a fundação informacional do SIGMUN.

Sua correta implementação será determinante para o sucesso da integração entre secretarias, redução de inconsistências, melhoria da eficiência administrativa e construção de uma gestão municipal orientada por dados.

---

**Documento:**003-Cadastro-Unico-Municipal.md
**Última atualização:** 2026-08-03
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
