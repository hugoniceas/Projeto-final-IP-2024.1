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
           'fantasma': [pygame.image.load('assets/ghost1.png'),pygame.image.load('assets/ghost2.png'),
                        pygame.image.load('assets/ghost3.png'),pygame.image.load('assets/ghost4.png'),
                        pygame.image.load('assets/ghost5.png'),pygame.image.load('assets/ghost6.png'),
                        pygame.image.load('assets/ghost7.png'),pygame.image.load('assets/ghost8.png')],
            'interrogacao': [pygame.image.load('assets/question1.png'),pygame.image.load('assets/question2.png'),
                             pygame.image.load('assets/question3.png'),pygame.image.load('assets/question4.png'),
                             pygame.image.load('assets/question5.png'),pygame.image.load('assets/question6.png'),
                             pygame.image.load('assets/question7.png'),pygame.image.load('assets/question8.png')]}