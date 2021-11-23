from typing import Collection
import cv2 as cv
import numpy as np

lena = cv.imread(r"C:\Users\Hean\Documents\GitHub\TraitementImages\testImages\lena.png")
#On transforme en niveaux de gris 
lenaBW = cv.cvtColor(lena,cv.COLOR_RGB2GRAY)
#données de l'image
a = lenaBW.shape[0]
b = lenaBW.shape[1]
#Tableau d'affiche
Carte = np.zeros((300,300,3), np.uint8)
 # La projection consiste à parcourir une image verticalement ou horizontalement et afficher un un point
 # sur chaque ligne correspondant à la moyenne des niveaux de gris de cette ême ligne ou colonne.
def projection():
    for X in range(a):
        Value = 0 #Somme des valeurs de niveaux de gris
        for Y in range(b):
           Value = Value + lenaBW[X,Y]
        Value = int(Value/b) #On fait la moyenne de cette somme apès avoir parcouru une ligne.
        print(Value)
        Point = cv.rectangle(Carte,(X+11,280-Value), (X+11,280-Value), color=(0,0,255), thickness=2)
def repere(): #Ceci est un repère.
    X = cv.line(Carte, (10,280),(280,280), color=(0,255,0), thickness=2)
    Y = cv.line(Carte,(10,280), (10,20), color=(0,255,0), thickness=2)

#Affichage
repere()
projection()
cv.imshow("Projetion Lena", Carte)
cv.imshow("Lena", lenaBW)
cv.waitKey(0)