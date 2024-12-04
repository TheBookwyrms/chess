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

def display(board):

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
    side_text = [
        f'         {"what each piece means":^28}',
        "         white pieces    black pieces",
        f'{"pawn":>6}   {inverted_nums_to_chess[7]:^12}    {inverted_nums_to_chess[1]:^12}',
        f'{"rook":>6}   {inverted_nums_to_chess[8]:^12}    {inverted_nums_to_chess[2]:^12}',
        f'{"knight":>6}   {inverted_nums_to_chess[9]:^12}    {inverted_nums_to_chess[3]:^12}',
        f'{"bishop":>6}   {inverted_nums_to_chess[10]:^12}    {inverted_nums_to_chess[4]:^12}',
        f'{"queen":>6}   {inverted_nums_to_chess[11]:^12}    {inverted_nums_to_chess[5]:^12}', 
        f'{"king":>6}   {inverted_nums_to_chess[12]:^12}    {inverted_nums_to_chess[6]:^12}',
        f'']
    print('\n')

    one = 1
    print("      a  b  c  d  e  f  g  h\n")
    for chess_row, i, side in zip(chess_rows, range(len(board)), side_text):        

        lst = []
        for j, x in enumerate(board[i]):
            if (j + one)%2 != 0:
                test = f' {colourer('07')}{inverted_nums_to_chess[int(x)]} {colourer(0)}'
            else:
                test = f' {normal_nums_to_chess[int(x)]} '
            lst.append(test)
        one += 1
        #lst = [f"{f"\033[07m{nums_to_chess[int(x)]+"   "}\033[0m":4}" for x in board[i]]
        row_text = "".join(lst)
        print(f'{chess_row}    {row_text}    {chess_row}       {side}')
    print("\n      a  b  c  d  e  f  g  h")

    print("\n")


def main():
    board, white_pieces, black_pieces = setup()

    game_over = False
    whos_turn = 0

    print("Let the game commence\n")
    print("\nWhite is on the top\nBlack is on the bottom\n")

    while not game_over:
        if whos_turn%2 == 0:
            display(board)
            print(f"{colourer('04')}white turn{colourer(0)}")
            board, game_over = turn(board, white_pieces, black_pieces, game_over) # white turn
        else:
            display(board)
            print(f"{colourer('04')}black turn{colourer(0)}")
            board, game_over = turn(board, black_pieces, white_pieces, game_over) # black turn

        whos_turn += 1
main()