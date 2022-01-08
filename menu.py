from jogo import *

def dificuldades(janela):
    ##setando nome da janela, a imagem do fundo, botao easy,medio,hard, setando mouse e teclado:

    global level
    janela.set_title("Dificuldades!")
    fundo = GameImage("imagens/fundo.jpg")
    botaoe = Sprite("imagens/buttoneasy.png", 1)
    botaom = Sprite("imagens/buttonmedium.png", 1)
    botaoh = Sprite("imagens/buttonhard.png", 1)
    mouse = Window.get_mouse()
    teclado = Window.get_keyboard()

    #################################

    ##setando as posições dos botões de cada dificuldade!:

    botaoe.x = janela.width/5 - botaoe.width/2
    botaoe.y = janela.height/2 - botaoe.height/2
    botaom.x = janela.width/2 - botaom.width/2
    botaom.y = janela.height/2 - botaom.height/2
    botaoh.x = janela.width/1.25 - botaoh.width/2
    botaoh.y = janela.height/2 - botaoh.height/2

    ##############################


    while True:
        ##setanndo se clicar esc volta;
        if (teclado.key_pressed("ESC")):
            break
        ##setando se clicar no botão easy:
        if (mouse.is_button_pressed(1)) and (mouse.is_over_object(botaoe)):
            return 2
        ##setando se clicar no botão medio:
        if (mouse.is_button_pressed(1)) and (mouse.is_over_object(botaom)):
            return 2
        ##setando se clicar no botão hard:
        if (mouse.is_button_pressed(1)) and (mouse.is_over_object(botaoh)):
            return 3
        #################################

        #desenhos do fundo e dos botões:
        fundo.draw()
        botaoe.draw()
        botaom.draw()
        botaoh.draw()
        janela.update()


def menu(level):
    ##setando janela, mouse, fundo, 4 botões (jogar,dificuldades,ranking,sair):

    janela = Window(1024,768)
    janela.set_title("Space-Invaders")
    mouse = Window.get_mouse()

    fundo = GameImage("imagens/fundo.jpg")
    botao = Sprite("imagens/button1.png", 1)
    botao2 = Sprite("imagens/button2.png", 1)
    botao3 = Sprite("imagens/button3.png", 1)
    botao4 = Sprite("imagens/button4.png", 1)

    #################################

    ##setando as coords dos botões:

    botao.x = janela.width/2 - botao.width /2
    botao.y = janela.height/4 - botao.height/2

    botao2.x = janela.width / 2 - botao2.width / 2
    botao2.y = janela.height / 2.6 - botao2.height / 2

    botao3.x = janela.width / 2 - botao3.width / 2
    botao3.y = janela.height / 1.9 - botao3.height / 2

    botao4.x = janela.width / 2 - botao4.width / 2
    botao4.y = janela.height / 1.40 - botao4.height / 2

    #################################

    while True:
        ##verificar se mouse esta pressionado e sobre botao, logo vai p jogar:
        if (mouse.is_button_pressed(1)):
            if (mouse.is_over_object(botao)):
                jogar(janela,level)
        ##verificar se mouse esta pressionado e sobre botao, logo vai p dificuldade:
        if (mouse.is_over_object(botao2)):
            if (mouse.is_button_pressed(1)):
                level = dificuldades(janela)
        ##verificar se mouse esta pressionado e sobre botao, logo vai p ranking:
        if (mouse.is_over_object(botao3)):
            if (mouse.is_button_pressed(1)):
                None
        ##verificar se mouse esta pressionado e sobre botao, logo vai p saida:
        if (mouse.is_over_object(botao4)):
            if (mouse.is_button_pressed(1)):
                janela.close()

        #################################

        ##desenhos:
        fundo.draw()
        botao.draw()
        botao2.draw()
        botao3.draw()
        botao4.draw()
        janela.update()