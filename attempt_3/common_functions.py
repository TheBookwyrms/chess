import numpy as np


chess_letters_to_system = {
    "a":1, "b":2, "c":3, "d":4,
    "e":5, "f":6, "g":7, "h":8
}
c_to_s = chess_letters_to_system

def where_to():
    position = input("type letter and number of position to move to, without spaces, in that order\n")
    lst = [i for i in position]
    target_col = c_to_s[lst[0]]-1
    target_row = int(lst[1])-1
    return target_row, target_col

def piece_to_move():
    position = input("type letter and number of piece to be moved, without spaces, in that order\n")
    lst = [i for i in position]
    col_pos = c_to_s[lst[0]]-1
    row_pos = int(lst[1])-1
    return col_pos, row_pos

def is_friendly_fire(target_col, target_row, board, your_pieces):
    if np.isin(board[target_row, target_col], your_pieces):
        return True
    elif not np.isin(board[target_row, target_col], your_pieces):
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