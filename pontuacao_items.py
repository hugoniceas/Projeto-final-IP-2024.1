import random
bonus=15
multiplicadores = [0, 2, 3]
def verificaçao(pontuacao, type_item=str()):
    if type_item == 'moeda':
        return(pontuacao + bonus)
    elif type_item=='interrogacao':
        return(random.choice(multiplicadores))
    else:
        return pontuacao