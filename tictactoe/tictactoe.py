"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xcount = 0
    Ocount = 0
    for row in board:
        Xcount += row.count(X)
        Ocount += row.count(O)
    return X if Xcount == Ocount else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionSet = set()

    for row in range(3):
        for column in range(3):
            if board[row][column] != X and board[row][column] != O:
                actionSet.add((row, column))
    return actionSet



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0] not in [0, 1, 2] or action[1] not in [0, 1, 2]:
        raise Exception("illegal action")

    new_board = [[EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]

    for row in range(3):
        for column in range(3):
            if board[row][column] == X:
                new_board[row][column] = X
            elif board[row][column] == O:
                new_board[row][column] = O

    curr_player = player(board)
    new_board[action[0]][action[1]] = curr_player
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check for horizontal winner
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O

    #check for vertical winner
    for row in range(3):
        verticalList = []
        for column in range(3):
            verticalList.append(board[column][row])
        if verticalList.count(X) == 3:
            return X
        elif verticalList.count(O) == 3:
            return O

    #check for diagonal winner
    diagonal1, diagonal2 = [], []
    for value in range(3):
        diagonal1.append(board[value][value])
        diagonal2.append(board[value][2-value])
    if diagonal2.count(X) == 3 or diagonal1.count(X) == 3:
        return X
    if diagonal2.count(O) == 3 or diagonal1.count(O) == 3:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    for row in board:
        if row.count(EMPTY) != 0:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == 'O':
        current_min = 2
        min_action = (1, 1)
        #run min_value on actions
        for action in actions(board):
            new_board = result(board, action)
            curr_val = max_value(new_board)
            if curr_val < current_min:
                current_min = curr_val
                min_action = action

        return min_action

    else:
        current_max = -2
        max_action = (1, 1)
        #run max_value on actions
        for action in actions(board):
            new_board = result(board, action)
            curr_val = min_value(new_board)
            if curr_val > current_max:
                current_max = curr_val
                max_action = action

        return max_action




def min_value(board):
    if terminal(board):
        return utility(board)

    v = 2


    for action in actions(board):
        new_board = result(board, action)
        v = min(v, max_value(new_board))

    #print(v)

    return v



def max_value(board):
    if terminal(board):
        return utility(board)

    v = -2


    for action in actions(board):
        new_board = result(board, action)
        v = max(v, min_value(new_board))

    #print(v)

    return v
