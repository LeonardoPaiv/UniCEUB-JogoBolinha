from platform import win32_edition
from pyparsing import line
from graphics import *
import time
from playsound import playsound
import os
import threading



# Tela de final do jogo quando player 1 vence
def vitoria_player1(win):

    texto_vitoria = Text(Point(800, 300), 'Jogador Numero 1 venceu')
    texto_vitoria.setSize(30)
    texto_vitoria.draw(win)

    jogar_novamente = Text(Point(800, 350), "jogar novamente")
    jogar_novamente.setSize(25)
    jogar_novamente.draw(win)
    sair = Text(Point(800, 400), "sair")
    sair.setSize(25)
    sair.draw(win)


    menu = True
    while menu:

        tecla = win.getKey()

        if tecla == "Up":
            jogar_novamente.undraw()
            jogar_novamente.setSize(30)
            jogar_novamente.draw(win)
            sair.undraw()
            sair.setSize(25)
            sair.draw(win)
            jogar_outra_vez = True


        if tecla == "Down":
            sair.undraw()
            sair.setSize(30)
            sair.draw(win)
            jogar_novamente.undraw()
            jogar_novamente.setSize(25)
            jogar_novamente.draw(win)
            jogar_outra_vez = False
            
        if tecla == 'Return' and jogar_outra_vez == True:
            win.close()
            jogo(0,0)
            

        if tecla == 'Return' and jogar_outra_vez == False:
            menu = False
            win.close()
            

        
# Tela de final do jogo qunado player 2 vence
def vitoria_player2(win):

    texto_vitoria = Text(Point(800, 300), '''Jogador Numero 2 venceu''')
    texto_vitoria.setSize(30)
    texto_vitoria.draw(win)

    jogar_novamente = Text(Point(800, 350), "jogar novamente")
    jogar_novamente.setSize(25)
    jogar_novamente.draw(win)
    sair = Text(Point(800, 400), "sair")
    sair.setSize(25)
    sair.draw(win)


    menu = True
    while menu:

        tecla = win.getKey()

        contador = None

        if tecla == "Up":
            jogar_novamente.undraw()
            jogar_novamente.setSize(30)
            jogar_novamente.draw(win)
            sair.undraw()
            sair.setSize(25)
            sair.draw(win)
            jogar_outra_vez = True


        if tecla == "Down":
            sair.undraw()
            sair.setSize(30)
            sair.draw(win)
            jogar_novamente.undraw()
            jogar_novamente.setSize(25)
            jogar_novamente.draw(win)
            jogar_outra_vez = False
            
        if tecla == 'Return' and jogar_outra_vez == True:
            win.close()
            jogo(0,0)
            

        if tecla == 'Return' and jogar_outra_vez == False:
            menu = False
            win.close()



def jogo(ponto_player1, ponto_player2):
    win = GraphWin("Bolinha ...", 1600, 600)

    # Limite superior
    linhaSuperior = Line(Point(0, 40), Point(1600, 40))
    linhaSuperior.setWidth(10)
    linhaSuperior.setFill(color_rgb(10, 100, 10))
    linhaSuperior.draw(win)

    # Limite inferior
    linhaInferior = Line(Point(0, 550), Point(1600, 550))
    linhaInferior.setWidth(10)
    linhaInferior.setFill(color_rgb(10, 100, 10))
    linhaInferior.draw(win)

    # Bolhinha
    col = 800
    lin = 300
    raio = 15
    circulo = Circle(Point(col, lin), raio)
    circulo.setFill(color_rgb(10, 10, 100))
    circulo.draw(win)

    # Sistema de pontuação
    placar = Text(Point(800, 300), str(ponto_player1) + ' : ' + str(ponto_player2))
    placar.setSize(30)
    placar.draw(win)

    # Barra esquerda
    linha_Barra_Esquerda = 205
    barra_Esquerda = Line(Point(10, linha_Barra_Esquerda), Point(10, linha_Barra_Esquerda + 100))
    barra_Esquerda.setFill(color_rgb(100, 10, 10))
    barra_Esquerda.setWidth(10)
    barra_Esquerda.draw(win)

    # Barra direita
    linha_Barra_Direita = 205
    barra_Direita = Line(Point(1590, linha_Barra_Direita), Point(1590, linha_Barra_Direita + 100))
    barra_Direita.setFill(color_rgb(100, 10, 10))
    barra_Direita.setWidth(10)
    barra_Direita.draw(win)

    velocidade_horizontal = 30
    velocidade_vertical = 10
    reset = False
    jogo_rolando = True
    

    while jogo_rolando:
        if reset:
            velocidade_horizontal = 30
            velocidade_horizontal = -velocidade_horizontal
            reset = False
        
            #Ponto para o player 1
        if (col + raio + velocidade_horizontal) > 1650:
            velocidade_horizontal = -velocidade_horizontal
            placar.undraw()
            ponto_player1 +=1
            placar = Text(Point(800, 300), str(ponto_player1) + ' : ' + str(ponto_player2))
            placar.setSize(30)
            placar.draw(win)

            # reset da bolhinha
            circulo.undraw()
            col = 800
            lin = 300
            raio = 15
            circulo = Circle(Point(col, lin), raio)
            circulo.setFill(color_rgb(10, 10, 100))
            circulo.draw(win)
            reset = True

            #Ponto para o player 2
        if (col - raio + velocidade_horizontal) < -50:
            velocidade_horizontal = -velocidade_horizontal
            placar.undraw()
            ponto_player2 +=1
            placar = Text(Point(800, 300), str(ponto_player1) + ' : ' + str(ponto_player2))
            placar.setSize(30)
            placar.draw(win)

            # reset da bolhinha
            circulo.undraw()
            col = 800
            lin = 300
            raio = 15
            circulo = Circle(Point(col, lin), raio)
            circulo.setFill(color_rgb(10, 10, 100))
            circulo.draw(win)
            reset = True

        # Altera a direção vertical quando bate em cima
        if lin < 65:
            velocidade_vertical = -velocidade_vertical

        # Altera a direção vertical quando bate embaixo
        if lin > 525:
            velocidade_vertical = - velocidade_vertical

        # Colisão com a barra acontece quando a bolhinha está na coluna 20 quando a velocidade lateral é 30
        if col == 20 and lin > linha_Barra_Esquerda and lin < (linha_Barra_Esquerda + 100):
            velocidade_horizontal = - velocidade_horizontal
            
            # Plays sound when ball hits bar
            sound_file_path = os.path.join(
                os.getcwd(),
                "ball_hit_bar.wav"
            )
            threading.Thread(
                target=playsound,
                args=(sound_file_path,),
                daemon=True
                ).start()
        
        # Colisão com a barra acontece quando a bolhinha está na coluna 1580 quando a velocidade lateral é 30
        if col == 1580 and lin > linha_Barra_Direita and lin < (linha_Barra_Direita + 100):
            velocidade_horizontal = - velocidade_horizontal

            # Plays sound when ball hits bar
            sound_file_path = os.path.join(
                os.getcwd(),
                "ball_hit_bar.wav"
            )
            threading.Thread(
                target=playsound,
                args=(sound_file_path,),
                daemon=True
                ).start()

        # Nova posição do círculo
        circulo.undraw()
        col += velocidade_horizontal
        lin += velocidade_vertical
        circulo = Circle(Point(col, lin), 15)
        circulo.setFill(color_rgb(10, 10, 100))
        circulo.draw(win)

        # Movimento horizontal da barra pelas setas direita/esquerda
        tecla = win.checkKey()

        # movimento da barra esquerda
        if tecla == "W" or tecla ==  "w":
            if (linha_Barra_Esquerda - 15) > 35:
                linha_Barra_Esquerda -= 40

            barra_Esquerda.undraw()
            barra_Esquerda = Line(Point(10, linha_Barra_Esquerda), Point(10, linha_Barra_Esquerda + 100))
            barra_Esquerda.setFill(color_rgb(100, 10, 10))
            barra_Esquerda.setWidth(10)
            barra_Esquerda.draw(win)

        # movimento da barra esquerda
        if tecla == "S" or tecla == "s":
            if (linha_Barra_Esquerda + 15) < 450:
                linha_Barra_Esquerda += 40
    
            barra_Esquerda.undraw()
            barra_Esquerda =Line(Point(10, linha_Barra_Esquerda), Point(10, linha_Barra_Esquerda + 100))
            barra_Esquerda.setFill(color_rgb(100, 10, 10))
            barra_Esquerda.setWidth(10)
            barra_Esquerda.draw(win)
        
        # movimento da barra Direita
        if tecla == "Up":
            if (linha_Barra_Direita - 15) > 35:
                linha_Barra_Direita -= 40
            
            barra_Direita.undraw()
            barra_Direita = Line(Point(1590, linha_Barra_Direita), Point(1590, linha_Barra_Direita + 100))
            barra_Direita.setFill(color_rgb(100, 10, 10))
            barra_Direita.setWidth(10)
            barra_Direita.draw(win)
        
        # movimento da barra Direita
        if tecla == "Down":
            if (linha_Barra_Direita + 15) < 450:
                linha_Barra_Direita += 40
    
            barra_Direita.undraw()
            barra_Direita =Line(Point(1590, linha_Barra_Direita), Point(1590, linha_Barra_Direita + 100))
            barra_Direita.setFill(color_rgb(100, 10, 10))
            barra_Direita.setWidth(10)
            barra_Direita.draw(win)
        
        # PAUSE, a lógica ficou mais complexa com 3 opções, caso precise só de continuar e sair,
        # dá para usar a mesma lógica da tela do final do jogo
        if tecla == 'Escape':

            def pause():
                # Texto de Pause
                stop = Text(Point(800, 400), 'Jogo Pausado, pressione qualquer coisa para continuar')
                stop.setSize(30)
                stop.draw(win)
                
                # Para lógica de selecionar o botão preenchido
                seletor = 2
                
                # Botão continuar
                continuar = Text(Point(600, 500), 'Continuar')
                continuar.setSize(25)
                continuar.draw(win)

                # Botão vazio
                botao = Text(Point(800, 500), 'Botão')
                botao.setSize(25)
                botao.draw(win)

                # Botão de sair
                sair = Text(Point(1000, 500), 'Sair')
                sair.setSize(25)
                sair.draw(win)

                # Loop de Pause
                pause = True
                while pause:

                    # Registro de tecla para o loop não travar jogo
                    tecla = win.getKey()

                    # Navegação do seletor pela tela
                    if tecla == "Left" and seletor < 3:
                        seletor += 1
                            
                    # Navegação do seletor pela tela
                    if tecla == "Right" and seletor > 1:
                        seletor -= 1
                    
                    # Continuar fica com a font 30 para demonstrar que o seletor está nele. seletor = 3
                    if seletor == 3:
                        continuar.undraw()
                        continuar.setSize(30)
                        continuar.draw(win)

                        botao.undraw()
                        botao.setSize(25)
                        botao.draw(win)

                        sair.undraw()
                        sair.setSize(25)
                        sair.draw(win)

                    # Botão fica com a font 30 para demonstrar que o seletor está nele. seletor = 2
                    if seletor == 2:
                        continuar.undraw()
                        continuar.setSize(25)
                        continuar.draw(win)

                        botao.undraw()
                        botao.setSize(30)
                        botao.draw(win)

                        sair.undraw()
                        sair.setSize(25)
                        sair.draw(win)
                    
                    # Sair fica com a font 30 para demonstrar que o seletor está nele. seletor = 1
                    if seletor == 1:
                        continuar.undraw()
                        continuar.setSize(25)
                        continuar.draw(win)

                        botao.undraw()
                        botao.setSize(25)
                        botao.draw(win)

                        sair.undraw()
                        sair.setSize(30)
                        sair.draw(win)


                    # Caso o seletor seja = 3 e precinem Enter, o jogo sai do pause
                    if tecla == 'Return' and seletor == 3:
                        pause = False
                        
                    # Caso o seletor seja = 2 nada acontece, está para programar
                    if tecla == "Return" and seletor == 2:
                        a = 'nada acontece'
                    
                    # Caso o seletor seja = 1 e precinem Enter, o jogo fecha
                    if tecla == "Return" and seletor == 1:
                        win.close()
                
                stop.undraw()
                continuar.undraw()
                botao.undraw()
                sair.undraw()
            
            pause()
        
        if ponto_player1 == 10:
            placar.undraw()
            barra_Esquerda.undraw()
            barra_Direita.undraw()
            circulo.undraw()
            jogo_rolando == False
            vitoria_player1(win)


        if ponto_player2 == 10:
            placar.undraw()
            barra_Esquerda.undraw()
            barra_Direita.undraw()
            circulo.undraw()
            jogo_rolando == False
            vitoria_player2(win)

        time.sleep(0.04)
            



jogo(0,0)