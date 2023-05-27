import pyautogui as pg
from time import sleep, strftime

class Excluir():
    def exclussão_em_massa(self):
        # pg.click(1084, 358)
        img = pg.locateCenterOnScreen('trash.png', confidence=0.7)
        pg.click(img.x, img.y)
        pg.press('tab')
        pg.press('enter')
        sleep(1.5)

class Atualizar():
    def atualizar_pagina(self):
        self.hora = strftime("%H")
        if self.hora >= "08" or self.hora <= "18":
            pg.press('f5')
            sleep(2)
        else:
            print('Horário não permitido')
            
while True:
    Excluir().exclussão_em_massa()