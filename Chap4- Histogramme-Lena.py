import cv2 as cv
import numpy as np
import math as math

# On importe l'image l'image Lena.png
LenaImage = cv.imread(r"C:\Users\Hean\Documents\GitHub\TraitementImages\testImages\lena.png")
#On la met en niveaux de gris
ResultImage = cv.cvtColor(LenaImage, cv.COLOR_BGR2GRAY)
#On recupère les dimensions
LenaImageX = ResultImage.shape[0]
LenaImageY = ResultImage.shape[1]
Cadre = np.zeros((400,400,3), np.uint8)

#Comptons le nombre de pixels de chaque niveau de gris
def trace ():
    #Fonction pour qui compte le nombre de pixels d'une couleur
    for X in range(255):
        for a in range(LenaImageX):
            Y = 0
            for b in range(LenaImageY):
                if ResultImage[a,b] == X:
                    Y = Y + 1
        Droite = cv.line(Cadre, (X+52,300), (X+52, (300-Y*10)), color=(255,0,0), thickness=1)
          
#Histogramme
def Histogramme ():
    global Cadre
    #Dessinons un repère
    X = cv.line(Cadre, (50,300), (305,300), color= (255,255,255), thickness=2)
    Y = cv.line(Cadre,(50,50),(50,300), color=(255,255,255), thickness=2)
    
trace()
Histogramme()
cv.imshow("Histogramme", Cadre)
cv.imshow("Lena", ResultImage)
cv.waitKey(0)