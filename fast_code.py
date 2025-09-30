import pygame as pg
import os, time, random
pg.init()
WIN , HEI = 360, 480
inital_x, inital_y = 0, 0
window = pg.display.set_mode((WIN, HEI), 0, 32)
class color_dector:
    def __init__(self, x, y, size:tuple):
        self.x = x
        self.y = y
        self.size = size
s = color_dector(inital_x, inital_y, (1, 1))
golf = pg.Surface((s.size))
golf.fill((0, 255, 255))
window.fill((0,0,0))
color = ()
Run = True
number_of_colors = WIN*HEI

color_list = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for i in range(number_of_colors+1)]
def main_function(color):
    pos = (s.x, s.y)
    
    pg.draw.line(window, color, pos, pos, 1)
    #pg.draw.line(window)

    s.x += 1
    window.blit(golf, (s.x, s.y))
    if s.x > WIN:
        s.x = 0
        s.y += 1
while Run:
    for color in color_list:
        main_function(color)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                Run = False
                print("Ended!!")
    pg.display.flip()

print(len(color_list))