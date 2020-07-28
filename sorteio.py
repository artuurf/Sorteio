import random


def sorteio():
    """Execute e coloco os nomes que irão participar, em seguida tecle enter"""
    i = []
    ganhador = []
    while i != 'sair':
        i = input('Sorteio, escreva os nomes que vão sortear ou tecle enter: ')
        if i == '':
            return random.choice(ganhador)
        ganhador.append(i.strip().title())

    ganhador.remove('sair' or '')
    return random.choice(ganhador)


print(f'O escolhido foi: {sorteio()}')
