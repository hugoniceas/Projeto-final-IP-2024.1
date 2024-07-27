import menu_inicial
import loja


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
    if proximo_estado == 'Sair':
        run = False
    return run

menu = menu_inicial.MenuInicial(True)
loja = loja.Loja(False)
run = True
while run:
    while menu.get_run():
        menu.abrir_menu()
        prox = menu.get_next_state()
        if prox != '':
            run = transicao(menu, prox)

    while loja.get_run():
        loja.abrir_loja()
        prox = loja.get_next_state()
        if prox != '':
            run = transicao(loja, prox)
