import time
import numpy as np
import pygame as pg
import NurcleGenerator as ng

class WorldMapper:
    def __init__(self, elevation, object, screen, width):
        #elevation: the matrix of elevation at each grid, for coloring
        #screen (pygame): where to color the world
        #width: width of each square in a grid
        self.elevation = elevation
        self.object = object
        self. screen = screen
        self. width = width

    def drawWorld(self, Tile):
        w, h = np.shape(self.object)
        for i in range(w):
            for j in range(h):
                self.drawTile(Tile, i, j)
        pg.display.flip()

    def plainDraw(self):
        #just draw
        pass

    def drawTile(self, Tile, i, j):
        R, G, B = [0, 0, 0]
        if Tile == "Grass":
            G += 250 * self.object[i, j]
        if Tile == "Tree":
            G += 50 * object[i, j]
        if Tile == "Coral":
            B += 150 * object[i, j]
        if Tile == "Bare Land":
            B = G = 200 * object[i, j]
        if Tile == "Soil":
            R += 150 * object[i, j]
            B += 150 * object[i, j]
        if Tile == "Test":
            R = B = G = 255
        R = min(255, R)
        B = min(255, B)
        G = min(255, G)
        self.colorSquare((R, G, B), i, j)

    def colorSquare(self, RGB, i, j):
        hue = self.elevation[i, j]
        col = np.array(RGB)*hue
        pg.draw.rect(self.screen, col,
                         [i*self.width + i, j*self.width + j, self.width, self.width])

    @staticmethod
    def drawMatrix(matrix, w = 10):
        pg.init()
        screen = pg.display.set_mode(shp * (w + 1))
        wm = WorldMapper(matrix, matrix, screen, w)
        done = False
        while not done:
            for event in pg.event.get():  # User did something
                if event.type == pg.QUIT:  # If user clicked close
                    done = True
            print("one flip")
            screen.fill((0, 60, 0))
            wm.drawWorld("Test")
            pg.display.flip()
            time.sleep(3)
            wm.object = update_object(nurcle, wm.object)
        pg.quit()


if __name__ == "__main__":
    shp = np.array([100, 50])
    w = 10
    elevation = np.ones(shp)
    object = np.zeros(shp)
    def update_object(nurcle, object):
        object = np.minimum(signal.convolve2d(object, nurcle, 'same') + object, np.ones_like(object))
        return object
    def drawArray(object, nurcle):
        pg.init()
        screen = pg.display.set_mode(shp*(w + 1))
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
            time.sleep(3)
            wm.object = update_object(nurcle, wm.object)
        pg.quit()

    from spicy import signal
    nurcle = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    nurcle = np.ones([10, 10])
    nur = ng.Nurcle(3, 1)
    nurcle = nur.matrix
    print(nurcle)
    #for i in [0, 1, 8, 9]:nurcle[0, i] = 0; nurcle[9, i] = 0
    #for i in [1, 8]: nurcle[i, 0] = nurcle[i, 9] = 0

    A = np.zeros(shp)
    B = np.zeros(shp)
    A[30, 30] = 1
    A[10, 5] = 1
    A[15, 6] = 1
    A[19, 9] = 1
    #A1 = signal.convolve2d(A, nurcle, 'same')
    #for i in range(1):
        #A1 = signal.convolve2d(A1, nurcle, 'same')

    drawArray(A, nurcle)













