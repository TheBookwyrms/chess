import numpy as np


chess_letters_to_system = {
    "a":1, "b":2, "c":3, "d":4,
    "e":5, "f":6, "g":7, "h":8
}
c_to_s = chess_letters_to_system

def where_to():
    target_col, target_row = "j", 9
    while not ((target_col in ["a", "b", "c", "d", "e", "f", "g", "h"]) and (target_row in [1, 2, 3, 4, 5, 6, 7, 8])):
        position = input("type letter and number of position to move to, without spaces, in that order\n")
        if len(position) == 2:
            target_col, target_row = position[0], int(position[1])
        if not ((target_col in ["a", "b", "c", "d", "e", "f", "g", "h"]) and (target_row in [1, 2, 3, 4, 5, 6, 7, 8])):
            print("invalid input, retry")

    target_col = c_to_s[target_col]-1
    target_row = int(target_row)-1
    return target_row, target_col

def piece_to_move():
    col_pos, row_pos = "j", 9
    while not ((col_pos in ["a", "b", "c", "d", "e", "f", "g", "h"]) and (row_pos in [1, 2, 3, 4, 5, 6, 7, 8])):
        position = input("type letter and number of piece to be moved, without spaces, in that order\n")
        if len(position) == 2:
            col_pos, row_pos = position[0], int(position[1])
        if not ((col_pos in ["a", "b", "c", "d", "e", "f", "g", "h"]) and (row_pos in [1, 2, 3, 4, 5, 6, 7, 8])):
            print("invalid input, retry")

    col_pos = c_to_s[col_pos]-1
    row_pos = int(row_pos)-1
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