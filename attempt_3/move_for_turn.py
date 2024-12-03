import numpy as np
from common_functions import *
from can_movements import *


def move(board, your_pieces, their_pieces):

    can_move = False

    while not can_move:

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

                if not ((col_pos == target_col) and (row_pos == target_row)):     
                    i = board[row_pos, col_pos] - 1 # prepares piece numbers for calling movement_list
                    i = (i) if (5 >= i) else (i - 6)

                    can_move = movement_list[int(i)](current, target, board, your_pieces, their_pieces)

                    if not can_move: # if can_move is False
                        print(f"{colourer('31')}invalid move, try again{colourer(0)}")
                    elif can_move: # if can_move is True 
                        a = np.copy(board)
                        if board[current] == your_pieces[-1]:
                            a[target] = your_pieces[-1]
                            a[current] = 0
                        king_can_be_attacked = in_check(a, your_pieces, their_pieces)

                        if np.isin(True, king_can_be_attacked):
                            print(f"{colourer('31')}this move would put you in check{colourer(0)}")
                            can_move = False
                        else:
                            if not eats_king(board, your_pieces):
                                board[target_row, target_col] = board[row_pos, col_pos]
                                board[row_pos, col_pos] = 0
                            else:
                                print(f"{colourer('31')}eating kings directly is not allowed, the game can only be ended by checkmate or stalemate\ntry again{colourer(0)}")
                                can_move = False
                else:
                    print(f"{colourer('31')}invalid move, pieces cannot be moved to they are{colourer(0)}")
            else:
                print(f"{colourer('31')}attacking your own pieces is not permitted, try again{colourer(0)}")  
        else:
            print(f"{colourer('31')}none of your pieces are in that position\n{colourer(0)}")
            
    return board

def pawn_movement(current, target, board, your_pieces, their_pieces):
    row_pos, col_pos = current
    target_row, target_col = target

    starting_point, one_jump, two_jump = 0, 0, 0
    (starting_point, one_jump, two_jump) = (1, 1, 2) if board[row_pos, col_pos] == 1 else (starting_point, one_jump, two_jump)
    (starting_point, one_jump, two_jump) = (6, -1, -2) if board[row_pos, col_pos] == 7 else (starting_point, one_jump, two_jump)

    if int(board[target_row, target_col]) == 0:
        if (row_pos + one_jump == target_row) and (target_col == col_pos):
            if not np.isin(board[target_row, target_col], their_pieces):
                return True

        if row_pos == starting_point:            
            if (row_pos + two_jump == target_row) and (target_col == col_pos):
                if not np.isin(board[target_row, target_col], their_pieces):
                    if not is_friendly_fire(target_col, target_row-1, board, your_pieces):
                        return True
            
    if (row_pos + one_jump == target_row) and ((target_col == col_pos + one_jump) or (target_col == col_pos - one_jump)):
        if np.isin(board[target_row, target_col], their_pieces):
            return True
            
    return False

        
def rook_movement(current, target, board, your_pieces, _):
    row_pos, col_pos = current
    target_row, target_col = target


    if is_horizontal(row_pos, target_row):
        can_move = can_horizontal(current, target, board)
                
    elif is_vertical(col_pos, target_col):  
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
            
    elif is_horizontal(row_pos, target_row):
        can_move = can_horizontal(current, target, board)
            
    elif is_vertical(col_pos, target_col):
        can_move = can_vertical(current, target, board)

    else:
        can_move = False 
    
    return can_move   
    

def king_movement(current, target, board, your_pieces, their_pieces):
    row_pos, col_pos = current
    target_row, target_col = target

    if np.abs(target_row-row_pos)>1 or np.abs(target_col-col_pos)>1:
        return False
    
    return True



def in_check(board, your_pieces, their_pieces):

    movement_list = [
                pawn_movement,
                rook_movement,
                knight_movement,
                bishop_movement,
                queen_movement,
                king_movement,
                ]

    can_be_attacked = np.zeros(16, dtype=bool)

    xth_piece = 0

    king_row, king_col = np.where(board == your_pieces[-1])
    your_king = int(king_row), int(king_col)



    
    for each_piece in their_pieces: # each_piece is number of piece
        that_piece_row, that_piece_col = np.where(board == each_piece)
        for piece in zip(that_piece_row, that_piece_col): # piece is position for every piece
            if can_be_attacked[xth_piece] == False:
                #print(each_piece, type(each_piece), each_piece == 7)
                if each_piece != 0:
                    #print(each_piece, type(each_piece), each_piece == 7)
                    i = (each_piece-1) if (5 >= each_piece) else (each_piece -1 - 6)
                    can_be_attacked[xth_piece] = movement_list[int(i)](piece, your_king, board, their_pieces, your_pieces)
                    #if each_piece == 7:
                     #   print(piece, your_king, board, their_pieces, your_pieces, movement_list[int(i)](piece, your_king, board, their_pieces, your_pieces))

                if each_piece == their_pieces[5]: # king
                    if np.abs(king_row-piece[0])<=1 and np.abs(king_col-piece[1])<=1:
                        can_be_attacked[xth_piece] = True

            #print(can_be_attacked)
            xth_piece += 1
    
    #print(can_be_attacked)
    return can_be_attacked