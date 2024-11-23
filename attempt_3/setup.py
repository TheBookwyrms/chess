import numpy as np

'''
types:

nothing = 0

white pawn = 1
white rook = 2
white knight = 3
white bishop = 4
white queen = 5
white king = 6

black pawn = 7
black rook = 8
black knight = 9
black bishop = 10
black queen = 11
black king = 12
'''
def setup():
    board = np.zeros((8,8))
    # format is board[column_position][row_position]

    board[1] = 1 # sets black pawns
    board[6] = 7 # sets white pawns
    board[2][0] = 1

    board[0][0] = 2 # sets white rook 1
    board[0][1] = 3 # white knight 1
    board[0][2] = 4 # white bishop 1
    board[0][3] = 5 # white queen
    board[0][4] = 6 # white king
    board[0][5] = 4 # white bishop 2
    board[0][6] = 3 # white knight 2
    board[0][7] = 2 # white rook 2

    board[7][0] = 8 # black rook 1
    board[7][1] = 9 # black knight 1
    board[7][2] = 10 # black bishop 1
    board[7][3] = 11 # black queen
    board[7][4] = 12 # black king
    board[7][5] = 10 # black bishop 2
    board[7][6] = 9 # black knight 2
    board[7][7] = 8 # black rook 2


    white_pieces = np.array([1,2,3,4,5,6])
    black_pieces = np.array([7,8,9,10,11,12])

    return board, white_pieces, black_pieces