import cv2 as cv
img = cv.imread(r"C:\Users\Hean\Documents\GitHub\TraitementImages\testImages\cat.jpg")

# pour une image en niveau de gris, les niveaux de rouge, vert et bleu doivent être egaux
#rendons la taille de l'image
a = img.shape[0]
b = img.shape[1]
#parcourons le tableau et egalisons les couleurs
for i in range(a):
    for j in range(b): 
        img[i,j][0] = img[i,j][2] #on assigne la valeur du picel rouge au pixel bleu
        img[i,j][1] = img[i,j][2] #on assigne la valeèr du pixel rouge au pixel vert

image = cv.cvtColor(img, cv.COLOR_BGR2LAB) # Fonction qui applique un filtre sur l'image.

cv.imshow("Mon chat", image) # on affiche image ou img 
cv.waitKey(0) #... plus longtemps

#ce code renvoie une image en niveau de gris