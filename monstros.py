from PPlay.sprite import *

##CRIANDO MATRIZ:
def monster(linha,coluna,janela):
    global matriz_monstro
    matriz_monstro = []
    for i in range(linha):
        lin = []
        for j in range(coluna):
            monstro = Sprite("imagens/enemie.png", 1)
            if j == 0:
                monstro.x = janela.width / 2 - (6* monstro.width)
                monstro.y = (i + 1) * monstro.height
                lin.append(monstro)
            else:
                monstro.x = lin[j - 1].x + monstro.width * 3 / 3
                monstro.y = (i + 1) * monstro.height
                lin.append(monstro)
        matriz_monstro.append(lin)
    return matriz_monstro

######################################################################

##MOVIMENTO DO MONSTRO:
def movimento(velmonx, level,janela):
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
