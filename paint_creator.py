import pyautogui as mouse
from time import sleep
from random import randint


class Iniciar(object):
    def __init__(self, tela_larg=1, tela_alt=1):
        self.tela_larg = tela_larg
        self.tela_alt = tela_alt
        self.tela_larg, self.tela_alt = mouse.size()
        try:
            mouse.press('win')
            sleep(2)
            mouse.typewrite('paint')
            sleep(2)
            mouse.press('enter')
            sleep(5)
            mouse.press('alt')
            sleep(1)
            mouse.typewrite('h')
            sleep(1)
            mouse.typewrite('p1')
            sleep(0.5)
            mouse.hotkey('alt', ' ')
            sleep(0.5)
            mouse.typewrite('x')
            sleep(0.5)
        except Exception as cancelamento:
            print('Processo cancelado! Erro:', cancelamento)

    def retonarTela(self):
        return self.tela_larg, self.tela_alt

    def centralizar(self):
        mouse.moveTo(init.tela_larg / 2, init.tela_alt / 2)


init = Iniciar()


def linha(direcao):
    if direcao == 1:
        mouse.dragRel(1, 0)  # direita
    elif direcao == 2:
        mouse.dragRel(-1, 0)  # esquerda
    elif direcao == 3:
        mouse.dragRel(0, 1)  # baixo
    elif direcao == 4:
        mouse.dragRel(0, -1)  # cima


def diagonal(direcao):
    if direcao == 1:
        mouse.dragRel(1, 1)  # sudeste
    elif direcao == 2:
        mouse.dragRel(-1, -1)  # noroeste
    elif direcao == 3:
        mouse.dragRel(1, -1)  # nordeste
    elif direcao == 4:
        mouse.dragRel(-1, 1)  # sudoeste


def c():
    try:
        mouse.PAUSE = 0.01
        init.centralizar()
        fim = 5000
        while fim > 0:
            x = randint(-30, 30)
            y = randint(-30, 30)
            z = randint(1, 3)
            if z == 1:
                mouse.dragRel(x, 0)
            else:
                mouse.dragRel(0, y)
            posicao_x, posicao_y = mouse.position()
            if posicao_y > 600 or posicao_y < 191 or posicao_x > 1341 or posicao_x < 100 and posicao_y < 100:
                init.centralizar()
                continue
            fim -= 1

    except Exception as cancelamento:
        print('Processo cancelado! Erro:', cancelamento)
    finally:
        mouse.PAUSE = 0.1
        mouse.mouseUp()


c()
