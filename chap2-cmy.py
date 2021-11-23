import cv2 as cv
img = cv.imread(r"TraitementImages\testImages\boy.bmp")

#imageCMY = cv.cvtColor(img, cv.color_rgb)

#Les composantes CMY sont égales à 1-rgb/255
#Pour isoler, le cyan, nous allons donc mettre le rouge à 0 car cyan (0.255.255), Magenta (255.0.255), yellow (255.255.0)
a = img.shape[0]
b = img.shape[1]

#for i in range(a):
    #for j in range(b):
        #img[i,j][0] = 1-(img[i,j][0])
        #img[i,j][1] = 1-(img[i,j][1])
        #img[i,j][2] = 0
# Dans le système CMYK Pour extraire la composante k on met les autres à O
        
       # img[i,j][2] = 0 - min(img[i,j])
        #img[i,j][1] = 0 - min(img[i,j])
        #img[i,j][0] = 0 - min(img[i,j])
#Autre facon avec une methode pour extraire le cyan : non trouvée

image = cv.cvtColor(img, cv.COLOR_BGR2Luv)

cv.imshow("boy", image)
cv.waitKey(0)