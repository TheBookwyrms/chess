import numpy as np
from move_for_turn import *


def in_stalemate(board, stalemated, stalemater_pieces):
    movement_list = [
                    pawn_movement,
                    rook_movement,
                    knight_movement,
                    bishop_movement,
                    queen_movement,
                    king_movement,
                    ]

    rows = np.array([0, 1, 2, 3, 4, 5, 6, 7])
    cols = np.array([0, 1, 2, 3, 4, 5, 6, 7])

    x_piece_can_move = np.zeros(16, dtype=bool)
    xth_piece = 0

    
    for each_piece in stalemated:
        that_piece_row, that_piece_col = np.where(board == each_piece)
        for piece in zip(that_piece_row, that_piece_col): # piece is position for every piece on your team
            for row in rows:
                for col in cols:
                    target = row, col
                    if x_piece_can_move[xth_piece] == False:
                        if not is_friendly_fire(col, row, board, stalemated):
                            a = np.copy(board)
                            a[row, col] = a[piece]
                            a[piece] = 0
                            king_can_be_attacked = in_check(a, stalemated, stalemater_pieces)
            
                            if not np.isin(True, king_can_be_attacked):
                                i = board[piece] - 1 # prepares piece numbers for calling movement_list
                                i = (i) if (5 >= i) else (i - 6)
                                x_piece_can_move[xth_piece] = movement_list[int(i)](piece, target, board, stalemated, stalemater_pieces)
                            
                                # if x_piece_can_move[xth_piece] == True:
                                #     #print(int(i), piece, target, board, stalemated, stalemater_pieces)
                                #     print(a[row], king_can_be_attacked)
                                #     print(piece, row, col, xth_piece)
                                #     print(each_piece, piece, board[piece], board[row, col])           
           
            xth_piece += 1

    #print(x_piece_can_move)

    for i in range(len(x_piece_can_move)):
        if i >= xth_piece:
            x_piece_can_move[i] = False

    #print(x_piece_can_move)

    if not np.isin(True, x_piece_can_move):
        return True
    else:
        return False