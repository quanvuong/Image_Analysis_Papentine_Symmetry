from PIL import Image
import copy
import numpy as np
import math
import string
import numpy

def LengthSubList(l):
    "Return the sum length of all the sublist of a list "

    length = 0
    for i in range(len(l)):
        length = length + len(l[i])
    return length

def rotate90(a): 
    "Rotate the image by 90 degree, for 180,270, repeat "

    b = numpy.array(zip(*a))
    for i in range(len(b)):
        b[i] = b[i][::-1]
    return b

def Papentine(a): #Calculate L1 length of 1 sequence 
    Score = 0 #Score is the L1 length
    
    Split = [] #split is a splitted whenever consecutive symbols are different

    Count = a[0]
    for i in range(len(a)-1):
        l = LengthSubList(Split)
        if a[i] != a[i+1]:
            Split.append(a[l:i+1])
            l = l + len(Split[len(Split)-1])

    Split.append(a[l:len(a)])

    Score = len(Split)

    for i in range(len(Split)):
        Score = Score + math.log(len(Split[i]),10)

    return Score

def PapentineMatrix(a): #Calculate L1 length of a matrix, whether horizontal or vertical
    Score = [] # Contains the score of the different lines in the matrix
    for i in range(len(a)):
        Score.append(Papentine(a[i]))

    return sum(Score)

def DiagonalP(a): #turn matrix into diagonal positive matrix
    Matrix = [[] for i in range(9)]
    
    for i in range(1,6)[::-1]:
        location = i-1
        j = copy.deepcopy(i)
        for k in range(j+1):
            Matrix[location].append(a[i][k])
            i -= 1 

    for i in range(1,6)[::-1]:
        Matrix[5].append(a[i][6-i])

    for i in range(2,6)[::-1]:
        Matrix[6].append(a[i][7-i])

    for i in range(3,6)[::-1]:
        Matrix[7].append(a[i][8-i])

    Matrix[8].append(a[5][4])
    Matrix[8].append(a[4][5])
            
    return Matrix

def Complete(image):
    Score = [] #Score contains the diagonal, Positive Diagonal, then Negative
    im = Image.open(image).convert('RGB')
    a = np.asarray(im) # a is the matrix representation of the original image
    a = np.array(a).tolist()

    b = DiagonalP(a)

    Score.append(PapentineMatrix(b))

    c = rotate90(a)

    c = np.array(c).tolist()

    d = DiagonalP(c)

    Score.append(PapentineMatrix(d))

    return Score

if __name__ == '__main__':
    pass

    img_amt = 15
        
    ImageName = [[] for i in range(img_amt)]

    Comparison = [[] for i in range(img_amt)]

    for i in range(img_amt):
        ImageName[i] = "p%i.png" %(i+1)

    for i in range(img_amt):
        Comparison[i] = Complete(ImageName[i])

    for i in range(img_amt):
        Comparison[i].append(i+1)

    for i in range(img_amt):
        Comparison[i].insert(0, i);

    for i in Comparison:
        print i
