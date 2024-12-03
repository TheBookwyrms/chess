from common_functions import *

def error(num):
    errors = {
        0:"",
        1:f"{colourer('31')}none of your pieces are in that position{colourer(0)}",
        2:f"{colourer('31')}attacking your own pieces is not permitted, try again{colourer(0)}",
        3:f"{colourer('31')}invalid move, pieces cannot be moved to where they are{colourer(0)}",
        4:f"{colourer('31')}invalid move, try again{colourer(0)}",
        5:f"{colourer('31')}this move would put you in check{colourer(0)}",
        6:f"{colourer('31')}eating kings directly is not allowed, the game can only be ended by checkmate or stalemate\ntry again{colourer(0)}",
        #7:,
        #8:,
        #9:,
    }
    return errors[num]