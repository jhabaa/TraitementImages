from typing import Collection
import cv2 as cv
import numpy as np
import numba as nb


#Commençons par importer l'image
Image = cv.imread(r"C:\Users\Hean\Documents\GitHub\TraitementImages\testImages\cameraman.tif")
ImageBW = cv.cvtColor(Image,cv.COLOR_BGR2GRAY) #Transformons l'image en Niveaux de gris
DessinCadre = np.ones((350,350,3), dtype=np.uint8)*255 #Dessinons un cadre blanc vide

histogramme = cv.calcHist(ImageBW, [0], None, [256], [0,256]) #Channel=0 car noir et blanc au lieu de [0,1,2]
def trace(): #Fonction qui trace les droites de l'histogramme
    for X in range(255):
        Y = histogramme[X]
        Y = int(Y) #La valeur retournée par la fonction Hist est en Float. Nous devons la convertir en Int
        Droite = cv.line(DessinCadre,((X + 22), 278),((X+22),(278-(Y*5))),color=(0,0,255), thickness=1)

def cadre(): #Fonction qui ajoute au cadre un repère 
    X = cv.line(DessinCadre,(20,280),(300,280), color=(255,0,0), thickness=2) #Axe des X
    Y = cv.line(DessinCadre, (20,280), (20,20), color=(255,0,0), thickness=2) #Axe des Y
    O = cv.putText(DessinCadre, "0", (18,300), cv.FONT_HERSHEY_PLAIN,1,color=(0,0,0),thickness=1) #Point 0 

cadre()
trace()
print(histogramme)
cv.imshow("Histogramm OpenCV", DessinCadre)
cv.imshow("ImageBW", ImageBW) 
cv.waitKey(0)