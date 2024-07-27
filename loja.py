import pygame
from game_state import GameState
class Loja(GameState):
    def __init__(self, run):
        super().__init__("Loja", run, '')

    def abrir_loja(self):
        tela = pygame.display.set_mode((1500, 800))
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.set_run(False)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.set_run(False)
                        self.set_next_state('Menu')
            tela.fill((0, 0, 0))
