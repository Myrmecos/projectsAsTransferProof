
import numpy as np
import pygame as pg
import time
import math
import NurcleGenerator as ng
from spicy import signal
import random



class WorldDrawer:
    def __init__(self, Rmatrix, Gmatrix, Bmatrix):
        self.Rmat = Rmatrix * 255
        self.Gmat = Gmatrix * 255
        self.Bmat = Bmatrix * 255

    def drawMatrix(self, pixel_width):
        pg.init()
        shp = np.shape(self.Rmat)
        shp_screen = shp[0]*(pixel_width + 1), shp[1]*(pixel_width + 1)
        screen = pg.display.set_mode(shp_screen)
        done = False
        while not done:
            for event in pg.event.get():  # User did something
                if event.type == pg.QUIT:  # If user clicked close
                    done = True
            screen.fill((0, 0, 0))
            print(1)
            for i in range(shp[0]):
                for j in range(shp[1]):
                    col = (self.Rmat[i, j], self.Gmat[i, j], self.Bmat[i, j])
                    pg.draw.rect(screen, col, [i * pixel_width + i, j * pixel_width + j, pixel_width, pixel_width])
            pg.display.flip()
            time.sleep(0.1)


'''a = np.random.random([100, 150])*255
b = np.random.random([100, 150])*255
c = np.random.random([100, 150])*255
wd = WorldDrawer(a, b, c)
wd.drawMatrix(5)'''


def spiral_func(theta):
    A = 1
    B = 0.5
    N = 4
    numerator = A
    denominator = math.log(B * math.tan(theta/(2*N)))
    return numerator/denominator

def drawmat(mat, new_x, new_y, neg):
    if neg == 0:
        mat[new_x, new_y] = 1
    else:
        mat[-new_x, -new_y] = 1


def normal_distribution(sigma, x, mu = 0):
    lft = 1/(sigma * math.sqrt(2* math.pi))
    rht = -0.5 * ((x - mu)/sigma)**2
    res = lft * math.exp(rht)
    return res
def drawFunction(spiral_func, mat, neg = 0):
    width, height = np.shape(mat)
    origin_x = width//2
    origin_y = height//2
    n = 5000
    for i in range(1, n):
        theta = 3 * math.pi/n * i
        distance = spiral_func(theta)
        x = round(distance * math.cos(theta)*50)
        y = round(distance * math.sin(theta)*50)

        new_x = origin_x + x
        new_y = origin_y + y
        a = 10 #the x range of x value of uniform function
        xshatter = normal_distribution(1, random.uniform(-a, a))

        yshatter = normal_distribution(1, random.uniform(-a, a))
        p = 1/50 # p is the percentage of screen width where stars are shattered
        new_x += xshatter * 40
        new_y += yshatter * 40
        new_x = round(new_x)
        new_y = round(new_y)
        if new_x < width:
            if new_y < height:
                if new_x >= 0:
                    if new_y >= 0:
                        drawmat(mat, new_x, new_y, neg)
    return mat




def makespiral(width, height):
    mat = np.zeros([width, height])
    drawFunction(spiral_func, mat)
    #drawFunction(spiral_func, mat, 1)
    return mat

def convolvespiral(mat, n):
    nurcle = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    nurcle = np.ones([10, 10])
    nur = ng.Nurcle(3, 1)
    nurcle = nur.matrix
    for i in range(n):
        mat = np.minimum(signal.convolve2d(mat, nurcle, 'same') + mat, np.ones_like(mat))

    return mat
mat = makespiral(500, 300)
#mat1 = makespiral(500, 300)
#mat1 = convolvespiral(mat0, 3)
#mat2 = convolvespiral(mat0, 20)
#mat3 = convolvespiral(mat0, 30)
#mat1 = convolvespiral(mat0, 3)
#mat = convolvespiral(mat0, 1)
wd = WorldDrawer(mat, mat, mat)
wd.drawMatrix(2)




