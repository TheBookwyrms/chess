import numpy as np
from common_functions import *
from can_movements import *


def move(board, your_pieces, their_pieces):

    col_pos, row_pos = piece_to_move()

    if np.isin(board[row_pos, col_pos], your_pieces):

        target_row, target_col = where_to()

        current = row_pos, col_pos # compresses current position
        target = target_row, target_col # compresses final position

        the_test_list = [
            pawn_movement,
            rook_movement,
            knight_movement,
            bishop_movement,
            queen_movement,
            # here go white king,
            # here go black king
            ]

        if (col_pos == target_col) and (row_pos == target_row):
            print("invalid move, pieces cannot be moved to they are")
            board = move(board, your_pieces, their_pieces)
            return board
        
        i = board[row_pos, col_pos] - 1
        i = (i) if (5 >= i) and (i != 12) else i if (i == 11) else (i - 6)

        can_move = the_test_list[int(i)](current, target, board, your_pieces)

        if not can_move: # if can_move is False
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
        print("none of your pieces are in that position\n")
        board = move(board, your_pieces, their_pieces)
        return board

def pawn_movement(current, target, board, your_pieces):
    row_pos, col_pos = current
    target_row, target_col = target

    if not is_friendly_fire(target_col, target_row, board, your_pieces):

        (starting_point, one_jump, two_jump) = (1, 1, 2) if board[row_pos, col_pos] == 1 else (starting_point, one_jump, two_jump)
        (starting_point, one_jump, two_jump) = (7, -1, -2) if board[row_pos, col_pos] == 7 else (starting_point, one_jump, two_jump)

        if (row_pos + one_jump == target_row) and (target_col == col_pos):
            return True

        if row_pos == starting_point:            
            if (row_pos + two_jump == target_row) and (target_col == col_pos):
                if not is_friendly_fire(target_col, target_row-1, board, your_pieces):
                    return True
                
        print("invalid move, try again")
        return False
    
    else:
        print("attacking your own pieces is not permitted, try again")
        return False    

        
def rook_movement(current, target, board, your_pieces):
    row_pos, col_pos = current
    target_row, target_col = target

    if not is_friendly_fire(target_col, target_row, board, your_pieces):

        if is_horizontal(col_pos, target_col):
            can_move = can_horizontal(current, target, board)
                    
        elif is_vertical(row_pos, target_row):
            can_move = can_vertical(current, target, board)        
        else:
            print("invalid move, try again")
            can_move = False  
        
        return can_move
    else:
        print("attacking your own pieces is not permitted, try again")
        return False    


def knight_movement(current, target, board, your_pieces):
    row_pos, col_pos = current
    target_row, target_col = target

    if not is_friendly_fire(target_col, target_row, board, your_pieces):
        possibilities = np.array([[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]])

        for i in possibilities:
            if (target_row == row_pos + i[0]) and (target_col == col_pos + i[1]):  
                return True

        print("invalid move, try again")
        return False 
    else:
        print("attacking your own pieces is not permitted, try again")
        return False


def bishop_movement(current, target, board, your_pieces):
    row_pos, col_pos = current
    target_row, target_col = target

    if not is_friendly_fire(target_col, target_row, board, your_pieces):
        if is_diagonal(target_row, row_pos, target_col, col_pos):
            can_move = can_diagonal(current, target, board)

        else:
            print("invalid move, try again")
            can_move = False
        
        return can_move
    
    else:
        print("attacking your own pieces is not permitted, try again")
        return False    


def queen_movement(current, target, board, your_pieces):
    row_pos, col_pos = current
    target_row, target_col = target

    if not is_friendly_fire(target_col, target_row, board, your_pieces):
        if is_diagonal(target_row, row_pos, target_col, col_pos):
            can_move = can_diagonal(current, target, board)
                
        elif is_horizontal(col_pos, target_col):
            can_move = can_horizontal(current, target, board)
                
        elif is_vertical(row_pos, target_row):
           can_move = can_vertical(current, target, board)

        else:
            print("invalid move, try again")
            can_move = False 
        
        return can_move
    else:
        print("attacking your own pieces is not permitted, try again")
        return False    