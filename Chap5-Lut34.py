import cv2 as cv
import numpy as np

#Load an Image
Image = cv.imread(r"TraitementImages\testImages\lena.png")
ImageBW = cv.cvtColor(Image, code=cv.COLOR_BGR2GRAY)
#Create a LUT array to reduct the gray level to 2
ToTwo = np.zeros((256,1), dtype=np.uint8)
#make back every number to 2 max
for a in range(256):
    if (ImageBW[a] > 2) :
        ToTwo[a] = 2
    else:
        ToTwo[a] = 0

result = cv.LUT(ImageBW,ToTwo)

#show
stack = np.concatenate((result, ImageBW), axis=1)
cv.imshow("Result", stack)
cv.waitKey(0)