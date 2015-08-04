import copy
import  numpy as np
from helper_functions import * 

def compare_two_matrix_dist(matrix_1, matrix_2 ):
    "If two matrix is the same, return 1 if they are the same, if not, return 0"
    Count = 0

    if np.array_equal(matrix_1 ,matrix_2 ) == True: 
        return 1 
    else: 
        return 0 

def fliplr_dist_score(matrix):

    fliplr = np.fliplr(matrix)

    return compare_two_matrix_dist(matrix, fliplr)

def flipud_dist_score(matrix):

    flipud = np.flipud(matrix)

    return compare_two_matrix_dist(matrix, flipud)

def pos_diag_dist_score(matrix):

    flipped_matrix = reflect_pos_diag(matrix)

    return compare_two_matrix_dist(matrix, flipped_matrix)

def neg_diag_dist_score(matrix):

    flipped_matrix = reflect_neg_diag(matrix)

    return compare_two_matrix_dist(matrix, flipped_matrix)

def rotate90_dist_score(matrix):

    rotated_matrix = rotate90(matrix)

    return compare_two_matrix_dist(matrix, rotated_matrix)

def rotate180_dist_score(matrix):

    rotated_matrix = rotate180(matrix)

    return compare_two_matrix_dist(matrix, rotated_matrix)

def rotate270_dist_score(matrix):

    rotated_matrix = rotate270(matrix)

    return compare_two_matrix_dist(matrix, rotated_matrix)

def dist_symmetry_score(matrix):

    score = {'ver_dist':0, 'hor_dist':0, \
    'diag_pos_dist':0, 'diag_neg_dist':0, '90_degree_dist':0, \
    '180_degree_dist':0, '270_degree_dist':0, 'ver+hor_dist':0, \
    'diag_pos_dist+diag_neg_dist':0, 'ver+hor_dist+diag_pos_dist+diag_neg_dist':0, '90+180+270_dist':0, 'sym_dist total':0}

    mini_matrixs = return_all_mini_matrix(matrix)


    for mini_matrix in mini_matrixs:
        if neg_diag_dist_score(mini_matrix) == 1: print mini_matrix
        score = {'ver_dist': score['ver_dist'] + fliplr_dist_score(mini_matrix), \
                 'hor_dist': score['hor_dist'] + flipud_dist_score(mini_matrix), \
                 'diag_pos_dist': score['diag_pos_dist'] + pos_diag_dist_score(mini_matrix), \
                 'diag_neg_dist': score['diag_neg_dist'] + neg_diag_dist_score(mini_matrix), \
                 '90_degree_dist': score['90_degree_dist'] + rotate90_dist_score(mini_matrix), \
                 '180_degree_dist': score['180_degree_dist'] + rotate180_dist_score(mini_matrix), \
                 '270_degree_dist': score['270_degree_dist'] + rotate270_dist_score(mini_matrix), \
                 'ver+hor_dist': score['ver+hor_dist'] + score['ver_dist'] + score['hor_dist'], \
                 'diag_pos_dist+diag_neg_dist': score['diag_pos_dist+diag_neg_dist'] + score['diag_pos_dist'] + score['diag_neg_dist'], \
                 'ver+hor_dist+diag_pos_dist+diag_neg_dist': score['ver+hor_dist+diag_pos_dist+diag_neg_dist'] + score['ver+hor_dist'] + score['diag_pos_dist+diag_neg_dist'], \
                 '90+180+270_dist': score['90+180+270_dist'] + score['90_degree_dist'] + score['180_degree_dist'] + score['270_degree_dist'], \
                 'sym_dist total': score['sym_dist total'] + score['ver+hor_dist+diag_pos_dist+diag_neg_dist'] + score['90+180+270_dist']}

    return score 

if __name__ == '__main__':
    pass 

