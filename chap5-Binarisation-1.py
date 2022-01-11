import cv2 as cv
import numpy as np

#Import de l'image
image = cv.imread(r"TraitementImages\testImages\lena.png")
#Rendre l'image en niveau de gris
imageBW = cv.cvtColor(image, code=cv.COLOR_BGR2HSV)
#Application de la Binarisation
#En OpenCV, il suffit de préciser sur quelle image on veut effectuer l'opération de binarisation (thresholding)
#, le seuil(threshold) et le niveau de gris qu affichera le résultat (en général 255 pour le blanc)
(thresh, binary)= cv.threshold(imageBW,100,255,cv.THRESH_BINARY)
#Affichage sur ligne
Hori = np.concatenate((imageBW, binary), axis=1)
cv.imshow("Results", Hori)
cv.waitKey(0)