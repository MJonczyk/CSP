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
        self.values_counter = []
        self.start_time = 0
        self.backtracking_iterations = 0
        self.forward_checking_iterations = 0
        self.backtracking_iterations_h = 0
        self.forward_checking_iterations_h = 0
        for i in range(self.dimension):
            self.values_counter.append([0, i + 1])
        for i in range(self.dimension):
            for j in range(self.dimension):
                sum = 0
                if self.constraints[0][j] != 0:
                    sum = sum + 1
                if self.constraints[1][j] != 0:
                    sum = sum + 1
                if self.constraints[2][i] != 0:
                    sum = sum + 1
                if self.constraints[3][i] != 0:
                    sum = sum + 1
                self.indices.append([i, j, sum])
                # self.indices.append([i, j, self.constraints[0][j] + self.constraints[1][j] + self.constraints[2][i] + self.constraints[3][i]])
        self.indices.sort(key=lambda x: x[2], reverse=True)
        # print(self.indices)

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

    def get_values_heuristic(self):
        return sorted(self.values_counter, key=lambda x: x[0])

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
            print("iterations: " + str(self.backtracking_iterations))
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
            print("iterations: " + str(self.backtracking_iterations_h))
            print(self.get_values_heuristic())
            return
        r, c = self.choose_square_heuristic()

        for i in self.get_values_heuristic():
            if self.is_valid(r, c, i[1]):
                self.game[r][c] = i[1]
                self.values_counter[i[1] - 1][0] = self.values_counter[i[1] - 1][0] + 1
                self.backtracking_with_heuristic(r, c)
                self.values_counter[i[1] - 1][0] = self.values_counter[i[1] - 1][0] - 1
                self.game[r][c] = 0

    def forward_checking(self):
        self.forward_checking_iterations = self.forward_checking_iterations + 1
        if self.game_solved():
            self.solutions.append(np.array(self.game, copy=True))
            print(self.game_to_int())
            print("rozwiazanie")
            print("solution time: " + str(time.time() - self.start_time))
            print("iterations: " + str(self.forward_checking_iterations))
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
            print("iterations: " + str(self.forward_checking_iterations_h))
            print(self.get_values_heuristic())
            return
        r, c = self.choose_square_heuristic()

        for i in self.get_values_heuristic():
            if self.is_valid(r, c, i[1]):
                self.game[r][c] = i[1]
                self.values_counter[i[1] - 1][0] = self.values_counter[i[1] - 1][0] + 1
                if self.columns_valid(self.dimension - 1) and self.rows_valid(self.dimension - 1):
                    self.forward_checking_with_heuristic()
                self.values_counter[i[1] - 1][0] = self.values_counter[i[1] - 1][0] - 1
                self.game[r][c] = 0

    def game_to_int(self):
        return np.array(self.game, copy=True)
