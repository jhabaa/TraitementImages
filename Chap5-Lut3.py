import cv2 as cv
import numpy as np
from numpy.core.fromnumeric import shape
import math as math

#Import an image
Image = cv.imread(r"TraitementImages\testImages\SinCity.jpg")
#Image in gray levels
ImageGray = cv.cvtColor(Image, code=cv.COLOR_BGR2GRAY)
#Fonction qui diminue le nombre de niveaux de gris (128,96,64,48,32,16...)
#identity = np.arange((256), dtype = np.dtype('uint8'))
#Fonctionne impécablement sur une ligne XD
#zeros = np.array([ math.pow(2,i) for i in range (0,256)]).clip(0,255).astype('uint8')

#Lets create a 256 values table for corresponding
lookUpTable = np.zeros((256,1), dtype=np.uint8)          
#We cann now save our values in the table
for a in range(256):
    if (math.pow(2,a))< 256:
        lookUpTable[a] = np.int64(math.pow(2,a))
    else:
        lookUpTable[a] = 255


render = cv.LUT(ImageGray, lookUpTable)
#show
hori = np.concatenate(Image, axis=1)
cv.imshow("render", render)
cv.waitKey()