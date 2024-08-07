import pygame 
from sys import exit
import menu_fim_jogo
import info_estatisticas
from BOTOES import Botao

pygame.init()
tela = pygame.display.set_mode((1500, 800))
sprite = pygame.image.load('assets/bg.jpg')
velocidade = 0
font_scores = pygame.font.SysFont("Verdana", 20)


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

INC_velocidade = pygame.USEREVENT + 1  #evento personalizado para aumentar a velocidade com o tempo
pygame.time.set_timer(INC_velocidade, 1000)

while True:
    relogio.tick(30)
    tela.fill((255,255,255))
    for eventos in pygame.event.get():
        botao_pressionado = pygame.key.get_pressed()
        if eventos.type == INC_velocidade: #aumenta a velocidade
            velocidade += 2  
        if eventos.type == pygame.QUIT or botao_pressionado[pygame.K_e]:
            pygame.quit()
            exit()
        if botao_pressionado[pygame.K_r]: #deve substituir pela batida, para que vá ao menu de fim de jogo
            menu_fim_jogo.menu_principal(tela)
        
    todas_sprites.draw(tela)
    # scores = Botao(image=None, pos=(10, 10),
    #                           text_input=f"PONTUAÇÃO: {Inf_para_adicionar.pontuacao}", font=get_font(55), base_color="Purple")
    todas_sprites.update(velocidade)
    scores = font_scores.render(str(Inf_para_adicionar.pontuaçao), True, (255,255,255))
    tela.blit(scores, (100, 100))

    pygame.display.flip()
