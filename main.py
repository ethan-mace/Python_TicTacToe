from assets import pvc
from assets.methods import *
# test_win_conditions()
# test_is_game_over()
# test_minimax()
# test_minimax_depth(1, 10, True)

cont_playing = True
level = 1
while cont_playing:
    container = BoardNodeContainer()
    cont_playing, x_win = pvc.play(container.get_board([0, 0]), minimax, is_game_over, is_winner, level)
    level = level + 1 if x_win else level




