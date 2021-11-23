import cv2 as rotation
import math as math
import numpy as np
image = rotation.imread(r"C:\Users\Hean\Documents\GitHub\TraitementImages\testImages\lambo.png")

#Creation d'une image vide
rotateImage = np.zeros((1000,1000,3), dtype=np.uint8)

#Fonction qui fait tourner une image d'un angle donné
def rotate(angle):
    global image, rotateImage
   # angle = angle * math.pi/180
    for a in range(image.shape[0]):
        for b in range(image.shape[1]):
            A = np.int64(a*math.cos(angle) - b*math.sin(angle))
            B = np.int64(b*math.sin(angle) + a*math.cos(angle))
            rotateImage[a,b] = image[A,B]
    rotation.imwrite("Render.png", rotateImage)
    rotation.imshow("Resultat", rotateImage)
    rotation.imshow("Base", image)
    rotation.waitKey(0)

rotate(0)
