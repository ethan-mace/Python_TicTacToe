from methods import *

"""
Test module
"""

board = container.get_board([0, 0])


def test_win_conditions():
    # Test Row 0
    board.set_player_position([0, 0], True)
    assert is_winner(board, True) is False

    board.set_player_position([0, 1], True)
    assert is_winner(board, True) is False

    board.set_player_position([0, 2], True)
    assert is_winner(board, True) is True

    board.reset()
    assert is_winner(board, True) is False

    # Test Row 1
    board.set_player_position([1, 0], True)
    assert is_winner(board, True) is False

    board.set_player_position([1, 1], True)
    assert is_winner(board, True) is False

    board.set_player_position([1, 2], True)
    assert is_winner(board, True) is True

    board.reset()
    assert is_winner(board, True) is False

    # Test Row 2
    board.set_player_position([2, 0], True)
    assert is_winner(board, True) is False

    board.set_player_position([2, 1], True)
    assert is_winner(board, True) is False

    board.set_player_position([2, 2], True)
    assert is_winner(board, True) is True

    board.reset()
    assert is_winner(board, True) is False

    # Test Col 0
    board.set_player_position([0, 0], True)
    assert is_winner(board, True) is False

    board.set_player_position([1, 0], True)
    assert is_winner(board, True) is False

    board.set_player_position([2, 0], True)
    assert is_winner(board, True) is True

    board.reset()
    assert is_winner(board, True) is False

    # Test Col 1
    board.set_player_position([0, 1], True)
    assert is_winner(board, True) is False

    board.set_player_position([1, 1], True)
    assert is_winner(board, True) is False

    board.set_player_position([2, 1], True)
    assert is_winner(board, True) is True

    board.reset()
    assert is_winner(board, True) is False

    # Test Col 2
    board.set_player_position([0, 2], True)
    assert is_winner(board, True) is False

    board.set_player_position([1, 2], True)
    assert is_winner(board, True) is False

    board.set_player_position([2, 2], True)
    assert is_winner(board, True) is True

    board.reset()
    assert is_winner(board, True) is False

    # Test Diag 0
    board.set_player_position([0, 0], True)
    assert is_winner(board, True) is False

    board.set_player_position([1, 1], True)
    assert is_winner(board, True) is False

    board.set_player_position([2, 2], True)
    assert is_winner(board, True) is True

    board.reset()
    assert is_winner(board, True) is False

    # Test Diag 1
    board.set_player_position([2, 0], True)
    assert is_winner(board, True) is False

    board.set_player_position([1, 1], True)
    assert is_winner(board, True) is False

    board.set_player_position([0, 2], True)
    assert is_winner(board, True) is True

    board.reset()
    assert is_winner(board, True) is False

    debug("Test: Win Conditions\n\tResult: Success - No Errors\n")


def test_is_game_over():
    assert is_game_over(board) is False

    board.set_player_position([2, 0], True)
    board.set_player_position([1, 1], True)
    board.set_player_position([0, 2], True)

    assert is_game_over(board) is True

    board.reset()
    assert is_game_over(board) is False

    board.set_player_position([2, 0], False)
    board.set_player_position([1, 1], False)
    board.set_player_position([0, 2], False)

    assert is_game_over(board) is True

    board.reset()
    assert is_game_over(board) is False

    debug("Test: Is Game Over\n\tResult: Success - No Errors\n")


def test_minimax():
    board.reset()

    # Player 1 - Move 1
    remaining_move_count = board.num_remaining_positions()

    player_1_move = minimax(board, True, 4, -float('Inf'), float('Inf'))[1]
    assert isinstance(player_1_move, list)

    board.set_player_position(player_1_move, True)
    assert board.num_remaining_positions() == (remaining_move_count - 1)

    # Player 2 - Move 1
    remaining_move_count = board.num_remaining_positions()

    player_2_move = minimax(board, False, 4, -float('Inf'), float('Inf'))[1]
    assert isinstance(player_2_move, list)
    assert player_2_move is not player_1_move

    board.set_player_position(player_2_move, False)
    assert board.num_remaining_positions() == (remaining_move_count - 1)

    board.display()

    # Player 1 - Move 2
    remaining_move_count = board.num_remaining_positions()

    player_1_move = minimax(board, True, 4, -float('Inf'), float('Inf'))[1]
    assert isinstance(player_1_move, list)

    board.set_player_position(player_1_move, True)
    assert board.num_remaining_positions() == (remaining_move_count - 1)

    # Player 2 - Move 2
    remaining_move_count = board.num_remaining_positions()

    player_2_move = minimax(board, False, 4, -float('Inf'), float('Inf'))[1]
    assert isinstance(player_2_move, list)
    assert player_2_move is not player_1_move

    board.set_player_position(player_2_move, False)
    assert board.num_remaining_positions() == (remaining_move_count - 1)

    board.display()

    # Player 1 - Move 3
    remaining_move_count = board.num_remaining_positions()

    player_1_move = minimax(board, True, 4, -float('Inf'), float('Inf'))[1]
    assert isinstance(player_1_move, list)

    board.set_player_position(player_1_move, True)
    assert board.num_remaining_positions() == (remaining_move_count - 1)

    # Player 2 - Move 3
    remaining_move_count = board.num_remaining_positions()

    player_2_move = minimax(board, False, 4, -float('Inf'), float('Inf'))[1]
    assert isinstance(player_2_move, list)
    assert player_2_move is not player_1_move

    board.set_player_position(player_2_move, False)
    assert board.num_remaining_positions() == (remaining_move_count - 1)

    board.display()

    # Player 1 - Move 4
    remaining_move_count = board.num_remaining_positions()

    player_1_move = minimax(board, True, 4, -float('Inf'), float('Inf'))[1]
    assert isinstance(player_1_move, list)

    board.set_player_position(player_1_move, True)
    assert board.num_remaining_positions() == (remaining_move_count - 1)

    # Player 2 - Move 4
    remaining_move_count = board.num_remaining_positions()

    player_2_move = minimax(board, False, 4, -float('Inf'), float('Inf'))[1]
    assert isinstance(player_2_move, list)
    assert player_2_move is not player_1_move

    board.set_player_position(player_2_move, False)
    assert board.num_remaining_positions() == (remaining_move_count - 1)

    board.display()

    debug("Test: MiniMax\n\tResult: Success - No Errors\n")

def test_minimax_depth(depth_player_1: int, depth_player_2: int, first_player: bool):
    is_max = first_player

    while not is_game_over(board):
        depth = depth_player_1 if is_max else depth_player_2
        move = minimax(board, is_max, depth, -float('Inf'), float('Inf'))[1]
        board.set_player_position(move, is_max)
        board.display()
        is_max = not is_max

    board.display_winner()
    debug("Test: MiniMax Depth\n\tResult: Success - No Errors\n")

