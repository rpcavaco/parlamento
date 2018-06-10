
# Atividades

Começam-se por descrever aspetos centrais da estrutura, tal como está explicada na documentação da AR, para depois mostrar como essa estrutura se reflete na prática sobre o efetivo conteúdo dos ficheiros JSON disponíveis.

## Tipos documentados

Segundo o documento de estrutura das atividades, estas podem ser dos seguintes tipos:

- Apreciação de  relatórios entregues por entidades  externas
- Audiências
- Audições
- Cerimónias
- Conta  Geral  do  Estado
- Debates
- Declarações Políticas
- Defesa  Nacional
- Deslocações  no  âmbito  das  Comissões
- Deslocações  do  Presidente  da República
- Eleição e composição para órgãos externos
- Eventos no âmbito de Comissões
- Grandes Opções do Conceito Estratégico da  Defesa Nacional
- Interpelações ao Governo
- Moções
- Orçamento e Conta de Gerência  da  AR
- Orientação  da  Política Orçamental
- Perguntas ao Governo, Programa  de  Estabilidade e Crescimento
- Programa do Governo
- Relatórios de Segurança Interna
- Segurança Interna
- Votos

## Estrutura JSON

O elemento de topo é um dicionário que contém as seguintes chaves, que agrupam atividades:

- AtividadesGerais
- Audicoes
- Audiencias
- Deslocações

### Atividades Gerais

As atividades gerais (*AtividadesGerais*) podem conter atividades dos tipos descritos acima. Contudo os ficheiros correspondentes a cada legislatura conterão apenas alguns daqueles. No caso da XIIª Legislatura encontramos, até 9 de Junho de de 2018, apenas os surgem os seguintes tipos:

- Eleições e composições de órgãos
- Cerimónia
- Interpelação ao Governo
- Moção
- Programa do Governo
- Voto


**Nota**: os nomes dos campos a **negrito *** com um asterisco, representam campos aparentemente obrigatórios que se repetem em todos os registos.

Os atributos das **atividades** são:

| Campo JSON | Descrição |
|------------|---------------|
| **assunto *** | Assunto a que a atividade diz respeito |
| autoresGP | Grupo Parlamentar autor da atividade |
| convidados | Lista de convidados representados pela estrutura **ConvidadosOut** |
| dataAgendamentoDebate | Data de agendamento do debate para essa atividade |
| dataEntrada | Data de entrada da atividade |
| **descTipo *** | Descrição do tipo de atividade parlamentar na Estrutura **TipodeAtividade**
| eleitos | Lista de eleitos representados pela estrutura **EleitosOut** |
| IniciativasConjuntas | Lista de iniciativas representadas pela estrutura **Iniciativas_DiscussaoConjuntaOut** |
| **legislatura *** | Legislatura |
| **numero *** | Identificador do tipo de atividade parlamentar na estrutura **TipodeAtividade** |
| observações | Observações associadas à atividade |
| orgaoExterior | Órgão externo, associado à atividade |
| publicação | Lista de publicações representadas pela estrutura **PublicacoesOut** |
| publicacaoDebate | Lista de publicações representadas pela estrutura **PublicacoesOut** |
| **sessão *** | Sessão Legislativa |
| texto | Texto relativo ao tipo de atividade parlamentar na estrutura **TipodeAtividade** |
| textosAprovados | Diplomas originados pela atividade |
| **tipo *** | Sigla de tipo de atividade parlamentar na estrutura **TipodeAtividade** |
| **tipoAutor *** | Campo Tipo na estrutura **TipodeAutor** |
| votacaoDebate | Lista de votações representadas pela estrutura **Votacao** |


### Estruturas auxiliares

#### ConvidadosOut

| Campo JSON | Descrição |
|------------|---------------|
| assunto | Assunto a que a atividade diz respeito |
| cargo | Cargo que o convidado exerce aquando da vinda à AR |
| honra | Indicação se é convidado de honra ou não |
| nome | Nome do convidado |
| pais | País da nacionalidade do convidado |

#### TipodeAtividade

| Campo JSON | Descrição |
|------------|---------------|
| AGP | Atividade do grupo parlamentar de amizade |
| AUD | Audiência |
| AUP | Audição |
| CER | Cerimónias |
| CGE | Conta Geral do Estado |
| DEB | Debates diversos |
| DES | Deslocação |
| DPO | Declarações políticas |
| DPR | Deslocações do Presidente da República |
| EGP | Eleição do grupo parlamentar de amizade |
| EVN | Evento |
| GOD | Grandes Opções do Conceito Estratégico de Defesa Nacional |
| IMU | Imunidade parlamentar |
| INI | Discussão de Iniciativas |
| ITG | Interpelação ao governo |
| MOC | Moção |
| OEX | Eleições e composições de órgãos |
| PEC | Programa de Estabilidade e Crescimento/Documento de Estratégia Orçamental |
| PEG | Perguntas ao Governo |
| PET | Discussão de petições |
| PII | Parecer de incompatibilidade / Levantamento de imunidade |
| POR | Orientação da Política Orçamental |
| PRC | Relatórios externos |
| PRG | Programa do Governo |
| PUE | Participação de Portugal na União Europeia |
| REP | Representações e delegações |
| RSI | Relatório de segurança interna |
| SES | Cerimónia |
| VOT | Voto |

#### EleitosOut

| Campo JSON | Descrição |
|------------|---------------|
| Cargo | Cargo do membro eleito para o órgão ou entidade |
| Nome | Nome do membro eleito para o órgão ou entidade |

#### Iniciativas_DiscussaoConjuntaOut
| Campo JSON | Descrição |
|------------|---------------|
| Dataentrada | Data de Entrada da Iniciativa |
| DescTipo | Descrição da iniciativa na estrutura TipodeIniciativa |
| Id | Identificador da iniciativa na estrutura TipodeIniciativa  |
| Leg | Legislatura |
| Nr | Número da Iniciativa |
| Sel | Sessão Legislativa |
| Tipo | Abreviatura da iniciativa em estrutura TipodeIniciativa |
| Titulo | Assunto da Iniciativa |
