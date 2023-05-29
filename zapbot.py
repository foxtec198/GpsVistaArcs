from selenium import webdriver
from time import sleep

class WhatsBot:
    def __init__(self):
        self.msg = ''
        self.ctt = ['43996617904']
        op =  webdriver.ChromeOptions()
        op.add_argument('lang = pt-br')
        self.driver = webdriver.Chrome(executable_path=r'driver.exe')
        