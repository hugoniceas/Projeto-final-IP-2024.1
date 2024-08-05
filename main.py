import pygame
from sys import exit
import menu_fim_jogo
import inimigo_teste
import items
import sprites
import constantes
import random
from pontuacao_items import verificaçao

pistas = [1, 2, 3, 4]

pygame.init()

tela = pygame.display.set_mode((1500, 800))
sprite = pygame.image.load('assets_mapa\\bg.jpg')

# Adicionando cenários
grama = pygame.image.load('assets_mapa\\grama.png')
areia = pygame.image.load('assets_mapa\\areia.png')
lava = pygame.image.load('assets_mapa\\lava.png')
grama_velha = pygame.image.load('assets_mapa\\grama_velha.png')

# Organiza os cenários em ordem
cenarios = [grama, grama_velha, areia, lava]

# Define o cenário inicial
cenario_atual = cenarios[0]

class Background(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x * self.rect.width, 0)

    def update(self, velocidade):
        self.rect.x -= 10 + velocidade
        if self.rect.right <= 0:
            self.rect.x += self.rect.width * 2

class Cenario(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x * self.rect.width, pos_y)
    
    def update(self, velocidade):
        self.rect.x -= 10 + velocidade
        if self.rect.right <= 0:
            self.rect.x += self.rect.width * 2

    def change_image(self, new_image):
        self.image = new_image
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

todas_sprites = pygame.sprite.Group()
grass_sprites = pygame.sprite.Group()

# Cria o cenário acima e abaixo da pista
for indice_cenario in range(2):
    pista = Background(indice_cenario)
    todas_sprites.add(pista)
    grass_top = Cenario(indice_cenario, 0, cenario_atual)
    grass_bottom = Cenario(indice_cenario, 680, cenario_atual)
    todas_sprites.add(grass_top)
    todas_sprites.add(grass_bottom)
    grass_sprites.add(grass_top)
    grass_sprites.add(grass_bottom)

relogio = pygame.time.Clock()
velocidade = 0

# Variáveis auxiliares da pontuação
indice_cenario = 0 # Variável de troca de cenário
tempo_de_troca = 45 # Tempo para trocar o primeiro cenário
tempo_vivo = 0.0 # Tempo de incrementação da pontuação
pontuacao_game = 0 # Pontuação

fonte = pygame.font.Font(None, 36) # Fonte da pontuação

# Classe do carro do jogador
class carro_jogador(object):
    def __init__(self, x, faixa, largura, altura):
        self.x = x
        self.y = constantes.faixas[faixa]
        self.largura = largura
        self.altura = altura
        self.velocidade = 1
        self.faixa = faixa
        self.hitbox = (self.x, self.y, 166, 100)

    def acelerar(self):
        if self.velocidade <= 20: # Velocidade máxima
            self.velocidade += 1

    def freiar(self):
        if self.velocidade > 1:
            self.velocidade -= 1

    def subir(self): # Sobe o carro em 1 faixa
        if self.faixa != 1:
            self.y -= 140
            self.faixa -= 1

    def descer(self): # Desce o carro em 1 faixa
        if self.faixa:
            if self.faixa != 4:
                self.y += 140
                self.faixa += 1

    def andar(self):
        self.x += self.velocidade
        if self.x >= 1500: # Retorna para o começo caso o jogador complete uma volta
            self.x = -166

    def draw(self, win, sprite): # Desenha o carro na tela
        self.hitbox = (self.x, self.y, 166, 100)
        win.blit(sprite, (self.x, self.y))

def redraw_window(): # Função para atualizar a tela
    tela.fill((255, 255, 255))
    todas_sprites.draw(tela)
    player.draw(tela, sprites.car_red)
    inimigo.draw(tela, sprites.car_green)

    for item_type in items.current_items.keys():
        for item in items.current_items[item_type]:
            current_sprite_cycle = item.sprite_cycle
            frame_atual = current_sprite_cycle // item.cycle_step
            sprite = sprites.items[item_type][frame_atual]
            item.draw(tela, sprite)

            if item.sprite_cycle == item.cycle_limit - 1:
                item.reset_sprite_cyle()
            else:
                item.increment_sprite_cycle()

    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao_game}", True, pygame.Color("white"))
    tela.blit(texto_pontuacao, (1250, 10))
    pygame.display.update()

def checar_colisao(objeto1, objeto2): # Função que checa colisão entre 2 objetos
    if objeto1.faixa == objeto2.faixa:
        if objeto1.x + objeto1.largura > objeto2.hitbox[0] and objeto1.x < objeto2.hitbox[0] + objeto2.hitbox[2]:
            return True
    return False

# Criação da janela
pygame.display.set_caption("Jogo")
player = carro_jogador(0, 4, 166, 100)
inimigo = inimigo_teste.carro_inimigo(1000, 4, 166, 100)

# Delay de troca de faixa
delay_faixa = 0

# Loop principal do jogo
running = True
while running:
    relogio.tick(60)

    if delay_faixa > 0:
        delay_faixa += 1
    if delay_faixa == 4:
        delay_faixa = 0

    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            running = False
        elif eventos.type == pygame.KEYDOWN:
            if eventos.key == pygame.K_e:
                running = False
            elif eventos.key == pygame.K_UP and delay_faixa == 0:
                player.subir()
                delay_faixa = 1
            elif eventos.key == pygame.K_DOWN and delay_faixa == 0:
                player.descer()
                delay_faixa = 1
            elif eventos.key == pygame.K_q:
                print(items.quantidade)
            elif eventos.key == pygame.K_f:  # Cria uma ficha de cassino
                items.current_items['ficha cassino'].append(items.criar_items('ficha cassino', random.choice(pistas)))
            elif eventos.key == pygame.K_m:  # Cria uma moeda
                items.current_items['moeda'].append(items.criar_items('moeda', random.choice(pistas)))
            elif eventos.key == pygame.K_g:  # Cria um fantasma
                items.current_items['fantasma'].append(items.criar_items('fantasma', random.choice(pistas)))
            elif eventos.key == pygame.K_i:  # Cria uma interrogação
                items.current_items['interrogacao'].append(items.criar_items('interrogacao', random.choice(pistas)))

    botao_pressionado = pygame.key.get_pressed()

    if botao_pressionado[pygame.K_RIGHT]:
        velocidade += 2
        player.acelerar()
    if botao_pressionado[pygame.K_LEFT]:
        if velocidade > 0:
            velocidade -= 1
        player.freiar()

    if pontuacao_game % tempo_de_troca == 0 and pontuacao_game != 0:
        if indice_cenario == 3:
            cenario_atual = cenarios[0]
            indice_cenario = 0
        else:
            cenario_atual = cenarios[indice_cenario + 1]
            indice_cenario += 1

        for grass_sprite in grass_sprites:
            grass_sprite.change_image(cenario_atual)
        tempo_de_troca += 45

    tempo_vivo += relogio.get_time() / 1000.0
    
    if tempo_vivo >= 1.0:
        pontuacao_game += 1
        tempo_vivo = 0.0

    if checar_colisao(player, inimigo):
        player.x = 0
        menu_fim_jogo.menu_principal(tela, pontuacao_game)

    for item_type in items.current_items.keys():
        for item in items.current_items[item_type]:
            if checar_colisao(player, item):
                print(pontuacao_game, type(item))
                pontuacao_game = verificaçao(pontuacao_game, item_type)
                items.current_items[item_type].remove(item)
                items.quantidade[item_type] += 1
                print(pontuacao_game)

    player.andar()
    todas_sprites.update(velocidade)
    redraw_window()

pygame.quit()
exit()
