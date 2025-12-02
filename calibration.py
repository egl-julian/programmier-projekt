import numpy as np
import cv2 as cv
import glob 
#ich hasse git hub und cedrik
def setup():
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001) # Kriterium zur Eckpunktfindung, entweder 30 Bilder oder Ergebniss ändert sich um weniger als 0.001 Pixel

    objp = np.zeros((6*9,3), np.float32)
    objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)

    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.

    images = glob.glob('kalib*.jpg') # findet alle Bilder im Verzeichniss die dem Muster kalib1.jpg folgen z.B. kalib01.jpg, kalib02.jpg, etc.

    for fname in images: # Schleife durchläuft jedes gefundene Bild in images
        img = cv.imread(fname) #ein Bild wird geladen
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #geladenes Bild wird in Graustufen umgewandelt
 
        # Findet die Ecken des Schachbrettmusters; 9x6 Muster
        ret, corners = cv.findChessboardCorners(gray, (9,6), None)
 
        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)
 
            corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
            imgpoints.append(corners2)

            if __name__ == '__main__':
                cv.drawChessboardCorners(img, (9,6), corners2, ret)
                cv.imshow('img', img)
                cv.waitKey(500)

        for i in corners2:
            print(i)

    ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1,None, None])

    return ret, mtx, dist, rvecs, tvecs

if __name__ == '__main__':
    setup()
