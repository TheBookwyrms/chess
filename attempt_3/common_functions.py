import numpy as np


def piece_to_move():
    position = input("type column and row of piece to be moved, as a single number\n")
    lst = [int(i) for i in position]
    col_pos = lst[0]-1
    row_pos = lst[1]-1
    return col_pos, row_pos


def is_friendly_fire(target_col, target_row, board, your_pieces):
    if np.isin(board[target_row][target_col], your_pieces):
        return True
    elif not np.isin(board[target_row][target_col], your_pieces):
        return False
    
def is_horizontal(col_pos, target_col):
    if col_pos == target_col:
        return True
    else:
        return False    
    
def is_vertical(row_pos, target_row):
    if row_pos == target_row:
        return True
    else:
        return False
    
def is_diagonal(target_row, row_pos, target_col, col_pos):
    if np.abs(target_row - row_pos) == (np.abs(target_col - col_pos)):
        return True
    else:
        return False