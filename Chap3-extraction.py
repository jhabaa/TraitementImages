import cv2 as cv
image = cv.imread(r"C:\Users\Hean\Documents\GitHub\TraitementImages\testImages\cat.bmp")
print (image.shape[0], image.shape[1])
imageCropped = image[30:400, 150:520]
cv.imshow("image 1", imageCropped)
cv.waitKey(0)