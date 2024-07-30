import pygame
import inimigo_teste
import items
import sprites
import constantes

pygame.init()

#classe do carro do jogador
class carro_jogador(object):
    #função construtora
    def __init__(self,x,faixa,largura,altura):
        self.x = x
        self.y = constantes.faixas[faixa]
        self.largura = largura
        self.altura = altura
        self.velocidade = 1
        self.faixa = faixa

        #hitbox temporária para teste dos itens
        self.hitbox = (self.x,self.y,166,100)

    def acelerar(self):
        if self.velocidade <= 20: #velocidade máxima
            self.velocidade += 1

    def freiar(self):
        if self.velocidade > 1:
            self.velocidade -= 1

    def subir(self): #sobe o carro em 1 faixa
        if self.faixa != 1:
            self.y -= 140
            self.faixa -= 1

    def descer(self): #desce o carro em 1 faixa
        if self.faixa:
            if self.faixa != 4:
                self.y += 140
                self.faixa += 1

    def andar(self):
        self.x += self.velocidade
        if self.x >= 1500: #retorna para o começo caso o jogador complete uma volta
            self.x = -166

    def draw(self, win, sprite): #desenha o carro na tela

        #hitbox temporária
        self.hitbox = (self.x, self.y, 166, 100)
        #pygame.draw.rect(win, (0,0,255), self.hitbox,2)

        win.blit(sprite, (self.x, self.y))

def redraw_window(): #função para atualizar a tela
    win.blit(sprites.bg, (0, 0))
    player.draw(win,sprites.car_red)
    inimigo.draw(win,sprites.car_green)

    #loop que passará por todos os items que atualmente estão na tela e os atualizarão
    for item_type in items.current_items.keys():
        for item in items.current_items[item_type]:
            current_sprite_cycle = item.sprite_cycle #os sprites dos items são divididos em ciclos, para que o sprite apenas mude após x quantidade de frames
            frame_atual = current_sprite_cycle//item.cycle_step
            sprite = sprites.items[item_type][frame_atual]
            item.draw(win,sprite)

            if item.sprite_cycle == item.cycle_limit-1:
                item.reset_sprite_cyle()
            else:
                item.increment_sprite_cycle()

    pygame.display.update()


def checar_colisao(objeto1,objeto2): #função que checa colisão entre 2 objetos
    if objeto1.faixa == objeto2.faixa:
        if objeto1.x + objeto1.largura > objeto2.hitbox[0] and objeto1.x < objeto2.hitbox[0] + objeto2.hitbox[2]:
            return True
    return False

#criação da janela
win = pygame.display.set_mode((1500,800))

#nome da janela
pygame.display.set_caption("Jogo")

#clock principal
clock = pygame.time.Clock()

#instancia inicial do jogador
player = carro_jogador(0,4,166,100)

#instancia do inimigo usado para teste
inimigo = inimigo_teste.carro_inimigo(1000,4,166,100)

#ficha de cassino teste
ficha_teste = items.ficha_cassino(800,80,80,2)

#moeda teste
moeda_teste = items.moeda(400,64,64,2)

#delay de troca de faixa
delay_faixa = 0

#loop principal do jogo
running = True
while running:
    clock.tick(30)

    if delay_faixa > 0:
        delay_faixa += 1
    if delay_faixa == 4:
        delay_faixa = 0

    #sair da janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #comandos temporários de desenvolvimento
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print(items.quantidade)
            if event.key == pygame.K_f: #cria uma ficha de cassino
                items.current_items['ficha cassino'].append(ficha_teste)
            if event.key == pygame.K_m: #cria uma moeda
                items.current_items['moeda'].append(moeda_teste)

    #colisão do carro com inimigo
    if checar_colisao(player,inimigo):
        player.x = 0

    #colisão do carro com items
    for item_type in items.current_items.keys():
        for item in items.current_items[item_type]:
            if checar_colisao(player,item):
                items.current_items[item_type].remove(item)
                items.quantidade[item_type] += 1


    #checa quais teclas estão sendo pressionadas e realiza os respectivos comandos
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



    # movimenta o jogador a partir da velocidade e checa caso ele vá completar uma volta
    player.andar()

    #atualiza a tela
    redraw_window()


pygame.quit()