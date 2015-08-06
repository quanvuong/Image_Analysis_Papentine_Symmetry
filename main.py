import sys
import os 

sys.path.insert(0, os.getcwd() + '/codes')

import xlsxwriter 
import papentine  
import sym_cont
import sym_dist
import helpers 
from PIL import Image 
import numpy as np 
import pprint 

def sort_picture(picture_names):

	change = False

	while change != True: 
		change = True
		for i in range(len(picture_names)-1):
			if len(picture_names[i]) > len(picture_names[i+1]): 
				picture_names[i], picture_names[i+1] = picture_names[i+1], picture_names[i]
				change = False 

	while change != True:
		change = True 
		for i in range(10):
			if picture_names[i] > picture_names[i+1]:
				picture_names[i], picture_names[i+1] = picture_names[i+1], picture_names[i]
				change = False 

	return picture_names

def create_empty_table(folder_namem, columns):

	workbook = xlsxwriter.Workbook('Image Analysis.xlsx')
	worksheet = workbook.add_worksheet()

	#Creating the colums 
	row = 0 
	col = 0 

	for column in columns:
		worksheet.write(row, col, column)
		col += 1 

	col = 0
	row = 1 

	#Get the names of the images and sort the name in ascending order" 
	picture_names = [picture for picture in os.listdir(folder_name)]

	picture_names = sort_picture(picture_names)

	for picture in picture_names:
		worksheet.write(row, col, picture)
		row += 1 

	workbook.close() 

def convert_image(image_name):
	'Convert image into numpy matrix'

	im = Image.open(image_name).convert('RGB')
	im_converted = np.asarray(im)
	im_converted = np.array(im_converted).tolist()
	return im_converted

def merge_dict(dict_1, dict_2):
	'Merge dict_1 and dict_2. Two dicts must not have overlapping key'

	temp_dict = {} 
	for key in dict_1.keys():
		temp_dict[key] = dict_1[key]

	for key in dict_2.keys():
		temp_dict[key] = dict_2[key]

	return temp_dict

if __name__ == '__main__':

	#The folder in which the images are in 
	folder_name = 'Chipman patterns'

	#image_score contains the scores of all images
	image_score = {}  

	picture_names = [picture for picture in os.listdir(folder_name)]

	picture_names = sort_picture(picture_names)

	if '.DS_Store' in picture_names: picture_names.remove('.DS_Store')

	for picture in picture_names:
		image_matrix = convert_image(os.getcwd() + '/' + folder_name + '/' + picture)

		cont_sym_score = sym_cont.cont_symmetry_score(image_matrix)
		dist_sym_score = sym_dist.dist_symmetry_score(image_matrix)
		papentine_score = papentine.papentine(image_matrix)

		cont_and_dist_sym_score = merge_dict(cont_sym_score, dist_sym_score)

		image_score[picture] = merge_dict(cont_and_dist_sym_score, papentine_score)
		print "done with " + picture

	pprint.pprint(image_score)

	# The commentted part below is for debugging 
	# for picture in picture_names:

	# 	if picture == 'p1.png':
	# 		im = convert_image(os.getcwd() + '/' + folder_name + '/' + picture)

	# 		print papentine.papentine(im)

	# 	if picture == 'p2.png':
	# 		im = convert_image(os.getcwd() + '/' + folder_name + '/' + picture)

	# 		print papentine.papentine(im)

	# 	if picture == 'p3.png':
	# 		im = convert_image(os.getcwd() + '/' + folder_name + '/' + picture)

	# 		print papentine.papentine(im)



	# create_empty_table(folder_name)





