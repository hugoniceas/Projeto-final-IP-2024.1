import menu_inicial
import loja
import cassino
from carro_atual import CarroAtual
from info_carro import InfoCarro
from jogo import jogo
from menu_fim_jogo import fim_jogo
from items import conta_jogador

def transicao(estado_atual, proximo_estado):
    global continuar_musica
    run = True
    if proximo_estado == 'Loja':
        loja.set_next_state('')
        if loja.get_next_state() == '':
            loja.set_run(True)
            estado_atual.set_run(False)
    if proximo_estado == 'Menu':
        menu.set_next_state('')
        if menu.get_next_state() == '':
            menu.set_run(True)
            estado_atual.set_run(False)
    if proximo_estado == 'Cassino':
        cassino.set_next_state('')
        if cassino.get_next_state() == '':
            cassino.set_run(True)
            estado_atual.set_run(False)
    if proximo_estado == 'Sair':
        run = False
    if proximo_estado == 'Jogo':
        jogo.set_next_state('')
        jogo.set_run(True)
        estado_atual.set_run(False)
    if proximo_estado == 'Fim':
        fim_jogo.set_next_state('')
        fim_jogo.set_run(True)
        estado_atual.set_run(False)
    if estado_atual.nome == 'Loja' or estado_atual.nome == 'Cassino':
        continuar_musica = True
    else:
        continuar_musica = False

    return run

conta = conta_jogador()
continuar_musica = False
menu = menu_inicial.MenuInicial(True)
loja = loja.Loja(False)
cassino = cassino.Cassino(False)
jogo = jogo('Jogo',False,'')
fim_jogo = fim_jogo('Fim',False,'')
carro_atual = CarroAtual()
info = InfoCarro()
run = True
while run:
    while menu.get_run():
        menu.abrir_menu(carro_atual,continuar_musica)
        prox = menu.get_next_state()
        if prox != '':
            run = transicao(menu, prox)

    while loja.get_run():

        loja.abrir_loja(carro_atual, info,conta)
        skin = carro_atual.skin
        prox = loja.get_next_state()
        if prox != '':
            run = transicao(loja, prox)

    while cassino.get_run():
        cassino.abrir_cassino(info,conta)
        prox = cassino.get_next_state()
        if prox != '':
            run = transicao(loja, prox)

    while jogo.get_run():
        jogo.abrir_jogo(carro_atual)
        prox = jogo.get_next_state()
        if prox != '':
            run = transicao(jogo, prox)

    while fim_jogo.get_run():
        fim_jogo.abrir_menu_fim(conta,False)
        prox = fim_jogo.get_next_state()
        if prox != '':
            run = transicao(fim_jogo, prox)
