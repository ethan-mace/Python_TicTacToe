from methods import *

# game loop
while True:
    opponent_row, opponent_col = [int(i) for i in input().split()]

    if opponent_row > -1 and opponent_col > -1:
        opponent_board = container.get_board([opponent_row, opponent_col])
        opponent_board.set_player_position([opponent_row, opponent_col], False)

    valid_action_count = int(input())
    input_container = {}

    for i in range(valid_action_count):
        row, col = [int(j) for j in input().split()]
        board_id = generate_board_id([row, col])
        if not board_id in input_container.keys():
            input_container[board_id] = [[row, col]]
        else:
            input_container[board_id].append([row, col])

    lowest_remaining_moves = float('Inf')
    id_to_use = ''
    for key in input_container.keys():
        temp_container = input_container[key]
        temp_len = len(temp_container)
        if temp_len < lowest_remaining_moves:
            lowest_remaining_moves = temp_len
            id_to_use = temp_container[0]

    my_board = container.get_board(id_to_use)
    my_move = minimax(my_board, True, 4, -float('Inf'), float('Inf'))[1]
    my_board.set_player_position(my_move, True)
    x, y = my_move

    print(x, y)
