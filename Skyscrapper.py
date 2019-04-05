import numpy as np


class Skyscrapper:
    def __init__(self, dimension, constraints):
        self.dimension = dimension
        self.constraints = constraints
        self.game = np.zeros((dimension, dimension))
