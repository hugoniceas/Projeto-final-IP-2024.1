import pygame
import items
import sprites
import constantes
import random
from game_state import GameState
from pontuacao_items import verificaçao
import info_estatisticas



class jogo(GameState):
    def __init__(self,nome,run,proximo_estado):
        super().__init__(nome,run,proximo_estado)


    def abrir_jogo(self,carro_atual):
        pygame.init()
        def tocar_musica():
            musica = pygame.mixer.music.load("assets/audios/musica_pista.mp3")
            pygame.mixer.music.play(-1)

        #classe do carro do jogador
        class carro_jogador(object):
            #função construtora
            def __init__(self,x,faixa,largura,altura,skin):
                self.x = x
                self.y = constantes.faixas[faixa]
                self.largura = largura
                self.altura = altura
                self.velocidade = 20
                self.faixa = faixa
                self.skin = skin

                #hitbox temporária para teste dos itens
                self.hitbox = (self.x,self.y,166,100)

            def subir(self): #sobe o carro em 1 faixa
                if self.faixa != 1:
                    self.y -= 140
                    self.faixa -= 1

            def descer(self): #desce o carro em 1 faixa
                if self.faixa:
                    if self.faixa != 4:
                        self.y += 140
                        self.faixa += 1

            def progredir(self):
                if self.x + self.velocidade <= 1334:
                    self.x += self.velocidade
                else:
                    self.x = 1334

            def voltar(self):
                if self.x - self.velocidade >= 0:
                    self.x -= self.velocidade
                else:
                    self.x = 0

            def draw(self, win, sprite): #desenha o carro na tela

                #hitbox
                self.hitbox = (self.x, self.y, 166, 100)
                #pygame.draw.rect(win, (0,0,255), self.hitbox,2)

                win.blit(sprite, (self.x, self.y))


        class Background(pygame.sprite.Sprite):
            def __init__(self, pos_x,sprite):
                pygame.sprite.Sprite.__init__(self)
                self.image = sprite
                self.rect = self.image.get_rect()
                self.rect.topleft = (0,0)
                self.rect.x = pos_x*1350

            def update(self, velocidade):
                if self.rect.topright[0] < 0 :
                    self.rect.x = 1500
                self.rect.x -= 10 + velocidade


        def pegar_valor_aleatorio_de_uma_tupla(tupla):

            numero = random.randint(0, (len(tupla) - 1))

            return tupla[numero]

        #classe do obstaluco/inimigo
        class obstaculos(object):


            def __init__(self):

                self.faixas_possiveis = (560, 420, 280, 140)

                self.y = pegar_valor_aleatorio_de_uma_tupla(self.faixas_possiveis)

                if self.y == 560 or self.y == 420:
                    self.x = pegar_valor_aleatorio_de_uma_tupla((-220, -440, -660))

                else:
                    self.x = pegar_valor_aleatorio_de_uma_tupla((1720, 1940, 2160))

                self.hitbox = (self.x, self.y, 166, 100)

            def get_y(self):
                return self.y

            def get_x(self):
                return self.x

            def andar(self, velocidade_faixa):
                self.x += velocidade_faixa

            def draw(self, win, sprite):
                self.hitbox = (self.x, self.y, 166, 100)
                win.blit(sprite, (self.x, self.y))

        class dificuldade(object):

            def __init__(self):
                self.dificuldade = 0
                self.contador_dificuldade = 0

            def get_dificuldade(self):
                return self.dificuldade

            def incrementar_dificuldade(self):
                self.contador_dificuldade += 0.7

            def atualizar_dificuldade(self):
                if self.contador_dificuldade < 1000:
                    self.dificuldade = 0

                elif 2000 > self.contador_dificuldade > 1000:
                    self.dificuldade = 1

                else:
                    self.dificuldade = 2

            def draw(self, win, font):
                texto = font.render('Dificuldade: ' + str(int(self.dificuldade)), 1, (255, 0, 0))
                win.blit(texto, (1100, 50))

        todas_sprites = pygame.sprite.Group()
        for i in range(4):
            pista = Background(i,sprites.cenarios[0])
            todas_sprites.add(pista)

        INC_velocidade = pygame.USEREVENT + 1  #evento personalizado para aumentar a velocidade com o tempo
        pygame.time.set_timer(INC_velocidade, 5000)

        tocar_musica()



        def redraw_window(): #função para atualizar a tela
            player.draw(win,player.skin)

            #loop que passará por todos os items que atualmente estão na tela e os atualizarão
            for item_type in items.current_items.keys():
                for item in items.current_items[item_type]:
                    current_sprite_cycle = item.sprite_cycle #os sprites dos items são divididos em ciclos, para que o sprite apenas mude após x quantidade de frames
                    frame_atual = current_sprite_cycle//item.cycle_step
                    sprite = sprites.items[item_type][frame_atual]
                    item.draw(win,sprite)

                    if item.sprite_cycle == item.cycle_limit-1:
                        item.reset_sprite_cyle()
                    else:
                        item.increment_sprite_cycle()

            for obstaculo in faixa1:
                if not fantasma_ativo:
                    obstaculo.draw(win, sprites.car_green_frente)
                else:
                    obstaculo.draw(win, sprites.car_green_frente_ghost)
            for obstaculo in faixa2:
                if not fantasma_ativo:
                    obstaculo.draw(win, sprites.car_green_frente)
                else:
                    obstaculo.draw(win, sprites.car_green_frente_ghost)
            for obstaculo in faixa3:
                if not fantasma_ativo:
                    obstaculo.draw(win, sprites.car_green_tras)
                else:
                    obstaculo.draw(win, sprites.car_green_tras_ghost)
            for obstaculo in faixa4:
                if not fantasma_ativo:
                    obstaculo.draw(win, sprites.car_green_tras)
                else:
                    obstaculo.draw(win, sprites.car_green_tras_ghost)

            if timer != "":
                timer.draw(win, fonte, indice_cenario)

            if indice_cenario != 3:
                texto_pontuacao = fonte.render(f"Pontuação: {info_estatisticas.pontuacao_game}", True, pygame.Color("white"))
            else:
                texto_pontuacao = fonte.render(f"Pontuação: {info_estatisticas.pontuacao_game}", True, pygame.Color("black"))
            win.blit(texto_pontuacao, (1000, 10))

            pygame.display.update()


        def checar_colisao(objeto1,objeto2,fantasma_ativo,tipo_objeto,faixa_inimigo): #função que checa colisão entre 2 objetos
            if tipo_objeto == "inimigo":
                if objeto1.faixa == faixa_inimigo and not fantasma_ativo:
                    if objeto1.x + objeto1.largura > objeto2.hitbox[0] and objeto1.x < objeto2.hitbox[0] + objeto2.hitbox[2]:
                        return True
                return False
            else:
                if objeto1.faixa == objeto2.faixa:
                    if objeto1.x + objeto1.largura > objeto2.hitbox[0] and objeto1.x < objeto2.hitbox[0] + objeto2.hitbox[2]:
                        return True
                return False

        #criação da janela
        win = pygame.display.set_mode((1500,800))

        #nome da janela
        pygame.display.set_caption("Jogo")

        # Define o cenário inicial
        cenario_atual = sprites.cenarios[0]


        # Variáveis auxiliares da pontuação
        indice_cenario = 0  # Variável de troca de cenário
        tempo_de_troca = 200  # Tempo para trocar o primeiro cenário
        tempo_vivo = 0.0  # Tempo de incrementação da pontuação
        info_estatisticas.pontuacao_game = 0
        info_estatisticas.distancia = 0

        #clock principal
        clock = pygame.time.Clock()

        caminho_skin_jogador = carro_atual.skin
        skin_jogador = pygame.image.load(caminho_skin_jogador)

        #instancia inicial do jogador
        player = carro_jogador(0,4,166,100,skin_jogador)

        pistas = [1, 2, 3, 4]


        items.item_reset()

        #variavel reservada ao timer dos items
        timer = ''

        #relógio de spawn dos items
        tempo_spawn = 0

        #faixas já ocupadas por itens
        faixas_ocupadas_itens = []

        #fonte usada para textos
        fonte = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 32)

        #faixas não ocupadas por itens
        faixas_livres_itens = [1,2,3,4]

        #flags de detecção se interrogacao ou fantasma estão ativos
        fantasma_ativo = False
        interrogacao_ativo = False

        #flags de detecção se existem interrogação ou fantasma na pista
        existe_powerup = False

        velocidade_pista = 1

        # Lista de obstaculos por faixa
        faixa1 = []
        faixa2 = []
        faixa3 = []
        faixa4 = []

        #multiplicador de pontuação da interrogação
        multiplicador_pontuacao = 1

        # instancia inicial da dificuldade
        dificuldade_atual = dificuldade()

        # Temporizador obstáculos
        timer_obstaculo = 0

        #loop principal do jogo
        while self.run:
            clock.tick(30)

            #timer dos itens já existentes
            tempo_atual = pygame.time.get_ticks()
            for item_type in items.current_items.keys():
                for item in items.current_items[item_type]:
                    tempo_vida = (tempo_atual - item.tempo_spawn)//1000
                    if tempo_vida >= 10:
                        items.current_items[item_type].remove(item)
                        if item_type == 'fantasma' or item_type == 'interrogacao':
                            existe_powerup = False
                        faixas_livres_itens.append(item.faixa)
                        faixas_ocupadas_itens.remove(item.faixa)



            #spawn aleatório dos items
            if tempo_spawn == 0:
                tempo_spawn = random.randrange(3,7)
                comeco_ciclo_items = pygame.time.get_ticks()

            if tempo_spawn != 0:
                ciclo_items_atual = pygame.time.get_ticks()
                if (ciclo_items_atual-comeco_ciclo_items)//1000 == tempo_spawn:
                    especial_ativo = interrogacao_ativo or fantasma_ativo
                    tempo_spawn, existe_powerup = items.spawnar_items(faixas_ocupadas_itens,faixas_livres_itens,items.current_items,
                                                      player.x,player.largura,especial_ativo,existe_powerup)


            #sair da janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.set_run(False)
                    self.set_next_state('Sair')
                if event.type == pygame.KEYDOWN:
                    #comandos de troca de faixa
                    if event.key == pygame.K_DOWN and not interrogacao_ativo:
                        player.descer()
                    elif event.key == pygame.K_DOWN and interrogacao_ativo:
                        player.subir()
                    if event.key == pygame.K_UP and not interrogacao_ativo:
                        player.subir()
                    elif event.key == pygame.K_UP and interrogacao_ativo:
                        player.descer()
                if event.type == INC_velocidade: #aumenta a velocidade
                    if velocidade_pista < 20:
                        velocidade_pista += 1

            #troca de cenários
            if info_estatisticas.pontuacao_game > tempo_de_troca and info_estatisticas.pontuacao_game != 0:
                if indice_cenario == len(sprites.cenarios)-1:
                    indice_cenario = 0
                    todas_sprites = pygame.sprite.Group()
                    for i in range(4):
                        pista = Background(i, sprites.cenarios[indice_cenario])
                        todas_sprites.add(pista)
                else:
                    indice_cenario += 1
                    todas_sprites = pygame.sprite.Group()
                    for i in range(4):
                        pista = Background(i, sprites.cenarios[indice_cenario])
                        todas_sprites.add(pista)

                tempo_de_troca += 200

            tempo_vivo += clock.get_time() / 1000.0

            if tempo_vivo >= 1.0:
                info_estatisticas.pontuacao_game += (1 * multiplicador_pontuacao)
                info_estatisticas.distancia += 1
                tempo_vivo = 0.0


            #spawn dos obstaculos/inimigos
            timer_obstaculo += 1
            for obstaculo in faixa4:
                if obstaculo.get_x() > -220:
                    obstaculo.andar(velocidade_das_faixas[3] * -1)
                else:
                    faixa4.pop(faixa4.index(obstaculo))

            for obstaculo in faixa3:
                if obstaculo.get_x() > -220:
                    obstaculo.andar(velocidade_das_faixas[2] * -1)
                else:
                    faixa3.pop(faixa3.index(obstaculo))

            for obstaculo in faixa2:
                if obstaculo.get_x() < 1720:
                    obstaculo.andar(velocidade_das_faixas[1])
                else:
                    faixa2.pop(faixa2.index(obstaculo))

            for obstaculo in faixa1:
                if obstaculo.get_x() < 1720:
                    obstaculo.andar(velocidade_das_faixas[0])
                else:
                    faixa1.pop(faixa1.index(obstaculo))

            if timer_obstaculo >= 210:
                velocidade_das_faixas = []
                if dificuldade_atual.get_dificuldade() == 0:
                    numero_carros = pegar_valor_aleatorio_de_uma_tupla((2,))
                    for i in range(4):
                        velocidade_das_faixas.append(pegar_valor_aleatorio_de_uma_tupla((8, 10, 13)))

                elif dificuldade_atual.get_dificuldade() == 1:
                    numero_carros = pegar_valor_aleatorio_de_uma_tupla((4,))
                    for i in range(4):
                        velocidade_das_faixas.append(pegar_valor_aleatorio_de_uma_tupla((11, 14, 17)))
                else:
                    numero_carros = pegar_valor_aleatorio_de_uma_tupla((6,))
                    for i in range(4):
                        velocidade_das_faixas.append(pegar_valor_aleatorio_de_uma_tupla((19, 21, 25)))

                for i in range(numero_carros):
                    obstaculo_atual = obstaculos()
                    if obstaculo_atual.get_y() == 560:
                        faixa1.append(obstaculo_atual)

                    elif obstaculo_atual.get_y() == 420:
                        faixa2.append(obstaculo_atual)

                    elif obstaculo_atual.get_y() == 280:
                        faixa3.append(obstaculo_atual)

                    else:
                        faixa4.append(obstaculo_atual)

                timer_obstaculo = 0




            #colisão do carro com inimigo
            for inimigo in faixa1:
                if checar_colisao(player,inimigo,fantasma_ativo,'inimigo',4):
                    pygame.mixer.music.stop()
                    self.set_next_state('Fim')
                    self.set_run(False)
            for inimigo in faixa2:
                if checar_colisao(player,inimigo,fantasma_ativo,'inimigo',3):
                    pygame.mixer.music.stop()
                    self.set_next_state('Fim')
                    self.set_run(False)
            for inimigo in faixa3:
                if checar_colisao(player,inimigo,fantasma_ativo,'inimigo',2):
                    pygame.mixer.music.stop()
                    self.set_next_state('Fim')
                    self.set_run(False)
            for inimigo in faixa4:
                if checar_colisao(player,inimigo,fantasma_ativo,'inimigo',1):
                    pygame.mixer.music.stop()
                    self.set_next_state('Fim')
                    self.set_run(False)

            #colisão do carro com items
            for item_type in items.current_items.keys():
                for item in items.current_items[item_type]:
                    if checar_colisao(player,item,fantasma_ativo,'item',0):
                        items.current_items[item_type].remove(item)
                        items.quantidade[item_type] += 1
                        if item_type == 'fantasma':
                            fantasma_ativo = True
                            tempo_ativacao = pygame.time.get_ticks()
                            existe_powerup = False
                        elif item_type == 'interrogacao':
                            interrogacao_ativo = True
                            tempo_ativacao = pygame.time.get_ticks()
                            existe_powerup = False
                            multiplicador_pontuacao = verificaçao(info_estatisticas.pontuacao_game, item_type)

                        #pontuação dos itens:
                        if item_type != 'interrogacao':
                            info_estatisticas.pontuacao_game = verificaçao(info_estatisticas.pontuacao_game, item_type)
                        faixas_livres_itens.append(item.faixa)
                        faixas_ocupadas_itens.remove(item.faixa)




            #timer de ativação dos power-ups
            if fantasma_ativo or interrogacao_ativo:
                tempo_atual = pygame.time.get_ticks()
                tempo_segundos = (tempo_atual - tempo_ativacao) // 1000
                #cria a instancia do timer ou altera o seu valor
                if timer == "":
                    timer = items.timer_items()
                else:
                    timer.alterar_tempo(15-tempo_segundos)

            #15 segundos de item ativo
                if tempo_segundos == 15:
                    fantasma_ativo = False
                    interrogacao_ativo = False
                    multiplicador_pontuacao = 1
                    timer = ''


            #checa quais teclas estão sendo pressionadas e realiza os respectivos comandos
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and not interrogacao_ativo:
                player.voltar()
            elif keys[pygame.K_LEFT] and interrogacao_ativo:
                player.progredir()

            if keys[pygame.K_RIGHT] and not interrogacao_ativo:
                player.progredir()
            elif keys[pygame.K_RIGHT] and interrogacao_ativo:
                player.voltar()




            #atualiza a tela
            todas_sprites.draw(win)
            todas_sprites.update(velocidade_pista)
            redraw_window()
            dificuldade_atual.incrementar_dificuldade()
            dificuldade_atual.atualizar_dificuldade()

