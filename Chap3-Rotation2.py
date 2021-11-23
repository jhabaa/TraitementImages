import cv2 as opencv
image = opencv.imread(r"C:\Users\Hean\Documents\GitHub\TraitementImages\testImages\cards.jpg")
 #Fonction openCV pour realiser la rotation
imageRotated = opencv.rotate(image,opencv.ROTATE_90_CLOCKWISE)

opencv.imshow("Grid", image)
opencv.waitKey(0)