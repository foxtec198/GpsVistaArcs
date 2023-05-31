import pyautogui as pg
from time import sleep

class WhatsBot:
    def __init__(self):
        pg.PAUSE = 0.5
        self.Automa_Whats()
        
    def atalho(self, *key):
        with pg.hold(key[0]):
            pg.press(key[1])
            
    def Automa_Whats(self):
        self.atalho('win', 'm')
        pg.write('tecnobreve')
        pg.press('enter')
        self.atalho('win', 'up')
        sleep(6)
        pg.click(172, 109)
        pg.write(self.name)
        pg.press('enter')
        pg.write(self.msg)
        pg.press('enter')
        sleep(2)
        self.atalho('ctrl', 'w')

