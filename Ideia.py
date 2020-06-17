from random import choice
from time import sleep
pos = ['posa', 'posb', 'posc', 'posd', 'pose', 'posf', 'posg', 'posh', 'posj']
local = {'posa': ['A', 'B', 'D'], 'posb': ['B', 'A', 'C'],
         'posc': ['C', 'B'], 'posd': ['D', 'A', 'E'],
         'pose': ['E', 'D', 'I'], 'posf': ['F', 'I', 'J'],
         'posg': ['G', 'H'], 'posh': ['H', 'G', 'I', 'J'],
         'posi': ['I', 'E', 'F', 'H'], 'posj': ['J', 'F', 'H']}


def esconder(lugarob, lugarjog):
    objeto = lugarob[:]
    for c in lugarjog:
        if c in lugarob:
            objeto.remove(c)
    print(lugarob)
    print(lugarjog)
    print(objeto)
    return objeto


def procurar():
    print(f'Você está na posição {posatual}.')
    print(f'Você pode ir até {posatual}')


'''print('Seja bem vindo ao hided!')
while True:
    nome = input('Digite seu nome: ')
    while True:
        confirma = str(input(f'Seu nome será {nome}, correto? [s/n] ')).upper()
        if confirma in ['S', 'N']:
            break
        else:
            print('Você digitou um caractere inválido! Por favor, digite "s" para sim ou "n" para não.')
    if confirma == 'S':
        break'''

inicial = choice(pos)
posobjeto = local[inicial]
posjogador = local['posi']
c = 0
fugir = []
while True:
    posatual = posjogador[0]
    #posjogador = procurar()
    if c == 0:
        fugir = esconder(posobjeto, posjogador)
        print(fugir)
    else:
        novapos = choice(fugir)
        print(novapos)
        for x in local:
            if novapos == local[x][0]:
                posobj1 = local[x]
                break
        fugir = esconder(posobjeto, posjogador)
    sleep(4)
    if posobjeto == posjogador:
        break
    c += 1