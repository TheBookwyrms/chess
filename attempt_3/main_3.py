from game_setup import *
from move_for_turn import *
from common_functions import *
from game_enders import *


# TODO: add en passant
# TODO: add castling


# which row (top to bottom) you're in, and then which column you're in (left to right)



def turn(board, your_pieces, their_pieces, game_over):

    if in_stalemate(board, your_pieces, their_pieces):
        if not np.isin(True, in_check(board, your_pieces, their_pieces)):
            print(f"{colourer('35')}a stalemate has occured, the game is over{colourer(0)}")
            game_over = True
        else:
            print(f"{colourer('35')}you are in checkmate, the game is over{colourer(0)}")
            game_over = True
    else:
        if np.isin(True, in_check(board, your_pieces, their_pieces)):
            print(f"{colourer('33')}you are in check, only moves that bring you out of check will be permitted\n{colourer(0)}")

        board = move(board, your_pieces, their_pieces)


    #if in_checkmate(board, your_pieces, their_pieces):
     #   pass

    return board, game_over


def main():
    board, white_pieces, black_pieces, side_text = setup()

    game_over = False
    whos_turn = 0

    print("Let the game commence\n")
    print("\nWhite is on the top\nBlack is on the bottom\n")

    while not game_over:
        if whos_turn%2 == 0:
            display(board, side_text, None)
            print(f"{colourer('04')}white turn{colourer(0)}")
            board, game_over = turn(board, white_pieces, black_pieces, game_over) # white turn
        else:
            display(board, side_text, None)
            print(f"{colourer('04')}black turn{colourer(0)}")
            board, game_over = turn(board, black_pieces, white_pieces, game_over) # black turn

        whos_turn += 1
main()