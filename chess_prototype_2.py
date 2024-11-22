import numpy as np
from setup import *
from movement_types import *

rows = np.array([1,2,3,4,5,6,7,8]) #position within a given row
cols = np.array([1,2,3,4,5,6,7,8]) #position within a given column

def print_game_status(white_pieces, black_pieces):
    pass

def update_black_deaths(piece, white_pieces, black_pieces):
    pass


def is_friendly_fire(piece, white_pieces, black_pieces, move_to):
    if piece[1][1] == 'w':
        for pieces in white_pieces:
            if (pieces[0] == move_to).all():
                print('''\nYou cannot move a piece to a space occupied by another of your pieces.\nPlease try again.''')
                return False
    
    elif piece[1][1] == 'b':
        for pieces in black_pieces:
            if (pieces[0] == move_to).all():
                print('''\nYou cannot move a piece to a space occupied by another of your pieces.\nPlease try again.''')
                return False
    
    return False



def move(index, piece, white_pieces, black_pieces, move_to):
    if not is_friendly_fire(piece, white_pieces, black_pieces, move_to):
        if str(piece[1][0]) == "p":
            white_pieces, black_pieces = pawn_movement(index, piece, white_pieces, black_pieces, move_to)
        # elif piece[1][0] == "r":
        #     white_pieces, black_pieces = rook_movement(index, piece, white_pieces, black_pieces, move_to)
        # elif piece[1][0] == "kn":
        #     white_pieces, black_pieces = knight_movement(index, piece, white_pieces, black_pieces, move_to)
        # elif piece[1][0] == "b":
        #     white_pieces, black_pieces = bishop_movement(index, piece, white_pieces, black_pieces, move_to)
        # elif piece[1][0] == "q":
        #     white_pieces, black_pieces = queen_movement(index, piece, white_pieces, black_pieces, move_to)
        # elif piece[1][0] == "k":
        #     white_pieces, black_pieces = king_movement(index, piece, white_pieces, black_pieces, move_to)
        else:
            raise ValueError("incorrect piece type, check piece definition in setup.py")



def white_turn(white_pieces, black_pieces):
    target = input("\ntype the row and column of the piece you wish to move, as a single number\n")
    move_from = np.array([(i) for i in target])


    pieces_not_used = []

    for index, piece in enumerate(white_pieces):
        if (piece[0] == move_from).all():
            target = input("\ntype the row and column you wish to move the piece to, as a single number\n")
            move_to = np.array([int(i) for i in target])

            if not (piece[0] == move_to).all():
                move(index, piece, white_pieces, black_pieces, move_to)
            else:
                print('''\nYou cannot move a piece to where it currently is.\nPlease try again.''')
                white_turn(white_pieces, black_pieces)
        else:
            pieces_not_used.append(piece)

    if len(pieces_not_used) == len(white_pieces):
        print('''\nThat is not a white piece.\nPlease try again.''')
        white_turn(white_pieces, black_pieces)

    update_black_deaths(piece, white_pieces, black_pieces)
    
    print_game_status(white_pieces, black_pieces)

    return white_pieces, black_pieces

    
def black_turn(white_pieces, black_pieces):
    return white_pieces, black_pieces

def game():
    white_pieces, black_pieces = setup()

    game_not_over = True
    while game_not_over:
        white_pieces, black_pieces = white_turn(white_pieces, black_pieces)
        white_pieces, black_pieces = black_turn(white_pieces, black_pieces)
    
    print("The game is over")

game()