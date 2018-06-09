
# Descrição da estrutura de dados abertos da Assembleia da República

Descrição genérica de alguns dos conjuntos de dados disponíveis. 

Os ficheiros disponibilizados têm uma estrutura confusa e repleta de redundâncias que carecem de ser resolvidas
antes de ser possível extrair alguma utilidade dos mesmos.

Assim, esta descrição lista as entidades disponíveis usando designações genéricas não necessáriamente iguais às 
usadas nos ficheiros propriamente ditos.

É usada como referência a informação relativa à 13ª legislatura (mais recente).

## Atividades dos deputados

A descrição da estrutura providenciada pela AR está neste [link](http://app.parlamento.pt/webutils/docs/doc.pdf?path=6148523063446f764c324679626d56304c3239775a57356b595852684c3052685a47397a51574a6c636e52766379394264476c32615752685a47567a4c31684a53556b6c4d6a424d5a57647063327868644856795953394264476c32615752685a47567a4c6e426b5a673d3d&fich=Atividades.pdf&Inline=true).

Ficheiro JSON existente [aqui](http://app.parlamento.pt/webutils/docs/doc.txt?path=6148523063446f764c324679626d56304c3239775a57356b595852684c3052685a47397a51574a6c636e52766379394264476c32615752685a47567a4c31684a53556b6c4d6a424d5a57647063327868644856795953394264476c32615752685a47567a57456c4a53563971633239754c6e523464413d3d&fich=AtividadesXIII_json.txt&Inline=true).

O elemento de topo é um dicionário de chave única ***AtividadeDeputado***

Dentro deste elemento existe uma **lista por deputado**, contendo:

- o conjunto das atividades do deputado na legislatura em causa
- dados sobre o deputado

### Tipos de atividades

Segundo o documento de estrutura das acitivdades, estas podem ser dos seguintes tipos:

- Apreciação de  relatórios entregues por entidades  externas,  
- Audiências,  Audições,  Cerimónias,  
- Conta  Geral  do  Estado
- Debates
- Declarações 
- Políticas
- Defesa  Nacional
- Deslocações  no  âmbito  das  Comissões
- Deslocações  do  Presidente  da República
- Eleição e composição para órgãos externos
- Eventos no âmbito de Comissões
- Grandes Opções do Conceito Estratégico da  Defesa Nacional, I
- Interpelações ao Governo, 
- Moções  
- Orçamento e Conta de Gerência  da  AR
- Orientação  da  Política Orçamental  
- Perguntas ao Governo, Programa  de  Estabilidade e Crescimento
- Programa do Governo, 
- Relatórios de Segurança Interna, 
- Segurança Interna, 
- Votos
