import pygame
from game_state import GameState
class Loja(GameState):
    def __init__(self, run):
        super().__init__("Loja", run, '')

    def abrir_loja(self):
        pygame.init()
        clock = pygame.time.Clock()
        tela = pygame.display.set_mode((1500, 800))
        fonte = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 32)
        cadeado = pygame.image.load('assets/sprites/cadeado_fechado.png')
        cadeado_loja = pygame.transform.scale(cadeado, (cadeado.get_width() * 0.2, cadeado.get_height() * 0.2))
        skin_1 = pygame.image.load('assets/sprites/car_blue.png')
        skin_1_loja = pygame.transform.rotate(pygame.transform.scale(skin_1, (skin_1.get_width() * 0.8, skin_1.get_height() * 0.8)), 90)
        skin_2 = pygame.image.load('assets/sprites/car_yellow.png')
        skin_2_loja = pygame.transform.rotate(pygame.transform.scale(skin_2, (skin_2.get_width() * 0.8, skin_2.get_height() * 0.8)), 90)
        skin_3 = pygame.image.load('assets/sprites/car_white.png')
        skin_3_loja = pygame.transform.rotate(pygame.transform.scale(skin_3, (skin_3.get_width() * 0.8, skin_3.get_height() * 0.8)), 90)
        skin_4 = pygame.image.load('assets/sprites/car_gold.png')
        skin_4_loja = pygame.transform.rotate(pygame.transform.scale(skin_4, (skin_4.get_width() * 0.8, skin_4.get_height() * 0.8)), 90)
        while self.run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.set_run(False)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.set_run(False)
                        self.set_next_state('Menu')
            tela.fill((173, 223, 255))
            self.escrever_texto_opcoes('50', fonte, 100, 100 + (skin_1_loja.get_height()) + 25, tela)
            tela.blit(skin_1_loja, (100, 100))
            self.escrever_texto_opcoes('50', fonte, 300, 100 + (skin_2_loja.get_height()) + 25, tela)
            tela.blit(skin_2_loja, (300, 100))
            self.escrever_texto_opcoes('50', fonte, 500, 100 + (skin_3_loja.get_height()) + 25, tela)
            tela.blit(skin_3_loja, (500, 100))
            tela.blit(skin_4_loja, (700, 100))
            tela.blit(cadeado_loja, (701.5, 101.5))
            pygame.display.flip()


if __name__ == '__main__':
    loja = Loja(True)
    loja.abrir_loja()