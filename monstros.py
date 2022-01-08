from PPlay.sprite import *
from random import randint

"""Criando Matriz:"""
def monster(linha,coluna,janela):
    matriz_monstro = []
    for i in range(linha):
        lin = []
        for j in range(coluna):
            monstro = Sprite("imagens/enemie.png", 1)
            if j == 0:
                monstro.x = janela.width / 2 - (6* monstro.width)
                monstro.y = (i + 1) * monstro.height
                """
                monstro.x = randint(10,janela.width)
                monstro.y = randint(monstro.height/2,janela.height/2-100)
                """
                lin.append(monstro)
            else:
                monstro.x = lin[j - 1].x + monstro.width * 3 / 3
                monstro.y = (i + 1) * monstro.height
                """
                monstro.x = randint(10, janela.width)
                monstro.y = randint(monstro.height / 2, janela.height/2 -100)
                """
                lin.append(monstro)
        matriz_monstro.append(lin)
    return matriz_monstro

######################################################################

"""Movimento do Monstro:"""
def movimento(velmonx, level,janela,matriz_monstro):
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
    for i in matriz_monstro:
        for j in i:
            j.draw()
            j.x += (velmonx * janela.delta_time() * level)
    return velmonx

######################################################################
