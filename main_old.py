from pyparsing import line
from graphics import *
import random
import time
from playsound import playsound
import os
import threading
import tkinter as tk

# Encontra a resolução da tela
root = tk.Tk()
tela_largura = root.winfo_screenwidth()
tela_altura = root.winfo_screenheight()
root.destroy()

# Inicia a janela do jogo
janela_largura = tela_largura/2
janela_altura = tela_altura/2
win = GraphWin("Bolinha ...", janela_largura, janela_altura)

# Limite superior
linhaSuperior = Line(Point(0, 40), Point(janela_largura, 40))
linhaSuperior.setWidth(10)
linhaSuperior.setFill(color_rgb(10, 100, 10))
linhaSuperior.draw(win)

# Limite inferior
linhaInferior = Line(
    Point(0, janela_altura - 40),
    Point(janela_largura, janela_altura - 40))
linhaInferior.setWidth(10)
linhaInferior.setFill(color_rgb(10, 100, 10))
linhaInferior.draw(win)

# Bolhinha
col = janela_largura/2
lin = janela_altura/2
raio = 15
circulo = Circle(Point(col, lin), raio)
circulo.setFill(color_rgb(10, 10, 100))
circulo.draw(win)

# regua testes
# regua = Line(Point(0,40), Point(15,40))
# regua.draw(win)

# Sistema de pontuação
pontos01 = 0
pontos02 = 0
placar = Text(
    Point(janela_largura/2, janela_altura/2),
    str(pontos01) + ' : ' + str(pontos02))
placar.setSize(30)
placar.draw(win)

# Barra esquerda
linha_Barra_Esquerda = janela_altura/2
barra_Esquerda = Line(
    Point(10, linha_Barra_Esquerda),
    Point(10, linha_Barra_Esquerda + 100))
barra_Esquerda.setFill(color_rgb(100, 10, 10))
barra_Esquerda.setWidth(10)
barra_Esquerda.draw(win)

# Barra direita
linha_Barra_Direita = janela_altura/2
barra_Direita = Line(
    Point(janela_largura-10, linha_Barra_Direita),
    Point(janela_largura-10, linha_Barra_Direita + 100))
barra_Direita.setFill(color_rgb(100, 10, 10))
barra_Direita.setWidth(10)
barra_Direita.draw(win)

'''
o que significa cada variável:
Passo = velocidade lateral da bolhinha
velocidade = velocidade vertical da bolhinha
bateu = eu usei para aleatoriedade quando resetar

Para mexer com a fisíca na lateral da bolhinha tem que pegar os dados
de "col" usando print(col) e vendo no console
Para mexer com a fisíca na verical da bolhinha tem que pegar os dados
de "lin" usando print(col) e vendo no console
'''
velocidade = 10
bateu = True
continuar = True
while continuar:
    if bateu:
        passo = 30  # random.randrange(5, 10)
        if random.random() < 0.5:
            passo = -passo
        bateu = False
    # Ponto para o player 1
    if (col + raio + passo) > janela_largura+50:
        passo = -passo
        placar.undraw()
        pontos01 += 1
        placar = Text(
            Point(janela_largura/2, janela_altura/2),
            str(pontos01) + ' : ' + str(pontos02))
        placar.setSize(30)
        placar.draw(win)

        # reset da bolhinha
        circulo.undraw()
        col = janela_largura/2
        lin = janela_altura/2
        raio = 15
        circulo = Circle(Point(col, lin), raio)
        circulo.setFill(color_rgb(10, 10, 100))
        circulo.draw(win)
        bateu = True

    # Ponto para o player 2
    if (col - raio + passo) < -50:
        passo = -passo
        placar.undraw()
        pontos02 += 1
        placar = Text(
            Point(janela_largura/2, janela_altura/2),
            str(pontos01) + ' : ' + str(pontos02))
        placar.setSize(30)
        placar.draw(win)

        # reset da bolhinha
        circulo.undraw()
        col = janela_largura/2
        lin = janela_altura/2
        raio = 15
        circulo = Circle(Point(col, lin), raio)
        circulo.setFill(color_rgb(10, 10, 100))
        circulo.draw(win)
        bateu = True

    # Altera a direção vertical quando bate em cima
    if lin < 65:
        velocidade = -velocidade

    # Altera a direção vertical quando bate embaixo
    if lin > janela_altura - 65:
        velocidade = - velocidade

    # Colisão com a barra acontece quando a bolhinha está na coluna 20
    if col < 50 \
            and col > 0 \
            and lin > linha_Barra_Esquerda \
            and lin < (linha_Barra_Esquerda + 100):
        passo = - passo

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

    # Colisão com a barra acontece quando a bolhinha está na coluna largura-20
    if col > janela_largura-50 \
            and col < janela_largura \
            and lin > linha_Barra_Direita \
            and lin < (linha_Barra_Direita + 100):
        passo = - passo

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
    col += passo
    lin += velocidade
    circulo = Circle(Point(col, lin), 15)
    circulo.setFill(color_rgb(10, 10, 100))
    circulo.draw(win)

    # Movimento horizontal da barra pelas setas direita/esquerda
    tecla = win.checkKey()

    # movimento da barra esquerda
    if tecla == "W" or tecla == "w":
        if linha_Barra_Esquerda-40 > 50:
            linha_Barra_Esquerda -= 40
        else:
            linha_Barra_Esquerda = 50

        barra_Esquerda.undraw()
        barra_Esquerda = Line(
            Point(10, linha_Barra_Esquerda),
            Point(10, linha_Barra_Esquerda + 100))
        barra_Esquerda.setFill(color_rgb(100, 10, 10))
        barra_Esquerda.setWidth(10)
        barra_Esquerda.draw(win)

    # movimento da barra esquerda
    if tecla == "S" or tecla == "s":
        if linha_Barra_Esquerda+40 < janela_altura-150:
            linha_Barra_Esquerda += 40
        else:
            linha_Barra_Esquerda = janela_altura-150

        barra_Esquerda.undraw()
        barra_Esquerda = Line(
            Point(10, linha_Barra_Esquerda),
            Point(10, linha_Barra_Esquerda + 100))
        barra_Esquerda.setFill(color_rgb(100, 10, 10))
        barra_Esquerda.setWidth(10)
        barra_Esquerda.draw(win)

    # movimento da barra Direita
    if tecla == "Up":
        if linha_Barra_Direita-40 > 50:
            linha_Barra_Direita -= 40
        else:
            linha_Barra_Direita = 50

        barra_Direita.undraw()
        barra_Direita = Line(
            Point(janela_largura-10, linha_Barra_Direita),
            Point(janela_largura-10, linha_Barra_Direita + 100))
        barra_Direita.setFill(color_rgb(100, 10, 10))
        barra_Direita.setWidth(10)
        barra_Direita.draw(win)

    # movimento da barra Direita
    if tecla == "Down":
        if linha_Barra_Direita+40 < janela_altura-150:
            linha_Barra_Direita += 40
        else:
            linha_Barra_Direita = janela_altura-150

        barra_Direita.undraw()
        barra_Direita = Line(
            Point(janela_largura-10, linha_Barra_Direita),
            Point(janela_largura-10, linha_Barra_Direita + 100))
        barra_Direita.setFill(color_rgb(100, 10, 10))
        barra_Direita.setWidth(10)
        barra_Direita.draw(win)

    # Sair do joguinho
    if tecla == "Escape":
        continuar = False
        continue

    if pontos01 == 10 or pontos02 == 10:
        continuar = False
        final_do_jogo = True
        continue

    # Esperar o ser humano reagir
    time.sleep(0.04)

while final_do_jogo:
    barra_Direita.undraw()
    barra_Esquerda.undraw()
    circulo.undraw()

    tecla = win.checkKey()

    if pontos01 == 10:
        placar.undraw()
        vitoria = Text(
            Point(janela_largura/2, janela_altura/2),
            'Jogador numero 1 venceu pressione esc para sair')
        vitoria.setSize(20)
        vitoria.draw(win)

    if pontos02 == 10:
        placar.undraw()
        vitoria = Text(
            Point(janela_largura/2, janela_altura/2),
            'Jogador numero 2 venceu pressione esc para sair')
        vitoria.setSize(20)
        vitoria.draw(win)

    if tecla == "Escape":
        final_do_jogo = False
        continue

win.close()
