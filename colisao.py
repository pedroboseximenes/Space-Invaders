from PPlay.window import *
from PPlay.sprite import *
from random import randint
import time

def colisao(matriz_monstro, lista_disparos, pontu, contadordemob):
    for z in lista_disparos:
        for i in matriz_monstro:
            for j in i:
                if(j.y >= z.y):
                    if z.collided(j):
                        lista_disparos.remove(z)
                        i.remove(j)
                        contadordemob += 1
                        pontu += randint(3, 7)
    return pontu, contadordemob

def colisaotirocomnave(vetortiromonster,nave,janela,vida,contagem, invencivel, tempoinvencivel):

    for z in vetortiromonster:
        if invencivel == True:
            tempoinvencivel += janela.delta_time()
            if tempoinvencivel >= 4:
                invencivel = False
                tempoinvencivel = 0
        if z.collided(nave):
            if invencivel == False:
                vetortiromonster.remove(z)
                vida -= 1
                nave.x = janela.width / 2 - nave.width / 2
                invencivel = True
    return vida, invencivel, tempoinvencivel