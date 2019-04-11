from Loader import Loader
from Futoshiki import Futoshiki
from Skyscrapper import Skyscrapper
import time
import numpy as np

loader = Loader()
(dimension, game, relations) = loader.load_futoshiki('research_data/test_futo_7_0.txt')
futoshiki = Futoshiki(dimension, game, relations)
(dimension, constraints) = loader.load_skyscrapper('research_data/test_sky_5_0.txt')
skyscraper = Skyscrapper(dimension, constraints)

"""------------------------------------------------------------FUTOSHIKI---------------------------------------------"""
start = time.time()
futoshiki.init_time()
futoshiki.backtracking()
end = time.time()
print("backtracking time: " + str(end - start))
print("backtracking iterations: " + str(futoshiki.backtracking_iterations))

start = time.time()
futoshiki.init_time()
futoshiki.backtracking_with_heuristic()
end = time.time()
print("backtracking_with_heuristic time: " + str(end - start))
print("backtracking_with_heuristic iterations: " + str(futoshiki.backtracking_iterations_h))

start = time.time()
futoshiki.init_time()
futoshiki.forward_checking()
end = time.time()
print("forward_checking time: " + str(end - start))
print("forward_checking iterations: " + str(futoshiki.forward_checking_iterations))

start = time.time()
futoshiki.init_time()
futoshiki.forward_checking_with_heuristic()
end = time.time()
print("forward_checking_with_heuristic time: " + str(end - start))
print("forward_checking_with_heuristic iterations: " + str(futoshiki.forward_checking_iterations_h))


"""------------------------------------------------------------SKYSCRAPER--------------------------------------------"""
# start = time.time()
# skyscraper.init_time()
# skyscraper.backtracking()
# end = time.time()
# print("backtracking time: " + str(end - start))
# print("backtracking iterations: " + str(skyscraper.backtracking_iterations))
#
# start = time.time()
# skyscraper.init_time()
# skyscraper.backtracking_with_heuristic()
# end = time.time()
# print("backtracking_with_heuristic time: " + str(end - start))
# print("backtracking_with_heuristic iterations: " + str(skyscraper.backtracking_iterations_h))
#
# start = time.time()
# skyscraper.init_time()
# skyscraper.forward_checking()
# end = time.time()
# print("forward_checking time: " + str(end - start))
# print("forward_checking iterations: " + str(skyscraper.forward_checking_iterations))
#
# start = time.time()
# skyscraper.init_time()
# skyscraper.forward_checking_with_heuristic()
# end = time.time()
# print("forward_checking_with_heuristic time: " + str(end - start))
# print("forward_checking_with_heuristic iterations: " + str(skyscraper.forward_checking_iterations_h))
# print(len(skyscraper.solutions))



# print(len(futoshiki.solutions))
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

# other_game = np.array([[4., 3., 2., 1.], [3., 4., 1., 2.], [2., 1., 3., 4.], [1., 2., 4., 3.]])
# skyscraper.game = other_game

# print("UPPER------------------------")
# print(skyscraper.is_valid_upper(0))
# print(skyscraper.is_valid_upper(1))
# print(skyscraper.is_valid_upper(2))
# print(skyscraper.is_valid_upper(3))
# print("LOWER------------------------")
# print(skyscraper.is_valid_lower(0))
# print(skyscraper.is_valid_lower(1))
# print(skyscraper.is_valid_lower(2))
# print(skyscraper.is_valid_lower(3))
# print("LEFT------------------------")
# print(skyscraper.is_valid_left(0))
# print(skyscraper.is_valid_left(1))
# print(skyscraper.is_valid_left(2))
# print(skyscraper.is_valid_left(3))
# print("RIGHT------------------------")
# print(skyscraper.is_valid_right(0))
# print(skyscraper.is_valid_right(1))
# print(skyscraper.is_valid_right(2))
# print(skyscraper.is_valid_right(3))
# skyscraper.game[0][0] = 1
# skyscraper.game[0][1] = 2
# skyscraper.game[0][2] = 3
# skyscraper.game[0][3] = 4
# print(skyscraper.is_valid_row(0, 1))
# print(skyscraper.is_valid_row(0, 2))
# print(skyscraper.is_valid_row(0, 3))
# print(skyscraper.is_valid_row(0, 4))
# print('-------------------------------')
# print(skyscraper.is_valid_upper(0))
# print(skyscraper.is_valid_upper(1))
# print(skyscraper.is_valid_upper(2))
# print(skyscraper.is_valid_upper(3))
# print('-------------------------------')
# skyscraper.game[0][0] = 1
# skyscraper.game[1][0] = 2
# skyscraper.game[2][0] = 3
# skyscraper.game[3][0] = 4
# print(skyscraper.is_valid_column(0, 1))
# print(skyscraper.is_valid_column(0, 2))
# print(skyscraper.is_valid_column(0, 3))
# print(skyscraper.is_valid_column(0, 4))
# print('-------------------------------')
# print(skyscraper.is_valid_upper(0))
# skyscraper.game[0][2] = 1
# skyscraper.game[1][2] = 2
# skyscraper.game[2][2] = 4
# skyscraper.game[3][2] = 3
# print(skyscraper.is_valid_lower(0))
# print(skyscraper.is_valid_lower(1))
# print(skyscraper.is_valid_lower(2))
# print(skyscraper.is_valid_lower(3))
# print(skyscraper.is_valid_upper(1))
# print(skyscraper.is_valid_upper(2))
# print(skyscraper.is_valid_upper(3))

# skyscraper.game[2][0] = 1
# skyscraper.game[2][1] = 1
# skyscraper.game[2][2] = 1
# skyscraper.game[2][3] = 1
# print('-------------------------------')
# print(skyscraper.is_valid_left(0))
# print(skyscraper.is_valid_left(1))
# print(skyscraper.is_valid_left(2))
# print(skyscraper.is_valid_left(3))
# print('-------------------------------')
# skyscraper.game[1][0] = 1
# skyscraper.game[1][1] = 1
# skyscraper.game[1][2] = 1
# skyscraper.game[1][3] = 1
# print('-------------------------------')
# print(skyscraper.is_valid_left(0))
# # skyscraper.game[0][2] = 1
# # skyscraper.game[1][2] = 2
# # skyscraper.game[2][2] = 4
# # skyscraper.game[3][2] = 3
# print(skyscraper.is_valid_right(0))
# print(skyscraper.is_valid_right(1))
# print(skyscraper.is_valid_right(2))
# print(skyscraper.is_valid_right(3))

# loader.load_skyscrapper('test_data/skyscrapper_4_0.txt')
