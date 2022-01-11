import cv2 as cv
import numpy as np
import math as math
#Chargeons une image
image = cv.imread(r"TraitementImages\testImages\lena.png")
#Image en niveau de gris
imageBW = cv.cvtColor(image,code=cv.COLOR_BGR2GRAY)
imageBWCompare = cv.cvtColor(image,code=cv.COLOR_BGR2GRAY)
#Graphe
graphe = np.ones((imageBW.shape[0], imageBW.shape[1]), dtype=np.uint8)
#Fonction qui applique une LUT simple sur une image
def lut1():
    for a in range(imageBW.shape[0]):
        for b in range(imageBW.shape[1]):
            x = imageBW[a,b]
            y = math.sqrt(imageBW[a,b])
            imageBW[a,b] = math.sqrt(imageBW[a,b])
            
            cv.rectangle(graphe,(int(x),265-int(y)),(int(x),265-int(y)),(255,255,0),3)

#Repère Lut
def repere():
    cv.line(graphe,(10,10), (10,265), (255,0,255),2)
    cv.line(graphe, (10,265), (265,265), 255, 2)

repere()
print(imageBW[100,20])      
lut1()
#Affichage
Hori = np.concatenate((graphe, imageBW, imageBWCompare), axis = 1)
cv.imshow("Result", Hori)
cv.waitKey(0)