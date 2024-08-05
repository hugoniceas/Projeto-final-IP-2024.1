import pygame, sys
from BOTOES import Botao

pygame.init()
pygame.mixer.init()

def tocar_musica():
    pygame.mixer.music.load("musicas\\04 Bordeaux.mp3")
    pygame.mixer.music.play(-1)

def get_font(size):  # Retorna a fonte Press-Start-2P no tamanho desejado
    return pygame.font.Font("assets_mapa\\PressStart2P-Regular.ttf", size)

def estatisticas(tela,pontuacao, distancia, items_coletados):
    BG_ESTATISTIVAS = pygame.image.load("assets_mapa\\AnimatedStreet.png")

    while True:
        botao_pressionado = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if botao_pressionado[pygame.K_BACKSPACE]:
                pygame.display.update()
                menu_principal(tela, pontuacao)
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
                              text_input=f"-ITÉMS COLETADOS: {items_coletados}", font=get_font(25), base_color="Black")
        OPCOES_VOLTAR.update(tela)
        ESTATISTICA.update(tela)
        ESTATISTICA_PONTUACAO.update(tela)
        ESTATISTICA_DISTANCIA.update(tela)
        ESTATISTICA_ITEMS_COLETADOS.update(tela)

        pygame.display.update()
#foi adicionado a pontuacao no parametro para facilitar o acesso
def menu_principal(tela, pontuacao):
    botao_selecionado = 0
    tocar_musica()

    botoes = [
        Botao(image=pygame.image.load("assets_mapa\\Menu_inicial.png"), pos=(750, 290), 
              text_input="MENU INICIAL", font=get_font(75), base_color="#d7fcd4"),
        Botao(image=pygame.image.load("assets_mapa\\Sombra_Estatisticas.png"), pos=(750, 470), 
              text_input="ESTATÍSTICAS", font=get_font(80), base_color="#d7fcd4"),
        Botao(image=pygame.image.load("assets_mapa\\Sombra_Sair.png"), pos=(750, 620), 
              text_input="SAIR", font=get_font(80), base_color="#d7fcd4")
    ]

    while True:
        BG = pygame.image.load("assets_mapa\\back1.jpg")
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
                        pass #voltar ao menu inicial
                    elif botao_selecionado == 1: #aqui coloca as estatísticas do
                        #removi pontuacao (vai ser dado na chamada da funcao)
                        distancia = 0
                        items_coletados = 0
                        estatisticas (tela, pontuacao, distancia, items_coletados)
                    elif botao_selecionado == 2:
                        pygame.quit()
                        sys.exit()

        pygame.display.update()

