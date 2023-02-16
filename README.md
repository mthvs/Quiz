Atividade Gerador Quiz – P2

Padrões Implementados e o motivo de ter sido escolhidos:

Singleton: Usei esse padrão para poder instanciar apenas uma vez o conteúdo presente no json, sendo assim mesmo alterando o conteúdo presente no json enquanto o programa estiver executando essas mudanças não irão aparecer.

Factory: Usei para separar os temas para que seja retornado o Quiz baseado no tema que o usuário escolher no menu.

Iterator:  É um padrão de projeto comportamental que permite a você percorrer elementos de uma coleção sem expor as representações dele, no meu caso foi usado para percorrer e iterar as listas de perguntas de cada quiz.

Command: Usei esse padrão para poder executar comandos de respostas para usuário de acordo de como ele foi no quis, fiz um comando para dar uma reposta de acordo com os acertos, e outro para falar ao usuário qual das questões ele errou.
