import pygame, sys
from BOTOES import Botao
import items
from game_state import GameState
import info_estatisticas

class fim_jogo(GameState):
    def __init__(self,nome,run,proximo_estado):
        super().__init__(nome,run,proximo_estado)

    def abrir_menu_fim(self,conta,ja_abriu):
        pygame.init()
        pygame.mixer.init()

        tela = pygame.display.set_mode((1500, 800))
        pygame.display.set_caption("Jogo")

        fichas = items.quantidade['ficha cassino']
        moedas = items.quantidade['moeda']

        if not ja_abriu:
            conta.depositar_dinheiro(moedas)
            conta.depositar_fichas(fichas)




        def get_font(size):  # Retorna a fonte Press-Start-2P no tamanho desejado
            return pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", size)

        def estatisticas(tela,pontuacao, distancia, items_coletados,moedas,fantasmas,interrogacoes,fichas):
            BG_ESTATISTIVAS = pygame.image.load("assets/backgrounds/AnimatedStreet.png")

            while self.run:
                botao_pressionado = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if botao_pressionado[pygame.K_BACKSPACE]:
                        pygame.display.update()
                        self.abrir_menu_fim(conta,True)
                tela.blit(BG_ESTATISTIVAS, (0,0))

                ESTATISTICA = Botao(image=None, pos=(650, 100),
                                      text_input="ESTATÍSTICAS DO JOGO:", font=get_font(55), base_color="Purple")
                OPCOES_VOLTAR = Botao(image=None, pos=(750, 660),
                                      text_input="CLICK EM BACKSPACE PARA VOLTAR", font=get_font(25), base_color="Black")
                ESTATISTICA_PONTUACAO = Botao(image=None, pos=(290, 160),
                                      text_input=f"-PONTUAÇÃO: {pontuacao}", font=get_font(25), base_color="Black")
                ESTATISTICA_DISTANCIA = Botao(image=None, pos=(290, 220),
                                      text_input=f"-DISTÂNCIA: {distancia}", font=get_font(25), base_color="Black")
                ESTATISTICA_ITEMS_COLETADOS = Botao(image=None, pos=(365, 280),
                                      text_input=f"-ITENS COLETADOS: {items_coletados}", font=get_font(25), base_color="Black")
                ESTATISTICA_MOEDAS_COLETADOS = Botao(image=None, pos=(365, 340),
                                                    text_input=f"-MOEDAS COLETADAS: {moedas}", font=get_font(25),
                                                    base_color="Black")
                ESTATISTICA_FANTASMAS_COLETADOS = Botao(image=None, pos=(420, 400),
                                                     text_input=f"-FANTASMAS COLETADOS: {fantasmas}", font=get_font(25),
                                                     base_color="Black")
                ESTATISTICA_INTERROGACOES_COLETADAS = Botao(image=None, pos=(440, 460),
                                                        text_input=f"-INTERROGACOES COLETADAS: {interrogacoes}", font=get_font(25),
                                                        base_color="Black")
                ESTATISTICA_FICHAS_COLETADAS = Botao(image=None, pos=(365, 520),
                                                        text_input=f"-FICHAS COLETADAS: {fichas}", font=get_font(25),
                                                        base_color="Black")
                OPCOES_VOLTAR.update(tela)
                ESTATISTICA.update(tela)
                ESTATISTICA_PONTUACAO.update(tela)
                ESTATISTICA_DISTANCIA.update(tela)
                ESTATISTICA_ITEMS_COLETADOS.update(tela)
                ESTATISTICA_MOEDAS_COLETADOS.update(tela)
                ESTATISTICA_FANTASMAS_COLETADOS.update(tela)
                ESTATISTICA_INTERROGACOES_COLETADAS.update(tela)
                ESTATISTICA_FICHAS_COLETADAS.update(tela)


                pygame.display.update()


        botao_selecionado = 0

        botoes = [
            Botao(image=pygame.image.load("assets/sprites/Menu_inicial.png"), pos=(750, 290),
                  text_input="MENU INICIAL", font=get_font(75), base_color="#d7fcd4"),
            Botao(image=pygame.image.load("assets/sprites/Sombra_Estatisticas.png"), pos=(750, 470),
                  text_input="ESTATÍSTICAS", font=get_font(80), base_color="#d7fcd4"),
            Botao(image=pygame.image.load("assets/sprites/Sombra_Sair.png"), pos=(750, 620),
                  text_input="SAIR", font=get_font(80), base_color="#d7fcd4")
        ]

        if not ja_abriu:
            som_batida = pygame.mixer.Sound("assets/audios/batida.mp3")
            som_batida.play()

        while self.run:
            BG = pygame.image.load("assets/backgrounds/back1.jpg")
            tela.blit(BG, (0, 0))

            MENU_TEXTO = get_font(120).render("VOCÊ BATEU!", True, "Red")
            MENU_RECT = MENU_TEXTO.get_rect(center=(750, 100))

            tela.blit(MENU_TEXTO, MENU_RECT)

            for i, botao in enumerate(botoes):
                if i == botao_selecionado:
                    botao.mudarCorBase("Black")
                else:
                    botao.mudarCorBase(botao.base_color)
                botao.update(tela)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        botao_selecionado = (botao_selecionado - 1) % len(botoes)
                    if event.key == pygame.K_DOWN:
                        botao_selecionado = (botao_selecionado + 1) % len(botoes)
                    if event.key == pygame.K_RETURN:
                        if botao_selecionado == 0:
                            self.set_next_state('Menu')
                            self.set_run(False)
                        elif botao_selecionado == 1: #aqui coloca as estatísticas do
                            pontuacao = info_estatisticas.pontuacao_game
                            distancia = info_estatisticas.distancia
                            items_coletados = sum(items.quantidade.values())
                            fantasmas = items.quantidade['fantasma']
                            interrogacoes = items.quantidade['interrogacao']


                            estatisticas (tela, pontuacao, distancia, items_coletados,moedas,fantasmas,interrogacoes,fichas)
                        elif botao_selecionado == 2:
                            pygame.quit()
                            sys.exit()

            pygame.display.update()

