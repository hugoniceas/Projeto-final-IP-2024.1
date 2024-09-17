from game_state import GameState
import pygame
import random
from info_carro import InfoCarro
class Cassino(GameState):
    def __init__(self, run):
        super().__init__('Cassino', run, '')

    def abrir_cassino(self, info):
        def girar_roleta(frame_atual):
            proximo = 0
            mensagem = ''
            if frame_atual >= 31:
                proximo = frame_atual % 31
            else:
                proximo = frame_atual + 1
            if proximo < 10:
                mensagem = '0' + str(proximo)
            else:
                mensagem = str(proximo)
            return mensagem

        def criar_retangulo(cor, coordenada_x, coordenada_y, largura, altura, tela):
            retangulo = pygame.Rect(coordenada_x, coordenada_y, largura, altura)
            pygame.draw.rect(tela, cor, retangulo)


        pygame.init()
        clock = pygame.time.Clock()
        carro_cassino = pygame.image.load('assets/sprites/car_gold.png')
        carro_cassino_escala = pygame.transform.scale(carro_cassino, (83, 50))
        fonte = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 32)
        tela = pygame.display.set_mode((1500, 800))
        roleta = pygame.image.load("assets/sprites/roleta/frame_00_delay-0.02s.jpg")
        roleta_tela = pygame.transform.scale(roleta, (800, 800))
        total_moedas = 100
        fichas_cassino = 2
        roda = False
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.set_run(False)
                    self.set_next_state('Sair')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if fichas_cassino > 0:
                            fichas_cassino -= 1
                            roda = True
                        elif total_moedas >= 50:
                            roda = True
                            total_moedas -= 50
                    if event.key == pygame.K_ESCAPE:
                        self.set_next_state('Menu')
                        self.set_run(False)
            tela.fill((0, 0, 0))
            tela.blit(roleta_tela, (350, 0))
            self.escrever_texto_opcoes(str(total_moedas), fonte, 1300, 700, tela)
            self.escrever_texto_opcoes(str(fichas_cassino), fonte, 1300, 600, tela)
            # Laranja (Casa 7)
            criar_retangulo((246, 118, 34), 1325, 425, 100, 100, tela)
            self.escrever_texto_opcoes('150', fonte, 1325, 450, tela)

            # Amarelo (Casa 6)
            criar_retangulo((254, 174, 53), 75, 300, 100, 100, tela)
            self.escrever_texto_opcoes('50', fonte, 100, 325, tela)

            #Vermelho (Casa 0)
            criar_retangulo((228, 59, 68), 1325, 300, 100, 100, tela)
            self.escrever_texto_opcoes('0', fonte, 1350, 325, tela)

            # Verde escuro (Casa 5)
            criar_retangulo((38, 92, 66), 75, 425, 100, 100, tela)
            self.escrever_texto_opcoes('0', fonte, 100, 450, tela)

            # Verde claro (Casa 4)
            criar_retangulo((99, 199, 77), 75, 50, 100, 100, tela)
            self.escrever_texto_opcoes('0', fonte, 100, 75, tela)

            # Azul (Casa 3)
            criar_retangulo((18, 78, 138), 75, 175, 100, 100, tela)
            self.escrever_texto_opcoes('50', fonte, 100, 200, tela)

            # Roxo (Casa 2)
            criar_retangulo((104, 56, 108), 1325, 50, 100, 100, tela)
            self.escrever_texto_opcoes('0', fonte, 1350, 75, tela)
            # Branco (Casa 1)
            criar_retangulo((225, 225, 225), 1325, 175, 100, 100, tela)
            if info.get_comprou(4):
                self.escrever_texto_opcoes('150', fonte, 1325, 200, tela)
            else:
                tela.blit(carro_cassino_escala, (1335, 200))
            pygame.display.flip()

            if roda:
                pygame.display.flip()
                pygame.time.wait(10)
                for i in range(63):
                    roleta = pygame.image.load(f"assets/sprites/roleta/frame_{girar_roleta(i)}_delay-0.02s.jpg")
                    roleta_tela = pygame.transform.scale(roleta, (800, 800))
                    pygame.time.delay(1)
                    tela.blit(roleta_tela, (350, 0))
                    pygame.display.flip()
                for i in range(31):
                    roleta = pygame.image.load(f"assets/sprites/roleta/frame_{girar_roleta(i)}_delay-0.02s.jpg")
                    roleta_tela = pygame.transform.scale(roleta, (800, 800))
                    pygame.time.delay(10)
                    tela.blit(roleta_tela, (350, 0))
                    pygame.display.flip()
                casa = random.randint(0, 7)
                for n in range(3 + (4 * casa)):
                    roleta = pygame.image.load(f"assets/sprites/roleta/frame_{girar_roleta(n)}_delay-0.02s.jpg")
                    roleta_tela = pygame.transform.scale(roleta, (800, 800))
                    pygame.time.delay(20)
                    tela.blit(roleta_tela, (350, 0))
                    pygame.display.flip()

                if casa == 0:
                    criar_retangulo((0, 0, 0), 352.5, 587.5, 810, 110, tela)
                    criar_retangulo((228, 59, 68), 355, 590, 800, 100, tela)
                    self.escrever_texto_opcoes('Que pena...', fonte, 400, 600, tela)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                elif casa == 1:
                    criar_retangulo((0, 0, 0), 352.5, 587.5, 810, 110, tela)
                    criar_retangulo((210, 210, 210), 355, 590, 800, 100, tela)
                    if not info.get_comprou(4):
                        info.set_comprou(4)
                        self.escrever_texto_opcoes('Você ganhou um carro novo', fonte, 360, 600, tela)
                    else:
                        total_moedas += 150
                        self.escrever_texto_opcoes('Você ganhou 150', fonte, 500, 600, tela)
                    pygame.display.flip()
                    pygame.time.wait(2000)

                elif casa == 2:
                    criar_retangulo((0, 0, 0), 352.5, 587.5, 810, 110, tela)
                    criar_retangulo((104, 56, 108), 355, 590, 800, 100, tela)
                    self.escrever_texto_opcoes('Que pena...', fonte, 400, 600, tela)
                    pygame.display.flip()
                    pygame.time.wait(2000)

                elif casa == 3:
                    criar_retangulo((0, 0, 0), 352.5, 587.5, 810, 110, tela)
                    criar_retangulo((18, 78, 138), 355, 590, 800, 100, tela)
                    total_moedas += 50
                    self.escrever_texto_opcoes('Você ganhou 50', fonte, 500, 600, tela)
                    pygame.display.flip()
                    pygame.time.wait(2000)

                elif casa == 4:
                    criar_retangulo((0, 0, 0), 352.5, 587.5, 810, 110, tela)
                    criar_retangulo((99, 199, 77), 355, 590, 800, 100, tela)
                    self.escrever_texto_opcoes('Que pena...', fonte, 400, 600, tela)
                    pygame.display.flip()
                    pygame.time.wait(2000)

                elif casa == 5:
                    criar_retangulo((0, 0, 0), 352.5, 587.5, 810, 110, tela)
                    criar_retangulo((38, 92, 66), 355, 590, 800, 100, tela)
                    self.escrever_texto_opcoes('Que pena...', fonte, 400, 600, tela)
                    pygame.display.flip()
                    pygame.time.wait(2000)

                elif casa == 6:
                    criar_retangulo((0, 0, 0), 352.5, 587.5, 810, 110, tela)
                    criar_retangulo((254, 174, 53), 355, 590, 800, 100, tela)
                    total_moedas += 50
                    self.escrever_texto_opcoes('Você ganhou 50', fonte, 500, 600, tela)
                    pygame.display.flip()
                    pygame.time.wait(2000)

                elif casa == 7:
                    total_moedas += 150
                    criar_retangulo((0, 0, 0), 352.5, 587.5, 810, 110, tela)
                    criar_retangulo((246, 118, 34), 355, 590, 800, 100, tela)
                    self.escrever_texto_opcoes('Você ganhou 150', fonte, 500, 600, tela)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                roda = False


if __name__ == '__main__':
    cassino = Cassino(True)
    info = InfoCarro()
    cassino.abrir_cassino(info)
