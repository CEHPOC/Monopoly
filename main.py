import pygame as pg
from Player import Player
from Tiles import Tiles
from display import Display

FPS=20

dsp= Display()

clock = pg.time.Clock()

tiles=Tiles()
green=Player(1)
red=Player(2)
state=False

msg=""

running = True
while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                dsp.turn=(dsp.turn+1)%4
                state=True
        if event.type == pg.QUIT:
            running = False

    #обработка
    if state:
        state,msg=dsp.processing(green,red,tiles)

        if green.money < 0:
            print("Зеленый стал банкротом")
            running = False
        elif red.money < 0:
            print("Красный стал банкротом")
            running = False

    #рисовка
    dsp.draw(green,red,tiles,msg)

pg.quit()
