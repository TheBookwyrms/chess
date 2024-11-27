import numpy as np
from common_functions import *
from can_movements import *


def move(board, your_pieces, their_pieces):

    col_pos, row_pos = piece_to_move()

    if np.isin(board[row_pos, col_pos], your_pieces):

        target_row, target_col = where_to()

        if not is_friendly_fire(target_col, target_row, board, your_pieces):

            current = row_pos, col_pos # compresses current position
            target = target_row, target_col # compresses final position

            movement_list = [
                pawn_movement,
                rook_movement,
                knight_movement,
                bishop_movement,
                queen_movement,
                king_movement,
                ]

            if (col_pos == target_col) and (row_pos == target_row):
                print("invalid move, pieces cannot be moved to they are")
                board = move(board, your_pieces, their_pieces)
                return board
            
            i = board[row_pos, col_pos] - 1 # prepares piece numbers for calling movement_list
            i = (i) if (5 >= i) else (i - 6)

            can_move = movement_list[int(i)](current, target, board, your_pieces, their_pieces)

            if not can_move: # if can_move is False
                print("invalid move, try again")
                board = move(board, your_pieces, their_pieces)
                return board
            elif can_move: # if can_move is True       
                board[target_row, target_col] = board[row_pos, col_pos]
                board[row_pos, col_pos] = 0
                return board
            else:
                print("a weird error has occured, reattempting")
                board = move(board, your_pieces, their_pieces)
                return board
        else:
            print("attacking your own pieces is not permitted, try again")
            board = move(board, your_pieces, their_pieces)
            return board    
    else:
        print("none of your pieces are in that position\n")
        board = move(board, your_pieces, their_pieces)
        return board

def pawn_movement(current, target, board, your_pieces, their_pieces):
    row_pos, col_pos = current
    target_row, target_col = target

    starting_point, one_jump, two_jump = 0, 0, 0
    (starting_point, one_jump, two_jump) = (1, 1, 2) if board[row_pos, col_pos] == 1 else (starting_point, one_jump, two_jump)
    (starting_point, one_jump, two_jump) = (6, -1, -2) if board[row_pos, col_pos] == 7 else (starting_point, one_jump, two_jump)

    if (row_pos + one_jump == target_row) and (target_col == col_pos):
        if not np.isin(board[target_row, target_col], their_pieces):
            return True

    if row_pos == starting_point:            
        if (row_pos + two_jump == target_row) and (target_col == col_pos):
            if not np.isin(board[target_row, target_col], their_pieces):
                if not is_friendly_fire(target_col, target_row-1, board, your_pieces):
                    return True
            
    if (row_pos + one_jump == target_row) and ((target_col == col_pos +1) or (target_col == col_pos -1)):
        if np.isin(board[target_row, target_col], their_pieces):
            return True
            
    return False

        
def rook_movement(current, target, board, your_pieces, _):
    row_pos, col_pos = current
    target_row, target_col = target


    if is_horizontal(col_pos, target_col):
        can_move = can_horizontal(current, target, board)
                
    elif is_vertical(row_pos, target_row):
        can_move = can_vertical(current, target, board)        
    else:
        can_move = False  
    
    return can_move


def knight_movement(current, target, board, your_pieces, _):
    row_pos, col_pos = current
    target_row, target_col = target

    possibilities = np.array([[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]])

    for i in possibilities:
        if (target_row == row_pos + i[0]) and (target_col == col_pos + i[1]):  
            return True

    return False 


def bishop_movement(current, target, board, your_pieces, _):
    row_pos, col_pos = current
    target_row, target_col = target

    if is_diagonal(target_row, row_pos, target_col, col_pos):
        can_move = can_diagonal(current, target, board)

    else:
        can_move = False
    
    return can_move 


def queen_movement(current, target, board, your_pieces, _):
    row_pos, col_pos = current
    target_row, target_col = target

    if is_diagonal(target_row, row_pos, target_col, col_pos):
        can_move = can_diagonal(current, target, board)
            
    elif is_horizontal(col_pos, target_col):
        can_move = can_horizontal(current, target, board)
            
    elif is_vertical(row_pos, target_row):
        can_move = can_vertical(current, target, board)

    else:
        can_move = False 
    
    return can_move   
    

def king_movement(current, target, board, your_pieces, their_pieces):
    row_pos, col_pos = current
    target_row, target_col = target

    if np.abs(target_row-row_pos >1) or np.abs(target_col-col_pos >1):
        return False


    can_be_attacked = np.zeros(16, dtype=bool)

    xth_piece = 0
    
    for each_piece in their_pieces: # each_piece is number of piece
        that_piece_row, that_piece_col = np.where(board == each_piece)
        for piece in zip(that_piece_row, that_piece_col): # piece is position for every piece
            if each_piece == 7: # black_pawn
                can_be_attacked[xth_piece] = pawn_movement(piece, target, board, their_pieces, None)
            if each_piece == 8: # black_rook
                can_be_attacked[xth_piece] = rook_movement(piece, target, board, their_pieces, None)
            if each_piece == 9: # black_knight
                can_be_attacked[xth_piece] = knight_movement(piece, target, board, their_pieces, None)
            if each_piece == 10: # black_bishop
                can_be_attacked[xth_piece] = bishop_movement(piece, target, board, their_pieces, None)
            if each_piece == 11: # black_queen
                can_be_attacked[xth_piece] = queen_movement(piece, target, board, their_pieces, None)
            if each_piece == 12: # black_king
                if np.abs(target_row-piece[0])<=1 and np.abs(target_col-piece[1])<=1:
                    can_be_attacked[xth_piece] = True

            xth_piece += 1
    
    if np.isin(True, can_be_attacked):
        print("an enemy piece can attack you")
        return False
    else:
        return True



