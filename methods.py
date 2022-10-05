from sys import stderr
from copy import deepcopy
from logging import DEBUG, debug, basicConfig

basicConfig(stream=stderr, level=DEBUG, format='%(message)s')


def generate_position_id(xy: list):
    """Converts x, y key pair to local board reference
    Necessary for comparing player positions to win_conditions

    :param xy: [x, y] key pair
    :return: str position reference
    """
    return ''.join([str(int(i % 3)) for i in xy])


def generate_board_id(xy: list):
    """Converts x, y key pair to BoardNodeContainer reference

    :param xy: [x, y] key pair
    :return: str board reference
    """
    return ''.join([str(int(i / 3)) for i in xy])


def generate_player_id(is_max: bool):
    """Returns player id based on maximizer True/False value

    :param is_max: bool
    :return: "X" is is_max == True, "O" otherwise
    """
    return "X" if is_max else "O"


class PositionNode(object):
    """
    Single position of a 3x3 board
    """
    def __init__(self, x: int, y: int, _id: str):
        # position id converted from [x, y] key pair
        self._id = _id

        # original [x, y] key pair
        self.x = x
        self.y = y

        # initial player id
        self.player = '.'

        # False is a player occupies this position
        self.open = True

    def get_id(self):
        """
        :return: position id
        """
        return self._id

    def is_open(self):
        """
        :return: True if no player occupies this position, False otherwise
        """
        return self.open

    def get_positions(self):
        """
        :return: original [x, y] key pair
        """
        return [self.x, self.y]

    def set_player(self, is_max):
        """Sets id of player occupying this position

        :param is_max: bool
        :return: player id
        """
        if self.open:
            self.player = generate_player_id(is_max)
            self.open = False
            return self.player
        debug(f'Error in PositionNode().set_player(is_max={is_max})')

    def get_player(self):
        """
        :return: id of player occupying this position
        """
        return self.player


class BoardNode:
    """
    3x3 Board
    """
    def __init__(self, _id='', board=None):
        # board id converted from [x, y] key pair
        self._id = _id

        # contains 3x3 board positions
        self.position_container = {}

        # contains open position key pairs
        self.remaining_position_list = []

        # if a board is passed as a parameter, this node becomes a copy of that board
        # used for minimax simulations
        if board is not None:
            self.__dict__ = deepcopy(board.__dict__)

    def generate_position(self, xy: list):
        """Creates a position node based on [x, y] key pair
        Stores node in position_container

        :param xy: [x, y] key pair
        :return: generated position node
        """
        pos_id = generate_position_id(xy)
        if pos_id not in self.position_container.keys():
            x, y = xy

            self.position_container[pos_id] = PositionNode(x, y, pos_id)
            self.remaining_position_list.append([x, y])
            self.remaining_positions = len(self.remaining_position_list)
            return self.position_container[pos_id]
        debug(f'Error in BoardNode().generate_position(xy={xy})')

    def set_player_position(self, xy: list, is_max: bool):
        """Occupies given xy position with player id based on is_max value

        :param xy: [x, y] key pair
        :param is_max: bool
        :return: original [x, y] key pair of occupied position
        """
        pos_id = generate_position_id(xy)
        if pos_id in self.position_container.keys():
            x, y = xy
            self.position_container[pos_id].set_player(is_max)
            idx = self.remaining_position_list.index([x, y])
            self.remaining_position_list.pop(idx)
            self.remaining_positions = len(self.remaining_position_list)
            return self.position_container[pos_id].get_positions()
        debug(f'Error in BoardNode().set_player_position(xy={xy}, is_max={is_max})')

    def has_remaining_positions(self):
        return self.remaining_positions > 0

    def num_remaining_positions(self):
        return len(self.remaining_position_list)

    def get_position(self, xy: list):
        """Gets PositionNode based on [x, y] key pair value

        :param xy: [x, y] key pair
        :return: PositionNode
        """
        position_id = generate_position_id(xy)
        if position_id in self.position_container.keys():
            return self.position_container[position_id]
        debug(f'Error in BoardNode.get_position(xy={xy}): position_id={position_id}')

    def reset(self):
        for node in self.position_container.values():
            node.player = '.'
            node.open = True
            self.remaining_positions += 1
        return

    def display(self):
        string = '\t-------\n\t|'

        idx = 1
        for key in self.position_container.keys():
            string += f'{self.position_container[key].get_player()}|'

            if idx % 3 == 0:
                if idx < 9:
                    string += '\n\t|'
            idx += 1
        string += '\n\t-------'
        debug(string)

    def display_winner(self):
        string = "\t*** "
        if is_winner(self, True):
            string += "X Wins"
        elif is_winner(self, False):
            string += "O Wins"
        else:
            string += "Tie"
        string += " ***\n"
        debug(string)


class BoardNodeContainer:
    """
    3x3 BoardNode container
    Each board contains 3x3 PositionNodes
    """
    def __init__(self):
        # BoardNode container
        self.nodes = {}

        # initiates board and position generation
        self.init()

    def init(self):
        """Loops through [x, y] key pairs from [0, 0] to [8, 8]
        Generates boards and position key pairs

        :return: None
        """
        for i in range(9):
            for ii in range(9):
                if (i + 1) % 3 == 0 and (ii + 1) % 3 == 0:
                    board_id = generate_board_id([i, ii])
                    node = BoardNode(_id=board_id)
                    for x in range(i - 2, i + 1):
                        for y in range(ii - 2, ii + 1):
                            node.generate_position([x, y])
                    if board_id not in self.nodes.keys():
                        self.nodes[board_id] = node
                    else:
                        debug(f'Error in BoardNode().init(): board_id already exists '
                              f'([i, ii]={[i, ii]}) (board_id={board_id})')
        return

    def get_board(self, xy: list):
        """Gets 3x3 board from node container based on [x, y] value

        :param xy: [x, y] key pair
        :return: BoardNode
        """
        board_id = generate_board_id(xy)
        if board_id in self.nodes.keys():
            return self.nodes[board_id]
        debug(f'Error in BoardNodeContainer().get_board(xy={xy}): board_id = {board_id}')


def win_conditions(board: BoardNode):
    """Returns a list of all possible win states for local board comparison

    :param board: BoardNode
    :return: list of x3 positions resulting in a win if a single player occupies all three
    """
    win_cons = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[2, 0], [1, 1], [0, 2]]
    ]

    arr = []
    for g in win_cons:
        group = []
        for p in g:
            group.append(board.get_position(p).get_player())
        arr.append(group)

    return arr


def is_winner(board: BoardNode, is_max):
    """Loops through win_conditions.  Checks if player occupies any three positions within a condition.

    :param board: BoardNode
    :param is_max: bool
    :return: bool - True if player occupies any three position within a win condition, False otherwise
    """

    wc = win_conditions(board)
    player = generate_player_id(is_max)
    for group in wc:
        if group.count(player) > 2:
            return True
    return False


def is_game_over(board: BoardNode):
    return is_winner(board, True) or is_winner(board, False) or not board.has_remaining_positions()


def evaluate(board: BoardNode):
    if is_winner(board, True):
        return 1
    elif is_winner(board, False):
        return -1
    else:
        return 0


def minimax(board: BoardNode, is_max, depth, alpha, beta):
    """Recursive method.  Checks all possible moves up to a given depth and returns most likely win state

    :param board: BoardNode
    :param is_max: bool
    :param depth: int - stops recursion if < 1
    :param alpha: determines whether a recursion branch is relevant to player if is_max == True
    :param beta:determines whether a recursion branch is relevant to player if is_max == False
    :return: [score, best_position] - score > 0 is a win state for is_max == True. < 0 for is_max == False. 0 for Tie.
    """

    # check if a winning move has been made; there are no remaining positions; or depth has reached 0
    if is_game_over(board) or depth < 1:
        return [evaluate(board), '']

    best_val = -float("Inf") if is_max else float("Inf")
    moves = board.remaining_position_list
    best_move = moves[0]

    for move in moves:
        new_board = BoardNode(board=board)
        new_board.set_player_position(move, is_max)
        sim_val = minimax(new_board, not is_max, depth - 1, alpha, beta)[0]

        if (is_max and sim_val > best_val) or (not is_max and sim_val < best_val):
            best_val = sim_val
            best_move = move
            if is_max:
                alpha = max(alpha, best_val)
            else:
                beta = min(beta, best_val)

            if alpha >= beta:
                break

    return [best_val, best_move]


