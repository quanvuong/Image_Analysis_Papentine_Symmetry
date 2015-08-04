# rotation 90, 180, 270
from PIL import Image
import copy
import np as np

def convert_image(image):
    "Convert an image into a matrix "
    im = Image.open(image).convert('RGB')
    image_converted  = numpy.asarray(im)

    return image_converted 

def get_mini_matrix(matrix, x_position, y_position, size):
    "Return a mini-matrix knowing the x,y-position of the upper right corner item of the mini-matrix "
    "and the size of the mini-matrix "

    mini_matrix = [] 

    for i in range(size):
        mini_matrix.append(matrix[y_position + i ][x_position : x_position+size])

    return mini_matrix 

def Complete(image):
    a = convert_image(image) # a is the matrix representation of the original image

    AllSet = [[] for i in range(num_mini_matrix(matrix))] #AllSet is used to contain all the minimatrix of a

    Count = 0 #Count is used to determine what is the size of each minimatrix

    for k in range(len(a)):
        for i in range(2,len(a)):
            if (k+i) > len(a): break
            for j in range(len(a)):
                if ((j + i)> len(a)): break
                else:
                    AllSet[Count].append(a[k][j:i+j])
                for m in range(1,i):
                    if (k+m) > len(a): break
                    AllSet[Count].append(a[k+m][j:j+i])

                Count += 1

    for i in range(len(AllSet)):
        AllSet[i] = np.concatenate([AllSet[i][0:len(AllSet[i])]])

    AllSet[len(AllSet)-1] = a


    def SymCal(a): #function to calculate symmetry of 1 matrix and return the total score
        # def rotate90(a): #Rotate the image by 90 degree, for 180,270, repeat 
        #     b = numpy.array(zip(*a))
        #     for i in range(len(b)):
        #         b[i] = b[i][::-1]
        #     return b

        # def SymCount(a,b):
        #   Count = 0

        #   if numpy.array_equal(a,b)==True: Count+=1

        #   if Count ==1 : return len(a)
        #   if Count ==0 : return 0

        # SymList = [0,0,0,0,0,0,0,0,0] 
        #SymList contains the no. of same pixel to reflected/rotated images
        # have compared to original image
        # in this order: lr, up, diagonal left-bottom_right-top, diagional left-top right-bottom,90, 180 ,270, and the total number of pixel in an image
        # and the total symmetry score
        
        # fliplr = numpy.fliplr(a) #reflect left right
        # flipud = numpy.flipud(a) #reflect up down


        # c = numpy.array(zip(*b)) # c is reflection along diagonal left-top right-bottom

        # for i in range(len(b)):
        #   b[i] = b[i][::-1]

        # b = zip(*b)

        # for i in range(len(b)):
        #   b[i] = b[i][::-1]

        # b = numpy.array(b) # b is reflection along diagonal left-bottom right-top

        # d = rotate90(a)

        # e = rotate90(d)

        # f = rotate90(e)

        # SymList[0] = SymCount(a,fliplr)
        # SymList[1] = SymCount(a,flipud)
        # SymList[2] = SymCount(a,b)
        # SymList[3] = SymCount(a,c)
        # SymList[4] = SymCount(a,d)
        # SymList[5] = SymCount(a,e)
        # SymList[6] = SymCount(a,f)
        # SymList[7] = len(a) * len(a[0])

        # for i in range(7):
        #     SymList[8] = SymList[8] + SymList[i]

        # return SymList

    # def SymCalTotal(AllSet):
    #     SymScore = [0,0,0,0,0,0,0,0,0]
    #     for i in range(len(AllSet)):
    #         SymList = SymCal(AllSet[i])
    #         for j in range(len(SymList)):
    #             SymScore[j] = SymList[j] + SymScore[j]
    #     return SymScore

    # return SymCalTotal(AllSet)

img_amt = 15

Comparison = [[] for i in range(img_amt)]

ImageName = [[] for i in range(img_amt)]

for i in range(img_amt):
    ImageName[i] = "p%i.png" %(i+1)


for i in range(len(ImageName)):
    Comparison[i] = Complete(ImageName[i])

for i in range(len(ImageName)):
    Comparison[i].append(i)

for i in range(len(Comparison)):
    print Comparison[i]
##
## 
    


##
## to flip a matrix along the diagonal left-bottom right-top, 1st: -1 within each mini-list, 2nd: zip(*matrix), 3rd: -1 within each mini-list
##
## to flip a matrix along the diagonal left-top right-bottom, just zip(*) the initial matrix
##
##a = numpy.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]])
##

## rank the images in the order of different measurement

## 5 experiments: calculate the symmetry:
# 1/ Only the total image  
# 2/ LR
# 3/ LR + UP + 2 diagonals
# 4/ LR + UP + 90 + 180 + 270
# 5/ 2 diagonals

##
##for i in range(len(AllSet)):
##    AllSet[i] = np.array(AllSet[0:len(AllSet)])
##
##AllSet
##                
##                if m == 1:print a[m][j:i+j]
##                if m >1  :print a[m+1][j:i+j]
                
            

##def rotate90(a):
##    b = np.array(zip(*a))
##    for i in range(len(b)):
##        b[i] = b[i][::-1]
##    return b
##
##b = rotate90(a)
##
##count = 0
##
##for i in range(len(a)):
##    if np.array_equal(a[i],b[i])==True:count+=1
