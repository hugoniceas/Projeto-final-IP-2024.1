import pygame


bg = pygame.image.load('assets/bg.jpg')
car_red = pygame.image.load('assets/car_red.png')
car_green = pygame.image.load('assets/car_green.png')



items = {'ficha cassino':[pygame.image.load('assets/ficha1.png'),pygame.image.load('assets/ficha2.png'),
                        pygame.image.load('assets/ficha3.png'),pygame.image.load('assets/ficha4.png')],
           'moeda': [pygame.image.load('assets/coin_1.png'),pygame.image.load('assets/coin_2.png'),
                     pygame.image.load('assets/coin_3.png'),pygame.image.load('assets/coin_4.png'),
                     pygame.image.load('assets/coin_5.png'),pygame.image.load('assets/coin_6.png'),
                     pygame.image.load('assets/coin_7.png'),pygame.image.load('assets/coin_8.png')],
           'fantasma': [],
            'interrogacao': []}