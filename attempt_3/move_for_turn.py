import numpy as np
from common_functions import *
from can_movements import *
from error_messages import *


# def display(board, piece):

#     board = np.flipud(board)

#     normal_nums_to_chess = {7:"♙", 8:"♖", 9:"♘", 10:"♗", 11:"♕", 12:"♔",
#                      1:"♟", 2:"♜", 3:"♞", 4:"♝", 5:"♛", 6:"♚",
#                      #0:"□"}
#                      0:" "}
#     inverted_nums_to_chess = {1:"♙", 2:"♖", 3:"♘", 4:"♗", 5:"♕", 6:"♔",
#                      7:"♟", 8:"♜", 9:"♞", 10:"♝", 11:"♛", 12:"♚",
#                      #0:"□"}
#                      0:" "}

#     chess_rows = np.array([8,7,6,5,4,3,2,1])
#     chess_letters = np.array(["a","b","c","d","e","f","g","h"])
#     side_text = [
#         f'         {f"Piece  {colourer('01')}{piece:^4}{colourer(0)}  can move to:":^28}',
#         f'         white pieces    black pieces',
#         f'         ',
#         f'         ',
#         f'         ',
#         f'         ',
#         f'         ', 
#         f'         ',
#         f'']
#     print('\n')

#     one = 1
#     print("      a  b  c  d  e  f  g  h\n")
#     for chess_row, i, side in zip(chess_rows, range(len(board)), side_text):        

#         lst = []
#         for j, x in enumerate(board[i]):
#             if (j + one)%2 != 0:
#                 test = f' {colourer('07')}{inverted_nums_to_chess[int(x)]} {colourer(0)}'
#             else:
#                 test = f' {normal_nums_to_chess[int(x)]} '
#             lst.append(test)
#         one += 1
#         #lst = [f"{f"\033[07m{nums_to_chess[int(x)]+"   "}\033[0m":4}" for x in board[i]]
#         row_text = "".join(lst)
#         print(f'{chess_row}    {row_text}    {chess_row}       {side}')
#     print("\n      a  b  c  d  e  f  g  h")

#     print("\n")


def where_can_move(board, position, col_pos, row_pos, your_pieces, their_pieces):
    piece = row_pos, col_pos
    rows = np.array([0, 1, 2, 3, 4, 5, 6, 7])
    cols = np.array([0, 1, 2, 3, 4, 5, 6, 7])
    movement_list = [
        pawn_movement,
        rook_movement,
        knight_movement,
        bishop_movement,
        queen_movement,
        king_movement,
        ]

    where_can_moves = []

    for row in rows:
        for col in cols:
            target = row, col
            if not is_friendly_fire(col, row, board, your_pieces):
                a = np.copy(board)
                a[row, col] = a[piece]
                a[piece] = 0
                king_can_be_attacked = in_check(a, your_pieces, their_pieces)

                if not np.isin(True, king_can_be_attacked):
                    i = board[piece] - 1 # prepares piece numbers for calling movement_list
                    i = (i) if (5 >= i) else (i - 6)
                    if movement_list[int(i)](piece, target, board, your_pieces, their_pieces):
                        where_can_moves.append(s_to_c[col+1]+str(row+1))

    len_side_rows = [0, 0, 0, 0, 0, 0, 0]
    for index, piece in enumerate(where_can_moves):
        len_side_rows[index//3] += 1

    side_text = [f'where piece   {colourer('01')}{colourer('04')}{colourer('32')}{position:^4}{colourer(0)}   can go:']

    a_row = 0
    for index, length in enumerate(len_side_rows):
        if length == 3:
            side_text.append("    "+f'{colourer('32')}{where_can_moves[0 + 3*a_row]:^8}{where_can_moves[1 + 3*a_row]:^8}{where_can_moves[2 + 3*a_row]:^8}{colourer(0)}')
        if length == 2:
            side_text.append("   "+f'{colourer('32')}{where_can_moves[-2]:^13}{where_can_moves[-1]:^13}{colourer(0)}')
        if length == 1:
            side_text.append("   "+f'{colourer('32')}{where_can_moves[-1]:^27}{colourer(0)}')
        if length == 0:
            side_text.append("")
        a_row += 1

    #print(side_text)

    # side_text = [
    #     f'where piece   {colourer('01')}{colourer('04')}{colourer('32')}{position:^4}{colourer(0)}   can go:',
    #     f'         a',
    #     f'         b',
    #     f'         c',
    #     f'         d',
    #     f'         e',
    #     f'         f', 
    #     f'         g',
    #     f'']

    display(board, side_text, position)

    return where_can_moves



def move(board, your_pieces, their_pieces):

    num = 0
    can_move = False

    while not can_move:

        print(error(num))
        col_pos, row_pos, position = piece_to_move()
        num = 1

        if np.isin(board[row_pos, col_pos], your_pieces):
            possibilities = where_can_move(board, position, col_pos, row_pos, your_pieces, their_pieces)

            num = 2
            target_row, target_col = where_to()

            if not is_friendly_fire(target_col, target_row, board, your_pieces):

                num = 3
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
                    num = 4
                    
                    if can_move: # if can_move is True 
                        a = np.copy(board)
                        if board[current] == your_pieces[-1]:
                            a[target] = your_pieces[-1]
                            a[current] = 0
                        king_can_be_attacked = in_check(a, your_pieces, their_pieces)
                        num = 5

                        if np.isin(True, king_can_be_attacked):
                            can_move = False
                        else:
                            if not eats_king(board, your_pieces):
                                board[target_row, target_col] = board[row_pos, col_pos]
                                board[row_pos, col_pos] = 0
                            else:
                                num = 6
                                can_move = False
            
    return board

def pawn_movement(current, target, board, your_pieces, their_pieces):
    row_pos, col_pos = current
    target_row, target_col = target

    starting_point, one_jump, two_jump = 0, 0, 0
    (starting_point, one_jump, two_jump) = (1, 1, 2) if board[row_pos, col_pos] == 1 else (starting_point, one_jump, two_jump)
    (starting_point, one_jump, two_jump) = (6, -1, -2) if board[row_pos, col_pos] == 7 else (starting_point, one_jump, two_jump)

    if int(board[target_row, target_col]) == 0:
        if (row_pos + one_jump == target_row) and (target_col == col_pos):
            #if not np.isin(board[target_row, target_col], their_pieces):
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

        
def rook_movement(current, target, board, _, __):

    can_move = False
    can_move = can_horizontal(current, target, board) if can_move == False else True
    can_move = can_vertical(current, target, board) if can_move == False else True
    
    return can_move


def knight_movement(current, target, board, your_pieces, _):
    row_pos, col_pos = current
    target_row, target_col = target

    possibilities = np.array([[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]])

    for i in possibilities:
        if (target_row == row_pos + i[0]) and (target_col == col_pos + i[1]):  
            return True

    return False 


def bishop_movement(current, target, board, _, __):

    can_move = False
    can_move = can_diagonal(current, target, board) if can_move == False else True
        
    return can_move 


def queen_movement(current, target, board, _, __):

    can_move = False
    can_move = can_diagonal(current, target, board) if can_move == False else True
    can_move = can_horizontal(current, target, board) if can_move == False else True
    can_move = can_vertical(current, target, board) if can_move == False else True
    
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