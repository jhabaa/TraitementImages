import cv2 as cv
import numpy as np

render = np.zeros((250,250,3), np.uint8)
render[:] = (255,255,255)

#Dessinons un carré sans la fonction rectangle... donc avec des lignes

for x in range(50,200):
    for y in range(50,200):
        cv.line(render,(x,y),(200, 200), (0,0,255),1)
cv.imshow("Render", render)
cv.waitKey(0)