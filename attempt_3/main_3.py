from setup import *
from move_for_turn import *
from common_functions import *


# TODO: give pawns diagonal attack
# TODO: make _x_ in check
# TODO: make _x_ in stalemate
# TODO: make _x_ in checkmate
# TODO


# which row (top to bottom) you're in, and then which column you're in (left to right)



def white_turn(board, white_pieces, black_pieces):

    board = move(board, white_pieces, black_pieces)
    return board


def black_turn(board, white_pieces, black_pieces):
    return board

def display(board):

    board = np.flipud(board)

    chess_rows = np.array([8,7,6,5,4,3,2,1])
    chess_letters = np.array(["a","b","c","d","e","f","g","h"])

    print('\n')

    print("        a   b   c   d   e   f   g   h\n")
    for chess_row, i in zip(chess_rows[:], range(len(board[:]))):
        
        row_i = str(board[i]).split(".")
        row_i[0] = f'{row_i[0][0]}  {row_i[0][-1]}'

        print(f'{chess_row}    {"  ".join(row_i)}    {chess_row}')
    print("\n        a   b   c   d   e   f   g   h")

    print("\n")


def main():
    board, white_pieces, black_pieces = setup()

    game_over = False

    print("Let the game commence\n")
    print("\nWhite is on the top\nBlack is on the bottom\n")
    print("columns are 1-8, left to right. rows are 1-8, top to bottom.")

    display(board)

    while not game_over:
        board = white_turn(board, white_pieces, black_pieces)
        #black_in_check = if_black_in_check()
        #black_in_stalemate = if_black_in_stalemate()
        #black_in_checkmate = if_black_in_checkmate()
        display(board)
        #board = black_turn(board, white_pieces, black_pieces)
        #display(board)
        #game_over = False

main()