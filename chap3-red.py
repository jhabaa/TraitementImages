import cv2 as cv
import math
img = cv.imread(r"C:\Users\Hean\Documents\GitHub\TraitementImages\testImages\cameraman.tif")
a = img.shape[0]
b = img.shape[1]

# Fonction qui prend un scale en pourcent et redimensionne l'image en fonction.
def redim (s):
    global a,b # Définition des variables globales
    a = int(a * s/100) # ne pas oublier le Int car le résultat est en Float
    b = int(b * s/100)
    scale = (a,b) # On crée une variable scale avec les nouvelles valeurs
    imageredim = cv.resize(img,scale, interpolation= cv.INTER_CUBIC) # On applique la fonction resize de OpenCV
    cv.imshow("cameraman", imageredim)
    cv.waitKey(0)
    

redim(500) # Execution de la fonction pour 500%


#resizedImage = cv.resize(img, scale, interpolation=cv.INTER_CUBIC)
print(a)

