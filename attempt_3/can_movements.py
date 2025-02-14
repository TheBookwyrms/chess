import numpy as np

def can_horizontal(current, target, board):
    row_pos, col_pos = current
    target_row, target_col = target

    if (row_pos == target_row):
        plus_minus_one = int((target_col - col_pos) / np.abs(target_col - col_pos))
        
        for i in range(col_pos + plus_minus_one, target_col + 0, plus_minus_one):
            if int(board[target_row][i]) != 0:
                return False     
        
        return True
    return False
    

def can_vertical(current, target, board):
    row_pos, col_pos = current
    target_row, target_col = target

    if col_pos == target_col:
        plus_minus_one = int((target_row - row_pos) / np.abs(target_row - row_pos))

        for i in range(row_pos + plus_minus_one, target_row + 0, plus_minus_one):
            if int(board[i][target_col]) != 0:
                return False
        
        return True
    return False


def can_diagonal(current, target, board):
    row_pos, col_pos = current
    target_row, target_col = target
    
    if np.abs(target_row - row_pos) == (np.abs(target_col - col_pos)):
        row_plus_minus_one = int((target_row - row_pos) / np.abs(target_row - row_pos))
        col_plus_minus_one = int((target_col - col_pos) / np.abs(target_col - col_pos))

        list_rows_to_traverse = list(range(row_pos+row_plus_minus_one, target_row, row_plus_minus_one))
        list_cols_to_traverse = list (range(col_pos+col_plus_minus_one, target_col, col_plus_minus_one))
        
        for i in zip(list_rows_to_traverse, list_cols_to_traverse):
            if int(board[i[0]][i[1]]) != 0:
                #print("invalid move, try again")
                return False
        
        return True
    return False


def eats_king(board, your_pieces):
    if not np.isin(your_pieces[-1], board):
        return True
    else:
        return False