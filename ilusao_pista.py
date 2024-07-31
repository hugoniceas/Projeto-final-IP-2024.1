import pygame 
from sys import exit
import menu_fim_jogo
from Inf_para_adicionar import velocidade

pygame.init()
tela = pygame.display.set_mode((1500, 800))
sprite = pygame.image.load('C:\\Users\\Aluno\\Desktop\\jogo_pacman\\imagens\\bg.jpg')

class Background(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        self.rect.x = pos_x*1350 

    def update(self, velocidade):
        if self.rect.topright[0] < 0 :
            self.rect.x = 1500
        self.rect.x -= 10 + velocidade
    

todas_sprites = pygame.sprite.Group()
for i in range(4):
    pista = Background(i)
    todas_sprites.add(pista)

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((255,255,255))
    for eventos in pygame.event.get():
        botao_pressionado = pygame.key.get_pressed()
        if eventos.type == pygame.QUIT or botao_pressionado[pygame.K_e]:
            pygame.quit()
            exit()
        if botao_pressionado[pygame.K_r]: #deve substituir pela batida, para que vá ao menu de fim de jogo
            menu_fim_jogo.menu_principal(tela)
        if botao_pressionado[pygame.K_RIGHT]: #aumenta a velocidade
            velocidade += 2
        if botao_pressionado[pygame.K_LEFT]:
            if velocidade >0:
                velocidade -= 1
        
    todas_sprites.draw(tela)
    todas_sprites.update(velocidade)

    pygame.display.flip()
