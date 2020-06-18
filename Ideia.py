from random import choice
from time import sleep

pos = ['posa', 'posb', 'posc', 'posd', 'pose', 'posf', 'posg', 'posh', 'posi', 'posj']
local = {'posa': ['A', 'B', 'D'], 'posb': ['B', 'A', 'C'],
         'posc': ['C', 'B'], 'posd': ['D', 'A', 'E'],
         'pose': ['E', 'D', 'I'], 'posf': ['F', 'I', 'J'],
         'posg': ['G', 'H'], 'posh': ['H', 'G', 'I', 'J'],
         'posi': ['I', 'E', 'F', 'H'], 'posj': ['J', 'F', 'H']}
while True:
    inicial = choice(pos)
    if inicial != 'posi':
        break
posobjeto = local[inicial]
posjogador = local['posi']
c = 0
fugir = []


def esconder(lugarob, lugarjog):
    objeto = lugarob[:]
    for c in lugarjog:
        if c in lugarob:
            objeto.remove(c)
    print(f'\033[1;31mprint teste posição do objeto antes de se mover-> {lugarob}\033[m')
    print(f'\033[1;31mprint teste lugar do jogador que vai limitar o objeto-> {lugarjog}\033[m')
    print(f'\033[1;31mprint teste opções do objeto depois de remover escolhas que não pode andar-> {objeto}\033[m')
    return objeto


def procurar():
    andou = []
    print(f'\033[1;31mprint teste posição do jogador antes de remover a atual {posjogador}\033[m')
    posjogador.remove(posjogador[0])
    podeir = posjogador
    print(f'Você está na posição {posatual}.')
    print(f'Você pode ir até {podeir}')
    andarpt1 = int(input('Você deseja ir para que posição? [utilize um número como posição'
                         ' desejada para ir, exemplo primeiro lugar, digite 1.] ')) - 1
    andarpt2 = podeir[andarpt1]
    print(f'\033[1;31mprint teste de local que irá {andarpt2}\033[m')
    for pos in local:
        if local[pos][0] == andarpt2:
            andou = local[pos]
            break
    return andou


print('Seja bem vindo ao hided!')
while True:
    nome = input('Digite seu nome: ')
    while True:
        confirma = str(input(f'Seu nome será {nome}, correto? [s/n] ')).upper()
        if confirma in ['S', 'N']:
            break
        else:
            print('Você digitou um caractere inválido! Por favor, digite "s" para sim ou "n" para não.')
    if confirma == 'S':
        break


while True:
    posatual = posjogador[0]
    trocapos = procurar()
    posjogador = trocapos
    if c == 0:
        fugir = esconder(posobjeto, posjogador)
        print(f'\033[1;31mprint teste possíveis posições do objeto-> {fugir}\033[m')
        if fugir == []:
            break
        novapos = choice(fugir)
        print(f'\033[1;31mprint teste depois de o objeto trocar a posição-> {novapos}\033[m')
    else:
        for x in local:
            if novapos == local[x][0]:
                posobj1 = local[x]
                break
        fugir = esconder(posobj1, posjogador)
        novapos = choice(fugir)
        print(f'\033[1;31mprint teste depois de o objeto trocar a posição-> {novapos}\033[m')
    sleep(4)
    if posobjeto == posjogador:
        break
    c += 1
print('Você conseguiu achar!!')
