import pygame
from game_state import GameState
from carro_atual import CarroAtual
from info_carro import  InfoCarro
class Loja(GameState):
    def __init__(self, run):
        super().__init__("Loja", run, '')

    def abrir_loja(self, carro, info):
        def criar_skin_loja(skin):
            skin_loja = pygame.transform.rotate(pygame.transform.scale(skin, (skin.get_width() * 0.8, skin.get_height() * 0.8)), 90)
            return skin_loja

        pygame.init()
        skin_atual = carro.skin
        skin = pygame.image.load(skin_atual)
        clock = pygame.time.Clock()
        tela = pygame.display.set_mode((1500, 800))
        fonte = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 32)
        cadeado = pygame.image.load('assets/sprites/cadeado_fechado.png')
        cadeado_loja = pygame.transform.scale(cadeado, (cadeado.get_width() * 0.2, cadeado.get_height() * 0.2))
        skin_padrao = pygame.image.load('assets/sprites/car_red.png')
        skin_padrao_loja = criar_skin_loja(skin_padrao)
        skin_1 = pygame.image.load('assets/sprites/car_blue.png')
        skin_1_loja = criar_skin_loja(skin_1)
        skin_2 = pygame.image.load('assets/sprites/car_yellow.png')
        skin_2_loja = criar_skin_loja(skin_2)
        skin_3 = pygame.image.load('assets/sprites/car_white.png')
        skin_3_loja = criar_skin_loja(skin_3)
        skin_4 = pygame.image.load('assets/sprites/car_gold.png')
        skin_4_loja = criar_skin_loja(skin_4)
        x_y_cursor = [87.5, 87.5]
        posicao_cursor = 0
        cursor = pygame.Rect(87.5, 87.5, skin_1_loja.get_width() + 25, skin_1_loja.get_height() + 25)
        total_moedas = 100
        while self.run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.set_run(False)
                    self.set_next_state('Sair')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.set_run(False)
                        self.set_next_state('Menu')
                    if event.key == pygame.K_RIGHT and x_y_cursor[0] != 887.5:
                        x_y_cursor[0] += 200
                        posicao_cursor += 1
                        cursor = pygame.Rect(x_y_cursor, (skin_1_loja.get_width() + 25, skin_1_loja.get_height() + 25))
                    if event.key == pygame.K_LEFT and x_y_cursor[0] != 87.5:
                        x_y_cursor[0] -= 200
                        posicao_cursor -= 1
                        cursor = pygame.Rect(x_y_cursor, (skin_1_loja.get_width() + 25, skin_1_loja.get_height() + 25))
                    if event.key == pygame.K_SPACE:
                        if not info.get_comprou(posicao_cursor):
                            if total_moedas >= info.get_preco(posicao_cursor):
                                total_moedas -= info.get_preco(posicao_cursor)
                                if posicao_cursor != 4:
                                    info.set_comprou(posicao_cursor)
                        else:
                            carro.skin_setter(info.get_path(posicao_cursor))
                            skin = pygame.image.load(f'{carro.skin}')
                            tela.blit(skin, (500, 600))
            tela.fill((173, 223, 255))
            pygame.draw.rect(tela, (255, 122, 122), cursor)
            tela.blit(skin_padrao_loja, (100, 100))
            self.escrever_texto_opcoes(str(total_moedas), fonte, 100, 600, tela)
            if not info.get_comprou(1):
                self.escrever_texto_opcoes('50', fonte, 300, 100 + (skin_1_loja.get_height()) + 25, tela)
            tela.blit(skin_1_loja, (300, 100))
            if not info.get_comprou(2):
                self.escrever_texto_opcoes('50', fonte, 500, 100 + (skin_2_loja.get_height()) + 25, tela)
            tela.blit(skin_2_loja, (500, 100))
            if not info.get_comprou(3):
                self.escrever_texto_opcoes('50', fonte, 700, 100 + (skin_3_loja.get_height()) + 25, tela)
            tela.blit(skin_3_loja, (700, 100))
            tela.blit(skin_4_loja, (900, 100))
            if not info.get_comprou(4):
                tela.blit(cadeado_loja, (901.5, 101.5))
            tela.blit(skin, (500, 600))
            pygame.display.flip()


if __name__ == '__main__':
    loja = Loja(True)
    skin = CarroAtual()
    info = InfoCarro()
    loja.abrir_loja(skin, info)
