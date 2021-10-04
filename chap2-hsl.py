#programme qui extrait la composante saturation dans une image HSL et l'affiche.
import cv2 as cv
img = cv.imread(r"TraitementImages\testImages\pool.png")
a = img.shape[0]
b = img.shape[1]

for i in range (a):
    for j in range (b):
        L = ((max(img[i,j])/255)+(min(img[i,j])/255))/2
        if L<0.5:
            S = ((max(img[i,j])/255) - (min(img[i,j])/255))/((max(img[i,j])/255) + (min(img[i,j])/255))
        else:
            S = ((max(img[i,j])/255) - (min(img[i,j])/255))/(2-((max(img[i,j])/255) + (min(img[i,j])/255)))

        if ((img[i,j][2])/255 == (max(img[i,j])/255)):
            H = 60*(((img[i,j][1])/255 - (img[i,j][0])/255)/((img[i,j][2])/255 - (min(img[i,j])/255)))
        if ((img[i,j][1]/255) == (max(img[i,j])/255)):
            H = 60*(2+((img[i,j][0])/255 - (img[i,j][2])/255)/((img[i,j][1])/255 - (min(img[i,j])/255)))
        if ((img[i,j][0])/255 == (max(img[i,j]))/255):
            H = 60*(4+((img[i,j][2])/255 - (img[i,j][1])/255)/((img[i,j][0])/255 - (min(img[i,j])/255)))


        img[i,j][0] = H 
        img[i,j][1] = L
        img[i,j][2] = S
image = cv.cvtColor(cv.imread(r"TraitementImages\testImages\pool.png"), cv.COLOR_BGR2HLS_FULL)

cv.imshow("Pool", img)
cv.waitKey(0)