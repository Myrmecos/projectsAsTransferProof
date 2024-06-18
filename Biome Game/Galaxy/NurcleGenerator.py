import numpy as np
import math

class Nurcle:
    def __init__(self, radius, fecundity):
        #radius is the radius of dispersal from pre-existing adult individual (1/2 width of matrix)
        #fecundity is the total offspring produced (area under normal curve)
        self.radius = radius
        self.fecundity = fecundity
        width = 2 * radius + 1
        self.matrix = np.zeros([width, width])
        mid = radius
        for i in range(width):
            for j in range(width):
                dis = math.sqrt((i - mid)**2 + (j - mid)**2)
                perc = dis/radius * 4
                self.matrix[i, j] = Nurcle.normal_distribution(radius/4, perc)*fecundity

    @staticmethod
    def normal_distribution(sigma, x, mu = 0):
        lft = 1/(sigma * math.sqrt(2* math.pi))
        rht = -0.5 * ((x - mu)/sigma)**2
        res = lft * math.exp(rht)
        return res
