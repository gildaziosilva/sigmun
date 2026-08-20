# 009 – Arquitetura de Dados

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

Este documento define a arquitetura de dados do SIGMUN, estabelecendo os princípios, padrões, modelos e estratégias para armazenamento, organização, integração, proteção e governança das informações municipais.

A arquitetura de dados tem como objetivo garantir que os dados tratados pela Prefeitura Municipal de Camacan sejam:

* confiáveis;
* íntegros;
* seguros;
* rastreáveis;
* disponíveis;
* reutilizáveis;
* compatíveis com requisitos legais.

---

# 2. Visão Geral

O SIGMUN será baseado em uma arquitetura corporativa de dados, onde os dados serão tratados como um ativo estratégico da administração municipal.

A arquitetura seguirá os princípios:

* dado único;
* responsabilidade definida;
* qualidade permanente;
* segurança por padrão;
* histórico completo;
* integração controlada.

---

# 3. Princípios de Dados

## 3.1 Dados como Patrimônio Institucional

As informações geradas e armazenadas pelo SIGMUN pertencem institucionalmente à Prefeitura Municipal de Camacan.

Os dados não deverão ficar vinculados a fornecedores, sistemas específicos ou pessoas.

---

## 3.2 Fonte Única da Verdade

Cada informação corporativa deverá possuir um domínio responsável.

Exemplo:

| Informação | Domínio Mestre       |
| ---------- | -------------------- |
| Pessoa     | Cadastro Único       |
| Servidor   | RH                   |
| Tributo    | Tributação           |
| Empenho    | Contabilidade        |
| Contrato   | Contratos            |
| Imóvel     | Cadastro Territorial |

---

## 3.3 Não Duplicação

O sistema deverá evitar múltiplas versões independentes da mesma informação.

Exemplo:

Um cidadão possuirá um único cadastro de pessoa.

Os módulos apenas complementarão informações específicas.

---

## 3.4 Histórico Permanente

Informações relevantes deverão possuir histórico.

Exemplo:

Alteração de endereço:

Antes:

```
Rua A, nº 100
```

Depois:

```
Rua B, nº 250
```

O sistema deverá manter ambas as informações com período de validade.

---

# 4. Modelo Corporativo de Dados

O SIGMUN será estruturado em quatro categorias principais.

---

# 4.1 Dados Mestres (Master Data)

São entidades compartilhadas por toda a organização.

Exemplos:

* Pessoa;
* Pessoa Jurídica;
* Endereço;
* Unidade Administrativa;
* Servidor;
* Fornecedor;
* Imóvel;
* Documento.

Responsabilidade:

Cadastro Único Municipal.

---

# 4.2 Dados Transacionais

Representam operações realizadas.

Exemplos:

* pagamento;
* atendimento;
* protocolo;
* lançamento tributário;
* empenho;
* compra;
* contrato.

---

# 4.3 Dados Documentais

Representam arquivos e documentos.

Exemplos:

* processos;
* contratos;
* pareceres;
* notas fiscais;
* relatórios.

---

# 4.4 Dados Analíticos

Dados preparados para:

* indicadores;
* BI;
* dashboards;
* planejamento.

---

# 5. Arquitetura de Banco de Dados

## Banco Principal

Tecnologia:

PostgreSQL.

Motivos:

* estabilidade;
* código aberto;
* segurança;
* recursos avançados;
* suporte geoespacial;
* grande comunidade.

---

# 6. Organização dos Dados

O banco será organizado por domínios.

Estrutura conceitual:

```
sigmun
│
├── core
│   ├── pessoas
│   ├── usuarios
│   ├── documentos
│   └── auditoria
│
├── rh
│
├── tributacao
│
├── contabilidade
│
├── compras
│
├── saude
│
├── educacao
│
└── assistencia
```

Cada domínio terá responsabilidade sobre suas próprias estruturas.

---

# 7. Convenções de Banco de Dados

## Nomenclatura

Padrão:

* tabelas no plural;
* nomes em português;
* snake_case.

Exemplo:

```
pessoas
pessoas_documentos
enderecos
servidores
contratos
```

---

# 8. Identificadores

Todas as entidades deverão possuir:

## Identificador interno

UUID gerado pelo SIGMUN.

Exemplo:

```
id:
550e8400-e29b-41d4-a716-446655440000
```

---

## Identificadores externos

Quando existentes:

* CPF;
* CNPJ;
* CNS;
* NIS;
* matrícula;
* código IBGE;
* código INEP;
* código CNES.

---

# 9. Auditoria de Dados

Todas as tabelas críticas deverão possuir informações de auditoria.

Campos padrão:

```
created_at
created_by

updated_at
updated_by

deleted_at
deleted_by
```

Quando necessário:

```
versao
vigencia_inicio
vigencia_fim
motivo_alteracao
```

---

# 10. Controle de Exclusão

Não será permitida exclusão física de dados críticos.

Será utilizado:

## Soft Delete

Exemplo:

```
deleted_at = 2026-07-30
```

Permitindo:

* auditoria;
* recuperação;
* histórico.

---

# 11. Dados Sensíveis

O SIGMUN tratará informações protegidas pela LGPD.

Exemplos:

* saúde;
* dados familiares;
* documentos pessoais;
* informações funcionais;
* dados socioassistenciais.

Esses dados deverão possuir:

* controle de acesso adicional;
* criptografia;
* registro de consultas;
* mascaramento quando necessário.

---

# 12. Qualidade dos Dados

A plataforma deverá possuir mecanismos para:

* validação cadastral;
* identificação de duplicidades;
* dados incompletos;
* inconsistências;
* conflitos entre sistemas.

Indicadores:

* completude;
* unicidade;
* atualização;
* consistência.

---

# 13. Migração de Dados Legados

O SIGMUN deverá migrar informações provenientes de:

## Sistemas existentes

* Firebird – Contabilidade;
* Firebird – Recursos Humanos;
* SQL Server – Tributação;
* demais bases existentes.

---

# Estratégia de Migração

Etapas:

1. Inventário dos dados existentes.
2. Análise de qualidade.
3. Mapeamento origem-destino.
4. Tratamento e limpeza.
5. Migração piloto.
6. Validação.
7. Migração definitiva.

---

# 14. Integração de Dados

A integração deverá ocorrer por:

* APIs;
* serviços;
* eventos;
* arquivos estruturados;
* SFTP;
* Web Services.

Não deverá ocorrer integração direta entre bancos sem controle.

---

# 15. Data Warehouse e BI

O SIGMUN deverá estar preparado para uma camada analítica.

Arquitetura futura:

```
Sistemas Operacionais
          |
          |
      ETL/ELT
          |
          |
 Data Warehouse
          |
          |
 Dashboards / BI
```

Objetivos:

* indicadores;
* planejamento;
* acompanhamento de metas;
* inteligência administrativa.

---

# 16. Dados Geográficos

O SIGMUN deverá considerar dados espaciais.

Possíveis aplicações:

* imóveis;
* obras;
* iluminação;
* equipamentos públicos;
* áreas rurais;
* mapas municipais.

Tecnologia prevista:

* PostgreSQL + PostGIS.

---

# 17. Backup e Recuperação

A estratégia deverá contemplar:

* backups automáticos;
* testes periódicos de restauração;
* cópias externas;
* retenção conforme requisitos legais.

---

# 18. Segurança dos Dados

Medidas previstas:

* criptografia;
* controle de acesso;
* segregação de ambientes;
* monitoramento;
* auditoria;
* gestão de privilégios.

---

# 19. Governança de Dados

A governança deverá definir:

* responsáveis pelos dados;
* regras de qualidade;
* políticas de acesso;
* ciclo de vida;
* classificação da informação.

---

# 20. Princípios para Evolução Futura

A arquitetura deverá permitir:

* crescimento do volume de dados;
* novos módulos;
* inteligência artificial;
* análise preditiva;
* automação;
* integração com novos órgãos.

---

# 21. Conclusão

A Arquitetura de Dados do SIGMUN estabelece a base para uma administração municipal orientada por informações confiáveis.

Ao transformar dados dispersos em um patrimônio corporativo organizado, seguro e governado, o SIGMUN permitirá maior eficiência administrativa, transparência e capacidade de planejamento estratégico.

A qualidade desta arquitetura será determinante para o sucesso de todos os módulos futuros da plataforma.

---

**Documento:**005-Arquitetura-de-Dados.md
**Última atualização:** 2026-08-03
**Responsável:** Equipe SIGMUN
**Status da revisão:** Vigente
