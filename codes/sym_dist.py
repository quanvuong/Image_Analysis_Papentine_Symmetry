import copy
import numpy as np
import helpers 

def compare_two_matrix_dist(matrix_1, matrix_2):
    "If two matrix is the same, return 1 if they are the same, if not, return 0"
    if np.array_equal(matrix_1 ,matrix_2) == True: 
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

    flipped_matrix = helpers.reflect_pos_diag(matrix)

    return compare_two_matrix_dist(matrix, flipped_matrix)

def neg_diag_dist_score(matrix):

    flipped_matrix = helpers.reflect_neg_diag(matrix)

    return compare_two_matrix_dist(matrix, flipped_matrix)

def rotate90_dist_score(matrix):

    rotated_matrix = helpers.rotate90(matrix)

    return compare_two_matrix_dist(matrix, rotated_matrix)

def rotate180_dist_score(matrix):

    rotated_matrix = helpers.rotate180(matrix)

    return compare_two_matrix_dist(matrix, rotated_matrix)

def rotate270_dist_score(matrix):

    rotated_matrix = helpers.rotate270(matrix)

    return compare_two_matrix_dist(matrix, rotated_matrix)

def dist_symmetry_score(matrix):

    mini_matrixs = helpers.return_all_mini_matrix(matrix)

    ver_dist_temp = 0 
    hor_dist_temp = 0 
    diag_pos_dist_temp = 0 
    diag_neg_dist_temp = 0 
    ninety_degree_dist_temp = 0 
    oneeighty_degree_dist_temp = 0 
    twoseventy_degree_dist_temp = 0 
    ver_and_hor_dist_temp = 0 
    diag_pos_and_neg_dist_temp = 0 
    ver_and_hor_diag_pos_and_neg_dist_temp = 0 
    ninety_180_270_dist_temp = 0 
    syn_dist_total_temp = 0

    for mini_matrix in mini_matrixs:
        ver_dist_temp += fliplr_dist_score(mini_matrix)
        hor_dist_temp += flipud_dist_score(mini_matrix)
        diag_neg_dist_temp += neg_diag_dist_score(mini_matrix) 
        diag_pos_dist_temp += pos_diag_dist_score(mini_matrix)
        ninety_degree_dist_temp += rotate90_dist_score(mini_matrix)
        oneeighty_degree_dist_temp += rotate180_dist_score(mini_matrix)
        twoseventy_degree_dist_temp += rotate270_dist_score(mini_matrix)

        ninety_180_270_dist_temp += ninety_degree_dist_temp + oneeighty_degree_dist_temp + twoseventy_degree_dist_temp
        syn_dist_total_temp += ver_and_hor_diag_pos_and_neg_dist_temp + ninety_180_270_dist_temp 

    score = {'ver_dist':ver_dist_temp, \
             'hor_dist':hor_dist_temp, \
              'diag_pos_dist':diag_pos_dist_temp, \
              'diag_neg_dist':diag_neg_dist_temp, \
              '90_degree_dist':ninety_degree_dist_temp, \
              '180_degree_dist':oneeighty_degree_dist_temp, \
              '270_degree_dist':twoseventy_degree_dist_temp}

    score['ver+hor_dist'] = score['ver_dist'] + score['hor_dist']

    score['diag_pos_dist+diag_neg_dist'] = score['diag_pos_dist'] + score['diag_neg_dist']

    score['ver+hor_dist+diag_pos_dist+diag_neg_dist'] = score['ver+hor_dist'] + score['diag_pos_dist+diag_neg_dist']
               
    score['90+180+270_dist'] = score['90_degree_dist'] + score['180_degree_dist'] + score['270_degree_dist']

    score['sym_dist_total'] = score['ver+hor_dist+diag_pos_dist+diag_neg_dist'] + score['90+180+270_dist']

    return score 

if __name__ == '__main__':
    pass 

