import numpy as np 
import copy
import sys

def rotate90(matrix):
    "Rotate the image by 90 degree in clock wise direction"
    return np.rot90(matrix, k=1, axes=(1, 0))

def rotate180(matrix):

    a = rotate90(matrix)

    b = rotate90(a)

    return b 

def rotate270(matrix):

    a = rotate180(matrix)

    b = rotate90(a)
    
    return b 

def merge_sublist(original_list):

    temp = [] 

    for y in original_list:
        for x in y:
            temp.append(x)

    return temp 

def num_mini_matrix(matrix):
    "Return the number of mini-matrix a matrix has"
    b = len(matrix) - 1

    mini_matrix = [[] for i in range(((b)*(b+1)*(2*b+1)/6))] #AllSet is used to contain all the minimatrix of a

    return mini_matrix 

def get_mini_matrix(matrix, curr_col,  curr_row, size):
    "Return a mini-matrix knowing the x,y-position of the upper right corner item of the mini-matrix "
    "and the size of the mini-matrix "

    mini_matrix = matrix[curr_row:curr_row + size, curr_col:curr_col + size]

    return mini_matrix

def all_mini_matrix_specific_size(matrix, size):
    "Return all mini_matrix with the specific size in the matrix"

    mini_matrix_data = []

    curr_col = 0
    curr_row = 0   

    while (curr_row + size) <= len(matrix):

        curr_col = 0

        while (curr_col + size) <= len(matrix[0]):
            mini_matrix_data.append(get_mini_matrix(matrix, curr_col, curr_row, size))
            curr_col += 1
        
        curr_row += 1

    return mini_matrix_data  

def return_all_mini_matrix(matrix):
    "Return all the mini_matrix in a matrix"
    "Each mini_matrix is returned in numpy format"

    size = len(matrix)

    while size > 1:
        curr_row = 0

        while (curr_row + size) <= len(matrix):

            curr_col = 0

            while (curr_col + size) <= len(matrix[0]):
                yield get_mini_matrix(matrix, curr_col, curr_row, size)
                curr_col += 1

            curr_row += 1

        size -= 1


def num_pixel_matrix(matrix):
    "Return the number of pixel in an image"

    num_pixel = 0

    for line in matrix:
        num_pixel += len(line)

    return num_pixel 

def reflect_pos_diag(matrix):
    "Reflect a matrix along the positive diagonal"

    rotated90_clockwise = rotate90(matrix)
    reflected_with_np = np.flipud(rotated90_clockwise)

    return reflected_with_np

def reflect_neg_diag(matrix):
    "Reflect a matrix along the negative diagonal"

    rotated90_clockwise = rotate90(matrix)
    reflected_with_np = np.fliplr(rotated90_clockwise)

    return reflected_with_np

def sort_list_by_length_sublist(mother_list):
    'Sort the content of a list by the length of the sublist in ascending order'

    state = True

    while state != True:
        state = False
        for i in range(len(mother_list)-1):
            if len(mother_list[i]) > len(mother_list[i+1]): 
                mother_list[i], mother_list[i+1] = mother_list[i+1], mother_list[i]
                state = True

if __name__ == '__main__':
    pass 

