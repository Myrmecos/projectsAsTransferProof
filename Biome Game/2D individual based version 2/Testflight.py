import numpy as np
import pygame as pg
import time
from WorldGenerator import WorldGenerator as WG
from WorldMapper import WorldMapper
A = np.zeros([3, 3])
B = np.ones([3, 3])

B[2, 2] = -1

print(np.minimum(A, B))
np.random.seed(10)
shp = np.array([100, 50])
w = 10
elevation = np.ones(shp)
object = np.zeros(shp)

def drawArray():
    pg.init()
    wg = WG(shp[0], shp[1])
    wg.add_seawater()
    object = wg.seawater
    screen = pg.display.set_mode(shp * (w + 1))
    wm = WorldMapper(elevation, object, screen, w)

    done = False
    while not done:
        for event in pg.event.get():  # User did something
            if event.type == pg.QUIT:  # If user clicked close
                done = True
        print("one flip")
        screen.fill((0, 60, 0))
        wm.drawWorld("Grass")
        pg.display.flip()
        time.sleep(2)
    pg.quit()

drawArray()
