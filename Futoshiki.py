import numpy as np


class Futoshiki:
    def __init__(self, dimension, game, relations):
        self.dimension = dimension
        self.game = game
        self.relations = relations
        self.solutions = []

    def game_solved(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.game[i][j].value == 0:
                    return False
        return True

    def available_row_values2(self, row):
        values = np.arange(1, self.dimension + 1)
        row_values = []
        for i in range(self.dimension):
            if self.game[row][i].value != 0:
                row_values.append(self.game[row][i].value - 1)
        return np.delete(values, row_values)

    def available_row_values(self, row):
        values = np.arange(1, self.dimension + 1)
        r = [ri.value for ri in self.game[row]]
        return [v for v in values if v not in r]

    def available_column_values2(self, column):
        values = np.arange(1, self.dimension + 1)
        column_values = []
        for i in range(self.dimension):
            if self.game[i][column].value != 0:
                column_values.append(self.game[i][column].value - 1)
        return np.delete(values, column_values)

    def available_column_values(self, column):
        values = np.arange(1, self.dimension + 1)
        c = [ri.value for ri in self.game.T[column]]
        return [v for v in values if v not in c]

    def available_values2(self, row, column):
        return np.intersect1d(np.intersect1d(self.available_row_values(row), self.available_column_values(column)),
                              self.check_relations(row, column))

    def available_values(self, row, column):
        values = np.arange(1, self.dimension + 1)
        r = self.available_row_values(row)
        c = self.available_column_values(column)
        rel = self.check_relations(row, column)
        return [v for v in values if v in r and v in c and v in rel]

    def not_empty_domains(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.game[i][j].value == 0:
                    if len(self.available_values(i, j)) == 0:
                        return False
        return True

    def check_relations(self, row, column):
        values = np.arange(1, self.dimension + 1)
        for rel in self.game[row][column].relations:
            index = rel.index((row, column))
            if index == 0:
                if self.game[rel[1][0]][rel[1][1]].value != 0:
                    values = [v for v in values if v < self.game[rel[1][0]][rel[1][1]].value]
                else:
                    values = [v for v in values if v != self.dimension]
            else:
                if self.game[rel[0][0]][rel[0][1]].value != 0:
                    values = [v for v in values if v > self.game[rel[0][0]][rel[0][1]].value]
                else:
                    values = [v for v in values if v != 1]
        return values

    def game_solved_correctly(self):
        values = np.arange(1, self.dimension + 1)
        for r in self.game:
            if np.intersect1d([ri.value for ri in r], values).size != self.dimension:
                return False
        for c in self.game.T:
            if np.intersect1d([ci.value for ci in c], values).size != self.dimension:
                return False
        for rel in self.relations:
            if self.game[rel[0][0]][rel[0][1]].value > self.game[rel[1][0]][rel[1][1]].value:
                return False
        return True

    def choose_square(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.game[i][j].value == 0:
                    return i, j
        return 0, 0

    def forward_checking(self):
        if self.game_solved():
            self.solutions.append(np.copy(self.game))
            print(self.game_to_int())
            print(self.game_solved_correctly())
            print("rozwiazanie")
            return
        r, c = self.choose_square()
        # print(self.available_values(r, c).size)
        # print(self.game_to_int())
        # print("elo")
        if not self.not_empty_domains():
            # print("no values")
            return

        for i in self.available_values(r, c):
            self.game[r][c].value = i
            self.forward_checking()
        self.game[r][c].value = 0
        # print("koniec metody")

    def backtracking(self):
        if self.game_solved():
            self.solutions.append(np.copy(self.game))
            print(self.game_to_int())
            print(self.game_solved_correctly())
            print("rozwiazanie")
            return
        r, c = self.choose_square()
        # print(self.available_values(r, c).size)
        # print(self.game)
        if len(self.available_values(r, c)) == 0:
            # print("no values")
            return

        for i in self.available_values(r, c):
            self.game[r][c].value = i
            self.backtracking()
        self.game[r][c].value = 0
        # print("koniec metody")

    def game_to_int(self):
        board = np.empty((self.dimension, self.dimension), dtype=object)
        i = 0
        for r in self.game:
            board[i] = [ri.value for ri in r]
            i = i + 1
        return board
