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

    inverted_nums_to_chess = {1:"♙", 2:"♖", 3:"♘", 4:"♗", 5:"♕", 6:"♔",
                     7:"♟", 8:"♜", 9:"♞", 10:"♝", 11:"♛", 12:"♚",
                     #0:"□"}
                     0:" "}

    side_text = [
            f'         {"what each piece means":^28}',
            "         white pieces    black pieces",
            f'{"pawn":>6}   {inverted_nums_to_chess[7]:^12}    {inverted_nums_to_chess[1]:^12}',
            f'{"rook":>6}   {inverted_nums_to_chess[8]:^12}    {inverted_nums_to_chess[2]:^12}',
            f'{"knight":>6}   {inverted_nums_to_chess[9]:^12}    {inverted_nums_to_chess[3]:^12}',
            f'{"bishop":>6}   {inverted_nums_to_chess[10]:^12}    {inverted_nums_to_chess[4]:^12}',
            f'{"queen":>6}   {inverted_nums_to_chess[11]:^12}    {inverted_nums_to_chess[5]:^12}', 
            f'{"king":>6}   {inverted_nums_to_chess[12]:^12}    {inverted_nums_to_chess[6]:^12}',
            f'']
    
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
    # board[7, 0] = 6
    # board[2, 0] = 4
    # board[3, 5] = 9
    # board[4, 7] = 7
    # board[0, 0] = 8
    # board[6, 7] = 8
    # board[0, 1] = 11 
    # board[2, 5] = 1
    # board[3, 7] = 1
    # board[0, 7] = 12


    # board = np.zeros((8,8))
    # board[5, 2] = 8
    # board[4, 7] = 6
    # board[0, 0] = 12


    return board, white_pieces, black_pieces, side_text