import numpy as np
from Square import Square


class Loader:
    def load_futoshiki(self, filename):
        with open(filename) as f:
            data = [line.rstrip() for line in f]

        dimension = int(data[0][0])
        game = np.empty((dimension, dimension), dtype=Square)
        relations = []
        temp_relations = data[3 + dimension:]

        for i in range(dimension):
            row = data[2 + i].split(';')
            for j in range(dimension):
                game[i][j] = Square(int(row[j]))

        for rel in temp_relations:
            current_relation = rel.split(';')
            index_relation = ((ord(current_relation[0][0]) - 65, int(current_relation[0][1]) - 1),
                              (ord(current_relation[1][0]) - 65, int(current_relation[1][1]) - 1))
            game[index_relation[0][0]][index_relation[0][1]].relations.append(index_relation)
            game[index_relation[1][0]][index_relation[1][1]].relations.append(index_relation)
            relations.append(index_relation)

        return dimension, game, relations

    def load_skyscrapper(self, filename):
        with open(filename) as f:
            data = [line.rstrip() for line in f]

        dimension = int(data[0][0])
        constraints = np.empty((dimension, dimension))

        for i in range(4):
            row = data[1 + i].split(';')
            constraint = []
            for j in range(dimension):
                constraint.append(int(row[j + 1]))
            constraints[i] = constraint

        return dimension, constraints
