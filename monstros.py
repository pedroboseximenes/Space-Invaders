from PPlay.sprite import *
from random import randint

"""Criando Matriz:"""
def monster(linha,coluna,janela, rounds):
    matriz_monstro = []
    for i in range(linha + rounds):
        lin = []
        for j in range(coluna + rounds):
            monstro = Sprite("imagens/enemie.png", 1)
            if j == 0:
                monstro.x = janela.width / 2 - (6* monstro.width)
                monstro.y = (i + 1) * monstro.height
                lin.append(monstro)
            else:
                monstro.x = lin[j - 1].x + monstro.width * 3 / 3
                monstro.y = (i + 1) * monstro.height
                lin.append(monstro)
                """
                monstro.x = randint(10, janela.width)
                monstro.y = randint(monstro.height / 2, janela.height/2 -100)
                """
        matriz_monstro.append(lin)
    return matriz_monstro

######################################################################
def verificarsetemmob(matriz_monstro,rounds,linha,coluna,janela):

    if matriz_monstro == [[],[]] or matriz_monstro == [[],[],[]] or matriz_monstro == [[],[],[],[]] or matriz_monstro == [[],[],[],[],[]] or matriz_monstro == [[],[],[],[],[],[]]:
        print(rounds)
        rounds += 1
        matriz_monstro = monster(linha,coluna,janela,rounds)
    return matriz_monstro, rounds


"""Movimento do Monstro:"""
def movimento(velmonx, level,janela,matriz_monstro,contadordemob):
    y_monster = 0
    for i in matriz_monstro:
        for j in i:
            if j.x >= janela.width - j.width - 5:
                velmonx *= -1
                y_monster += j.width / 2
                for i in matriz_monstro:
                    for j in i:
                        j.x -= y_monster / 2
                        j.y += y_monster + 35
            if j.x <5:
                velmonx *= -1
                y_monster += j.width/2
                for i in matriz_monstro:
                    for j in i:
                        j.x += y_monster/2
                        j.y += y_monster + 35
    if contadordemob >= 1:
        if velmonx > 0:
            velmonx += (contadordemob * 25 * level)
        elif velmonx < 0:
            velmonx -= (contadordemob * 25 * level)
        contadordemob = 0
    for i in matriz_monstro:
        for j in i:
            j.draw()
            j.x += (velmonx * janela.delta_time() * level)
    return velmonx, contadordemob

######################################################################

def tiromonstro(time,matriz_monstro,vetortiromonster,janela):
    if time >= 1.70:
        aux = 0
        for i in matriz_monstro:
            for j in i:
                aux += 1
                atirador = randint(0,aux)
        for i in matriz_monstro:
            for j in i:
                if atirador == aux:
                    tirom = Sprite("imagens/tiro.png", 1)
                    tirom.x = j.x
                    tirom.y =j.y
                    vetortiromonster.append(tirom)
                aux -= 1
        time = 0
    else:
        time += janela.delta_time()
    return time

def retirardatela(vetortiromonster,janela):
    for x in vetortiromonster:
        if (x.y + x.height / 2 > janela.height):
            vetortiromonster.remove(x)