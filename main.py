import pygame
import inimigo_teste
import sprites

pygame.init()

#classe do carro do jogador
class carro_jogador(object):
    #função construtora
    def __init__(self,x,y,largura,altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.velocidade = 1
        self.faixa = 4

        #hitbox temporária para teste dos itens
        self.hitbox = (self.x,self.y,166,100)

    def acelerar(self):
        if self.velocidade <= 20: #velocidade máxima
            self.velocidade += 1

    def freiar(self):
        if self.velocidade > 1:
            self.velocidade -= 1

    def subir(self): #sobe o carro em 1 faixa
        if self.faixa != 1:
            self.y -= 140
            self.faixa -= 1

    def descer(self): #desce o carro em 1 faixa
        if self.faixa:
            if self.faixa != 4:
                self.y += 140
                self.faixa += 1

    def andar(self):
        self.x += self.velocidade
        if self.x >= 1500: #retorna para o começo caso o jogador complete uma volta
            self.x = -166

    def draw(self, win, sprite): #desenha o carro na tela

        #hitbox temporária
        self.hitbox = (self.x, self.y, 166, 100)
        #pygame.draw.rect(win, (0,0,255), self.hitbox,2)

        win.blit(sprite, (self.x, self.y))

def redraw_window(): #função para atualizar a tela
    win.blit(sprites.bg, (0, 0))
    player.draw(win,sprites.car_red)
    inimigo.draw(win,sprites.car_green)
    pygame.display.update()


#criação da janela
win = pygame.display.set_mode((1500,800))

#nome da janela
pygame.display.set_caption("Jogo")

#clock principal
clock = pygame.time.Clock()

#instancia inicial do jogador
player = carro_jogador(0,560,166,100)

#instancia do inimigo usado para teste
inimigo = inimigo_teste.carro_inimigo(1000,560,166,100)

#delay de troca de faixa
delay_faixa = 0

#loop principal do jogo
running = True
while running:
    clock.tick(30)

    if delay_faixa > 0:
        delay_faixa += 1
    if delay_faixa == 4:
        delay_faixa = 0

    #sair da janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #colisão com o carro
    if player.faixa == inimigo.faixa:
        if player.x + player.largura > inimigo.hitbox[0] and player.x < inimigo.hitbox[0] + inimigo.hitbox[2]:
            player.x = 0


    #checa quais teclas estão sendo pressionadas e realiza os respectivos comandos
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.freiar()
    if keys[pygame.K_RIGHT]:
        player.acelerar()
    if keys[pygame.K_UP] and delay_faixa == 0:
        player.subir()
        delay_faixa = 1
    if keys[pygame.K_DOWN] and delay_faixa == 0:
        player.descer()
        delay_faixa = 1
    # movimenta o jogador a partir da velocidade e checa caso ele vá completar uma volta
    player.andar()

    #atualiza a tela
    redraw_window()


pygame.quit()