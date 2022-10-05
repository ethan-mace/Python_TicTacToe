import logging
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


def win_conditions():
    """Returns a list of all possible win states for local board comparison

    :return: list of x3 positions resulting in a win if a single player occupies all three
    """
    return [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[2, 0], [1, 1], [0, 2]]
    ]


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
        self.player = generate_player_id(is_max)
        return self.player

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

        # reference for number of open positions
        self.remaining_positions = 9

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
            self.position_container[pos_id].set_player(is_max)
            return self.position_container[pos_id].get_positions()
        debug(f'Error in BoardNode().set_player_position(xy={xy}, is_max={is_max})')


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
