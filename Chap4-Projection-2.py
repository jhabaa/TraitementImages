import cv2 as cv
import numpy as np
from numpy.core.fromnumeric import shape
originalImage = cv.imread(r"C:\Users\Hean\Documents\GitHub\TraitementImages\testImages\lena.png")
#Même image en niveau de gris
bwImage = cv.cvtColor(originalImage,code=cv.COLOR_BGR2GRAY)
#Données de l'Image 
a = bwImage.shape[0]
b = bwImage.shape[1]
# Tablea de projection
tab = np.ones((300,300,3), np.uint8)
# La projection parcours l'image horizontalement et renvoie la moyenne de niveau de gris pour chaque ligne
#sur un niveau de gris B=G=R
def projection ():
    for x in range(b):
        level = 0
        for y in range(a):
            level += bwImage[x,y]
        #Moyenne de cette somme à la fin de chaque ligne
        level = level/(a)


cv.imshow("OriginalImage",bwImage)
cv.imshow("Tab", tab)
cv.waitKey(0)