from setup import *
from white_movements import *

# which row (top to bottom) you're in, and then which column you're in (left to right)

def update_for_black_deaths(board, white_pieces, black_pieces):
    pass

def piece_to_move():
    print("columns are 1-8, left to right. rows are 1-8, top to bottom.")
    position = input("type column and row of piece to be moved, as a single number\n")
    lst = [int(i) for i in position]
    col_pos = lst[0]-1
    row_pos = lst[1]-1
    return col_pos, row_pos

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
    print(board)
    print("\n")

def main():
    board, white_pieces, black_pieces = setup()

    game_over = False

    print("Let the game commence\n")
    print("\nWhite is on the top\nBlack is on the bottom\n")
    display(board)

    while not game_over:
        board = white_turn(board, white_pieces, black_pieces)
        display(board)
        print(type(board))
        #board = black_turn(board, white_pieces, black_pieces)
        #display(board)
        #game_over = False

main()