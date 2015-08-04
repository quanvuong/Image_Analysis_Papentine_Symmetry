from PIL import Image
import copy
import  numpy as np

def merge_sublist(original_list):

    temp = [] 

    for y in original_list:
        for x in y:
            temp.append(x)

    return temp 

def convert_image(image):
    "Convert an image into a matrix "
    im = Image.open(image).convert('RGB')
    image_converted  = np.asarray(im)

    return image_converted 

def num_mini_matrix(matrix):
    "Return the number of mini-matrix a matrix has"
    b = len(matrix) - 1 # b is used to calculate how many mini-matrix a has

    AllSet = [[] for i in range(((b)*(b+1)*(2*b+1)/6))] #AllSet is used to contain all the minimatrix of a

    return AllSet 

def get_mini_matrix(matrix, x_pos,  y_pos, size):
    "Return a mini-matrix knowing the x,y-position of the upper right corner item of the mini-matrix "
    "and the size of the mini-matrix "

    mini_matrix = [] 

    for i in range(size):
        mini_matrix.append(matrix[y_pos + i ][x_pos : x_pos + size])

    return mini_matrix 

def all_mini_matrix_specific_size(matrix, size):
    "Return all mini_matrix with the specific size in the matrix"

    mini_matrix_data = []

    x_pos = 0
    y_pos = 0   

    while (y_pos + size) <= len(matrix):

        x_pos = 0

        while (x_pos + size) <= len(matrix):
            mini_matrix_data.append(get_mini_matrix(matrix, x_pos, y_pos, size))
            x_pos += 1
        
        y_pos += 1


    return mini_matrix_data  

def return_all_mini_matrix(matrix):
    "Return all the mini_matrix in a matrix in a list format"

    size = len(matrix)

    mini_matrix_data = []

    while size > 1:
        mini_matrix_data.append(all_mini_matrix_specific_size(matrix, size))
        size -= 1

    mini_matrix_data = merge_sublist(mini_matrix_data)

    return mini_matrix_data  

def rotate90(matrix ): 
    "Rotate the image by 90 degree"
    b = np.array(zip(*matrix))
    for i in range(len(b)):
        b[i] = b[i][::-1]
    return b

def rotate180(matrix):

    a = rotate90(matrix)

    b = rotate90(a )

    return b 

def rotate270(matrix ):

    a = rotate180(matrix )

    b = rotate90(a)

    return b 

def num_pixel_matrix(matrix ):
    "Return the number of pixel in an image "

    num_pixel = 0

    for line in matrix:
        num_pixel += len(line)

    return num_pixel 

def compare_two_matrix_cont(matrix_1, matrix_2 ):
    "If two matrix is the same, return the number of pixel in each image, if not, return 0"
    Count = 0

    if np.array_equal(matrix_1 ,matrix_2 ) == True: 
        return num_pixel_matrix(matrix_1 )
    else: 
        return 0 

def reflect_left_bot_right_top(matrix):
    "Reflect a matrix along the left_bottom and right_top line "
    for i in range(len(matrix)):
      matrix[i] = matrix[i][::-1]

    matrix = zip(*matrix)

    for i in range(len(matrix)):
      matrix[i] = matrix[i][::-1]

    matrix = np.array(matrix) 

    return matrix 

def reflect_left_top_right_bot(matrix):
    "Reflect a matrix along the left_top and right_bottom line "

    matrix = np.array(zip(*matrix)) # c is reflection along diagonal left-top right-bottom

    return matrix 

def seven_operation(matrix):
    "Return the score of seven operations on the matrix in the form of a list "
    "In the order of lr, up, diagonal left-bottom_right-top, diagional left-top right-bottom,90, 180 ,270"

    score_list = [0, 0, 0, 0, 0, 0, 0] 

    fliplr  = np.fliplr(matrix) #reflect left right
    flipud = np.flipud(matrix) #reflect up down

    ref_left_bot_right_top = reflect_left_bot_right_top(matrix )

    ref_left_top_right_bot = reflect_left_top_right_bot(matrix )

    matrix_rotate90   = rotate90(matrix)

    matrix_rotate180 = rotate180(matrix )

    matrix_rotate270 = rotate270(matrix )

    score_list[0] = compare_two_matrix_cont(matrix ,fliplr) 
    score_list[1] = compare_two_matrix_cont(matrix ,flipud)  
    score_list[2] = compare_two_matrix_cont(matrix ,ref_left_bot_right_top)
    score_list[3] = compare_two_matrix_cont(matrix ,ref_left_top_right_bot)
    score_list[4] = compare_two_matrix_cont(matrix ,matrix_rotate90)
    score_list[5] = compare_two_matrix_cont(matrix ,matrix_rotate180) 
    score_list[6] = compare_two_matrix_cont(matrix ,matrix_rotate270)

    return score_list 

def cont_symmetry_score(matrix):
    "return the continuous symmetry score of a matrix along the seven operations "

    score_list = [0, 0, 0, 0, 0, 0, 0]

    mini_matrix_data = return_all_mini_matrix(matrix)

    print len(mini_matrix_data)

    for mini_matrix in mini_matrix_data:
        mini_matrix_score_list = seven_operation(mini_matrix)
        for i in range(len(mini_matrix_score_list)):
            score_list[i] = score_list[i] + mini_matrix_score_list[i]

    return score_list 

if __name__ == '__main__':
    matrix = convert_image('p25.png')

    print cont_symmetry_score(matrix )


