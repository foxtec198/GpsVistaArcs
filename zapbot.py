import pyautogui as pg
from time import sleep

class WhatsBot:
    def __init__(self):
        pg.PAUSE = 0.5
        self.Automa_Whats()
        # print(pg.position())
    
    def atalho(self, *key):
        with pg.hold(key[0]):
            pg.press(key[1])
            
    def Automa_Whats(self):
        self.atalho('win', 'm')
        pg.write('tecnobreve')
        pg.press('enter')
        self.atalho('win', 'up')
        sleep(5)
        pg.click(172, 109)
        pg.write('Gui GPS')
        pg.press('enter')
        pg.write(self.msg)
        pg.press('enter')
        sleep(1)
        self.atalho('ctrl', 'w')
    
WhatsBot.msg = 'Ola tudo bem com você?'
WhatsBot()