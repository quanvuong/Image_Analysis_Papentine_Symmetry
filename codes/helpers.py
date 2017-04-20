import numpy as np 
import copy

def rotate90(matrix): 
    "Rotate the image by 90 degree"
    b = np.array(zip(*matrix))
    for i in range(len(b)):
        b[i] = b[i][::-1]
    return b

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

    mini_matrix = []

    for i in range(size):
        mini_matrix.append(matrix[curr_row + i][curr_col : curr_col + size])

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

    mini_matrixs = []

    while size > 1:
        mini_matrixs.append(all_mini_matrix_specific_size(matrix, size))
        size -= 1

    mini_matrixs = merge_sublist(mini_matrixs)

    for i in range(len(mini_matrixs)):
        mini_matrixs[i] = np.array(mini_matrixs[i])

    return mini_matrixs  

def num_pixel_matrix(matrix):
    "Return the number of pixel in an image"

    num_pixel = 0

    for line in matrix:
        num_pixel += len(line)

    return num_pixel 

def reflect_pos_diag(matrix):
    "Reflect a matrix along the positive diagonal"

    temp_matrix = copy.deepcopy(matrix)
    for i in range(len(matrix)):
      temp_matrix[i] = temp_matrix[i][::-1]

    temp_matrix = zip(*temp_matrix)

    for i in range(len(temp_matrix)):
      temp_matrix[i] = temp_matrix[i][::-1]

    temp_matrix = np.array(temp_matrix) 

    return temp_matrix 

def reflect_neg_diag(matrix):
    "Reflect a matrix along the negative diagonal"

    temp_matrix = copy.deepcopy(matrix)
    temp_matrix = np.array(zip(*temp_matrix)) 

    return temp_matrix 

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
