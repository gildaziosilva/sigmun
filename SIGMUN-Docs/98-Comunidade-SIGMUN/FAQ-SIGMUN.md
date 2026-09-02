# FAQ — SIGMUN

**Perguntas Frequentes sobre o SIGMUN**

---

# 1. Identificação do Documento

| Campo | Informação |
|---|---|
| **Título** | FAQ — SIGMUN |
| **Projeto** | SIGMUN — Sistema Integrado de Gestão da Prefeitura Municipal de Camacan-BA |
| **Classificação da Informação** | Pública |
| **Versão** | 1.0 |
| **Status** | Vigente |
| **Tipo** | Comunicação / Orientação |
| **Documento Mestre** | `000-CONSTITUICAO-DO-PROJETO-SIGMUN.md` |

---

# 2. Sobre o SIGMUN

## 2.1 O que é o SIGMUN?

O SIGMUN é um Sistema Integrado de Gestão Pública desenvolvido para apoiar a transformação digital dos municípios brasileiros.

Seu objetivo é integrar processos, dados, serviços e informações municipais, reduzindo retrabalho, duplicidade de informações e isolamento entre sistemas.

---

## 2.2 O que significa SIGMUN?

SIGMUN significa:

> **Sistema Integrado de Gestão da Prefeitura Municipal de Camacan-BA**

Em contextos mais amplos, o projeto também pode ser apresentado como uma plataforma de gestão pública integrada para municípios.

---

## 2.3 Qual é o objetivo principal do SIGMUN?

O objetivo principal é proporcionar uma base tecnológica integrada para apoiar:

- gestão pública;
- integração de processos;
- integração de dados;
- tomada de decisão;
- transparência;
- segurança;
- interoperabilidade;
- transformação digital.

---

## 2.4 O SIGMUN é apenas um sistema administrativo?

Não.

O SIGMUN possui visão de plataforma integrada de gestão pública, podendo abranger processos administrativos, operacionais, estratégicos e serviços de campo.

Sua arquitetura permite evolução por domínios de negócio.

---

## 2.5 O SIGMUN é um ERP?

O SIGMUN possui características de um ERP Público, especialmente pela integração de processos e informações entre diferentes áreas da administração municipal.

Entretanto, sua arquitetura é orientada especificamente às necessidades da gestão pública municipal.

---

# 3. Público e Municípios

## 3.1 Para quem o SIGMUN é desenvolvido?

O SIGMUN é destinado principalmente a:

- municípios;
- administrações públicas municipais;
- secretarias;
- órgãos municipais;
- gestores;
- servidores;
- equipes técnicas;
- cidadãos, por meio dos serviços e informações disponibilizados.

---

## 3.2 O SIGMUN será utilizado somente em Camacan?

Não necessariamente.

O projeto possui origem e aplicação inicial relacionada à Prefeitura Municipal de Camacan-BA, mas sua arquitetura busca possibilitar evolução para outros municípios.

---

## 3.3 Outros municípios poderão utilizar o SIGMUN?

Sim, conforme os modelos de implantação, governança, sustentabilidade e licenciamento definidos pelo projeto.

A expansão deverá ocorrer de maneira controlada e estruturada.

---

## 3.4 O que é um Município Piloto?

É um município participante de uma etapa controlada de validação do SIGMUN.

O piloto permite avaliar:

- processos;
- funcionalidades;
- integração;
- usabilidade;
- desempenho;
- segurança;
- aderência às necessidades municipais.

---

## 3.5 Como um município pode participar do programa piloto?

A participação deverá seguir o processo definido no:

`PROGRAMA-DE-MUNICIPIOS-PILOTO.md`

A seleção deverá considerar critérios técnicos, institucionais e operacionais.

---

## 3.6 O que é um Município Mantenedor?

É um município que participa da sustentabilidade e evolução do ecossistema SIGMUN conforme modelo institucional específico.

O conceito é diferente de município piloto.

---

# 4. Arquitetura

## 4.1 Como o SIGMUN é organizado?

O SIGMUN é organizado por domínios de negócio, componentes e serviços.

A arquitetura busca reduzir acoplamento e manter as regras de negócio dentro dos respectivos domínios.

---

## 4.2 O que é um domínio SIGMUN?

Um domínio representa uma área de negócio ou capacidade da administração pública.

Exemplos:

- Gestão de Compras e Contratações;
- Gestão de Pessoas;
- Gestão Financeira;
- Gestão Tributária;
- Gestão Documental;
- outros domínios definidos na arquitetura.

---

## 4.3 Por que utilizar arquitetura orientada a domínios?

Para:

- separar responsabilidades;
- reduzir acoplamento;
- facilitar manutenção;
- facilitar testes;
- permitir evolução independente;
- melhorar rastreabilidade;
- evitar duplicação de regras.

---

## 4.4 Os domínios podem acessar diretamente o banco de dados uns dos outros?

Como regra arquitetural, não.

Cada domínio deve respeitar os limites de responsabilidade definidos pela arquitetura.

Quando um domínio precisar de informações de outro, deverá utilizar mecanismos de integração apropriados.

---

## 4.5 O SIGMUN utiliza APIs?

Sim.

APIs podem ser utilizadas para integração entre componentes, domínios e sistemas externos.

Os contratos devem ser documentados e versionados quando aplicável.

---

## 4.6 O SIGMUN utiliza eventos e mensageria?

A arquitetura pode utilizar mensageria e eventos para comunicação assíncrona entre componentes e domínios quando isso for adequado ao caso de uso.

---

# 5. Dados

## 5.1 O SIGMUN possui uma estratégia de governança de dados?

Sim.

A governança de dados faz parte da arquitetura corporativa do projeto.

O objetivo é garantir:

- qualidade;
- consistência;
- rastreabilidade;
- segurança;
- disponibilidade;
- interoperabilidade.

---

## 5.2 O SIGMUN possui uma fonte única de informação?

A arquitetura busca evitar duplicação desnecessária de informações e estabelecer fontes oficiais para cada tipo de dado.

A definição da fonte de verdade depende do domínio e da entidade envolvida.

---

## 5.3 Os dados podem ser compartilhados entre domínios?

Sim, quando houver necessidade legítima e de acordo com os contratos de integração, regras de segurança e governança de dados.

---

# 6. Segurança e LGPD

## 6.1 O SIGMUN considera segurança desde a arquitetura?

Sim.

Segurança é um princípio arquitetural do SIGMUN.

A abordagem é:

> **Segurança por princípio.**

---

## 6.2 O SIGMUN precisa cumprir a LGPD?

Sim.

Quando houver tratamento de dados pessoais, o projeto deverá observar a legislação aplicável, incluindo a Lei Geral de Proteção de Dados Pessoais — LGPD.

---

## 6.3 O SIGMUN trabalha somente com dados públicos?

Não.

Um sistema de gestão municipal pode trabalhar com diferentes categorias de informação.

Por isso, o SIGMUN adota o princípio:

> **Classificação da Informação por política.**

---

## 6.4 Como funciona a classificação da informação?

As informações devem ser classificadas conforme as políticas de governança e segurança do SIGMUN.

A classificação determina, entre outros aspectos:

- possibilidade de publicação;
- acesso;
- compartilhamento;
- armazenamento;
- retenção;
- descarte.

---

## 6.5 O SIGMUN publica todos os seus códigos e documentos?

Não necessariamente.

O princípio adotado é:

> **Aberto sempre que possível, restrito sempre que necessário.**

Informações públicas e artefatos adequados podem ser publicados.

Informações que possam comprometer segurança, privacidade ou obrigações legais devem receber tratamento apropriado.

---

# 7. Transparência

## 7.1 O SIGMUN foi projetado para promover transparência?

Sim.

A transparência é um dos princípios do projeto:

> **Transparência por padrão.**

---

## 7.2 Transparência significa publicar todas as informações?

Não.

Transparência deve respeitar:

- segurança;
- privacidade;
- LGPD;
- classificação da informação;
- legislação;
- interesse público.

---

# 8. Comunidade

## 8.1 O SIGMUN possui uma comunidade?

Sim.

O projeto possui uma visão de comunidade aberta e colaborativa formada por:

- desenvolvedores;
- colaboradores;
- gestores;
- pesquisadores;
- especialistas;
- municípios;
- instituições;
- parceiros;
- interessados.

---

## 8.2 Como posso contribuir?

As contribuições podem ocorrer por meio de:

- código;
- documentação;
- testes;
- correções;
- sugestões;
- análise;
- pesquisa;
- arquitetura;
- UX/UI;
- segurança;
- integração;
- conhecimento de domínio.

---

## 8.3 Preciso ser desenvolvedor para contribuir?

Não.

Contribuições de conhecimento de negócio, documentação, testes, análise de processos, UX, segurança, governança e outras áreas também são importantes.

---

## 8.4 Como registrar uma sugestão ou problema?

Utilize o template oficial de Issue:

`feature_or_bug.md`

A Issue deve conter informações suficientes para permitir análise e rastreabilidade.

---

## 8.5 Como enviar uma alteração de código?

As alterações devem seguir o fluxo definido no:

`000E-GUIA-DE-CONTRIBUICAO.md`

Quando aplicável, a alteração deverá ser submetida por Pull Request.

---

## 8.6 O que é um Pull Request?

É uma solicitação para que uma alteração seja revisada e eventualmente incorporada ao projeto.

O PR deve apresentar:

- descrição;
- rastreabilidade;
- impacto;
- testes;
- documentação;
- riscos;
- evidências.

---

## 8.7 Existe um Código de Conduta?

Sim.

A participação na comunidade deve respeitar o:

`CODIGO-DE-CONDUTA.md`

---

## 8.8 Existe um Guia do Colaborador?

Sim.

O:

`GUIA-DO-COLABORADOR.md`

orienta colaboradores sobre participação, responsabilidades, comunicação e boas práticas.

---

## 8.9 Existe um Guia de Contribuição?

Sim.

O:

`000E-GUIA-DE-CONTRIBUICAO.md`

define o processo para contribuição ao projeto.

---

# 9. SIGMUN-DEV-AGENT

## 9.1 O que é o SIGMUN-DEV-AGENT?

É um agente de apoio ao desenvolvimento do SIGMUN, destinado a auxiliar atividades técnicas dentro das regras e padrões definidos pelo projeto.

---

## 9.2 O SIGMUN-DEV-AGENT substitui os colaboradores?

Não.

O agente é uma ferramenta de apoio.

A responsabilidade pela análise, decisão, revisão e aprovação das alterações permanece com as pessoas responsáveis pelo projeto.

---

## 9.3 O agente pode criar código?

Quando autorizado e dentro do processo definido pelo projeto, o agente pode auxiliar na criação ou alteração de código.

As alterações devem passar pelos mecanismos normais de revisão e validação.

---

## 9.4 O agente pode tomar decisões arquiteturais sozinho?

Não.

Decisões arquiteturais relevantes devem seguir o processo de governança e, quando aplicável, ser registradas em ADR.

---

# 10. Documentação

## 10.1 Onde está a documentação do SIGMUN?

A documentação está organizada no diretório:

```text
SIGMUN-Docs/