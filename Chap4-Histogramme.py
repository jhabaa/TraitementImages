import numpy as np
import cv2 as cv

image = np.ones((255,300,3), np.uint8)*255
image[:] = 255,0,0
#The function line draws the line segment between pt1 and pt2 points in the image. 
cv.line(image,(0,0),(image.shape[1], image.shape[0]), (255,255,255),1) #pt1 = (0.0) & pt2 = (image.shape[1], image.shape[0])

cv.rectangle(image,(0,0),(250,200),(255,255,255),2)
cv.circle(image, (150,150), 20, (255,255,255),4)
cv.putText(image,"Hello there", (0,100), cv.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),3)
cv.imshow("image", image)
cv.waitKey(0)
