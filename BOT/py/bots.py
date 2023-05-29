import pyautogui as pg
from time import sleep, strftime

class Excluir():
    def exclussão_em_massa(self):
        pg.click(1117, 334)
        pg.press('tab')
        pg.press('enter')
        sleep(5)

class Atualizar():
    def atualizar_pagina(self):
        hora = strftime("%H")
        if hora >= "08" or hora <= "18":
            pg.press('f5')
            sleep(600)
        else:
            print('Horário não permitido')