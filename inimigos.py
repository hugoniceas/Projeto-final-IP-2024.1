import pygame
import random

pygame.init()

def pegar_valor_aleatorio_de_uma_tupla (tupla):

    numero = random.randint(0, (len(tupla)-1))

    return tupla[numero]
# classe do carro do jogador
class carro_jogador(object):
    # função construtora
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.velocidade = 0
        self.faixa = 4

    def acelerar(self):
        if self.velocidade < 20:  # velocidade máxima
            self.velocidade += 1

    def freiar(self):
        if self.velocidade > -20:
            self.velocidade -= 1

    def subir(self):  # sobe o carro em 1 faixa
        if self.faixa != 1:
            self.y -= 140
            self.faixa -= 1

    def descer(self):  # desce o carro em 1 faixa
        if self.faixa:
            if self.faixa != 4:
                self.y += 140
                self.faixa += 1

    def andar(self):
        if self.x >= 1300 and self.velocidade > 0:

            self.velocidade = 0

        elif self.x <= 50 and self.velocidade < 0:
            self.velocidade = 0

        self.x += self.velocidade

    def draw(self, win, sprite):  # desenha o carro na tela
        win.blit(sprite, (self.x, self.y))
        # pygame.draw.rect(win, (255,0,0), (self.x,self.y,self.largura,self.altura))



class obstaculos(object):

     #Velocidade, faixa e numero de obstaculos

    def __init__(self):

        self.faixas_possiveis = (560, 420, 280, 140)



        self.y = pegar_valor_aleatorio_de_uma_tupla(self.faixas_possiveis)



        if self.y == 560 or self.y == 420:
            self.x = pegar_valor_aleatorio_de_uma_tupla((-220, -440, -660))

        else:
            self.x = pegar_valor_aleatorio_de_uma_tupla((1720, 1940, 2160))



    def get_y(self):
        return self.y

    def get_x(self):
        return self.y
    def andar(self, velocidade_faixa):
        self.x += velocidade_faixa
    def draw(self, win, sprite):

        win.blit(sprite, (self.x, self.y))



class dificuldade(object):

    def __init__(self):
        self.dificuldade = 0
        self.contador_dificuldade = 0

    def get_dificuldade(self):
        return self.dificuldade

    def incrementar_dificuldade(self):
        self.contador_dificuldade += 0.7


    def atualizar_dificuldade(self):
        if self.contador_dificuldade < 1000:
            self.dificuldade = 0

        elif 2000 > self.contador_dificuldade > 1000:
            self.dificuldade = 1

        else:
            self.dificuldade = 2

    def draw(self, win, font):
        texto = font.render('Dificuldade: ' + str(int(self.dificuldade)), 1, (255, 0, 0))
        win.blit(texto, (1100, 50))






class placar(object):  # servirá como forma de guardar pontuação, voltas e quantidade de itens coletados
    # função construtora
    def __init__(self):
        self.metros = 0



    def incrementar_voltas(self):
        self.metros += 0.7

    def draw(self, win, font):
        texto = font.render('Metros: ' + str(int(self.metros)), 1, (255, 0, 0))
        win.blit(texto, (1200, 10))



def redraw_window():  # função para atualizar a tela
    win.blit(bg, (0, 0))
    player.draw(win, car_red)
    placar.draw(win, font)
    dificuldade_atual.draw(win, font)

    for obstaculo in faixa1:
        obstaculo.draw(win, car_blue_frente)
    for obstaculo in faixa2:
        obstaculo.draw(win, car_blue_frente)
    for obstaculo in faixa3:
        obstaculo.draw(win, car_blue_tras)
    for obstaculo in faixa4:
        obstaculo.draw(win, car_blue_tras)

    pygame.display.update()


# criação da janela
win = pygame.display.set_mode((1500, 800))

# nome da janela
pygame.display.set_caption("Jogo")

# clock principal
clock = pygame.time.Clock()

# fonte usada no placar
font = pygame.font.SysFont('arial', 50, True)

# instancia inicial do jogador
player = carro_jogador(0, 560, 200, 100)

# instancia do placar
placar = placar()

# instancia inicial da dificuldade
dificuldade_atual = dificuldade()


# delay de troca de faixa
delay_faixa = 0

#Temporizador obstáculos
timer_obstaculo = 0

# imagens
bg = pygame.image.load('bg.jpg')
car_red = pygame.image.load('car_red.png')
car_blue_tras = pygame.image.load('car_blue1.png')
car_blue_frente = pygame.image.load('car_blue2.png')


#Lista de obstaculos por faixa
faixa1 = []
faixa2 = []
faixa3 = []
faixa4 = []


velocidades_disponiveis = ((5, 7, 9), (11, 14, 17), (15, 18, 23))

# loop principal do jogo
running = True
while running:
    clock.tick(30)

    if delay_faixa > 0:
        delay_faixa += 1
    if delay_faixa == 4:
        delay_faixa = 0

    # sair da janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    timer_obstaculo += 1

    for obstaculo in faixa4:
        if obstaculo.get_x() > -220:
            obstaculo.andar(velocidade_das_faixas[3] * -1)
        else:
            faixa4.pop(faixa4.index(obstaculo))

    for obstaculo in faixa3:
        if obstaculo.get_x() > -220:
            obstaculo.andar(velocidade_das_faixas[2] * -1)
        else:
            faixa3.pop(faixa3.index(obstaculo))

    for obstaculo in faixa2:
        if obstaculo.get_x() < 1720:
            obstaculo.andar(velocidade_das_faixas[1])
        else:
            faixa2.pop(faixa2.index(obstaculo))

    for obstaculo in faixa1:
        if obstaculo.get_x() < 1720:
            obstaculo.andar(velocidade_das_faixas[0])
        else:
            faixa1.pop(faixa1.index(obstaculo))



    if timer_obstaculo >= 210:
        velocidade_das_faixas = []
        if dificuldade_atual.get_dificuldade() == 0:
            numero_carros = pegar_valor_aleatorio_de_uma_tupla((2,))
            for i in range (4):
               velocidade_das_faixas.append(pegar_valor_aleatorio_de_uma_tupla((8, 10, 13)))

        elif dificuldade_atual.get_dificuldade() == 1:
            numero_carros = pegar_valor_aleatorio_de_uma_tupla((4,))
            for i in range (4):
               velocidade_das_faixas.append(pegar_valor_aleatorio_de_uma_tupla((11, 14, 17)))
        else:
            numero_carros = pegar_valor_aleatorio_de_uma_tupla((6,))
            for i in range (4):
               velocidade_das_faixas.append(pegar_valor_aleatorio_de_uma_tupla((19, 21, 25)))



        for i in range(numero_carros):
            obstaculo_atual = obstaculos()
            if obstaculo_atual.get_y() == 560:
                faixa1.append(obstaculo_atual)

            elif obstaculo_atual.get_y() == 420:
                faixa2.append(obstaculo_atual)

            elif obstaculo_atual.get_y() == 280:
                faixa3.append(obstaculo_atual)

            else:
                faixa4.append(obstaculo_atual)




        timer_obstaculo = 0






    # checa quais teclas estão sendo pressionadas e realiza os respectivos comandos
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.freiar()
    if keys[pygame.K_RIGHT]:
        player.acelerar()
    if keys[pygame.K_UP] and delay_faixa == 0:
        player.subir()
        delay_faixa = 1
    if keys[pygame.K_DOWN] and delay_faixa == 0:
        player.descer()
        delay_faixa = 1

    player.andar()
    placar.incrementar_voltas()
    dificuldade_atual.incrementar_dificuldade()
    dificuldade_atual.atualizar_dificuldade()


    # atualiza a tela
    redraw_window()

pygame.quit()