import numpy as np
from error_messages import *


chess_letters_to_system = {
    "a":1, "b":2, "c":3, "d":4,
    "e":5, "f":6, "g":7, "h":8
}
c_to_s = chess_letters_to_system

system_to_chess_letters = {
    1:"a", 2:"b", 3:"c", 4:"d",
    5:"e", 6:"f", 7:"g", 8:"h"
}
s_to_c = system_to_chess_letters

def where_to():
    num = 0
    target_col, target_row = "j", 9
    while not ((target_col in ["a", "b", "c", "d", "e", "f", "g", "h"]) and (target_row in [1, 2, 3, 4, 5, 6, 7, 8])):
        print(error(num))
        position = input("type letter and number of position to move to, without spaces, in that order\n")
        
        if not len(position) == 2:
            num = 7
        else:
            if not ((position[0] in ["a", "b", "c", "d", "e", "f", "g", "h"]) and (position[1] in ["1", "2", "3", "4", "5", "6", "7", "8"])):
                num = 7
            else:
                if len(position) == 2:
                    target_col, target_row = position[0], int(position[1])

    target_col = c_to_s[target_col]-1
    target_row = int(target_row)-1
    return target_row, target_col

def piece_to_move(board):
    num = 0
    col_pos, row_pos = "j", 9
    while not ((col_pos in ["a", "b", "c", "d", "e", "f", "g", "h"]) and (row_pos in [1, 2, 3, 4, 5, 6, 7, 8])):
        print(error(num))
        position = input("type letter and number of piece to be moved, without spaces, in that order\n")
        
        if not len(position) == 2:
            num = 7
        else:
            if not ((position[0] in ["a", "b", "c", "d", "e", "f", "g", "h"]) and (position[1] in ["1", "2", "3", "4", "5", "6", "7", "8"])):
                num = 7
            else:
                if len(position) == 2:
                    col_pos, row_pos = position[0], int(position[1])

    col_pos = c_to_s[col_pos]-1
    row_pos = int(row_pos)-1

    return col_pos, row_pos, position

def is_friendly_fire(target_col, target_row, board, your_pieces):
    if np.isin(board[target_row, target_col], your_pieces):
        return True
    elif not np.isin(board[target_row, target_col], your_pieces):
        return False 
    
def is_diagonal(target_row, row_pos, target_col, col_pos):
    if np.abs(target_row - row_pos) == (np.abs(target_col - col_pos)):
        return True
    else:
        return False

def display(board, side_text, position):
    row, col, = 9, 9
    if position != None:
        col = (chess_letters_to_system[position[0]]-1)
        row = 7-(int(position[1])-1)

    board = np.flipud(board)

    normal_nums_to_chess = {7:"♙", 8:"♖", 9:"♘", 10:"♗", 11:"♕", 12:"♔",
                     1:"♟", 2:"♜", 3:"♞", 4:"♝", 5:"♛", 6:"♚",
                     #0:"□"}
                     0:" "}
    inverted_nums_to_chess = {1:"♙", 2:"♖", 3:"♘", 4:"♗", 5:"♕", 6:"♔",
                     7:"♟", 8:"♜", 9:"♞", 10:"♝", 11:"♛", 12:"♚",
                     #0:"□"}
                     0:" "}

    chess_rows = np.array([8,7,6,5,4,3,2,1])
    chess_letters = np.array(["a","b","c","d","e","f","g","h"])
    
    print('\n')

    one = 1
    print("      a  b  c  d  e  f  g  h\n")
    for chess_row, i, side in zip(chess_rows, range(len(board)), side_text):        
        if i != row:
            lst = []
            for j, x in enumerate(board[i]):
                if (j + one)%2 != 0:
                    test = f' {colourer('07')}{inverted_nums_to_chess[int(x)]} {colourer(0)}'
                else:
                    test = f' {normal_nums_to_chess[int(x)]} '
                lst.append(test)
        else:
            lst = []
            for j, x in enumerate(board[i]):
                if j != col:
                    if (j + one)%2 != 0:
                        test = f' {colourer('07')}{inverted_nums_to_chess[int(x)]} {colourer(0)}'
                    else:
                        test = f' {normal_nums_to_chess[int(x)]} '
                else:
                    if (j + one)%2 != 0:
                        test = f' {colourer('07')}{colourer('32')}{inverted_nums_to_chess[int(x)]} {colourer(0)}'
                    else:
                        test = f' {colourer('32')}{colourer('07')}{normal_nums_to_chess[int(x)]} {colourer(0)}'
                lst.append(test)

        one += 1
        #lst = [f"{f"\033[07m{nums_to_chess[int(x)]+"   "}\033[0m":4}" for x in board[i]]
        row_text = "".join(lst)
        print(f'{chess_row}    {row_text}    {chess_row}       {side}')
    print("\n      a  b  c  d  e  f  g  h")

    print("\n")