import pygame as pg
import os, time, random
times_run = 0
pg.init()
WIN , HEI = 360, 480
inital_x, inital_y = 0, 0
inital_x2, inital_y2 = (0,HEI//2)
window = pg.display.set_mode((WIN, HEI), 0, 32)

class color_dector:
    def __init__(self, x, y, size:tuple):
        self.x = x
        self.y = y
        self.size = size
s = color_dector(inital_x, inital_y, (1, 1))
s2 = color_dector(inital_x2, inital_y2, (1,1))
golf = pg.Surface((s.size))
golf2 = pg.Surface((s2.size))
golf.fill((0, 255, 255))
window.fill((0,0,0))
color = ()
Run = True
color_list = []
while Run:
    pos = (s.x, s.y)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pg.draw.line(window, color, pos, pos, 1)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pos2 = (s2.x, s2.y)
    pg.draw.line(window, color, pos2, pos2, 1)
    #pg.draw.line(window)

    s.x += 1
    s2.x +=1
    window.blit(golf, (s.x, s.y))
    window.blit(golf2, (s2.x, s2.y))
    if s.x > WIN and s.y < HEI//2:
        s.x = 0
        s.y += 1
    if s2.x > WIN and s.y < HEI:
        s2.x = 0
        s2.y +=1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                Run = False
                print("Ended!!")
    pg.display.flip()