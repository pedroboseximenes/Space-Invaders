from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from monstros import *
from colisao import *


def jogar(janela, level):
    """setando imagem do fundo, nave, pegando o telcado:"""
    fundo = GameImage("imagens/fundo.jpg")
    nave = Sprite("imagens/nave.png", 1)
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
    linha = 3
    coluna = 3
    matriz_monstro = monster(linha, coluna, janela)
    pontu = 0
    #################################

    """contador(para colocar fps na tela), fps, relogio(delta_time()):"""
    contador = 0
    fps = 0
    relogio = 0
    #################################

    while True:
        """saindo p tela inicial:"""
        if (teclado.key_pressed("ESC")):
            break
        """pegando movimento do player na nave:"""
        if (teclado.key_pressed("LEFT") and (nave.x >= 0)):
            nave.x = nave.x - (velocidadex * janela.delta_time())
        if (teclado.key_pressed("RIGHT") and (nave.x < janela.width - nave.width)):
            nave.x = nave.x + (velocidadex * janela.delta_time())

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
        janela.draw_text(str(pontu), janela.width - 40, 10, 50, (255, 0, 0), "Boulder", False, False)
        janela.draw_text(str(fps), 10, 10, 27, (255, 0, 0), "Boulder", False, False)
        nave.draw()
        for x in lista_disparos:
            x.draw()
        velmonx = movimento(velmonx, level, janela, matriz_monstro)
        pontu = colisao(matriz_monstro, lista_disparos, pontu)
        janela.update()
