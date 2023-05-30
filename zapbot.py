import pyautogui as pg
from time import sleep
from selenium import webdriver as wb

class WhatsBot:
    def __init__(self):
        pass
    
    def Automa_Whats(self):
        nv = wb.Chrome()
    
    def criar_grupo(self):
        pg.write('- GPS')
        pg.press('Enter')
    
WhatsBot().Automa_Whats()