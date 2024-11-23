import numpy as np

def white_piece_to_move():
    print("columns are 1-8, left to right. rows are 1-8, top to bottom.")
    position = input("type column and row of piece to be moved, as a single number\n")
    lst = [int(i) for i in position]
    col_pos = lst[0]-1
    row_pos = lst[1]-1
    return col_pos, row_pos

def move_white(col_pos, row_pos, board, white_pieces):
    position = input("type row and column to move to, as a single number\n")
    lst = [int(i) for i in position]
    target_col = lst[0]-1
    target_row = lst[1]-1
    initial_board = np.copy(board)


    if (col_pos == target_col) and (row_pos == target_row):
        print("invalid move, pieces cannot be moved to they are")
        col_pos, row_pos = white_piece_to_move()
        board = move_white(col_pos, row_pos, board, white_pieces)
        return board
   

    elif board[row_pos][col_pos] == 1: # if piece is white pawn
        board = white_pawn_movement(col_pos, target_col, row_pos, target_row, board, white_pieces)
        if (initial_board == board).all():
            print("bad")
            col_pos, row_pos = white_piece_to_move()
            board = move_white(col_pos, row_pos, board, white_pieces)
            return board
        else:
            print("good")
            return board

    elif board[row_pos][col_pos] == 2: # if piece is white rook
        board = white_rook_movement(col_pos, target_col, row_pos, target_row, board, white_pieces)
        if (initial_board == board).all():
            print("bad")
            col_pos, row_pos = white_piece_to_move()
            board = move_white(col_pos, row_pos, board, white_pieces)
            return board
        else:
            print("good")
            return board

    elif board[row_pos][col_pos] == 3: # if piece is white knight
        pass
    elif board[row_pos][col_pos] == 4: # if piece is white bishop
        pass
    elif board[row_pos][col_pos] == 5: # if piece is white queen
        pass
    elif board[row_pos][col_pos] == 6: # is piece is white king
        pass



def is_friendly_fire(target_col, target_row, board, white_pieces):
    print(f'\n\n{board[target_row][target_col]}, \n\n')
    if np.isin(board[target_row][target_col], white_pieces):
        return True
    elif not np.isin(board[target_row][target_col], white_pieces):
        return False

def white_pawn_movement(col_pos, target_col, row_pos, target_row, board, white_pieces):
    if not is_friendly_fire(target_col, target_row, board, white_pieces):

        if row_pos == 1:
            if (row_pos + 1 == target_row) and (target_col == col_pos):
                board[row_pos][col_pos] = 0
                board[target_row][target_col] = 1
                return board
            elif (row_pos + 2 == target_row) and (target_col == col_pos):

                if not is_friendly_fire(target_col, target_row-1, board, white_pieces):
                    board[row_pos][col_pos] = 0
                    board[target_row][target_col] = 1
                    return board
                
                else:
                    print("case 3: error, something went wrong.\nPlease retry")
                    return board
            else:
                print("invalid move, try again")
                return board
        else:
            if (row_pos + 1 == target_row) and (target_col == col_pos):
                board[row_pos][col_pos] = 0
                board[target_row][target_col] = 1
                return board
            else:
                print("invalid move, try again")
                return board
    else:
        print("attacking your own pieces is not permitted, try again")
        return board    

        
def white_rook_movement(col_pos, target_col, row_pos, target_row, board, white_pieces):
    if not is_friendly_fire(target_col, target_row, board, white_pieces):

        if (col_pos == target_col):
            plus_minus_one = int((target_row - row_pos) / np.abs(target_row - row_pos))
            for i in range(row_pos + plus_minus_one, target_row + plus_minus_one, plus_minus_one):
                if int(board[i][target_col]) != 0:
                    print("invalid move, try again")
                    board = move_white(col_pos, row_pos, board, white_pieces)
                    return board
            board[row_pos][col_pos] = 0
            board[target_row][target_col] = 2
            return board
        
        elif (row_pos == target_row):
            plus_minus_one = int((target_col - col_pos) / np.abs(target_col - col_pos))
            for i in range(col_pos + plus_minus_one, target_col+1, plus_minus_one):
                if int(board[target_row][i]) != 0:
                    print("invalid move, try again")
                    board = move_white(col_pos, row_pos, board, white_pieces)
                    return board
            board[row_pos][col_pos] = 0
            board[target_row][target_col] = 2
            return board
        
        else:
            print("invalid move, try again")
            return board    
    else:
        print("attacking your own pieces is not permitted, try again")
        return board    
