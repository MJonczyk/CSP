from Loader import Loader
from Futoshiki import Futoshiki
import numpy as np

loader = Loader()
(dimension, game, relations) = loader.load_futoshiki('test_data/futoshiki_4_0.txt')
futoshiki = Futoshiki(dimension, game, relations)
# print(game)
# print(futoshiki.is_solved())
print(relations)
print(futoshiki.check_relations(3, 3))
print(futoshiki.available_row_values(3))
print(futoshiki.available_column_values(3))
print(futoshiki.available_values(3, 3))
other_game = np.array([[0., 0., 0., 3.], [0., 1., 0., 0.], [2., 0., 0., 2.], [4., 0., 0., 0.]])
# other_game = np.array([[1., 2., 4., 3.], [3., 4., 1., 2.], [2., 1., 3., 4.], [4., 3., 2., 1.]])
futoshiki.game = other_game
# print(relations)
# print(futoshiki.check_relations(3, 3))
# print(futoshiki.available_row_values(0))
# print(futoshiki.available_column_values(0))
# print(futoshiki.available_values(0, 0))
# print(other_game)
# print(futoshiki.is_solved())
# solved_game = np.array([[1., 2., 4., 3.], [3., 4., 1., 2.], [2., 1., 3., 4.], [4., 3., 2., 1.]])
# futoshiki.game = solved_game
# print(solved_game)
# print(futoshiki.is_solved())




# loader.load_skyscrapper('test_data/skyscrapper_4_0.txt')
