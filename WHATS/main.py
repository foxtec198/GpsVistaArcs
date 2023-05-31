from botwhats import WhatsBot as wt
from openpyxl import load_workbook as lw

pln = lw(r'WHATS/clb.xlsx')
ws = pln.active

for i in range(2, 1000):
    nome = ws[f'A{i}'].value
    mesr = 'Marco'
    if nome != None:
        wt.name = nome
        nm = nome.split()
        nm = nm[0].capitalize()
        wt.msg = f"""Oiiie {nm}, Me chamo Guilherme, Sou assistente de projetos da Denise.
        Verifiquei aqui que voce tem folhas em pendentes no aplicativo GPSvc.
        Essas folhas são relativas a {mesr}, conto com sua ajuda para assinalar !!!"""
        wt()