from NurcleGenerator import Nurcle
from spicy import signal
import numpy as np

class Behaviors:
    def __init__(self):
        pass
    @staticmethod
    def spread(nurcle, object):
        object = np.minimum(signal.convolve2d(object, nurcle, 'same') + object, np.ones_like(object))
        return object
