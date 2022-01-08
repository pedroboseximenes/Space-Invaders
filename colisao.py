from PPlay.window import *
from PPlay.sprite import *
from random import randint
def colisao(matriz_monstro, lista_disparos, pontu):
    for z in lista_disparos:
       # if (matriz_monstro[0][2].y <= z.y):# and matriz_monstro[2][2].x >= z.x and matriz_monstro[0][0].x <= z.x):
        for i in matriz_monstro:
            for j in i:
                if z.collided(j):
                    lista_disparos.remove(z)
                    i.remove(j)
                    pontu += randint(3,7)
    return pontu