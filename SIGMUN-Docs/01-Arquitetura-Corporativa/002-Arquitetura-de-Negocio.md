# 003 – Arquitetura de Negócio

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

Este documento define a Arquitetura de Negócio do SIGMUN, estabelecendo a organização dos domínios de negócio, os serviços corporativos compartilhados, as responsabilidades funcionais de cada módulo e os princípios que orientarão a construção de toda a plataforma.

A Arquitetura de Negócio é independente de tecnologia e servirá como referência para a arquitetura de software, o modelo de dados, as APIs e as integrações.

---

# 2. Princípios da Arquitetura de Negócio

O SIGMUN será construído com base nos seguintes princípios:

* informação única;
* cadastro corporativo compartilhado;
* integração entre secretarias;
* eliminação de redundâncias;
* processos digitais;
* interoperabilidade;
* rastreabilidade completa;
* segurança da informação;
* conformidade legal;
* reutilização de serviços.

Nenhum módulo poderá manter cópias permanentes de informações pertencentes a outro domínio quando houver um serviço corporativo responsável por esses dados.

---

# 3. Estrutura Geral

A plataforma será organizada em quatro grandes camadas de negócio:

## Camada Corporativa

Responsável pelos serviços compartilhados por toda a Prefeitura.

Inclui:

* Cadastro Único Municipal
* Gestão de Usuários
* Autenticação
* Perfis de acesso
* Gestão Documental
* Protocolo Eletrônico
* Assinaturas
* Auditoria
* Notificações
* Configurações Gerais
* Barramento de Integração
* APIs Corporativas

---

## Camada Administrativa

Responsável pela gestão administrativa da Prefeitura.

Inclui:

* Recursos Humanos
* Folha de Pagamento
* Patrimônio
* Almoxarifado
* Compras
* Licitações
* Contratos
* Convênios
* Frota
* Diárias
* Viagens
* Controle Interno
* Procuradoria

---

## Camada Financeira

Responsável pela gestão financeira e orçamentária.

Inclui:

* Contabilidade
* Planejamento
* Orçamento
* Execução Orçamentária
* Tesouraria
* Receita
* Tributos
* Dívida Ativa
* Arrecadação

---

## Camada Finalística

Responsável pelas políticas públicas.

Inclui:

* Saúde
* Educação
* Assistência Social
* Obras
* Meio Ambiente
* Agricultura
* Cultura
* Turismo
* Esporte
* Desenvolvimento Econômico
* Defesa Civil
* Gestão de Cemitérios

---

# 4. Núcleo Corporativo

O Núcleo Corporativo representa o coração do SIGMUN.

Todos os demais módulos obrigatoriamente utilizarão seus serviços.

O núcleo será composto por:

* Cadastro Único Municipal
* Gestão Organizacional
* Gestão de Pessoas
* Gestão de Empresas
* Gestão Territorial
* Gestão Documental
* Gestão de Processos
* Segurança
* Auditoria
* APIs
* Integrações
* Configurações

Nenhum módulo poderá criar sua própria implementação desses serviços.

---

# 5. Cadastro Único Municipal

O Cadastro Único Municipal será a principal base de dados do SIGMUN.

Toda entidade deverá existir apenas uma vez.

As principais entidades corporativas incluem:

## Pessoas

* cidadão
* servidor
* contribuinte
* paciente
* aluno
* fornecedor (pessoa física)
* representante legal
* responsável familiar

---

## Pessoas Jurídicas

* fornecedores
* empresas
* entidades
* associações
* órgãos públicos
* organizações conveniadas

---

## Endereços

Cadastro padronizado conforme:

* CEP
* logradouro
* bairro
* distrito
* município
* estado
* país
* coordenadas geográficas

---

## Organização Administrativa

* Prefeitura
* Secretarias
* Departamentos
* Divisões
* Setores
* Unidades
* Centros de custo

---

## Patrimônio Territorial

* imóveis
* terrenos
* edificações
* lotes
* cemitérios
* equipamentos públicos

---

## Recursos Materiais

* bens patrimoniais
* materiais
* estoque
* veículos
* máquinas
* equipamentos

---

# 6. Domínios de Negócio

Cada domínio possuirá autonomia sobre seus dados específicos.

## Recursos Humanos

Responsável por:

* servidores
* cargos
* funções
* lotações
* férias
* folha
* frequência
* avaliações

---

## Tributação

Responsável por:

* IPTU
* ISS
* ITBI
* taxas
* dívida ativa
* arrecadação
* fiscalização

---

## Contabilidade

Responsável por:

* PCASP
* empenhos
* liquidações
* pagamentos
* receitas
* despesas
* orçamento
* balanços

---

## Compras

Responsável por:

* solicitações
* pesquisas de preço
* licitações
* dispensas
* atas
* fornecedores

---

## Patrimônio

Responsável por:

* inventário
* depreciação
* transferências
* baixas
* incorporações

---

## Saúde

Responsável por:

* pacientes
* atendimentos
* equipes
* unidades
* vacinação
* prontuários (conforme legislação aplicável)

---

## Educação

Responsável por:

* escolas
* matrículas
* turmas
* calendário
* transporte escolar
* alimentação escolar

---

## Assistência Social

Responsável por:

* famílias
* benefícios
* programas
* atendimentos
* acompanhamento social

---

# 7. Serviços Compartilhados

Serviços reutilizados por todos os módulos:

* autenticação
* autorização
* notificações
* auditoria
* armazenamento de documentos
* protocolo
* assinatura eletrônica
* workflow
* filas
* anexos
* CEP
* geolocalização
* emissão de documentos
* geração de PDF
* QR Code
* envio de e-mail
* envio de SMS
* integração WhatsApp
* relatórios
* BI

---

# 8. Comunicação entre Domínios

Os módulos não acessarão diretamente os dados internos uns dos outros.

A comunicação ocorrerá por:

* APIs internas;
* eventos de domínio;
* serviços corporativos;
* barramento de integração.

Isso reduz acoplamento e facilita evolução tecnológica.

---

# 9. Governança dos Dados

Cada informação possuirá um único domínio responsável.

Exemplos:

| Informação | Domínio Responsável  |
| ---------- | -------------------- |
| Pessoa     | Cadastro Único       |
| Empresa    | Cadastro Único       |
| Endereço   | Cadastro Único       |
| Servidor   | Recursos Humanos     |
| Imóvel     | Cadastro Territorial |
| Veículo    | Frota                |
| Contrato   | Contratos            |
| Processo   | Protocolo            |
| Documento  | Gestão Documental    |
| Empenho    | Contabilidade        |
| Tributo    | Tributação           |

Outros módulos poderão consultar essas informações, mas não alterar os dados de responsabilidade de outro domínio sem mecanismos próprios de integração e autorização.

---

# 10. Fluxo Corporativo

Toda operação seguirá, sempre que aplicável, um fluxo padronizado:

1. Identificação do usuário.
2. Verificação de permissões.
3. Validação das regras de negócio.
4. Registro da operação.
5. Persistência dos dados.
6. Geração de auditoria.
7. Publicação de eventos.
8. Atualização dos módulos dependentes.
9. Notificação dos interessados.
10. Disponibilização para relatórios e transparência, quando permitido.

---

# 11. Princípios de Evolução

A arquitetura deverá permitir:

* inclusão de novos módulos;
* criação de novos serviços;
* integração com novos sistemas;
* substituição gradual de componentes;
* escalabilidade horizontal;
* implantação incremental;
* evolução sem interrupção dos serviços.

Nenhuma evolução deverá comprometer os módulos existentes.

---

# 12. Diretrizes para os Próximos Documentos

Os documentos subsequentes deverão respeitar integralmente esta Arquitetura de Negócio.

Em especial:

* o Modelo Corporativo de Dados deverá refletir os domínios definidos neste documento;
* a Arquitetura de Software deverá preservar os limites entre os domínios;
* as APIs deverão expor serviços compatíveis com as responsabilidades aqui estabelecidas;
* os módulos funcionais deverão utilizar exclusivamente os serviços corporativos compartilhados quando aplicável.

Este documento constitui a referência de alto nível para todas as decisões de modelagem, desenvolvimento, integração e governança do SIGMUN.

---

**Documento:**002-Arquitetura-de-Negocio.md
**Última atualização:** 2026-08-03
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
