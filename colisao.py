from PPlay.window import *
from PPlay.sprite import *
from random import randint


def colisao(matriz_monstro, lista_disparos, pontu):
    for z in lista_disparos:
        for i in matriz_monstro:
            for j in i:
                if(j.y >= z.y):
                    if z.collided(j):
                        lista_disparos.remove(z)
                        i.remove(j)
                        pontu += randint(3, 7)
    return pontu
