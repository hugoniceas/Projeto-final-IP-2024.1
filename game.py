import menu_inicial
import loja
import cassino
from carro_atual import CarroAtual
from info_carro import InfoCarro
def transicao(estado_atual, proximo_estado):
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
    return run

menu = menu_inicial.MenuInicial(True)
loja = loja.Loja(False)
cassino = cassino.Cassino(False)
carro_atual = CarroAtual()
info = InfoCarro()
run = True
while run:
    while menu.get_run():
        menu.abrir_menu(carro_atual, info)
        prox = menu.get_next_state()
        if prox != '':
            run = transicao(menu, prox)

    while loja.get_run():
        loja.abrir_loja(carro_atual, info)
        skin = carro_atual.skin
        prox = loja.get_next_state()
        if prox != '':
            run = transicao(loja, prox)

    while cassino.get_run():
        cassino.abrir_cassino(info)
        prox = cassino.get_next_state()
        if prox != '':
            run = transicao(loja, prox)