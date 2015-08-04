import os 
import numpy as np 
import math 
from helper_functions import *

def sum_length_sublist(l):
    "Return the sum length of the sublists of a list"

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

	count = sequence[0]

	length_sublist = 0 

	for i in range(len(sequence)-1):
	    length_sublist = sum_length_sublist(split_sublist)
	    if np.array_equal(sequence[i], sequence[i+1]):
	        split_sublist.append(sequence[length_sublist:i+1])
	        length_sublist = length_sublist + len(split_sublist[len(split_sublist)-1])

	split_sublist.append(sequence[length_sublist:len(sequence)])

	return split_sublist

def papentine_one_seq(sequence): #Calculate L1 length of 1 sequence 
	'Calculate the L1 score of sequence a'
	score = 0 

	split_sublist = papentine_split(sequence)

	score = len(split_sublist)

	for i in range(len(split_sublist)):
	    score = score + math.log(len(split_sublist[i]),10)

	return score

def papentine_matrix(matrix): 
	'Sum of the L1 scores of the horizontal lines of a matrix' 

	score = 0 

	for line in matrix:
		score += papentine_one_seq(line)

	return score

def adj_pixel_top_right(matrix, curr_row, curr_col):
	'Return the pixel touching the current pixel at its top right corner'

	try:
		if curr_row-1 < 0: 
			return 'error: out of bound at the top' 
		elif curr_col+1 > 5:
			return 'error: out of bound on the left'
		else: 
			return matrix[curr_row-1][curr_col+1]
	except IndexError:
		print curr_col
		print curr_row
		print matrix

def pos_diag_one_line(input_matrix, curr_row, curr_col):
	'return the positive diag line of a matrix given the row and column of the first pixel'

	output_line = [] 

	output_line.append(input_matrix[curr_row][curr_col])

	while adj_pixel_top_right(input_matrix, curr_row, curr_col) != 'error: out of bound at the top':
		if adj_pixel_top_right(input_matrix, curr_row, curr_col) == 'error: out of bound on the left':
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

	return papentine_matrix(matrix) 

def papentine_neg_diag(matrix):

	matrix = rotate90(matrix)
	matrix = pos_diag_into_matrix(matrix)

	return papentine_matrix(matrix)

def papentine(matrix):
	'return the papentine score of a matrix, along the horizontal, vertical, pos diag and neg diag vectors'

	score = {} 

	score = {'papentine hor': papentine_hor(matrix), \
			 'papentine ver': papentine_ver(matrix), \
			 'papentine pos diag': papentine_pos_diag(matrix),\
			 'papentine neg diag': papentine_neg_diag(matrix)}


	score = {'papentine hor+ver': score['papentine pos diag'] + score['papentine neg diag'],\
			 'papentine pos diag+neg diag': score['papentine pos diag'] + score['papentine neg diag']}

	score = {'papentine Total': score['papentine hor+ver'] + score['papentine pos diag+neg diag']
				 }

 	return score 

if __name__ == '__main__':
    pass 












