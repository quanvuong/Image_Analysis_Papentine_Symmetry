import os 
import numpy as np 
import math 
from helpers import *
from PIL import Image

def sum_length_sublist(l):
    "Return the total length of the sublists of a list"

    length = 0
    for sublist in l:
        length = length + len(sublist)

    return length

def image_into_matrix(image):
	im = Image.open(image).convert('RGB')
	a = np.asarray(im) 
	a = np.array(a).tolist()

	return a 

def papentine_split(sequence):
	'Split the sequence whenever consecutive symbols occur'

	split_sublist = [] #split_sublist contains sublist of a list. The split_sublist is made whenever two consecutive symbols are different 

	length_split_sublist = 0	

	for i in range(len(sequence) - 1):
		if np.array_equal(sequence[i], sequence[i+1]) == False:
			split_sublist.append(sequence[length_split_sublist: (i+1)])

			length_split_sublist += len(split_sublist[-1])

	split_sublist.append(sequence[length_split_sublist: (len(sequence) + 1)])

	return split_sublist

def papentine_one_seq(sequence): #Calculate L1 length of 1 sequence 
	'Calculate the L1 score of sequence a'
	score = 0 

	split_sublist = papentine_split(sequence)

	score += len(split_sublist)

	for i in range(len(split_sublist)):
	    score += math.log(len(split_sublist[i]),10)

	return score

def papentine_matrix(matrix): 
	'Sum of the L1 scores of the horizontal lines of a matrix' 

	score = 0 

	for line in matrix:
		score += papentine_one_seq(line)

	return score

def adj_pixel_top_right(matrix, curr_row, curr_col):
	'Return the pixel touching the current pixel at its top right corner'

	if curr_row-1 < 0: 
		return 'error: out of bound at the top' 
	elif curr_col+2 > len(matrix[1]):
		return 'error: out of bound on the right'
	else: 
		return matrix[curr_row-1][curr_col+1]

def pos_diag_one_line(input_matrix, curr_row, curr_col):
	'return the positive diag line of a matrix given the row and column of the first pixel'

	output_line = [] 

	output_line.append(input_matrix[curr_row][curr_col])

	while adj_pixel_top_right(input_matrix, curr_row, curr_col) != 'error: out of bound at the top':
		if adj_pixel_top_right(input_matrix, curr_row, curr_col) == 'error: out of bound on the right':
			break 
		output_line.append(adj_pixel_top_right(input_matrix, curr_row, curr_col))
		curr_row -= 1 
		curr_col += 1

	return output_line 

def pos_diag_into_matrix(input_matrix): 
	'Turn the positive diag lines of a matrix into a matrix'

	output_matrix = []

	for i in range(1, len(input_matrix)):
		output_matrix.append(pos_diag_one_line(input_matrix, i, 0))

	for i in range(1, len(input_matrix[0])):
		output_matrix.append(pos_diag_one_line(input_matrix, len(input_matrix)-1, i))

	return output_matrix

def verticalize(matrix): 
	'turn the vertical lines of a matrix into another matrix' 
	matrix = zip(*matrix)
	return matrix

def papentine_hor(matrix): 

	return papentine_matrix(matrix)	

def papentine_ver(matrix):

	matrix = verticalize(matrix)

	return papentine_matrix(matrix)

def papentine_pos_diag(matrix):

	matrix = pos_diag_into_matrix(matrix)

	del matrix[-1]

	return papentine_matrix(matrix) 

def papentine_neg_diag(matrix):

	matrix = rotate90(matrix)
	matrix = pos_diag_into_matrix(matrix)

	del matrix[-1]

	return papentine_matrix(matrix)

def papentine(matrix):
	'return the papentine score of a matrix, along the horizontal, vertical, pos diag and neg diag vectors'

	score = {} 

	score = {'papentine horizontal': papentine_hor(matrix), \
			 'papentine vertical': papentine_ver(matrix), \
			 'papentine positive diagonal': papentine_pos_diag(matrix),\
			 'papentine negative diagonal': papentine_neg_diag(matrix)}

	score['papentine horizontal + vertical'] = score['papentine horizontal'] + score['papentine vertical']

	score['papentine positive + negative diagonal'] = score['papentine positive diagonal'] + score['papentine negative diagonal']

	score['papentine total'] = score['papentine horizontal + vertical'] + score['papentine positive + negative diagonal']

 	return score 

if __name__ == '__main__':
    pass 












