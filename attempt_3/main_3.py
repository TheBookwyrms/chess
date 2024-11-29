from game_setup import *
from move_for_turn import *
from common_functions import *


# TODO: give pawns diagonal attack
# TODO: add en passant
# TODO: add castling
# TODO: make _x_ in check
# TODO: make _x_ in stalemate
# TODO: make _x_ in checkmate
# TODO


# which row (top to bottom) you're in, and then which column you're in (left to right)



def turn(board, your_pieces, their_pieces):

    board = move(board, your_pieces, their_pieces)
    return board

def display(board):

    board = np.flipud(board)

    chess_rows = np.array([8,7,6,5,4,3,2,1])
    chess_letters = np.array(["a","b","c","d","e","f","g","h"])

    print('\n')

    print("     a   b   c   d   e   f   g   h\n")
    for chess_row, i in zip(chess_rows[:], range(len(board[:]))):        

        row_text = "".join(f"{int(x):4}" for x in board[i])
        print(f'{chess_row} {row_text}    {chess_row}')
    print("\n     a   b   c   d   e   f   g   h")

    print("\n")


def main():
    board, white_pieces, black_pieces = setup()

    game_over = False

    print("Let the game commence\n")
    print("\nWhite is on the top\nBlack is on the bottom\n")
    print("columns are 1-8, left to right. rows are 1-8, top to bottom.")

    display(board)

    while not game_over:
        print("white turn")
        board = turn(board, white_pieces, black_pieces) # white turn
        #black_in_check = if_black_in_check()
        #black_in_stalemate = if_black_in_stalemate()
        #black_in_checkmate = if_black_in_checkmate()
        display(board)
        #print("black turn")
        #board = turn(board, black_pieces, white_pieces) # black turn
        #display(board)
        #game_over = False

main()