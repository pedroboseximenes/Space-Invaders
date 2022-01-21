from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameimage import *
from monstros import *
from colisao import *


def jogar(janela, level):
    """setando imagem do fundo, nave, pegando o telcado:"""
    fundo = GameImage("imagens/fundo.jpg")
    #nave = Sprite("imagens/nave.png", 1)
    nave = Animation("imagens/nave.png",4,loop =True)
    janela.set_title("Space Invaders")
    teclado = Window.get_keyboard()
    #################################

    """coord da nave:"""
    nave.x = janela.width / 2 - nave.width / 2
    nave.y = janela.height / 1.17
    #################################

    """setando velocidade da nave, do tiro, do monstro:"""
    velocidadex = 180
    velotiro = 150
    velmonx = 65
    #################################

    """setando o tempo (contagem para o pause entre os tiros), criando lista dos monstros e dos tiros:
    linha,coluna para matriz_monstro:
    pontuação"""

    tempo = 0
    lista_disparos = []
    linha = 1
    coluna = 1
    pontu = 0
    #################################

    """contador(para colocar fps na tela), fps, relogio(delta_time()):"""
    contador = 0
    fps = 0
    relogio = 0
    #################################
    vetortiromonster = []
    time = 0
    vida = 3
    contagem = 0
    """
    coracao e estrela
    """
    coracao = GameImage("imagens/heart.png")
    coracao.x, coracao.y = [janela.width/2- coracao.width/2 - 50, 10]
    estrela = GameImage("imagens/star.png")
    estrela.x, estrela.y = [920, 10]

    rounds = 1
    matriz_monstro =monster(linha, coluna, janela,rounds)

    contadordemob = 0
    """
    invencivel = False e o tempo para ficar invencivel!
    """
    invencivel = False
    tempoinvencivel = 0

    while True:

        """saindo p tela inicial:"""
        if (teclado.key_pressed("ESC")):
            break
        """pegando movimento do player na nave:"""
        if (teclado.key_pressed("LEFT") and (nave.x >= 0)):
            nave.x = nave.x - (velocidadex * janela.delta_time())
        if (teclado.key_pressed("RIGHT") and (nave.x < janela.width - nave.width)):
            nave.x = nave.x + (velocidadex * janela.delta_time())
        if vida <= 0:
            break
        #################################

        """pegando fps do jogo:"""

        relogio += janela.delta_time()
        contador += 1
        if relogio >= 1:
            fps = contador
            relogio = 0
            contador = 1
        #################################



        """criando os tiros qnd apertar espaço e com um time:"""

        tempo += janela.delta_time()
        if (teclado.key_pressed("SPACE") and tempo >= 0.68 * level):
            tiro = Sprite("imagens/tiro.png", 1)
            tiro.x = nave.x + tiro.width / 2 + nave.width / 2.72
            tiro.y = nave.y - tiro.height / 2
            lista_disparos.append(tiro)
            tempo = 0

        #################################

        """retirando os tiros que sairem da tela:"""

        for x in lista_disparos:
            x.y -= (velotiro * janela.delta_time())
            if (x.y + x.height / 2 < 0):
                lista_disparos.remove(x)

        #################################

        """desenhos de fundo,fps,pontuação,tiros,monsto se movimentando, colisão:"""
        fundo.draw()
        janela.draw_text(str(pontu), janela.width - 40, 10, 50, (30, 0, 0), "Boulder", False, False)
        janela.draw_text(str(fps), 10, 10, 32, (100, 0, 0), "Boulder", False, False)
        janela.draw_text(str(vida), janela.width/2 , 10, 50, (255, 0, 0), "Boulder", False, False)
        nave.draw()

        matriz_monstro, rounds = verificarsetemmob(matriz_monstro, rounds, linha, coluna, janela)
        velmonx, contadordemob = movimento(velmonx, level, janela, matriz_monstro, contadordemob)

        time = tiromonstro(time,matriz_monstro,vetortiromonster,janela)
        vida, invencivel, tempoinvencivel = colisaotirocomnave(vetortiromonster, nave, janela, vida,contagem, invencivel , tempoinvencivel)
        retirardatela(vetortiromonster,janela)

        for i in vetortiromonster:
            i.y += (200 * janela.delta_time() * level)
            i.draw()
        for x in lista_disparos:
            x.draw()

        pontu, contadordemob = colisao(matriz_monstro, lista_disparos, pontu, contadordemob)
        coracao.draw()
        estrela.draw()
        janela.update()