from pyparsing import line
from graphics import *
import random

win = GraphWin("Bolinha ...", 1600, 600)

linhaSuperior = Line(Point(0, 40), Point(1600, 40))
linhaSuperior.setWidth(10)
linhaSuperior.setFill(color_rgb(10, 100, 10))
linhaSuperior.draw(win)

linhaInferior = Line(Point(0, 550), Point(1600, 550))
linhaInferior.setWidth(10)
linhaInferior.setFill(color_rgb(10, 100, 10))
linhaInferior.draw(win)

col = 390
lin = 80
raio = 15
circulo = Circle(Point(col, lin), raio)
circulo.setFill(color_rgb(10, 10, 100))
circulo.draw(win)

# Sistema de pontuação

#def placar(pts_p1, pts_p2, soma1, soma2):
#    pts_p1 += soma1
#    pts_p2 += soma2
#    Start_Score = Text(Point(800, 300), str(pts_p1) + ' : ' + str(pts_p2))
#    Start_Score.setSize(30)
#    Start_Score.draw(win)
#
## Placar inicial
#placar(0, 0, 0, 0)


    

colIni = 340
tamanho = 100
barra = Line(Point(colIni, 530), Point(colIni+tamanho, 530))
barra.setFill(color_rgb(100, 10, 10))
barra.setWidth(10)
barra.draw(win)


linha_Barra_Esquerda = 200
barra_Esquerda = Line(Point(10, linha_Barra_Esquerda), Point(10, linha_Barra_Esquerda + 100))
barra_Esquerda.setFill(color_rgb(100, 10, 10))
barra_Esquerda.setWidth(10)
barra_Esquerda.draw(win)

linha_Barra_Direita = 200
barra_Direita = Line(Point(1590, linha_Barra_Direita), Point(1590, linha_Barra_Direita + 100))
barra_Direita.setFill(color_rgb(100, 10, 10))
barra_Direita.setWidth(10)
barra_Direita.draw(win)


velocidade = 5
bateu = True
continuar = True
while continuar:
    if bateu:
        passo = random.randrange(1, 10)
        if random.random() < 0.5:
            passo = -passo
        bateu = False

    if (col + raio + passo) > 1600:
        passo = -passo

    if (col - raio + passo) < 0:
        passo = -passo

    if lin < 65:
        velocidade = -velocidade

    if lin > 525:
        velocidade = - velocidade

    if lin == 515 and col > colIni and col < (colIni+tamanho):
        velocidade = -velocidade

    # Nova posição do círculo
    circulo.undraw()
    col += passo
    lin += velocidade
    circulo = Circle(Point(col, lin), 15)
    circulo.setFill(color_rgb(10, 10, 100))
    circulo.draw(win)

    # Movimento horizontal da barra pelas setas direita/esquerda
    tecla = win.checkKey()

    # Sair do joguinho
    if tecla == "Escape":
        continuar = False
        continue

    if tecla == "Right":
        if (colIni + 20) < 701:
            colIni = colIni + 20

        barra.undraw()
        barra = Line(Point(colIni, 530), Point(colIni + 100, 530))
        barra.setFill(color_rgb(100, 10, 10))
        barra.setWidth(10)
        barra.draw(win)

    if tecla == "Left":
        if (colIni - 20) > -1:
            colIni = colIni - 20

        barra.undraw()
        barra = Line(Point(colIni, 530), Point(colIni + 100, 530))
        barra.setFill(color_rgb(100, 10, 10))
        barra.setWidth(10)
        barra.draw(win)
        print(colIni)

    if tecla == "Up":
        if (linha_Barra_Esquerda - 15) > 35:
            linha_Barra_Esquerda -= 17

        barra_Esquerda.undraw()
        barra_Esquerda = Line(Point(10, linha_Barra_Esquerda), Point(10, linha_Barra_Esquerda + 100))
        barra_Esquerda.setFill(color_rgb(100, 10, 10))
        barra_Esquerda.setWidth(10)
        barra_Esquerda.draw(win)

    if tecla == "Down":
        if (linha_Barra_Esquerda + 15) < 450:
            linha_Barra_Esquerda += 17
 
        barra_Esquerda.undraw()
        barra_Esquerda =Line(Point(10, linha_Barra_Esquerda), Point(10, linha_Barra_Esquerda + 100))
        barra_Esquerda.setFill(color_rgb(100, 10, 10))
        barra_Esquerda.setWidth(10)
        barra_Esquerda.draw(win)
    
    if tecla == "W" or tecla ==  "w":
        if (linha_Barra_Direita - 15) > 35:
            linha_Barra_Direita -= 17
        
        barra_Direita.undraw()
        barra_Direita = Line(Point(1590, linha_Barra_Direita), Point(1590, linha_Barra_Direita + 100))
        barra_Direita.setFill(color_rgb(100, 10, 10))
        barra_Direita.setWidth(10)
        barra_Direita.draw(win)

    if tecla == "S" or tecla == "s":
        if (linha_Barra_Direita + 15) < 450:
            linha_Barra_Direita += 17
 
        barra_Direita.undraw()
        barra_Direita =Line(Point(1590, linha_Barra_Direita), Point(1590, linha_Barra_Direita + 100))
        barra_Direita.setFill(color_rgb(100, 10, 10))
        barra_Direita.setWidth(10)
        barra_Direita.draw(win)

    
    # Esperar o ser humano reagir
    time.sleep(.07)

win.close()
