import cv2 as cv # Chargement de la librairie
img = cv.imread(r'C:\Users\Hean\Documents\GitHub\TraitementImages\testImages\lena.png') # Lecture de l'image
a = img.shape[0] #renvoie la hauteur d'une image
b = img.shape[1] 
print (a)
print (b)
for i in range(a) : 
    for j in range(b) : #Pour extraire la composante rouge, je mets le bleu et le vert à 0
      img[i,j][0] = (0) #img[] donne la valeur du pixel à un point donné
      img[i,j][1] = (0)  

cv.imshow('Lena', img) #affichage de l'image
cv.waitKey(0) #empeche au programme de se fermer trop rapidement

#Ceci est un programme pour extraire la composante rouge d'une image et la renvoyer.