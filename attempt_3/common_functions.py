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