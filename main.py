from functions import *
import pyautogui as pg
import time

iniciar()
time.sleep(1.5)
res970_90()
time.sleep(1)

fecha_campanha = pg.locateOnScreen('dropdown.png')

if fecha_campanha:
    x, y = pg.center(fecha_campanha)
    pg.click(x, y)

res1248_250()
pg.hotkey('alt','f4')