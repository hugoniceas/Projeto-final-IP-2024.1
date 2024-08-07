import constantes
import pygame
from random import randrange, choice
class item(object):
    #função construtora
    def __init__(self,x,largura,altura,faixa,tempo_spawn):
        self.x = x
        self.y = constantes.faixas[faixa]
        self.largura = largura
        self.altura = altura
        self.faixa = faixa
        self.hitbox = (self.x,self.y,largura,altura)
        self.sprite_cycle = 0
        self.tempo_spawn = tempo_spawn

    def draw(self, win, sprite):
        win.blit(sprite, (self.x,self.y))

        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2) (desenha hitbox do item, usado apenas no desenvolvimento)

    def reset_sprite_cyle(self):
        self.sprite_cycle = 0

    def increment_sprite_cycle(self):
        self.sprite_cycle += 1

    def hit(self): #executa um comando ao colidir com o jogador
        pass

class ficha_cassino(item):
    def __init__(self,x,largura,altura,faixa,tempo_spawn):
        super().__init__(x,largura,altura,faixa,tempo_spawn)
        self.cycle_limit = 12
        self.cycle_step = 3

class moeda(item):
    def __init__(self,x,largura,altura,faixa,tempo_spawn):
        super().__init__(x,largura,altura,faixa,tempo_spawn)
        self.cycle_limit = 24
        self.cycle_step = 3
        self.hitbox = (self.x+18,self.y+18,largura,altura)

class fantasma(item):
    def __init__(self,x,largura,altura,faixa,tempo_spawn):
        super().__init__(x,largura,altura,faixa,tempo_spawn)
        self.cycle_limit = 32
        self.cycle_step = 4
        self.hitbox = (self.x+22,self.y,largura,altura)

class interrogacao(item):
    def __init__(self,x,largura,altura,faixa,tempo_spawn):
        super().__init__(x,largura,altura,faixa,tempo_spawn)
        self.cycle_limit = 24
        self.cycle_step = 3
        self.hitbox = (self.x+34,self.y,largura,altura)


class timer_items(object):
    def __init__(self):
        self.tempo = 15

    def draw(self,win,font,indice_cenario):
        if indice_cenario != 3:
            texto = font.render('Tempo restante:' + str(self.tempo),1, (255,255,255))
        else:
            texto = font.render('Tempo restante:' + str(self.tempo), 1, (0,0,0))
        win.blit(texto,(900,750))

    def alterar_tempo(self,tempo):
        self.tempo = tempo


class conta_jogador(object):
    def __init__(self):
        self.dinheiro = 70
        self.fichas = 1

    def mudar_dinheiro(self,valor):
        self.dinheiro = valor

    def mudar_fichas(self,valor):
        self.fichas = valor

    def depositar_dinheiro(self,valor):
        self.dinheiro += valor

    def depositar_fichas(self,valor):
        self.fichas += valor

    def gastar_dinheiro(self,valor):
        self.dinheiro -= valor

    def diminuir_ficha(self):
        self.fichas -= 1


def item_reset():
    global current_items
    global quantidade
    for chave in current_items:
        current_items[chave] = []
        quantidade[chave] = 0


#dicionario que conterá todos os itens que estarão na tela:
current_items = {'ficha cassino':[],
           'moeda': [],
           'fantasma': [],
            'interrogacao': []}

#dicionário com a quantidade de itens coletados naquela jogada
quantidade  = {'ficha cassino':0,
           'moeda': 0,
           'fantasma': 0,
            'interrogacao': 0}





'''um item vai spawnar a cada intervalo de 3-6 segundos (ok)
o máximo de items por faixa é 1 (ok)
fantasmas não podem spawnar caso interrogação esteja ativada e vice-versa (ok)
fanstasmas não podem spawnar caso haja alguma interrogação e vice-versa (ok)
não pode ter mais de um fantasma por vez, mesmo pra interrogação (ok)
itens somem após 10 segundos


chances de spawn
moeda = 75% (95% caso fantasma ou interrogação estejam ativos)
fantasma = 10%
interrogação = 10%
ficha cassino = 5%'''





def spawnar_items(faixas_ocupadas,faixas_disponiveis,current_items,x_player,largura_player,especial_ativo,existe_powerup):
#só tentara spawnar algum item caso tenha alguma faixa não ocupada
    if len(faixas_ocupadas) < 4:
        faixa_item = choice(faixas_disponiveis)
        faixas_disponiveis.remove(faixa_item)
        faixas_ocupadas.append(faixa_item)



        #x do carro é a traseira
        #coordenada x do item
        x_valido = False
        while not x_valido:
            x_coord_item = randrange(100,1401)
            if x_coord_item + 80 < x_player or x_coord_item > x_player + largura_player:
                x_valido = True

        #tipo do item, especial ativo não permite que fantasmas ou interrogações aparecam quando tem um powerup ativo
        tipo_item = randrange(101)
        tempo_spawn = pygame.time.get_ticks()
        if tipo_item <= 75 or ((especial_ativo or existe_powerup) and tipo_item <= 95):
            item_atual = moeda(x_coord_item,64,64,faixa_item,tempo_spawn)
            current_items['moeda'].append(item_atual)
        elif tipo_item <= 85:
            item_atual = fantasma(x_coord_item,56,100,faixa_item,tempo_spawn)
            current_items['fantasma'].append(item_atual)
            existe_powerup = True
        elif tipo_item <= 95:
            item_atual = interrogacao(x_coord_item,32,100,faixa_item,tempo_spawn)
            current_items['interrogacao'].append(item_atual)
            existe_powerup = True
        else:
            item_atual = ficha_cassino(x_coord_item,80,80,faixa_item,tempo_spawn)
            current_items['ficha cassino'].append(item_atual)



    return (0,existe_powerup)