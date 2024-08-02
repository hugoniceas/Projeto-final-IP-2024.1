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
        self.velocidade = 20
        self.faixa = faixa

        #hitbox temporária para teste dos itens
        self.hitbox = (self.x,self.y,166,100)

    def subir(self): #sobe o carro em 1 faixa
        if self.faixa != 1:
            self.y -= 140
            self.faixa -= 1

    def descer(self): #desce o carro em 1 faixa
        if self.faixa:
            if self.faixa != 4:
                self.y += 140
                self.faixa += 1

    def progredir(self):
        if self.x + self.velocidade <= 1334:
            self.x += self.velocidade
        else:
            self.x = 1334

    def voltar(self):
        if self.x - self.velocidade >= 0:
            self.x -= self.velocidade
        else:
            self.x = 0

    def draw(self, win, sprite): #desenha o carro na tela

        #hitbox temporária
        self.hitbox = (self.x, self.y, 166, 100)
        #pygame.draw.rect(win, (0,0,255), self.hitbox,2)

        win.blit(sprite, (self.x, self.y))



def redraw_window(): #função para atualizar a tela
    win.blit(sprites.bg, (0, 0))
    player.draw(win,sprites.car_red)

    #loop que passará por todos os inimigos que estão na tela e os atualizarão
    for inimigo in inimigos:
        if not fantasma_ativo:
            inimigo.draw(win,sprites.car_green)
        else: #faz os inimigos piscarem caso fantasma esteja ativo
            if tempo_segundos%2 == 1:
                inimigo.draw(win, sprites.car_green)

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

    if timer != "":
        timer.draw(win, fonte)

    pygame.display.update()


def checar_colisao(objeto1,objeto2,fantasma_ativo,tipo_objeto): #função que checa colisão entre 2 objetos
    if tipo_objeto == "inimigo":
        if objeto1.faixa == objeto2.faixa and not fantasma_ativo:
            if objeto1.x + objeto1.largura > objeto2.hitbox[0] and objeto1.x < objeto2.hitbox[0] + objeto2.hitbox[2]:
                return True
        return False
    else:
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
inimigos = []
inimigo = inimigo_teste.carro_inimigo(1000,4,166,100)
inimigos.append(inimigo)

#ficha de cassino teste
ficha_teste = items.ficha_cassino(800,80,80,2)

#moeda teste
moeda_teste = items.moeda(400,64,64,2)

#fantasma teste
fantasma_teste = items.fantasma(600,56,100,1)

#interrogacao teste
interrogacao_teste = items.interrogacao(500,32,100,3)

#variavel reservada ao timer dos items
timer = ''


#flags de detecção se os interrogacao ou fantasma estão ativos
fantasma_ativo = False
interrogacao_ativo = False

#loop principal do jogo
running = True
while running:
    clock.tick(30)


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
            if event.key == pygame.K_g: #cria um fantasma
                items.current_items['fantasma'].append(fantasma_teste)
            if event.key == pygame.K_i: #cria uma interrogação
                items.current_items['interrogacao'].append(interrogacao_teste)
            if event.key == pygame.K_x:
                print(player.x)

            #comandos de troca de faixa
            if event.key == pygame.K_DOWN and not interrogacao_ativo:
                player.descer()
            elif event.key == pygame.K_DOWN and interrogacao_ativo:
                player.subir()

            if event.key == pygame.K_UP and not interrogacao_ativo:
                player.subir()
            elif event.key == pygame.K_UP and interrogacao_ativo:
                player.descer()




    #colisão do carro com inimigo
    if checar_colisao(player,inimigo,fantasma_ativo,'inimigo'):
        player.x = 0

    #colisão do carro com items
    for item_type in items.current_items.keys():
        for item in items.current_items[item_type]:
            if checar_colisao(player,item,fantasma_ativo,'item'):
                item.hit()
                items.current_items[item_type].remove(item)
                items.quantidade[item_type] += 1
                if item_type == 'fantasma':
                    fantasma_ativo = True
                    tempo_ativacao = pygame.time.get_ticks()
                elif item_type == 'interrogacao':
                    interrogacao_ativo = True
                    tempo_ativacao = pygame.time.get_ticks()


    #timer dos items
    if fantasma_ativo or interrogacao_ativo:
        tempo_atual = pygame.time.get_ticks()
        tempo_segundos = (tempo_atual - tempo_ativacao) // 1000
        fonte = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 32)
        #cria a instancia do timer ou altera o seu valor
        if timer == "":
            timer = items.timer_items()
        else:
            timer.alterar_tempo(15-tempo_segundos)

    #15 segundos de item ativo
        if tempo_segundos == 15:
            fantasma_ativo = False
            interrogacao_ativo = False
            timer = ''


    #checa quais teclas estão sendo pressionadas e realiza os respectivos comandos
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and not interrogacao_ativo:
        player.voltar()
    elif keys[pygame.K_LEFT] and interrogacao_ativo:
        player.progredir()

    if keys[pygame.K_RIGHT] and not interrogacao_ativo:
        player.progredir()
    elif keys[pygame.K_RIGHT] and interrogacao_ativo:
        player.voltar()




    #atualiza a tela
    redraw_window()


pygame.quit()