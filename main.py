import sys
import os

import xlsxwriter
from codes import papentine
from codes import sym_cont
from codes import sym_dist
from codes import helpers
from PIL import Image
import numpy as np
from scipy.stats import spearmanr
import pprint


chipman_human_scores = [
    0.4,
    15.7,
    38.8,
    5.6,
    25.1,
    16,
    9.7,
    7,
    1.4,
    4,
    3.5,
    22.2,
    0.7,
    12.1,
    20.9,
    36.7,
    31.9,
    36.2,
    44.9,
    32.4,
    29.2,
    34.3,
    23,
    33.8,
    33.2,
    29.2,
    29.4,
    33.1,
    34.3,
    36.2,
    22.2,
    5.3,
    2.8,
    10,
    9,
    10.2,
    7.2,
    6,
    2.2,
    8.1,
    7.4,
    5.7,
    30.5,
    12.1,
    18,
]

chinese_human_scores = [
    i for i in range(15)
]

def sort_picture(picture_names):
    change = False

    while change != True:
        change = True
        for i in range(len(picture_names) - 1):
            if len(picture_names[i]) > len(picture_names[i + 1]):
                picture_names[i], picture_names[i + 1] = picture_names[i + 1], picture_names[i]
                change = False

    while change != True:
        change = True
        for i in range(10):
            if picture_names[i] > picture_names[i + 1]:
                picture_names[i], picture_names[i + 1] = picture_names[i + 1], picture_names[i]
                change = False

    return picture_names


def convert_image(image_name):
    'Convert image into numpy matrix'

    im = Image.open(image_name).convert('L')
    im_converted = np.array(im)
    return im_converted


def merge_two_dict(dict_1, dict_2):
    'Merge dict_1 and dict_2. Two dicts must not have overlapping key'

    temp_dict = {}
    for key in dict_1.keys():
        temp_dict[key] = dict_1[key]

    for key in dict_2.keys():
        temp_dict[key] = dict_2[key]

    return temp_dict


def go_dir(picture, folder_name):
    'Return the directory of a picture'

    return os.getcwd() + '/' + folder_name + '/' + picture


def merge_three_dict(dict_1, dict_2, dict_3):
    temp_dict = merge_two_dict(dict_1, dict_2)

    return merge_two_dict(temp_dict, dict_3)


def get_image_names(folder_name):
    'return the sorted images name'

    picture_names = [picture for picture in os.listdir(folder_name)]

    picture_names = sort_picture(picture_names)

    return picture_names


if __name__ == '__main__':

    # The folder in which the images are in
    # folder_name = 'Chipman patterns'
    # excel_file_name = 'Chipman Image Analysis.xlsx'

    # Chinese data
    folder_name = 'Chinese Characters/Chinese Compressed'
    # excel_file_name = 'Chinese Compressed Character Image Analysis.xlsx'
    excel_file_name = 'Chinese Compressed Character both terms of L1.xlsx'

    # human_scores = chipman_human_scores
    human_scores = chinese_human_scores

    # image_score contains the scores of all images
    image_score = {}

    # picture_names = get_image_names(folder_name)
    picture_names = ['Layer 1.png', 'Layer 2.png', 'Layer 3.png', 'Layer 4.png', 'Layer 5.png', 'Layer 6.png', 'Layer 7.png', 'Layer 8.png', 'Layer 9.png', 'Layer 10.png', 'Layer 11.png', 'Layer 12.png', 'Layer 13.png', 'Layer 14.png', 'Layer 15.png']

    for picture in picture_names:
        image_matrix = convert_image(go_dir(picture, folder_name))

        print('Finish converting picture', picture)
        sys.stdout.flush()
        cont_sym_score = sym_cont.cont_symmetry_score(image_matrix)

        print('Finish cont_sym_score for', picture)
        sys.stdout.flush()
        dist_sym_score = sym_dist.dist_symmetry_score(image_matrix)

        print('Finish dist_sym_score for', picture)
        sys.stdout.flush()
        papentine_score = papentine.papentine(image_matrix)

        print('Finish processing for picture', picture)
        sys.stdout.flush()

        image_score[picture] = papentine_score
        # image_score[picture] = merge_three_dict(cont_sym_score, dist_sym_score, papentine_score)

    # writing data onto an excel file
    workbook = xlsxwriter.Workbook(excel_file_name)
    worksheet = workbook.add_worksheet()

    # This is so that this line works with both chinese and chipman patterns
    # Example of hard-coded value below
    # columns = sorted(image_score['p1.png'])
    # columns = sorted(image_score['Layer\ 1.png'])
    columns = sorted(image_score[image_score.keys()[0]])

    col = 0
    row = 0
    for column in columns:
        col += 1

        worksheet.write(row, col, column)

    col = 0
    row = 0

    for picture in picture_names:
        col = 0
        row += 1
        worksheet.write(row, col, picture)
        for column in columns:
            col += 1
            worksheet.write(row, col, image_score[picture][column])

    # Write spearman values
    worksheet.write(row + 1, 0, 'Spearman rho')
    worksheet.write(row + 2, 0, 'Spearman p value')

    col = 1
    for column in columns:
        scores = []
        for pic in picture_names:
            scores.append(image_score[pic][column])
        rho, p_value = spearmanr(human_scores, scores)
        rho = round(rho, 3)
        p_value = round(p_value, 3)
        worksheet.write(row + 1, col, str(rho))
        worksheet.write(row + 2, col, str(p_value))

        col += 1

    workbook.close()

    print('Saved analysis to', excel_file_name)

    # rb1 = xlrd.open_workbook(excel_file_name)
    # rb2 = xlrd.open_workbook('Unoptimized_Chipman Image Analysis.xlsx')
    #
    # sheet1 = rb1.sheet_by_index(0)
    # sheet2 = rb2.sheet_by_index(0)
    #
    # for rownum in range(max(sheet1.nrows, sheet2.nrows)):
    #     if rownum < sheet1.nrows:
    #         row_rb1 = sheet1.row_values(rownum)
    #         row_rb2 = sheet2.row_values(rownum)
    #
    #         for colnum, (c1, c2) in enumerate(izip_longest(row_rb1, row_rb2)):
    #             if c1 != c2:
    #                 print "Row {} Col {} - {} != {}".format(rownum+1, colnum+1, c1, c2)
    #     else:
    #         print "Row {} missing".format(rownum+1)
    # print('New Results equal to old unoptimized code results')


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
