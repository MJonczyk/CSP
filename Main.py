from Loader import Loader
from Futoshiki import Futoshiki
import time
import numpy as np

loader = Loader()
(dimension, game, relations) = loader.load_futoshiki('research_data/test_futo_6_0.txt')
futoshiki = Futoshiki(dimension, game, relations)
# print(futoshiki.game)
start = time.time()
futoshiki.backtracking()
end = time.time()
print("backtracking time: " + str(end - start))
start = time.time()
futoshiki.forward_checking()
end = time.time()
print("forward_checking time: " + str(end - start))
print(len(futoshiki.solutions))
# for i in range(len(futoshiki.solutions)):
#     print(futoshiki.solutions[i])
# print(game)
# print(futoshiki.game)
# print(futoshiki.game_solved())
# print(relations)
# print("rel(3,3) = " + str(futoshiki.check_relations(3, 3)))
# print(futoshiki.available_row_values(3))
# print(futoshiki.available_column_values(3))
# print(futoshiki.available_values(3, 3))
# print("rel(2,3) = " + str(futoshiki.check_relations(2, 3)))
# print(futoshiki.available_row_values(2))
# print(futoshiki.available_column_values(3))
# print(futoshiki.available_values(2, 3))
# print("rel(0,0) = " + str(futoshiki.check_relations(0, 0)))
# print(futoshiki.available_row_values(0))
# print(futoshiki.available_column_values(0))
# print(futoshiki.available_values(0, 0))
# other_game = np.array([[0., 0., 0., 3.], [0., 1., 0., 2.], [2., 0., 0., 4.], [4., 2., 3., 0.]])
# other_game = np.array([[1., 2., 4., 3.], [3., 4., 1., 2.], [2., 1., 3., 4.], [4., 3., 2., 1.]])
# futoshiki.game = other_game
# print(relations)
# print(futoshiki.check_relations(3, 3))
# print(futoshiki.available_row_values(3))
# print(futoshiki.available_column_values(3))
# print(futoshiki.available_values(3, 3))
# print(other_game)
# print(futoshiki.is_solved())
# solved_game = np.array([[1., 2., 4., 3.], [3., 4., 1., 2.], [2., 1., 3., 4.], [4., 3., 2., 1.]])
# futoshiki.game = solved_game
# print(solved_game)
# print(futoshiki.is_solved())




# loader.load_skyscrapper('test_data/skyscrapper_4_0.txt')
