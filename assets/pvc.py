def display_game_title(level):
    print("-------")
    print("|T|I|C|")
    print("|T|A|C|")
    print("|T|O|E|")
    print("-------")
    print()
    print(f"Level: {level}")


def play(board, minimax, is_game_over, is_winner, level):
    size = range(3)

    display_game_title(level)

    while not is_game_over(board):
        valid_moves = []
        string = '\nCurrent Board State:\n\t  '
        for i in size:
            for ii in size:
                position = board.get_position([i, ii])
                string += f'|{position.player}'
                if position.player == '.':
                    valid_moves.append(position)
            string += '|\n\t  '
        print(string)

        print("Select a Position:")
        for i in range(len(valid_moves)):
            print(f'\t{i + 1}: {valid_moves[i].get_positions()}')

        int_pos = 0
        while int_pos < 1 or int_pos > len(valid_moves):
            player_position = input(f'Enter number between 1 - {len(valid_moves)}: ')

            try:
                int_pos = int(player_position)
            except:
                int_pos = 0

            if not int_pos > 0 and not int_pos <= len(valid_moves):
                int_pos = 0
        player_move = valid_moves[int_pos - 1].get_positions()

        board.set_player_position(player_move, True)

        if not is_game_over(board):
            opponent_move = minimax(board, False, level, -float('Inf'), float('Inf'))[1]
            board.set_player_position(opponent_move, False)

    board.display()
    print()
    board.display_winner()
    player_res = input("Play Again? (Y/N): ").upper()
    x_win = is_winner(board, True)
    if player_res == "N":
        print("\nGoodbye.")
        return False, ''
    else:
        return True, x_win

