import numpy as np
from common_functions import *


def move_white(col_pos, row_pos, board, white_pieces):
    position = input("type row and column to move to, as a single number\n")
    lst = [int(i) for i in position]
    target_col = lst[0]-1
    target_row = lst[1]-1
    initial_board = np.copy(board)

    # position_information = (col_pos, row_pos, target_col, target_row)
    # use this to reduce term overload
    # ___doesn't work in this form___

    if (col_pos == target_col) and (row_pos == target_row):
        print("invalid move, pieces cannot be moved to they are")
        col_pos, row_pos = piece_to_move()
        board = move_white(col_pos, row_pos, board, white_pieces)
        return board
   
    elif board[row_pos][col_pos] == 1: # if piece is white pawn
        board = white_pawn_movement(col_pos, target_col, row_pos, target_row, board, white_pieces)

    elif board[row_pos][col_pos] == 2: # if piece is white rook
        board = white_rook_movement(col_pos, target_col, row_pos, target_row, board, white_pieces)

    elif board[row_pos][col_pos] == 3: # if piece is white knight
        board = white_knight_movement(col_pos, target_col, row_pos, target_row, board, white_pieces)

    elif board[row_pos][col_pos] == 4: # if piece is white bishop
        board = white_bishop_movement(col_pos, target_col, row_pos, target_row, board, white_pieces)
        
    elif board[row_pos][col_pos] == 5: # if piece is white queen
        board = white_queen_movement(col_pos, target_col, row_pos, target_row, board, white_pieces)

    elif board[row_pos][col_pos] == 6: # is piece is white king
        pass

    if (initial_board == board).all(): # if the board is same as before (move failed), redoes turn
            col_pos, row_pos = piece_to_move()
            board = move_white(col_pos, row_pos, board, white_pieces)
            return board
    else:
        return board


def white_pawn_movement(col_pos, target_col, row_pos, target_row, board, white_pieces):
    if not is_friendly_fire(target_col, target_row, board, white_pieces):

        if row_pos == 1:
            if (row_pos + 1 == target_row) and (target_col == col_pos):
                board[row_pos][col_pos] = 0
                board[target_row][target_col] = 1
                return board
            
            elif (row_pos + 2 == target_row) and (target_col == col_pos):
                if not is_friendly_fire(target_col, target_row-1, board, white_pieces):
                    board[row_pos][col_pos] = 0
                    board[target_row][target_col] = 1
                    return board
                
                else:
                    print("case 3: error, something went wrong.\nPlease retry")
                    return board
            else:
                print("invalid move, try again")
                return board
        else:
            if (row_pos + 1 == target_row) and (target_col == col_pos):
                board[row_pos][col_pos] = 0
                board[target_row][target_col] = 1
                return board
            else:
                print("invalid move, try again")
                return board
    else:
        print("attacking your own pieces is not permitted, try again")
        return board    

        
def white_rook_movement(col_pos, target_col, row_pos, target_row, board, white_pieces):
    if not is_friendly_fire(target_col, target_row, board, white_pieces):

        if is_horizontal(col_pos, target_col):
            plus_minus_one = int((target_row - row_pos) / np.abs(target_row - row_pos))

            for i in range(row_pos + plus_minus_one, target_row + 0, plus_minus_one):
                if int(board[i][target_col]) != 0:
                    print("invalid move, try again")
                    return board
                
            board[row_pos][col_pos] = 0
            board[target_row][target_col] = 2
            return board
        
        elif is_vertical(row_pos, target_row):
            plus_minus_one = int((target_col - col_pos) / np.abs(target_col - col_pos))
            
            for i in range(col_pos + plus_minus_one, target_col + plus_minus_one, plus_minus_one):
                if int(board[target_row][i]) != 0:
                    print("invalid move, try again")
                    return board
                
            board[row_pos][col_pos] = 0
            board[target_row][target_col] = 2
            return board
        
        else:
            print("invalid move, try again")
            return board    
    else:
        print("attacking your own pieces is not permitted, try again")
        return board    


def white_knight_movement(col_pos, target_col, row_pos, target_row, board, white_pieces):
    if not is_friendly_fire(target_col, target_row, board, white_pieces):
        possibilities = np.array([[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]])

        for i in possibilities:
            if (target_row == row_pos + i[0]) and (target_col == col_pos + i[1]):  
                board[row_pos][col_pos] = 0
                board[target_row][target_col] = 3
                return board

        print("invalid move, try again")
        return board 
    else:
        print("attacking your own pieces is not permitted, try again")
        return board


def white_bishop_movement(col_pos, target_col, row_pos, target_row, board, white_pieces):
    if not is_friendly_fire(target_col, target_row, board, white_pieces):
        if is_diagonal(target_row, row_pos, target_col, col_pos):

            row_plus_minus_one = int((target_row - row_pos) / np.abs(target_row - row_pos))
            col_plus_minus_one = int((target_col - col_pos) / np.abs(target_col - col_pos))

            list_rows_to_traverse = list(range(row_pos+row_plus_minus_one, target_row, row_plus_minus_one))
            list_cols_to_traverse = list (range(col_pos+col_plus_minus_one, target_col, col_plus_minus_one))
            
            for i in zip(list_rows_to_traverse, list_cols_to_traverse):
                if int(board[i[0]][i[1]]) != 0:
                    print("invalid move, try again")
                    return board
                
            board[row_pos][col_pos] = 0
            board[target_row][target_col] = 4
            return board

        else:
            print("invalid move, try again")
            return board
    else:
        print("attacking your own pieces is not permitted, try again")
        return board    


def white_queen_movement(col_pos, target_col, row_pos, target_row, board, white_pieces):
    if not is_friendly_fire(target_col, target_row, board, white_pieces):
        if is_diagonal(target_row, row_pos, target_col, col_pos):
            row_plus_minus_one = int((target_row - row_pos) / np.abs(target_row - row_pos))
            col_plus_minus_one = int((target_col - col_pos) / np.abs(target_col - col_pos))

            list_rows_to_traverse = list(range(row_pos+row_plus_minus_one, target_row, row_plus_minus_one))
            list_cols_to_traverse = list (range(col_pos+col_plus_minus_one, target_col, col_plus_minus_one))
            
            for i in zip(list_rows_to_traverse, list_cols_to_traverse):
                if int(board[i[0]][i[1]]) != 0:
                    print("invalid move, try again")
                    return board
                
            board[row_pos][col_pos] = 0
            board[target_row][target_col] = 5
            return board
            
        elif is_horizontal(col_pos, target_col):
            plus_minus_one = int((target_row - row_pos) / np.abs(target_row - row_pos))

            for i in range(row_pos + plus_minus_one, target_row + 0, plus_minus_one):
                if int(board[i][target_col]) != 0:
                    print("invalid move, try again")
                    return board
                
            board[row_pos][col_pos] = 0
            board[target_row][target_col] = 5
            return board
        
        elif is_vertical(row_pos, target_row):
            plus_minus_one = int((target_col - col_pos) / np.abs(target_col - col_pos))
            
            for i in range(col_pos + plus_minus_one, target_col + plus_minus_one, plus_minus_one):
                if int(board[target_row][i]) != 0:
                    print("invalid move, try again")
                    return board
                
            board[row_pos][col_pos] = 0
            board[target_row][target_col] = 5
            return board
            
        else:
            print("invalid move, try again")
            return board 
    else:
        print("attacking your own pieces is not permitted, try again")
        return board    



