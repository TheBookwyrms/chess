from setup import *
from white_movements import *
from common_functions import *

# which row (top to bottom) you're in, and then which column you're in (left to right)

def update_for_black_deaths(board, white_pieces, black_pieces):
    pass



def white_turn(board, white_pieces, black_pieces):
    col_pos, row_pos = piece_to_move()

    if np.isin(board[row_pos][col_pos], white_pieces):
        board = move_white(col_pos, row_pos, board, white_pieces)
        black_pieces = update_for_black_deaths(board, white_pieces, black_pieces)
    else:
        print("none of your pieces are in that position\n")
        white_turn(board, white_pieces, black_pieces)
    
    return board



def black_turn(board, white_pieces, black_pieces):
    return board

def display(board):
    print("\n")
    print(board)
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
        display(board)
        print(type(board))
        #board = black_turn(board, white_pieces, black_pieces)
        #display(board)
        #game_over = False

main()