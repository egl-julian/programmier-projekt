import cv2 as cv
import numpy as np

def undistortion(imgName, mtx, dist):
    img = cv.imread(imgName) # liest das Bild mit dem übergebenen Namen ein
    h, w = img.shape[:2] # h: Höhe des Bildes; w: Breite des Bildes
    newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h)) # erstellt optimierte Kameramatrix; roi: Reagon of intrest, benötigt um schwarze Ränder zu vermeiden

    dst = cv.undistort(img, mtx, dist, None, newcameramtx) # entfernt die Verzerrungen im Bild 

    x, y, w, h = roi 
    dst = dst[y:y+h, x:x+w] # schneidet das bild zu / die schwarzen Ränder ab
    cv.imwrite('kalibriert.png', dst) # speichert das kalibrierte Bild ab 