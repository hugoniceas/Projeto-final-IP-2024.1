import pygame

#carros inimigos que ficarão fixos na tela, usados apenas para testar o funcionamento dos itens
class carro_inimigo(object):

    def __init__(self,x,y,largura,altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.hitbox = (self.x, self.y, 166, 100)
        self.faixa = 4


    def draw(self,win,sprite):

        #pygame.draw.rect(win, (255, 0, 0), self.hitbox,2)

        win.blit(sprite, (self.x, self.y))





