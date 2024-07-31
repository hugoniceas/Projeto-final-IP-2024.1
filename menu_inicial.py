import pygame
from game_state import GameState


class MenuInicial(GameState):
    def __init__(self, run):
        super().__init__('Menu', run, '')


    def abrir_menu(self):
        pygame.init()
        Clock = pygame.time.Clock()
        pygame.display.set_caption('Direção Perigosa')
        fonte_titulo = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 64)
        fonte_menu = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 32)
        plano_de_fundo = pygame.image.load("assets/backgrounds/bg.jpg")
        carro = pygame.image.load("assets/sprites/car_red.png")
        tamanho_cursor = (int(carro.get_width()) * 0.4, int(carro.get_height()) * 0.4)
        cursor = pygame.transform.flip(pygame.transform.scale(carro, tamanho_cursor), True, False)
        tela = pygame.display.set_mode((1500, 800))
        x_cursor = 550
        y_cursor = 348
        distancia_cursor = 20
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.set_run(False)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if y_cursor == 348:  # Jogar
                            self.set_run(False)
                            self.set_next_state('Jogo')
                        if y_cursor == 398:  # Cassino
                            self.set_run(False)
                            self.set_next_state('Cassino')
                        if y_cursor == 448:  # Loja
                            self.set_run(False)
                            self.set_next_state('Loja')
                        if y_cursor == 498:
                            self.set_run(False)
                            self.set_next_state('Configurações')
                        if y_cursor == 548:  # Sair
                            self.set_run(False)
                            self.set_next_state('Sair')
                    if event.key == pygame.K_UP:
                        if y_cursor != 348:
                            y_cursor -= 50
                    if event.key == pygame.K_DOWN:
                        if y_cursor != 548:
                            y_cursor += 50
            titulo = fonte_titulo.render('Direção Perigosa', True, (255, 255, 255))
            sombra_titulo = fonte_titulo.render('Direção Perigosa', True, (0, 0, 0))
            Clock.tick(60)
            if y_cursor == 348:
                x_cursor = 305 + pygame.font.Font.size(fonte_menu, 'Dirigir')[0] + distancia_cursor
            if y_cursor == 398:
                x_cursor = 305 + pygame.font.Font.size(fonte_menu, 'Cassino')[0] + distancia_cursor
            if y_cursor == 448:
                x_cursor = 305 + pygame.font.Font.size(fonte_menu, 'Loja')[0] + distancia_cursor
            if y_cursor == 498:
                x_cursor = 305 + pygame.font.Font.size(fonte_menu, 'Configurações')[0] + distancia_cursor
            if y_cursor == 548:
                x_cursor = 305 + pygame.font.Font.size(fonte_menu, 'Sair')[0] + distancia_cursor
            tela.blit(plano_de_fundo, (0, 0))
            tela.blit(sombra_titulo, (240, 205))
            tela.blit(titulo, (250, 200))
            self.escrever_texto_opcoes('Dirigir', fonte_menu, 305, 348, tela)
            self.escrever_texto_opcoes('Cassino', fonte_menu, 305, 398, tela)
            self.escrever_texto_opcoes('Loja', fonte_menu, 305, 448, tela)
            self.escrever_texto_opcoes('Configurações', fonte_menu, 305, 498, tela)
            self.escrever_texto_opcoes('Sair', fonte_menu, 305, 548, tela)
            tela.blit(cursor, (x_cursor, y_cursor))
            pygame.display.flip()

if __name__ == '__main__':
    menu = MenuInicial(True)
    menu.abrir_menu()