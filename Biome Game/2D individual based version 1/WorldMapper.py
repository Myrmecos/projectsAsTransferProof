#obj: add: grass should be controlled by shadows
#add: soil. grass have high mortality if on soil
#add: play designate a block to place grass


import numpy
import GrassLauncher as GL
import pygame
import Tiles
import time
#import PerlinNoise
import PerlinNoise1
SQUAREWIDTH = 5
WIDTH = 120 * 2 * 5 //SQUAREWIDTH
HEIGHT = 70 * 2 * 5 //SQUAREWIDTH
print(WIDTH, HEIGHT)
#world = numpy.round(numpy.random.random((WIDTH, HEIGHT))*240)
#world = abs(PerlinNoise.generate_perlin_noise(WIDTH, HEIGHT, 2)*175)
numpy.random.seed(40)
world = (PerlinNoise1.generate_perlin_noise_2d((WIDTH, HEIGHT), res = (2, 2)) + 0.2) * 120
soil = numpy.zeros((WIDTH, HEIGHT))

tree = numpy.zeros((WIDTH, HEIGHT))
tree[80, 20] = 1;
class WorldMapper:
    @staticmethod
    def normalizeNoise(noise):
        minNoise = numpy.min(noise)
        noiseRng = numpy.max(noise) - minNoise
        noise = (noise - minNoise)/noiseRng
        return noise


    def drawWorld(normalizedNoise, tree):
        pygame.init()
        size = [WIDTH*(SQUAREWIDTH + 1), HEIGHT*(SQUAREWIDTH + 1)]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("New Biome!")
        # Loop until the user clicks the close button.
        done = False
        clock = pygame.time.Clock()

        myTile = Tiles.Tiles(SQUAREWIDTH,SQUAREWIDTH)

        #while not done:
        i = 0
        frm = 20
        t0 = time.time()
        while i < frm:
            i += 1
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
            # Clear the screen and set the screen background
            screen.fill((0, 60, 0))

            Tiles.Tiles.drawWorld(normalizedNoise, tree, soil, screen, myTile)
            tree = GL.BioInteraction.grassTick(tree, soil, normalizedNoise)

            pygame.display.flip()

            time.sleep(0.01)
            print("one tick")
        pygame.quit()
        t1 = time.time()
        print((t1 - t0)/frm)

if __name__ == "__main__":
    nml = WorldMapper.normalizeNoise(world)
    WorldMapper.drawWorld(nml, tree)