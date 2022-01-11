#Exercice Somme
import cv2 as cv
import numpy as np

#Load Images
Image1 = cv.imread(r"TraitementImages\testImages\zelda.png")
Image1 = cv.cvtColor(Image1, code=cv.COLOR_BGR2GRAY)
Image2 = cv.imread(r"TraitementImages\testImages\lena.bmp")
Image2 = cv.cvtColor(Image2, code=cv.COLOR_BGR2GRAY)
Image3 = np.zeros((Image2.shape[0],Image2.shape[1]), dtype=np.uint8)

def SumOperation(img1,img2,img3):
    for a in range(img3.shape[0]):
        for b in range (img3.shape[1]):
            img3[a,b] = int(img1[a,b]/2) + int(img2[a,b]/2)
    return img3

stack = np.concatenate((Image1, Image2,SumOperation(Image1, Image2, Image3)), axis=1)
cv.imshow("return", stack)
cv.waitKey(0)

