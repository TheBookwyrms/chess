from game_setup import *
from move_for_turn import *
from common_functions import *
from game_enders import *


# TODO: give pawns diagonal attack
# TODO: add en passant
# TODO: add castling
# TODO: make _x_ in check
# TODO: make _x_ in stalemate
# TODO: make _x_ in checkmate
# TODO


# which row (top to bottom) you're in, and then which column you're in (left to right)



def turn(board, your_pieces, their_pieces, game_over):

    if np.isin(True, in_check(board, your_pieces, their_pieces)):
        print("you are in check, only moves that bring you out of check will be permitted\n")

    board = move(board, your_pieces, their_pieces)

    if in_stalemate(board, their_pieces, your_pieces):
        print(f"a stalemate has occured, the game is over")
        game_over = True

    #if in_checkmate(board, your_pieces, their_pieces):
     #   pass

    return board, game_over

def display(board):

    board = np.flipud(board)

    chess_rows = np.array([8,7,6,5,4,3,2,1])
    chess_letters = np.array(["a","b","c","d","e","f","g","h"])

    print('\n')

    print("     a   b   c   d   e   f   g   h\n")
    for chess_row, i in zip(chess_rows, range(len(board))):        

        row_text = "".join(f"{int(x):4}" for x in board[i])
        print(f'{chess_row} {row_text}    {chess_row}')
    print("\n     a   b   c   d   e   f   g   h")

    print("\n")


def main():
    board, white_pieces, black_pieces = setup()

    game_over = False

    whos_turn = 0

    print("Let the game commence\n")
    print("\nWhite is on the top\nBlack is on the bottom\n")
    print("columns are 1-8, left to right. rows are 1-8, top to bottom.")

    display(board)

    while not game_over:
        if whos_turn%2 == 0:
            print("white turn")
            board, game_over = turn(board, white_pieces, black_pieces, game_over) # white turn
            display(board)
        else:
            print("black turn")
            board, game_over = turn(board, black_pieces, white_pieces, game_over) # black turn
            display(board)

        
        #black_in_check = if_black_in_check()
        #black_in_stalemate = if_black_in_stalemate()
        #black_in_checkmate = if_black_in_checkmate()
        
        whos_turn += 1

        #game_over = False

main()