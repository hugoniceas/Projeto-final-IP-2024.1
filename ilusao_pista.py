import pygame
from sys import exit
import menu_fim_jogo



pygame.init()
tela = pygame.display.set_mode((1500, 800))
sprite = pygame.image.load('sprites\\bg.jpg')
#adicionando cenarios
grama = pygame.image.load('sprites\\grama.png')
areia = pygame.image.load('sprites\\areia.png')
lava = pygame.image.load('sprites\\lava.png')
grama_velha = pygame.image.load('sprites\\grama_velha.png')

#organiza os cenarios em ordem
cenarios = [grama, grama_velha, areia, lava]

#define o cenario inicial
cenario_atual = cenarios[0]

class Background(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x * self.rect.width, 0)

    def update(self, velocidade):
        self.rect.x -= 10 + velocidade
        if self.rect.right <= 0:
            self.rect.x += self.rect.width * 2

class Cenario(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x * self.rect.width, pos_y)
    
    def update(self, velocidade):
        self.rect.x -= 10 + velocidade
        if self.rect.right <= 0:
            self.rect.x += self.rect.width * 2

    def change_image(self, new_image):
        self.image = new_image
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

todas_sprites = pygame.sprite.Group()

grass_sprites = pygame.sprite.Group()



# cria o cenario acima e abaixo da pista

for indice_cenario in range(2):
    pista = Background(indice_cenario)
    todas_sprites.add(pista)
    grass_top = Cenario(indice_cenario, 0, cenario_atual)
    grass_bottom = Cenario(indice_cenario, 680, cenario_atual)
    todas_sprites.add(grass_top)
    todas_sprites.add(grass_bottom)
    grass_sprites.add(grass_top)
    grass_sprites.add(grass_bottom)

relogio = pygame.time.Clock()

velocidade=0

#variaveis auxiliares da pontuacao\
indice_cenario=0 #variavel de troca de cenario
tempo_de_troca=45 #tempo para trocar o primeiro cenario
tempo_vivo = 0.0 # tempo de incrementacao da pontuacao
pontuacao_game = 0 #pontuacao

fonte = pygame.font.Font(None, 36) #fonte da pontuacao

while True:
    relogio.tick(60)
    tela.fill((255, 255, 255))
    
    for eventos in pygame.event.get():
        botao_pressionado = pygame.key.get_pressed()

        if eventos.type == pygame.QUIT or botao_pressionado[pygame.K_e]:
            pygame.quit()
            exit()
        if botao_pressionado[pygame.K_r]:  # deve substituir pela batida, para que vá ao menu de fim de jogo
            menu_fim_jogo.menu_principal(tela, pontuacao_game)

        if botao_pressionado[pygame.K_RIGHT]:  # aumenta a velocidade
            velocidade += 2
        if botao_pressionado[pygame.K_LEFT]:
            if velocidade > 0:
                velocidade -= 1

    if pontuacao_game%tempo_de_troca==0 and pontuacao_game!=0:  # deve substituir pela pontuaçao/tempo
        
        if indice_cenario==3:
            cenario_atual=cenarios[0]
            indice_cenario=0

        else:
            cenario_atual= cenarios[indice_cenario+1]
            indice_cenario+=1

        for grass_sprite in grass_sprites:
            grass_sprite.change_image(cenario_atual)
        tempo_de_troca+=45

    tempo_vivo += relogio.get_time() / 1000.0 # Converte milissegundos para segundos
    
    #incrementa a pontuacao
    if tempo_vivo >= 1.0:
        pontuacao_game += 15
        tempo_vivo = 0.0

    todas_sprites.update(velocidade)
    todas_sprites.draw(tela)

    
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao_game}", True, pygame.Color("white"))

    tela.blit(texto_pontuacao, (10, 10))
    pygame.display.flip()
