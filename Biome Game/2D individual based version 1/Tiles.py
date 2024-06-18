import pygame
import numpy
import time

WIDTH = 120 * 2
HEIGHT = 70 * 2

class Tiles:
    width = 5
    height = 5
    Sealevel = 0.5
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def drawWorld(normalizedNoise, grass, soil, screen, myTile):
        width, height = numpy.shape(normalizedNoise)
        soil = Tiles.tickSoil(soil, grass)
        print("draw World used")
        for i in range(width):
            for j in range(height):
                #print(j)
                #if i == 2: return
                myTile.drawGroundWithShadow([i * myTile.height + i, j * myTile.width + j], normalizedNoise[i, j], screen, normalizedNoise, (i, j), grass, soil)

                if i == 80 and j == 20:
                    print(soil[80, 20])
                    time.sleep(0)

    @staticmethod
    def drawTile(latlong, elevation, screen):
        #tileType[0] for elevation, [1] for water, [2] for brightness
        #world is screen, tiletype is the string name of tile type
        Tiles.drawGroundWithShadow(latlong, elevation, screen)
        #drawWater(tileType, world)



    def drawGround(self, latlong, elevation, screen):
        add = 0
        R, G, B = (155* elevation, 200*elevation + 55, 20 + 180 + 55 * elevation)
        if elevation > 0.5:
            R += 10
            G += 10
            B += 10

        R = min(R, 255)
        G = min(G, 255)
        B = min(B, 255)



        pygame.draw.rect(screen, (R, G, B), [latlong[0], latlong[1], self.width, self.height])  # x, y
        #pygame.draw.rect(screen, (155 * elevation, 200 * elevation + 55,0), [latlong[0], latlong[1], Tiles.width, Tiles.height])  # x, y
        #pygame.draw.rect(screen, (min(155* elevation + add, 255), min(200*elevation + 55, 255), min(20 + 180 + 55 * elevation + add, 255)), [latlong[0], latlong[1], Tiles.width, Tiles.height])  # x, y

    def drawGroundWithShadow(self, latlong, elevation, screen, world, pos, grass, soil):
        R, G, B = (155 * elevation, 200 * elevation + 55, 20 + 180 + 55 * elevation)
        if elevation > 0.5:
            R += 150
            G += 40
            B += 0
        x, y = pos
        print(x, y)
        if soil[x, y] > 0 and grass[x, y] == 0:
            R -= 100 * soil[x, y]
            G -= 100 * soil[x, y]
            B -= 100 * soil[x, y]
        if Tiles.lowerAtTile(world, pos, -1, -1) and elevation > Tiles.Sealevel:
            R -= 80*elevation
            G -= 80*elevation
            B -= 80*elevation
            if elevation < Tiles.Sealevel:
                R += 15
                G += 15
                B += 15


            #pygame.draw.rect(screen, 'black', [latlong[0], latlong[1], Tiles.width, Tiles.height])  # x, y

        R = max(min(R, 255), 0)
        G = max(min(G, 255), 0)
        B = max(min(B, 255), 0)
        if grass[pos[0], pos[1]] != 0:
            G = max(R, B, G) - 40
            R = B = 0
            G = max(min(G, 255), 0)
        #R = max(min(R, 255), 0)
        #G = max(min(G, 255), 0)
        #B = max(min(B, 255), 0)

        print(self.width, self.height)
        pygame.draw.rect(screen, (max(R, G), max(R, G), B), [latlong[0], latlong[1], self.width, self.height])  # x, y

    def drawGrass(self, latlong, elevation, screen):
        #col = 200 + elevation
        #if col > 240:
            #col = 240
        pygame.draw.rect(screen, (0, min(240*(1-elevation + 0.5), 255), 10) ,
                         [latlong[0], latlong[1], self.width, self.height])

    @staticmethod
    def lowerAtTile(world, pos, p, q):
        #p, q: the block that's supposed to block light.
        width = numpy.shape(world)[0]
        height = numpy.shape(world)[1]
        x = pos[0]
        y = pos[1]
        currentHeight = world[x, y]
        truth = (x - p < width) and x - p > 0 and (y - q < height) and y - p > 0
        if truth:
            blockingHeight = world[x - p, y - q]
            if currentHeight < blockingHeight:
                return True
        return False

    @staticmethod
    def tickSoil(soil, grass):
        soil += 0.05 * grass
        soil = numpy.minimum(soil, numpy.ones_like(soil))
        return soil

if __name__ == '__main__':
    soil = numpy.zeros((WIDTH, HEIGHT))
    print(soil)
    grass = numpy.zeros((WIDTH, HEIGHT))
    soil = Tiles.tickSoil(soil, grass)
    print(soil)
