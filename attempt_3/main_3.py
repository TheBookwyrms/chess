from game_setup import *
from move_for_turn import *
from common_functions import *
from game_enders import *


# TODO: add en passant
# TODO: add castling
# TODO: fix pawn error: after e2-e4, b7-b5 doesn't work


# which row (top to bottom) you're in, and then which column you're in (left to right)


def upgrade_pawns(board, your_pieces, their_pieces):
    end_point = 0
    end_point = 7 if your_pieces[0] == 1 else end_point
    end_point = 0 if your_pieces[0] == 7 else end_point

    col = np.where(board[end_point] == your_pieces[0])[0][0] if np.where(board[end_point] == your_pieces[0])[0].size > 0 else np.array([])

    if col.size > 0:
        letter = s_to_c[int(col)+1]
        if board[end_point][col] == your_pieces[0]:
            promoted = False
            print(f"your pawn on {letter}{end_point+1} must promote")
            while promoted == False:
                upgrade_to = input("your pawn upgrades to:        (knight, rook, bishop, queen)\n")
                promoted = True
                if upgrade_to == "rook":
                    board[end_point][col] = your_pieces[1]
                elif upgrade_to == "knight":
                    board[end_point][col] = your_pieces[2]
                elif upgrade_to == "bishop":
                    board[end_point][col] = your_pieces[3]
                elif upgrade_to == "queen":
                    board[end_point][col] = your_pieces[4]
                else:
                    print("that does not promote your pawn, retry")
                    promoted = False

    return board



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
        board = upgrade_pawns(board, your_pieces, their_pieces)


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