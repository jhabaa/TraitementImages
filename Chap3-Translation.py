import cv2 as opencv
import numpy as np
image = opencv.imread(r"C:\Users\Hean\Documents\GitHub\TraitementImages\testImages\zelda.png")
#creation d'une nouvelle image 
zeldaTranslation = np.zeros((700,700,3),dtype=np.uint8)
#Fonction de translation
#On selectionne tous les pixels
def translation(x): # translation d'un x à droite
    global image, zeldaTranslation
    for a in range (image.shape[0]):
        for b in range (image.shape[1]):
            zeldaTranslation[a+x,b+x] = image[a,b]

translation (50)
opencv.imshow("Zeldatranslate", zeldaTranslation)
opencv.imshow("Original", image )
opencv.waitKey(0)