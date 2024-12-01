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
    # format is board[row_position][column_position]

    board[6] = 7 # sets black pawns
    board[1] = 1 # sets white pawns
    board[0] = [2,3,4,5,6,4,3,2]
    board[7] = [8,9,10,11,12,10,9,8]


    white_pieces = np.array([1,2,3,4,5,6])
    black_pieces = np.array([7,8,9,10,11,12])


    
    # board = np.zeros((8,8))
    # board[7, 0] = 12
    # board[2, 0] = 10
    # board[3, 5] = 7
    # board[4, 7] = 7
    # board[0, 0] = 2
    # board[6, 7] = 2
    # board[0, 1] = 5 
    # board[2, 5] = 3
    # board[3, 7] = 1
    # board[0, 7] = 6


    # board = np.zeros((8,8))
    # board[5, 2] = 8
    # board[4, 7] = 6


    return board, white_pieces, black_pieces