import pyautogui as pg
import os
import time

caminho_pasta = 'C:\Prints_Campanhas_Robo'

def iniciar():
    pg.press('win')
    time.sleep(1)
    pg.write('chrome')
    pg.press('enter')
    time.sleep(2)
    pg.write("https://www.poder360.com.br")
    pg.press("enter")


def printscreen(nome_arquivo):
    printscreen = pg.screenshot()
    printscreen.save(os.path.join(caminho_pasta,f'{nome_arquivo}.png'))


def res970_90():
    pg.press('down', presses = 9)
    time.sleep(1.5)
    printscreen('970_90')


def res1248_250():
    pg.press('pgup', presses = 3)
    time.sleep(3)
    printscreen('1248_250')