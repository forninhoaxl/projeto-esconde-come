from random import choice

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

posobjetoini = local[inicial]
posjogadorini = local['posi']
posinicial = 'I'  # posição inicial do jogador
c = 0
fugir = []  # lista apresentada por frescura do pycharm
posatualjog = posjogadorini[:]
posatualobj = posobjetoini


def procurar(posatual):
    jogandou = []
    print(f'Você está na posição {posatual[0]}.')
    posatual.remove(posatual[0])
    podeir = posatual
    print(f'Você pode ir até {podeir}.')
    andarjpt1 = int(input('Você deseja ir para que posição? [utilize um número como posição'
                         ' desejada para ir, exemplo primeiro lugar, digite 1.] ')) - 1
    andarjpt2 = podeir[andarjpt1]
    for lugar in local:
        if local[lugar][0] == andarjpt2:
            jogandou = local[lugar]
            break
    return jogandou


def esconder(lugarob, lugarjog):
    objandou = []
    objeto = lugarob[:]
    for c in lugarjog:
        if c in lugarob:
            objeto.remove(c)
            if objeto == []:
                objeto.append(lugarob[0])
                break
    print(f'\033[1;31mprint teste posição do objeto antes de se mover-> {lugarob}\033[m')
    print(f'\033[1;31mprint teste lugar do jogador que vai limitar o objeto-> {lugarjog}\033[m')
    print(f'\033[1;31mprint teste opções do objeto depois de remover escolhas que não pode andar-> {objeto}\033[m')
    andaro = choice(objeto)
    for lugar in local:
        if local[lugar][0] == andaro:
            objandou = local[lugar]
            break
    return objandou


while True:
    posatualjog = procurar(posatualjog)
    posatualobj = esconder(posatualobj, posatualjog)
    if posatualjog == posatualobj:
        break
print('Você conseguiu achar o objeto!')

