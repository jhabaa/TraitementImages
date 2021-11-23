import cv2 as cv
image = cv.imread(r"C:\Users\Hean\Documents\GitHub\TraitementImages\testImages\barbara.bmp")
imageinverse = cv.flip(image,2)
cv.imshow("barbara Inverse", imageinverse)
cv.waitKey(0)