from PIL import Image
import copy
import numpy as np
import math
import string

def Vertical(matrix): #turn the vertical lines of a matrix into another matrix:
    matrix = zip(*matrix)
    return matrix

def reflect_left_bot_right_top(matrix):
    "Reflect a matrix along the left_bottom and right_top line "
    for i in range(len(matrix)):
      matrix[i] = matrix[i][::-1]

    matrix = zip(*matrix)

    for i in range(len(matrix)):
      matrix[i] = matrix[i][::-1]

    matrix = np.array(matrix) 

    return matrix 

def reflect_left_bot_right_top(a):
    b = copy.deepcopy(a)
    for i in range(len(b)):
        b[i] = b[i][::-1]
    b = zip(*b)
    for i in range(len(b)):
        b[i] = b[i][::-1]
    return b

def LengthSubList(l):
    length = 0
    for i in range(len(l)):
        length = length + len(l[i])
    return length

def papentine_oneline(sequence ): #Calculate L1 length of 1 sequence 
    score = 0 #score is the L1 length
    
    split = [] #split contains splitted sequence whenever consecutive symbols are different

    for i in range(len(sequence)-1):
        len_sublist_split = LengthSubList(split)
        if sequence[i] != sequence[i+1]:
            split.append(sequence[len_sublist_split : i+1])
            len_sublist_split = len_sublist_split + len(split[-1])

    split.append(sequence[len_sublist_split : len(sequence)])

    score = len(split)

    for i in range(len(split)):
        score = score + math.log(len(split[i]),10)

    return score

def papentine_matrix(a): #Calculate L1 length of a matrix, whether horizontal or vertical

    score = [] # Contains the score of the different lines in the matrix
    for i in range(len(a)):
        score.append(papentine_oneline(a[i]))

    return sum(score)

def papentine_matrix_hor_ver(a): #return the horizontal and vertical score

    score = []
    score.append(papentine_matrix(a)) #Horizontal score
    a = Vertical(a)
    score.append(papentine_matrix(a)) #Vertical score
    return score

def Complete(image):
    im = Image.open(image).convert('RGB')
    a = np.asarray(im) # a is the matrix representation of the original image
    a = np.array(a).tolist()

    return papentine_matrix_hor_ver(a)

if __name__ == '__main__':

    human_score = [0.4, 15.7, 38.8, 5.6, 25.1, 16, 9.7, 7 1.4, 4, 3.5, 22.2, 0.7, 12.1, 20.9, 36.7, 31.9, 36.2, 44.9, 32.4, 29.2, 34.3, 23, 33.8, 33.2, 29.2, 29.4, 33.1, 34.3, 36.2, 22.2, 5.3, 2.8, 10, 9, 10.2, 7.2, 6, 2.2, 8.1, 7.4, 5.7, 30.5, 12.1, 18]

    papentine_score = [] 



    img_amt = 15

    ImageName = [[] for i in range(img_amt)]

    for i in range(img_amt):
        ImageName[i] = "p%i.png" %(i+1)

    Comparison = [[] for i in range(img_amt)]


    for i in range(img_amt):
        Comparison[i] = Complete(ImageName[i])


    for i in Comparison:
        print i


    

