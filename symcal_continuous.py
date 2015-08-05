import copy
import numpy as np
from helper_functions import * 

def compare_two_matrix_cont(matrix_1, matrix_2):
    "Return the number of pixels in two matrixes that are the same"
    num_pixel_same = 0 

    for i in range(len(matrix_1)):
        for j in range(len(matrix_2)):
            if (matrix_1[i][j]==matrix_2[i][j]).all() == True:
                num_pixel_same += 1 

    return num_pixel_same

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

    mini_matrixs = return_all_mini_matrix(matrix)

    ver_cont_temp = 0 
    hor_cont_temp = 0 
    diag_pos_cont_temp = 0 
    diag_neg_cont_temp = 0 
    ninety_degree_cont_temp = 0 
    oneeighty_degree_cont_temp = 0 
    twoseventy_degree_cont_temp = 0 
    ver_and_hor_cont_temp = 0 
    diag_pos_and_neg_cont_temp = 0 
    ver_and_hor_diag_pos_and_neg_cont_temp = 0 
    ninety_180_270_cont_temp = 0 
    syn_cont_total_temp = 0


    rejected_diag_pos_cont = [] 
    for mini_matrix in mini_matrixs:
        if pos_diag_cont_score(mini_matrix) == 0: 
            rejected_diag_pos_cont.append(mini_matrix)
        ver_cont_temp += fliplr_cont_score(mini_matrix)
        hor_cont_temp += flipud_cont_score(mini_matrix)
        diag_neg_cont_temp += neg_diag_cont_score(mini_matrix) 
        diag_pos_cont_temp += pos_diag_cont_score(mini_matrix)
        ninety_degree_cont_temp += rotate90_cont_score(mini_matrix)
        oneeighty_degree_cont_temp += rotate180_cont_score(mini_matrix)
        twoseventy_degree_cont_temp += rotate270_cont_score(mini_matrix)

        ninety_180_270_cont_temp += ninety_degree_cont_temp + oneeighty_degree_cont_temp + twoseventy_degree_cont_temp
        syn_cont_total_temp += ver_and_hor_diag_pos_and_neg_cont_temp + ninety_180_270_cont_temp 

    print len(rejected_diag_pos_cont)
    score = {'ver_cont':ver_cont_temp, \
             'hor_cont':hor_cont_temp, \
              'diag_pos_cont':diag_pos_cont_temp, \
              'diag_neg_cont':diag_neg_cont_temp, \
              '90_degree_cont':ninety_degree_cont_temp, \
              '180_degree_cont':oneeighty_degree_cont_temp, \
              '270_degree_cont':twoseventy_degree_cont_temp}

    score['ver+hor_cont'] = score['ver_cont'] + score['hor_cont']

    score['diag_pos_cont+diag_neg_cont'] = score['diag_pos_cont'] + score['diag_neg_cont']

    score['ver+hor_cont+diag_pos_cont+diag_neg_cont'] = score['ver+hor_cont'] + score['diag_pos_cont+diag_neg_cont']
               
    score['90+180+270_cont'] = score['90_degree_cont'] + score['180_degree_cont'] + score['270_degree_cont']

    score['sym_cont_total'] = score['ver+hor_cont+diag_pos_cont+diag_neg_cont'] + score['90+180+270_cont']

    return score 

if __name__ == '__main__':
    pass 


