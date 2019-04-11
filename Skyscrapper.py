import numpy as np
from collections import Counter
import time


class Skyscrapper:
    def __init__(self, dimension, constraints):
        self.dimension = dimension
        self.constraints = constraints
        self.game = np.zeros((dimension, dimension))
        self.solutions = []
        self.indices = []
        self.start_time = 0
        self.backtracking_iterations = 0
        self.forward_checking_iterations = 0
        self.backtracking_iterations_h = 0
        self.forward_checking_iterations_h = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.indices.append([i, j, self.constraints[0][i] + self.constraints[1][i] + self.constraints[2][j]
                                     + self.constraints[3][j]])
        self.indices.sort(key=lambda x: x[2], reverse=True)

    def game_solved(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.game[i][j] == 0:
                    return False
        return True

    def init_time(self):
        self.start_time = time.time()

    def is_valid_row(self, row, e):
        return all([e != self.game[row][ri] for ri in range(self.dimension)])

    def is_valid_column(self, column, e):
        return all([e != self.game[ci][column] for ci in range(self.dimension)])

    def is_valid_upper(self, column):
        if self.constraints[0][column] == 0:
            return True
        visible = 0
        for i in range(self.dimension):
            is_visible = True
            if self.game[i][column] == 0:
                return True
            for j in range(i):
                if not self.game[i][column] > self.game[j][column]:
                    is_visible = False
            if is_visible:
                visible = visible + 1
        return visible == self.constraints[0][column]

    def is_valid_lower(self, column):
        if self.constraints[1][column] == 0:
            return True
        visible = 0
        for i in range(self.dimension - 1, -1, -1):
            is_visible = True
            if self.game[i][column] == 0:
                return True
            for j in range(self.dimension - 1, i, -1):
                if not self.game[i][column] > self.game[j][column]:
                    is_visible = False
            if is_visible:
                visible = visible + 1
        return visible == self.constraints[1][column]

    def is_valid_left(self, row):
        if self.constraints[2][row] == 0:
            return True
        visible = 0
        for i in range(self.dimension):
            is_visible = True
            if self.game[row][i] == 0:
                return True
            for j in range(i):
                if not self.game[row][i] > self.game[row][j]:
                    is_visible = False
            if is_visible:
                visible = visible + 1
        return visible == self.constraints[2][row]

    def is_valid_right(self, row):
        if self.constraints[3][row] == 0:
            return True
        visible = 0
        for i in range(self.dimension - 1, -1, -1):
            is_visible = True
            if self.game[row][i] == 0:
                return True
            for j in range(self.dimension - 1, i, -1):
                if not self.game[row][i] > self.game[row][j]:
                    is_visible = False
            if is_visible:
                visible = visible + 1
        return visible == self.constraints[3][row]

    def is_valid(self, row, column, e):
        row_valid = all([e != self.game[row][ri] for ri in range(self.dimension)])
        if row_valid:
            column_valid = all([e != self.game[ci][column] for ci in range(self.dimension)])
            if column_valid:
                return True
        return False

    def choose_square(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.game[i][j] == 0:
                    return i, j
        return -1, -1

    def choose_square_heuristic(self):
        for i in self.indices:
            if self.game[i[0]][i[1]] == 0:
                return i[0], i[1]
        return -1, -1

    def columns_valid(self, column):
        for i in range(0, column + 1):
            if not self.is_valid_lower(i):
                return False
            if not self.is_valid_upper(i):
                return False
        return True

    def rows_valid(self, row):
        for i in range(0, row + 1):
            if not self.is_valid_left(i):
                return False
            if not self.is_valid_right(i):
                return False
        return True

    def helper_row(self):
        for i in range(0, self.dimension):
            x = Counter(self.game[i])
            del x[0.0]
            for key in x:
                if x[key] != 1:
                    return False
        return True

    def helper_column(self):
        for i in range(0, self.dimension):
            x = Counter(self.game.T[i])
            del x[0.0]
            for key in x:
                if x[key] != 1:
                    return False
        return True

    def unique_board(self):
        return self.helper_column() and self.helper_row()

    def backtracking(self, row=0, column=0):
        self.backtracking_iterations = self.backtracking_iterations + 1
        if not self.rows_valid(row):
            return
        if not self.columns_valid(column):
            return
        if self.game_solved():
            self.solutions.append(np.array(self.game, copy=True))
            print(self.game_to_int())
            print("rozwiazanie")
            print("solution time: " + str(time.time() - self.start_time))
            return
        r, c = self.choose_square()

        for i in range(1, self.dimension + 1):
            if self.is_valid(r, c, i):
                self.game[r][c] = i
                self.backtracking(r, c)
                self.game[r][c] = 0

    def backtracking_with_heuristic(self, row=0, column=0):
        self.backtracking_iterations_h = self.backtracking_iterations_h + 1
        if not self.rows_valid(row):
            return
        if not self.columns_valid(column):
            return
        if self.game_solved():
            self.solutions.append(np.array(self.game, copy=True))
            print(self.game_to_int())
            print("rozwiazanie")
            print("solution time: " + str(time.time() - self.start_time))
            return
        r, c = self.choose_square_heuristic()

        for i in range(1, self.dimension + 1):
            if self.is_valid(r, c, i):
                self.game[r][c] = i
                self.backtracking_with_heuristic(r, c)
                self.game[r][c] = 0

    def forward_checking(self):
        self.forward_checking_iterations = self.forward_checking_iterations + 1
        if self.game_solved():
            self.solutions.append(np.array(self.game, copy=True))
            print(self.game_to_int())
            print("rozwiazanie")
            print("solution time: " + str(time.time() - self.start_time))
            return
        r, c = self.choose_square()

        for i in range(1, self.dimension + 1):
            if self.is_valid(r, c, i):
                self.game[r][c] = i
                if self.columns_valid(self.dimension - 1) and self.rows_valid(self.dimension - 1):
                    self.forward_checking()
                self.game[r][c] = 0

    def forward_checking_with_heuristic(self):
        self.forward_checking_iterations_h = self.forward_checking_iterations_h + 1
        if self.game_solved():
            self.solutions.append(np.array(self.game, copy=True))
            print(self.game_to_int())
            print("rozwiazanie")
            print("solution time: " + str(time.time() - self.start_time))
            return
        r, c = self.choose_square_heuristic()

        for i in range(1, self.dimension + 1):
            if self.is_valid(r, c, i):
                self.game[r][c] = i
                if self.columns_valid(self.dimension - 1) and self.rows_valid(self.dimension - 1):
                    self.forward_checking_with_heuristic()
                self.game[r][c] = 0

    def game_to_int(self):
        return np.array(self.game, copy=True)
