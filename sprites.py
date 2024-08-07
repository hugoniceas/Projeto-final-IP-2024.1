import pygame

car_green_tras = pygame.image.load('assets/sprites/car_green1.png')
car_green_frente = pygame.image.load('assets/sprites/car_green2.png')

car_green_tras_ghost = pygame.image.load('assets/sprites/car_green1_ghost.png')
car_green_frente_ghost = pygame.image.load('assets/sprites/car_green2_ghost.png')

grama = pygame.image.load('assets/backgrounds/bg_grama.jpg')
areia = pygame.image.load('assets/backgrounds/bg_areia.jpg')
lava = pygame.image.load('assets/backgrounds/bg_lava.jpg')
neve = pygame.image.load('assets/backgrounds/bg_snow.jpg')
grama_morta = pygame.image.load('assets/backgrounds/bg_grama_morta.jpg')
bg = pygame.image.load('assets/backgrounds/bg.jpg')

cenarios = (bg,grama,bg,neve ,bg,grama_morta, bg,areia,bg, lava)

bg = pygame.image.load('assets/backgrounds/bg.jpg')

class CarroAtual:
    def __init__(self):
        self.skin = "assets/sprites/car_red.png"

    def skin_setter(self, skin):
        self.skin = skin




items = {'ficha cassino':[pygame.image.load('assets/sprites/ficha1.png'),pygame.image.load('assets/sprites/ficha2.png'),
                        pygame.image.load('assets/sprites/ficha3.png'),pygame.image.load('assets/sprites/ficha4.png')],
           'moeda': [pygame.image.load('assets/sprites/coin_1.png'),pygame.image.load('assets/sprites/coin_2.png'),
                     pygame.image.load('assets/sprites/coin_3.png'),pygame.image.load('assets/sprites/coin_4.png'),
                     pygame.image.load('assets/sprites/coin_5.png'),pygame.image.load('assets/sprites/coin_6.png'),
                     pygame.image.load('assets/sprites/coin_7.png'),pygame.image.load('assets/sprites/coin_8.png')],
           'fantasma': [pygame.image.load('assets/sprites/ghost1.png'),pygame.image.load('assets/sprites/ghost2.png'),
                        pygame.image.load('assets/sprites/ghost3.png'),pygame.image.load('assets/sprites/ghost4.png'),
                        pygame.image.load('assets/sprites/ghost5.png'),pygame.image.load('assets/sprites/ghost6.png'),
                        pygame.image.load('assets/sprites/ghost7.png'),pygame.image.load('assets/sprites/ghost8.png')],
            'interrogacao': [pygame.image.load('assets/sprites/question1.png'),pygame.image.load('assets/sprites/question2.png'),
                             pygame.image.load('assets/sprites/question3.png'),pygame.image.load('assets/sprites/question4.png'),
                             pygame.image.load('assets/sprites/question5.png'),pygame.image.load('assets/sprites/question6.png'),
                             pygame.image.load('assets/sprites/question7.png'),pygame.image.load('assets/sprites/question8.png')]}