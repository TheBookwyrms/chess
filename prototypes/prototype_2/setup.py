import numpy as np

def make_white_pieces():
    #[row, column, type, colour, status (True if alive, False if dead), pawn initial position (True if yes, False if not)]
    w_p_1 = [np.array([2, 1]), ['p','w'], [True, True]] #?
    w_p_2 = np.array([[2, 2], ['p','w'], [True, True]])
    w_p_3 = np.array([[2, 3], ['p','w'], [True, True]])
    w_p_4 = np.array([[2, 4], ['p','w'], [True, True]])
    w_p_5 = np.array([[2, 5], ['p','w'], [True, True]])
    w_p_6 = np.array([[2, 6], ['p','w'], [True, True]])
    w_p_7 = np.array([[2, 7], ['p','w'], [True, True]])
    w_p_8 = np.array([[2, 8], ['p','w'], [True, True]])
    w_r_1 = np.array([[1, 1], ['r','w'], [True, None]])
    w_r_2 = np.array([[1, 8], ['r','w'], [True, None]])
    w_kn_1 = np.array([[1, 2], ['kn','w'], [True, None]])
    w_kn_2 = np.array([[1, 7], ['kn','w'], [True, None]])
    w_b_1 = np.array([[1, 3], ['b','w'], [True, None]])
    w_b_2 = np.array([[1, 6], ['b','w'], [True, None]])
    w_q = np.array([[1, 4], ['q','w'], [True, None]])
    w_k = np.array([[1, 5], ['k','w'], [True, None]])
    white_pieces = np.array([
        w_p_1, w_p_2, w_p_3, w_p_4,
        w_p_5, w_p_6, w_p_7, w_p_8,
        w_r_1, w_r_2,
        w_kn_1, w_kn_2,
        w_b_1, w_b_2,
        w_q, w_k
        ])
    return white_pieces

def make_black_pieces():
    #[row, column, type, colour, status (True if alive, False if dead), pawn initial position (True if yes, False if not)]
    b_p_1 = np.array([[7, 1], ['p','b'], [True, True]])
    b_p_2 = np.array([[7, 2], ['p','b'], [True, True]])
    b_p_3 = np.array([[7, 3], ['p','b'], [True, True]])
    b_p_4 = np.array([[7, 4], ['p','b'], [True, True]])
    b_p_5 = np.array([[7, 5], ['p','b'], [True, True]])
    b_p_6 = np.array([[7, 6], ['p','b'], [True, True]])
    b_p_7 = np.array([[7, 7], ['p','b'], [True, True]])
    b_p_8 = np.array([[7, 8], ['p','b'], [True, True]])
    b_r_1 = np.array([[8, 1], ['r','b'], [True, None]])
    b_r_2 = np.array([[8, 8], ['r','b'], [True, None]])
    b_kn_1 = np.array([[8, 2], ['kn','b'], [True, None]])
    b_kn_2 = np.array([[8, 7], ['kn','b'], [True, None]])
    b_b_1 = np.array([[8, 3], ['b','b'], [True, None]])
    b_b_2 = np.array([[8, 6], ['b','b'], [True, None]])
    b_q = np.array([[8, 4], ['q','b'], [True, None]])
    b_k = np.array([[8, 5], ['k','b'], [True, None]])
    black_pieces = np.array([
        b_p_1, b_p_2, b_p_3, b_p_4,
        b_p_5, b_p_6, b_p_7, b_p_8,
        b_r_1, b_r_2,
        b_kn_1, b_kn_2,
        b_b_1, b_b_2,
        b_q, b_k
        ])
    return black_pieces


def setup():

    white_pieces = make_white_pieces()
    black_pieces = make_black_pieces()

    return white_pieces, black_pieces

setup()