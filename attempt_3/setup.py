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


    board[1] = 7 # sets black pawns
    board[6] = 1 # sets white pawns

    board[0][0] = 2
    board[0][1] = 3
    board[0][2] = 4
    board[0][3]
    board[0][4]
    board[0][5]
    board[0][6]
    board[0][7]

    board[7][0]
    board[7][1]
    board[7][2]
    board[7][3]
    board[7][4]
    board[7][5]
    board[7][6]
    board[7][7]


    print(board)

setup()