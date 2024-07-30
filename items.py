import constantes
import pygame
class item(object):
    #função construtora
    def __init__(self,x,largura,altura,faixa):
        self.x = x
        self.y = constantes.faixas[faixa]
        self.largura = largura
        self.altura = altura
        self.faixa = faixa
        self.hitbox = (self.x,self.y,largura,altura)
        self.sprite_cycle = 0

    def draw(self, win, sprite):
        win.blit(sprite, (self.x,self.y))

        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def reset_sprite_cyle(self):
        self.sprite_cycle = 0

    def increment_sprite_cycle(self):
        self.sprite_cycle += 1
class ficha_cassino(item):
    def __init__(self,x,largura,altura,faixa):
        super().__init__(x,largura,altura,faixa)
        self.cycle_limit = 12
        self.cycle_step = 3

class moeda(item):
    def __init__(self,x,largura,altura,faixa):
        super().__init__(x,largura,altura,faixa)
        self.cycle_limit = 24
        self.cycle_step = 3
        self.hitbox = (self.x+18,self.y+18,largura,altura)

class fantasma(item):
    def __init__(self,x,largura,altura,faixa):
        super().__init__(x,largura,altura,faixa)
        self.cycle_limit = 32
        self.cycle_step = 4
        self.hitbox = (self.x+22,self.y,largura,altura)

class interrogacao(item):
    def __init__(self,x,largura,altura,faixa):
        super().__init__(x,largura,altura,faixa)
        self.cycle_limit = 24
        self.cycle_step = 3
        self.hitbox = (self.x+34,self.y,largura,altura)


#dicionario que conterá todos os itens que estarão na tela:
current_items = {'ficha cassino':[],
           'moeda': [],
           'fantasma': [],
            'interrogacao': []}

#dicionário com a quantidade de itens coletados
quantidade  = {'ficha cassino':0,
           'moeda': 0,
           'fantasma': 0,
            'interrogacao': 0}
