from methods import *

"""
Test module
"""

container = BoardNodeContainer()
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

    debug("Test: Win Conditions\n\tResult: Success - No Errors")
