import pyautogui as pg
from time import sleep

class WhatsBot:
    def __init__(self):
        for i in range(100):
            self.criar_grupo()
            sleep(1)
    
    def criar_grupo(self):
        # pg.click(122, 352)
        pg.write('- GPS')
        pg.press('Enter')
    
WhatsBot()