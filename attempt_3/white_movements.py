import numpy as np
from common_functions import *


def move(col_pos, row_pos, board, your_pieces):
    position = input("type row and column to move to, as a single number\n")
    lst = [int(i) for i in position]
    target_col = lst[0]-1
    target_row = lst[1]-1
    initial_board = np.copy(board)

    current = row_pos, col_pos
    target = target_row, target_col

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
        col_pos, row_pos = piece_to_move()
        board = move(col_pos, row_pos, board, your_pieces)
        return board
    
    i = board[row_pos, col_pos] - 1
    i = (i) if (5 >= i) and (i != 12) else i if (i == 11) else (i - 6)

    board = the_test_list[int(i)](current, target, board, your_pieces)

    if (initial_board == board).all(): # if the board is same as before (move failed), redoes turn
        col_pos, row_pos = piece_to_move()
        board = move(col_pos, row_pos, board, your_pieces)
        return board
    else:
        return board


def pawn_movement(current, target, board, your_pieces):
    row_pos, col_pos = current
    target_row, target_col = target

    if not is_friendly_fire(target_col, target_row, board, your_pieces):
        if board[row_pos, col_pos] == 1:
            starting_point = 1
            one_jump = 1
            two_jump = 2

        elif board[row_pos, col_pos] == 7:
            starting_point = 7
            one_jump = -1
            two_jump = -2


        if row_pos == starting_point:
            if (row_pos + one_jump == target_row) and (target_col == col_pos):
                board[target_row, target_col] = board[row_pos, col_pos]
                board[row_pos, col_pos] = 0
                return board
            
            elif (row_pos + two_jump == target_row) and (target_col == col_pos):
                if not is_friendly_fire(target_col, target_row-1, board, your_pieces):
                    board[target_row, target_col] = board[row_pos, col_pos]
                    board[row_pos, col_pos] = 0
                    return board
                
                else:
                    print("case 3: error, something went wrong.\nPlease retry")
                    return board
            else:
                print("invalid move, try again")
                return board
        else:
            if (row_pos + one_jump == target_row) and (target_col == col_pos):
                board[target_row, target_col] = board[row_pos, col_pos]
                board[row_pos, col_pos] = 0
                return board
            else:
                print("invalid move, try again")
                return board
    else:
        print("attacking your own pieces is not permitted, try again")
        return board    

        
def rook_movement(current, target, board, your_pieces):
    row_pos, col_pos = current
    target_row, target_col = target

    if not is_friendly_fire(target_col, target_row, board, your_pieces):

        if is_horizontal(col_pos, target_col):
            plus_minus_one = int((target_row - row_pos) / np.abs(target_row - row_pos))

            for i in range(row_pos + plus_minus_one, target_row + 0, plus_minus_one):
                if int(board[i][target_col]) != 0:
                    print("invalid move, try again")
                    return board
                
            board[target_row, target_col] = board[row_pos, col_pos]
            board[row_pos, col_pos] = 0
            return board
        
        elif is_vertical(row_pos, target_row):
            plus_minus_one = int((target_col - col_pos) / np.abs(target_col - col_pos))
            
            for i in range(col_pos + plus_minus_one, target_col + plus_minus_one, plus_minus_one):
                if int(board[target_row][i]) != 0:
                    print("invalid move, try again")
                    return board
                
            board[target_row, target_col] = board[row_pos, col_pos]
            board[row_pos, col_pos] = 0
            return board
        
        else:
            print("invalid move, try again")
            return board    
    else:
        print("attacking your own pieces is not permitted, try again")
        return board    


def knight_movement(current, target, board, your_pieces):
    row_pos, col_pos = current
    target_row, target_col = target

    if not is_friendly_fire(target_col, target_row, board, your_pieces):
        possibilities = np.array([[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]])

        for i in possibilities:
            if (target_row == row_pos + i[0]) and (target_col == col_pos + i[1]):  
                board[target_row, target_col] = board[row_pos, col_pos]
                board[row_pos, col_pos] = 0
                return board

        print("invalid move, try again")
        return board 
    else:
        print("attacking your own pieces is not permitted, try again")
        return board


def bishop_movement(current, target, board, your_pieces):
    row_pos, col_pos = current
    target_row, target_col = target

    if not is_friendly_fire(target_col, target_row, board, your_pieces):
        if is_diagonal(target_row, row_pos, target_col, col_pos):

            row_plus_minus_one = int((target_row - row_pos) / np.abs(target_row - row_pos))
            col_plus_minus_one = int((target_col - col_pos) / np.abs(target_col - col_pos))

            list_rows_to_traverse = list(range(row_pos+row_plus_minus_one, target_row, row_plus_minus_one))
            list_cols_to_traverse = list (range(col_pos+col_plus_minus_one, target_col, col_plus_minus_one))
            
            for i in zip(list_rows_to_traverse, list_cols_to_traverse):
                if int(board[i[0]][i[1]]) != 0:
                    print("invalid move, try again")
                    return board
                
            board[target_row, target_col] = board[row_pos, col_pos]
            board[row_pos, col_pos] = 0
            return board

        else:
            print("invalid move, try again")
            return board
    else:
        print("attacking your own pieces is not permitted, try again")
        return board    


def queen_movement(current, target, board, your_pieces):
    row_pos, col_pos = current
    target_row, target_col = target

    if not is_friendly_fire(target_col, target_row, board, your_pieces):
        if is_diagonal(target_row, row_pos, target_col, col_pos):
            row_plus_minus_one = int((target_row - row_pos) / np.abs(target_row - row_pos))
            col_plus_minus_one = int((target_col - col_pos) / np.abs(target_col - col_pos))

            list_rows_to_traverse = list(range(row_pos+row_plus_minus_one, target_row, row_plus_minus_one))
            list_cols_to_traverse = list (range(col_pos+col_plus_minus_one, target_col, col_plus_minus_one))
            
            for i in zip(list_rows_to_traverse, list_cols_to_traverse):
                if int(board[i[0]][i[1]]) != 0:
                    print("invalid move, try again")
                    return board
                
            board[target_row, target_col] = board[row_pos, col_pos]
            board[row_pos, col_pos] = 0
            return board
            
        elif is_horizontal(col_pos, target_col):
            plus_minus_one = int((target_row - row_pos) / np.abs(target_row - row_pos))

            for i in range(row_pos + plus_minus_one, target_row + 0, plus_minus_one):
                if int(board[i][target_col]) != 0:
                    print("invalid move, try again")
                    return board
                
            board[target_row, target_col] = board[row_pos, col_pos]
            board[row_pos, col_pos] = 0
            return board
        
        elif is_vertical(row_pos, target_row):
            plus_minus_one = int((target_col - col_pos) / np.abs(target_col - col_pos))
            
            for i in range(col_pos + plus_minus_one, target_col + plus_minus_one, plus_minus_one):
                if int(board[target_row][i]) != 0:
                    print("invalid move, try again")
                    return board
                
            board[target_row, target_col] = board[row_pos, col_pos]
            board[row_pos, col_pos] = 0
            return board
            
        else:
            print("invalid move, try again")
            return board 
    else:
        print("attacking your own pieces is not permitted, try again")
        return board    



