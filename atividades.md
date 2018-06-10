
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


Os atributos das **atividades** são:

| Campo JSON | Descrição |
|------------|---------------|
| assunto | Assunto a que a atividade diz respeito |
| autoresGP | Grupo Parlamentar autor da atividade |
| convidados | Lista de convidados representados pela estrutura **ConvidadosOut** |
| dataAgendamentoDebate | Data de agendamento do debate para essa atividade |
| dataEntrada | Data de entrada da atividade |
| descTipo | Descrição do tipo de atividade parlamentar na Estrutura **TipodeAtividade**
| eleitos | Lista de eleitos representados pela estrutura **EleitosOut** |
| IniciativasConjuntas | Lista de iniciativas representadas pela estrutura **Iniciativas_DiscussaoConjuntaOut** |
| legislatura | Legislatura |
| numero | Identificador do tipo de atividade parlamentar na estrutura **TipodeAtividade** |
| observações | Observações associadas à atividade |
| orgaoExterior | Órgão externo, associado à atividade |
| publicação | Lista de publicações representadas pela estrutura **PublicacoesOut** |
| publicacaoDebate | Lista de publicações representadas pela estrutura **PublicacoesOut** |
| sessão | Sessão Legislativa |
| Texto | Texto relativo ao tipo de atividade parlamentar na estrutura **TipodeAtividade** |
| textosAprovados | Diplomas originados pela atividade |
| tipo | Sigla de tipo de atividade parlamentar na estrutura **TipodeAtividade** |
| tipoAutor | Campo Tipo na estrutura **TipodeAutor** |
| votacaoDebate | Lista de votações representadas pela estrutura **Votacao** |

As estruturas auxiliares são descritas no final.

......


### Estruturas auxiliares

ConvidadosOut

| Campo JSON | Descrição |
|------------|---------------|
| assunto | Assunto a que a atividade diz respeito |
