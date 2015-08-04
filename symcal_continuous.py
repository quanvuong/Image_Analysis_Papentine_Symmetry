import copy
import numpy as np
from helper_functions import * 

def compare_two_matrix_cont(matrix_1, matrix_2):
    "If two matrix is the same, return the number of pixel in each image, if not, return 0"
    Count = 0

    if np.array_equal(matrix_1 , matrix_2) == True: 
        return num_pixel_matrix(matrix_1)
    else: 
        return 0 

def fliplr_cont_score(matrix):

    fliplr = np.fliplr(matrix)

    return compare_two_matrix_cont(matrix, fliplr)

def flipud_cont_score(matrix):

    flipud = np.flipud(matrix)

    return compare_two_matrix_cont(matrix, flipud)

def pos_diag_cont_score(matrix):

    flipped_matrix = reflect_pos_diag(matrix)

    return compare_two_matrix_cont(matrix, flipped_matrix)

def neg_diag_cont_score(matrix):

    flipped_matrix = reflect_neg_diag(matrix)

    return compare_two_matrix_cont(matrix, flipped_matrix)

def rotate90_cont_score(matrix):

    rotated_matrix = rotate90(matrix)

    return compare_two_matrix_cont(matrix, rotated_matrix)

def rotate180_cont_score(matrix):

    rotated_matrix = rotate180(matrix)

    return compare_two_matrix_cont(matrix, rotated_matrix)

def rotate270_cont_score(matrix):

    rotated_matrix = rotate270(matrix)

    return compare_two_matrix_cont(matrix, rotated_matrix)

def cont_symmetry_score(matrix):

    score = {'ver_cont':0, 'hor_cont':0, \
    'diag_pos_cont':0, 'diag_neg_cont':0, '90_degree_cont':0, \
    '180_degree_cont':0, '270_degree_cont':0, 'ver+hor_cont':0, \
    'diag_pos_cont+diag_neg_cont':0, 'ver+hor_cont+diag_pos_cont+diag_neg_cont':0, '90+180+270_cont':0, 'sym_cont total':0}

    mini_matrixs = return_all_mini_matrix(matrix)

    for mini_matrix in mini_matrixs:
        score = {'ver_cont': score['ver_cont'] + fliplr_cont_score(mini_matrix), \
                 'hor_cont': score['hor_cont'] + flipud_cont_score(mini_matrix), \
                 'diag_pos_cont': score['diag_pos_cont'] + pos_diag_cont_score(mini_matrix), \
                 'diag_neg_cont': score['diag_neg_cont'] + neg_diag_cont_score(mini_matrix), \
                 '90_degree_cont': score['90_degree_cont'] + rotate90_cont_score(mini_matrix), \
                 '180_degree_cont': score['180_degree_cont'] + rotate180_cont_score(mini_matrix), \
                 '270_degree_cont': score['270_degree_cont'] + rotate270_cont_score(mini_matrix), \
                 'ver+hor_cont': score['ver+hor_cont'] + score['ver_cont'] + score['hor_cont'], \
                 'diag_pos_cont+diag_neg_cont': score['diag_pos_cont+diag_neg_cont'] + score['diag_pos_cont'] + score['diag_neg_cont'], \
                 'ver+hor_cont+diag_pos_cont+diag_neg_cont': score['ver+hor_cont+diag_pos_cont+diag_neg_cont'] + score['ver+hor_cont'] + score['diag_pos_cont+diag_neg_cont'], \
                 '90+180+270_cont': score['90+180+270_cont'] + score['90_degree_cont'] + score['180_degree_cont'] + score['270_degree_cont'], \
                 'sym_cont total': score['sym_cont total'] + score['ver+hor_cont+diag_pos_cont+diag_neg_cont'] + score['90+180+270_cont']}

    return score 

if __name__ == '__main__':
    pass 


