import copy
import numpy as np
import helpers
from pprint import pprint


def compare_two_matrix_cont(matrix_1, matrix_2):
    "Return the number of pixels in two matrixes that are the same"
    num_pixel_same = np.count_nonzero(matrix_1 == matrix_2)

    return num_pixel_same

def fliplr_cont_score(matrix):

    fliplr = np.fliplr(matrix)

    return compare_two_matrix_cont(matrix, fliplr)

def flipud_cont_score(matrix):

    flipud = np.flipud(matrix)

    return compare_two_matrix_cont(matrix, flipud)

def pos_diag_cont_score(matrix):

    flipped_matrix = helpers.reflect_pos_diag(matrix)

    return compare_two_matrix_cont(matrix, flipped_matrix)

def neg_diag_cont_score(matrix):

    flipped_matrix = helpers.reflect_neg_diag(matrix)

    return compare_two_matrix_cont(matrix, flipped_matrix)

def rotate90_cont_score(matrix):

    rotated_matrix = helpers.rotate90(matrix)

    return compare_two_matrix_cont(matrix, rotated_matrix)

def rotate180_cont_score(matrix):

    rotated_matrix = helpers.rotate180(matrix)

    return compare_two_matrix_cont(matrix, rotated_matrix)

def rotate270_cont_score(matrix):

    rotated_matrix = helpers.rotate270(matrix)

    return compare_two_matrix_cont(matrix, rotated_matrix)

def cont_symmetry_score(matrix):

    mini_matrixs = helpers.return_all_mini_matrix(matrix)

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

    for mini_matrix in mini_matrixs:
        # if pos_diag_cont_score(mini_matrix) == 0:
        #     rejected_diag_pos_cont.append(mini_matrix)
        ver_cont_temp += fliplr_cont_score(mini_matrix)
        hor_cont_temp += flipud_cont_score(mini_matrix)
        diag_neg_cont_temp += neg_diag_cont_score(mini_matrix) 
        diag_pos_cont_temp += pos_diag_cont_score(mini_matrix)
        ninety_degree_cont_temp += rotate90_cont_score(mini_matrix)
        oneeighty_degree_cont_temp += rotate180_cont_score(mini_matrix)
        twoseventy_degree_cont_temp += rotate270_cont_score(mini_matrix)

        ninety_180_270_cont_temp += ninety_degree_cont_temp + oneeighty_degree_cont_temp + twoseventy_degree_cont_temp
        syn_cont_total_temp += ver_and_hor_diag_pos_and_neg_cont_temp + ninety_180_270_cont_temp 

    score = {'Continuous Left Right':ver_cont_temp, \
             'Continuous Up Down':hor_cont_temp, \
              'Continuous NW-SE':diag_pos_cont_temp, \
              'Continuous NE-SW':diag_neg_cont_temp, \
              'Continuous 90 degree':ninety_degree_cont_temp, \
              'Continuous 180 degree':oneeighty_degree_cont_temp, \
              'Continuous 270 degree':twoseventy_degree_cont_temp}

    score['Continuous Left Right + Up Down'] = score['Continuous Left Right'] + score['Continuous Up Down']

    score['Continuous NW-SE + NE-SW'] = score['Continuous NW-SE'] + score['Continuous NE-SW']

    score['Continuous Left Right + Up Down + NW-SE + NE-SW'] \
        = score['Continuous Left Right + Up Down'] + score['Continuous NW-SE + NE-SW']
               
    score['Continuous 90 + 180 + 270'] = score['Continuous 90 degree'] \
                                         + score['Continuous 180 degree'] + score['Continuous 270 degree']

    score['Continuous Total'] = score['Continuous Left Right + Up Down + NW-SE + NE-SW'] \
                                + score['Continuous 90 + 180 + 270']

    return score 

if __name__ == '__main__':
    pass 


