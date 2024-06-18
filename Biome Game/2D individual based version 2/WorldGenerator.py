import numpy as np
import PerlinNoise1 as pn
from Behaviors import Behaviors
from NurcleGenerator import Nurcle
import numpy as np

class WorldGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.seawater = np.zeros((width, height))
        self.light = np.ones((width, height))
        elev_matrix = pn.generate_perlin_noise_2d((width, height), res = (2, 2))
        difference = np.max(elev_matrix) - np.min(elev_matrix)
        np.random.seed(10)
        self.norm_elev_matrix = (elev_matrix - np.min(elev_matrix))/difference

    def add_seawater(self):
        nur = Nurcle(5, 1)
        ncl = nur.matrix
        improbable_sites = np.less(np.ones([self.width, self.height]) * 0.4, self.norm_elev_matrix)
        Flag = False
        for i in range(100):
            for j in range(50):
                if self.norm_elev_matrix[i, j] <= 0.4:
                    self.seawater[i, j] = 1
                    Flag = True
                    break
            if Flag == True:
                break
        for i in range(100):
            self.seawater = Behaviors.spread(ncl, self.seawater)
            self.seawater[improbable_sites] = 0
        self.seawater[self.seawater > 0] = 1



























