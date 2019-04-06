import numpy as np


class Futoshiki:
    def __init__(self, dimension, game, relations):
        self.dimension = dimension
        self.game = game
        self.relations = relations

    def available_row_values(self, row):
        values = np.arange(1, self.dimension + 1)
        row_values = []
        for i in range(self.dimension):
            if self.game[row][i] != 0:
                row_values.append(self.game[row][i] - 1)
        return np.delete(values, row_values)

    def available_column_values(self, column):
        values = np.arange(1, self.dimension + 1)
        column_values = []
        for i in range(self.dimension):
            if self.game[i][column] != 0:
                column_values.append(self.game[i][column] - 1)
        return np.delete(values, column_values)

    def available_values(self, row, column):
        return np.intersect1d(np.intersect1d(self.available_row_values(row), self.available_column_values(column)),
                              self.check_relations(row, column))

    def check_relations(self, row, column):
        values = np.arange(1, self.dimension + 1)
        index_values = np.arange(self.dimension)
        for rel in self.relations:
            if (row, column) in rel:
                index = rel.index((row, column))
                if index == 0:
                    if self.game[rel[1][0]][rel[1][1]] != 0:
                        index_values = [iv for iv in index_values if iv > self.game[rel[1][0]][rel[1][1]]]
                    else:
                        index_values = [iv for iv in index_values if iv == self.dimension - 1]
                else:
                    if self.game[rel[0][0]][rel[0][1]] != 0:
                        index_values = [iv for iv in index_values if iv < self.game[rel[0][0]][rel[0][1]]]
                    else:
                        index_values = [iv for iv in index_values if iv == 1]
        return np.delete(values, index_values)

    def is_solved(self):
        values = np.arange(1, self.dimension + 1)
        for r in self.game:
            if np.intersect1d(r, values).size != self.dimension:
                return False
        for c in self.game.T:
            if np.intersect1d(c, values).size != self.dimension:
                return False
        for rel in self.relations:
            if self.game[rel[0][0]][rel[0][1]] > self.game[rel[1][0]][rel[1][1]]:
                return False
        return True
#kodkoamdiwmpdamdpawoidmpawdmpaidmwpaidnpwiadnapidnpwiadndpa
#fowjfowfwfnowfnofinqwpfoinfne0ifiownfiwnfowfnieowfowef
