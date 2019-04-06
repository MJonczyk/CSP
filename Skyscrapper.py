import numpy as np


class Skyscrapper:
    def __init__(self, dimension, constraints):
        self.dimension = dimension
        self.constraints = constraints
        self.game = np.zeros((dimension, dimension))

    def available_row_values(self, row):
        values = np.arange(1, self.dimension + 1)
        row_values = []
        for i in range(self.dimension):
            if self.game[row][i] != 0:
                row_values.append(self.game[row][i] - 1)
            print(row_values)
        return np.delete(values, row_values)

    def available_column_values(self, column):
        values = np.arange(1, self.dimension + 1)
        column_values = []
        for i in range(self.dimension):
            if self.game[i][column] != 0:
                column_values.append(self.game[i][column] - 1)
            print(column_values)
        return np.delete(values, column_values)

    def is_solved(self):
        values = np.arange(1, self.dimension + 1)
        for r in self.game:
            if np.intersect1d(r, values).size != self.dimension:
                return False
        for c in self.game.T:
            if np.intersect1d(c, values).size != self.dimension:
                return False
        """check number of visible skyscrapers"""
        return True
