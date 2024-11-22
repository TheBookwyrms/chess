import numpy as np
from chess_prototype_2 import *

def pawn_movement(index, piece, white_pieces, black_pieces, move_to):
    if piece[1][1] == 'w':
        if ((piece[0] + np.array([1,1]) == move_to) | (piece[0] + np.array([1, -1]))) and (([True if piece[0] == move_to else False for piece in black_pieces]).any()): # pawn-diagonal-move
            white_pieces[index][0] = move_to
            return white_pieces
        if (piece[2][1] == True) and (not is_friendly_fire(piece, white_pieces, black_pieces, piece[0]+np.array([0,1]))):
            if (move_to == piece[0] + np.array([1,0])) | (move_to == piece[0] + np.array([2,0])):
                white_pieces[index][0] = move_to
                return white_pieces
        elif piece[2][1] == False:
            if (move_to == piece[0] + np.array([1,0])):
                white_pieces[index][0] = move_to
                return white_pieces


    elif piece[1][1] == 'b':
        if piece[2][1] == True:
            pass
        elif piece[2][1] == False:
            pass

def rook_movement(index, piece, white_pieces, black_pieces, move_to):
    pass

def knight_movement(index, piece, white_pieces, black_pieces, move_to):
    pass

def bishop_movement(index, piece, white_pieces, black_pieces, move_to):
    pass

def queen_movement(index, piece, white_pieces, black_pieces, move_to):
    pass

def king_movement(index, piece, white_pieces, black_pieces, move_to):
    pass