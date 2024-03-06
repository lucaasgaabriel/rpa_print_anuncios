from functions import *
import pyautogui as pg
import time


def main():
    iniciar()
    time.sleep(2.5)
    res970_90()
    time.sleep(1)

    fecha_campanha = pg.locateOnScreen('dropdown.png')

    if fecha_campanha:
        x, y = pg.center(fecha_campanha)
        pg.click(x, y)

    res1248_250()
    pg.hotkey('alt','f4')

if __name__ == '__main__':
    main()