import numpy as np

# tiles = np.array([
#     81, 82, 83, 84, 85, 86, 87, 88,
#     71, 72, 73, 74, 75, 76, 77, 78,
#     61, 62, 63, 64, 65, 66, 67, 68,
#     51, 52, 53, 54, 55, 56, 57, 58,
#     41, 42, 43, 44, 45, 46, 47, 48,
#     31, 32, 33, 34, 35, 36, 37, 38,
#     21, 22, 23, 24, 25, 26, 27, 28,
#     11, 12, 13, 14, 15, 16, 17, 18
# ])

white = 1
black = 2
rows = np.array([1, 2, 3, 4, 5, 6, 7, 8]) # row positions
cols = np.array([1, 2, 3, 4, 5, 6, 7, 8]) # column positions

# TODO make not_friendly_fire and not_blocked | in all
# TODO make pawn hostile_move
# TODO setup initial positions

class movement_options:
    def king_valid_row(self, target_row):
        if (self.row + 1 == target_row) | (self.row - 1 == target_row) | (self.row == target_row):
            return True
        else:
            return False
        
    def king_valid_col(self, target_col):
        if (self.col + 1 == target_col) | (self.col - 1 == target_col) | (self.col == target_col):
            return True
        else:
            return False
        
    def is_diagonal(self, target_row, target_col):
        if np.abs(self.row - target_row) == np.abs(self.col - target_col):
            return True
        else:
            return False

    def valid_row_constant_col(self, target_row, target_col):
        if (self.row != target_row) and (self.col == target_col):
            return True
        else:
            return False
        
    def valid_col_constant_row(self, target_row, target_col):
        if (self.col != target_col) and (self.row == target_row):
            return True
        else:
            return False
    
    def is_linear(self, target_row, target_col):
        if self.valid_row_constant_col(target_row, target_col) ^ self.valid_col_constant_row(target_row, target_col):
            return True
        else:
            return False

    def is_valid_knight_move(self, target_row, target_col):
        if (np.abs(self.row - target_row) == 2) and (np.abs(self.col - target_col) == 1):
            return True
        elif (np.abs(self.row - target_row) == 1) and (np.abs(self.col - target_col) == 2):
            return True
        else:
            return False
    
    def is_valid_non_hostile(self, target_row, target_col):
        if self.row == target_row:
            if self.col + 1 == target_col:
                return True
            elif (self.col + 2 == target_col) and (self.row == self.initial_row) and (self.col == self.initial_col):
                return True
            else:
                return False
        else:
            return False
        
    def is_valid_hostile(self, target_row, target_col):
        pass

    def is_valid_overall(self, target_row, target_col):
        if self.is_valid_non_hostile(target_row, target_col) or self.is_valid_hostile(target_row, target_col):
            return True
        else:
            return False

class movement_validation:
    def not_blocked(self, target_row, target_col):
        pass
    
    def not_friendly_fire(self, target_row, target_col):
        pass

    def king_not_friendly_fire(self, target_row, target_col, colour):
        for piece in self.white_pieces:
            if piece.row == target_row and piece.col == target_col:
                return False
        return True

        

class king(movement_options, movement_validation):
    def __init__(self, initial_row, initial_column, colour):
        self.row = initial_row
        self.col = initial_column
        self.colour = colour
    
    def valid_move(self, target_row, target_col, colour):
        reqs = np.array([
            np.isin(target_row, rows),
            np.isin(target_col, cols),
            not (self.row == target_row) & (self.col == target_col),
            self.king_valid_row(target_row),
            self.king_valid_col(target_col),
            self.king_not_friendly_fire(target_row, target_col, colour)
        ])

        if reqs.all() == True:
            return True
        else:
            return False
        
    def move(self, target_row, target_col, colour):
        if self.valid_move(target_row, target_col, colour):
            self.row = target_row
            self.col = target_col
            print("move valid")
        else:
            print("move invalid")

class queen(movement_options, movement_validation):
    def __init__(self, initial_row, initial_column, colour):
        self.row = initial_row
        self.col = initial_column
        self.colour = colour
        
    def valid_move(self, target_row, target_col):
        reqs = np.array([
            np.isin(target_row, rows),
            np.isin(target_col, cols),
            not (self.row == target_row) & (self.col == target_col),
            self.is_linear(target_row, target_col) or self.is_diagonal(target_row, target_col),
            #self.not_friendly_fire(target_row, target_col),
            #self.not_blocked(target_row, target_col)
        ])

        if reqs.all() == True:
            return True
        else:
            return False
        
    def move(self, target_row, target_col):
        if self.valid_move(target_row, target_col):
            self.row = target_row
            self.col = target_col
            print("move valid")
        else:
            print("move invalid")

class rook(movement_options, movement_validation):
    def __init__(self, initial_row, initial_column, colour):
        self.row = initial_row
        self.col = initial_column
        self.colour = colour
    
        
    def valid_move(self, target_row, target_col):
        reqs = np.array([
            np.isin(target_row, rows),
            np.isin(target_col, cols),
            not ((self.row == target_row) & (self.col == target_col)),
            self.is_linear(target_row, target_col),
            #self.not_friendly_fire(target_row, target_col),
            #self.not_blocked(target_row, target_col)
        ])

        if reqs.all() == True:
            return True
        else:
            return False
        
    def move(self, target_row, target_col):
        if self.valid_move(target_row, target_col):
            self.row = target_row
            self.col = target_col
            print("move valid")
        else:
            print("move invalid")

class knight(movement_options, movement_validation):
    def __init__(self, initial_row, initial_column, colour):
        self.row = initial_row
        self.col = initial_column
        self.colour = colour
    
    def valid_move(self, target_row, target_col):
        reqs = np.array([
            np.isin(target_row, rows),
            np.isin(target_col, cols),
            not ((self.row == target_row) & (self.col == target_col)),
            self.is_valid_knight_move(target_row, target_col),
            #self.not_friendly_fire(target_row, target_col),
        ])

        if reqs.all() == True:
            return True
        else:
            return False
        
    def move(self, target_row, target_col):
        if self.valid_move(target_row, target_col):
            self.row = target_row
            self.col = target_col
            print("move valid")
        else:
            print("move invalid")

class bishop(movement_options, movement_validation):
    def __init__(self, initial_row, initial_column, colour):
        self.row = initial_row
        self.col = initial_column
        self.colour = colour
    
    
        
    def valid_move(self, target_row, target_col):
        reqs = np.array([
            np.isin(target_row, rows),
            np.isin(target_col, cols),
            not (self.row == target_row) & (self.col == target_col),
            self.is_diagonal(target_row, target_col),
            #self.not_friendly_fire(target_row, target_col),
            #self.not_blocked(target_row, target_col)
        ])

        if reqs.all() == True:
            return True
        else:
            return False
        
    def move(self, target_row, target_col):
        if self.valid_move(target_row, target_col):
            self.row = target_row
            self.col = target_col
            print("move valid")
        else:
            print("move invalid")

class pawn(movement_options, movement_validation):
    def __init__(self, initial_row, initial_column, colour):
        self.initial_row = initial_row
        self.initial_col = initial_column
        self.row = initial_row
        self.col = initial_column
        self.colour = colour
    
    
        
    def valid_move(self, target_row, target_col):
        reqs = np.array([
            np.isin(target_row, rows),
            np.isin(target_col, cols),
            not (self.row == target_row) & (self.col == target_col),
            self.is_valid_overall(target_row, target_col),
            #self.not_friendly_fire(target_row, target_col),
            #self.not_blocked(target_row, target_col)
        ])

        if reqs.all() == True:
            return True
        else:
            return False
        
    def move(self, target_row, target_col):
        if self.valid_move(target_row, target_col):
            self.row = target_row
            self.col = target_col
            print("move valid")
        else:
            print("move invalid")

class all_pieces:
    def __init__(self):
        super().__init__()
        self.white_pawn_1 = pawn(2,1,white)
        self.white_pawn_2 = pawn(2,2,white)
        self.white_pawn_3 = pawn(2,3,white)
        self.white_pawn_4 = pawn(2,4,white)
        self.white_pawn_5 = pawn(2,5,white)
        self.white_pawn_6 = pawn(2,6,white)
        self.white_pawn_7 = pawn(2,7,white)
        self.white_pawn_8 = pawn(2,8,white)
        self.white_rook_1 = rook(1,1,white)
        self.white_rook_2 = rook(1,8,white)
        self.white_knight_1 = knight(1,2,white)
        self.white_knight_2 = knight(1,7,white)
        self.white_bishop_1 = bishop(1,3,white)
        self.white_bishop_2 = bishop(1,6,white)
        self.white_queen = queen(1,4,white)
        white_king = king(1,5,white)

        white_pieces = np.array([
            self.white_pawn_1, self.white_pawn_2,
            self.white_pawn_3, self.white_pawn_4,
            self.white_pawn_5, self.white_pawn_6,
            self.white_pawn_7, self.white_pawn_8,
            self.white_rook_1, self.white_rook_2,
            self.white_knight_1, self.white_knight_2,
            self.white_bishop_1, self.white_bishop_2,
            self.white_queen, white_king
        ])

        self.black_pawn_1 = pawn(7,1,black)
        self.black_pawn_2 = pawn(7,2,black)
        self.black_pawn_3 = pawn(7,3,black)
        self.black_pawn_4 = pawn(7,4,black)
        self.black_pawn_5 = pawn(7,5,black)
        self.black_pawn_6 = pawn(7,6,black)
        self.black_pawn_7 = pawn(7,7,black)
        self.black_pawn_8 = pawn(7,8,black)
        self.black_rook_1 = rook(8,1,black)
        self.black_rook_2 = rook(8,8,black)
        self.black_knight_1 = knight(8,2,black)
        self.black_knight_2 = knight(8,7,black)
        self.black_bishop_1 = bishop(8,3,black)
        self.black_bishop_2 = bishop(8,6,black)
        self.black_queen = queen(8,4,black)
        self.black_king = king(8,5,black)

        self.black_pieces = np.array([
            self.black_pawn_1, self.black_pawn_2,
            self.black_pawn_3, self.black_pawn_4,
            self.black_pawn_5, self.black_pawn_6,
            self.black_pawn_7, self.black_pawn_8,
            self.black_rook_1, self.black_rook_2,
            self.black_knight_1, self.black_knight_2,
            self.black_bishop_1, self.black_bishop_2,
            self.black_queen, self.black_king
        ])





'''
ideas:

white_pieces class?

how to call all pieces at start of game, and then can modify them?
white_king = king(x, y, white)?
black_king = king(x, y, black)?
that should let me modify each piece by itself later, which would be useful

how do i do death?
a status condition that changes, or a part of a higher class?
i have to figure out class inheritance
as a condition, __init__ sets it to alive,
if they get killed, it gets set to False,
for every move, etc, action we have a if alive: qualifier

for not_friendly_fire, if a piece is in the way and is of same colour,
then you can't move
how to do this?
checking for all pieces if any are in that position is slow
then again, Alex did that for planets in force_awakens
it would work

isn't not_friendly_fire a subcategory of not_blocked?
actually, can't i just only do one category?
no
because if it lands on a spot and that's the same colour
so, i compute if it's blocked
if not blocked, i compute if it's friendly fire
because blocked is only if something is in the path ON the way
friendly fire is about destination

how to i do no_blocked?
that was the big problem in v1
i think if i return out the path, i can check along the path
otherwise, i have to check incrementally
which would be a pain and be very slow

i should also condense all the move stuff into a parent class
for readability, brevity, and generally it's a good idea

so i have to figure out inheritance
'''

