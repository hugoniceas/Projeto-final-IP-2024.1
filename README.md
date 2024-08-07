# Projeto-final-IP-2024.1

Direção Perigosa
Alisson Silva <asb3>
Aline Rodrigues <asr2>
Diego Lyra <dfal>
Gabriel Moraes <gbm2>
Hugo Nicéas <han2>

Arquitetura do projeto:
Primeiramente , criamos um esqueleto base para o jogo, com features simples. Utilizando esse sistema, cada integrante poderia trabalhar independentemente em cima da mesma base do jogo. O nosso plano foi modularizar o projeto ao máximo possível, criando blocos independentes que funcionam mesmo sozinhos, porém, quando juntos, funcionam em conjunto com poucas alterações.
A ferramenta base para a modularização foi a classe GameState, que permitiu ao arquivo game.py gerir qual código deve estar ativo em cada momento da execução do programa. A maioria das “telas” do jogo são classes próprias, filhas de GameState, possuindo tanto funções e métodos únicos quanto compartilhados. Dentro do arquivo game.py, são criados objetos para cada uma dessas telas, todos contendo 3 elementos:
- nome (string), é como o programa se refere ao objeto
- run (bool), determina se o programa está ativo (True) ou não (False)
- próximo_estado (string), quando vazio, o código permanece rodando, caso contrário, o arquivo game.py realiza a operação de transição entre o estado atual e o estado referenciado neste atributo.

Cada objeto da classe GameState (e filhas) possui também as funções:
get_run, que retorna o valor booleano contido no atributo run
set_run, que altera o valor do atributo run
set_next_state, que altera o valor contido no atributo proximo_estado
get_next_state, que retorna a string contida no atributo proximo_estado
escrever_texto_opcoes, que permite a escrita padronizada de texto, no formato do texto (essa não foi usada em todos os módulos)

Ferramentas, bibliotecas e frameworks:

pygame : A biblioteca pygame foi escolhida para o projeto como base de construção do código. Ela permite que jogos sejam construídos em python de maneira simples e intuitiva para quem está familiarizado com a linguagem. Visto que sua documentação é extensa e existem diversos materiais para auxílio e estudo em pygame, ela foi nossa escolha.

random: A biblioteca random do python foi utilizada para gerar números aleatórios. Esses números aleatórios foram utilizados para medições de tempo, spawn de itens, spawn de inimigos, cassino, e qualquer outra funcionalidade que necessite de uma geração aleatória de números.


paint.net,ezgif, GIMP: As ferramentas de edição de imagem foram utilizadas para compor a parte gráfica do nosso jogo. Seja criar backgrounds, cortar sprites, separar os frames de gifs em várias imagens ou redimensionar imagens, toda a parte gráfica do jogo passou por editores de imagem em algum momento.

Audacity: O editor de áudio foi essencial para cortar e definir as músicas e os sons contidos no jogo e no menu. 


Divisão de trabalho dentro do grupo:

Aline:
Determinar e implementar o funcionamento da pontuação
Criar backgrounds para o jogo


Alisson:
Criar a ilusão de ótica da pista se movimentando cada vez mais rápido
Tela de morte com estatísticas do scoreboard
Scoreboard que exibe as estatísticas do jogador em tempo real

Diego:
Criar a lógica de spawn dos inimigos
Implementar o spawn dos inimigos
Determinar a velocidade na qual o jogo progride

Gabriel:
Implementar o cassino
Implementar a loja de skins
Implementar os menus do jogo

Hugo:
Criar os itens coletáveis do jogo
Implementar a funcionalidade dos itens
Criar e implementar a lógica de spawn dos itens


Conceitos utilizados:

Comandos condicionais:
O código está repleto de condicionais, pois, tudo dentro da lógica do jogo depende de outros fatores estarem acontecendo ou não. Um exemplo de comando condicional é checar se determinada tecla está sendo pressionada para mover o carro.

Laços de repetição:
O jogo em si é um laço de repetição principal, no qual todos os comandos nele contidos são executados indefinidamente até o fim do jogo. Portanto, o principal exemplo é o laço while running

Listas:
Listas servem como estruturas para armazenar diversos elementos em apenas um local da memória. Um exemplo de utilização de lista é a lista inimigos, na qual estão contidas todos os objetos que são considerados inimigos.

Funções:
Funções são utilizadas diversas vezes, como forma de manter o código mais organizado ou de facilitar a implementação de blocos mais complexos. Um exemplo de função é redraw_window, que serve para atualizar o que está sendo exibido na tela a cada iteração do laço while running

Recursão:
Não foi utilizada recursão em muitos momentos, porém, um exemplo de recursão é no menu final, no qual, dentro da função estatísticas, chama ele mesmo.

Tuplas:
Tuplas servem como listas imutáveis que permitem armazenar elementos de forma que não mudem ou retornar mais de um resultado de uma vez em uma função. Um exemplo da utilização de tuplas é na função spawnar_items, que retorna uma tupla com o valor (0, uma variável booleana)

Dicionários:
Os dicionários serviram como forma de organizar elementos de forma mais legível e flexível do que listas. Um exemplo de dicionário é current_items, no qual cada chave guarda uma lista. As chaves são os tipos de itens existentes no jogo, e cada lista contém todos os itens daquele tipo que estão presentes naquele momento.


Modulos e pacotes:
Modularizar o nosso projeto o máximo possível para garantir independência entre as partes e um fluxo de projeto melhor. O principal exemplo são todos os módulos que fizemos para as features, e depois importamos para main.

Programação orientada a objetos:
Utilizar as técnicas de programação orientada a objetos nos permitiu organizar melhor nosso código e o tornar mais legível, podendo criar diferentes instâncias desses objetos de forma prática. Um exemplo de objeto que criamos é o carro do jogador.

Desafios e erros:
Não houve um acordo para determinar como seriam implementados certos aspectos do jogo, o que acarretou no aumento da quantidade de ajustes a serem feitos na hora de juntar os módulos individuais, além de resultar em um código menos organizado.
Um exemplo disso é o carregamento de imagens, enquanto os módulos Menu, Loja e Cassino (feitos por Gabriel) utilizam a função pygame.image.load(caminho da imagem) dentro do próprio código para carregar as imagens, os módulos feitos por Hugo e Alisson importam os sprites de um arquivo separado, no qual é utilizada a função pygame.image.load(). Isso causou  dificuldades para fazer com que todos os módulos estejam sempre com as mesmas informações.
Na implementação da roleta (Cassino), houve dificuldade para lidar com o botão de espaço ser apertado diversas vezes enquanto a roleta gira.
Na implementação dos diferentes backgrounds, houve grande dificuldade de conseguir fazer com que vários backgrounds diferentes se encaixassem na estrutura que havia sido feita anteriormente para apenas um background.
Mesmo utilizando modularização, ainda houve bastante trabalho manual para juntar as partes separadas e corrigir problemas que não estavam evidentes antes ou que surgiram após essas junções.
