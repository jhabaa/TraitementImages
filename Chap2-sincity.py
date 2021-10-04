#Transformons l'image en niveau de gris sauf pour les portions rouges
import cv2 as cv
image = cv.imread(r"TraitementImages\testImages\SinCity.jpg")
#definition des bornes
a = image.shape[0]
b = image.shape[1]
#Parcours du tableau
for x in range(a):
    for y in range(b):
        #On accentue uniquement les zones avec un maximum de rouge uniquement les zones rouges.
        if (image[x,y][2] > 120):
            if(image[x,y][1] < 35):
                if(image[x,y][0] < 35):
                    image[x,y][2] = 255
                    image[x,y][1] = 0
                    image[x,y][0] = 0
        if (image[x,y][2] != 0):
            if(image[x,y][1] != 0):
                if(image[x,y][0] != 0):
                    image[x,y][0] = image[x,y][2]
                    image[x,y][1] = image[x,y][2]
                




cv.imshow("Sin City", image)
cv.waitKey(0)
