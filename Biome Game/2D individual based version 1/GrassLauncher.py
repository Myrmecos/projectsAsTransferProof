import numpy
import copy
import random

class BioInteraction:
    @staticmethod
    def grassTick(tree, soil, world):
        tree1 = copy.deepcopy(tree)
        for i in range(numpy.shape(tree)[0]):
            for j in range(numpy.shape(tree)[1]):
                if BioInteraction.is_suitable(world, tree, i, j):
                    tree1[i, j] = 1
                if random.random() > soil[i, j]*0.5 + 0.40: #if soil is good, lower death rates
                    tree1[i, j] = 0
                #else: grass1[i, j] = 0
        tree = tree1
        tree[80, 20] = 1
        return tree

    @staticmethod
    def is_suitable(world, grass, i, j):
        width, height = numpy.shape(world)
        sourced = False
        altitude_suitable = False
        if grass[max(0, i-1), j] or grass[min(i + 1, width-1), j] or grass[i, max(j - 1, 0)] or grass[i, min(j + 1, height-1)] \
                or grass[max(0, i-1), max(j - 1, 0)] or grass[min(i + 1, width-1), max(j - 1, 0)] or grass[max(0, i-1), min(j + 1, height-1)] \
                or grass[max(0, i-1), min(j + 1, height-1)]:
            sourced = True
        if world[i, j] > 0.6 and world[i, j] <= 1:
            altitude_suitable = True
        random_passed = (random.random() > 0.5)
        if sourced & altitude_suitable & random_passed:
            return True

 #next step: add marine environment
