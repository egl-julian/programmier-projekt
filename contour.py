import cv2 as cv
import numpy as np

def contour():
    img = cv.imread('kalibriert.png')
    img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    ret, thresh = cv.threshold(img_grey, 130, 255, cv.THRESH_BINARY_INV)
    cv.imwrite('Bild_graustufen.png', thresh)

    contours, hierachy = cv.findContours(img = thresh, mode = cv.RETR_EXTERNAL, method = cv.CHAIN_APPROX_NONE)
    cnt = max(contours, key=cv.contourArea) # speichert die größte gefundene Kontur ab

    img_copy = img.copy()
    cv.drawContours(img = img_copy, contours = contours, contourIdx = -1, color = (0, 255, 0), thickness = -1, LineType = cv.LINE_AA)

    return cnt

if __name__ == '__main__':
    print(contour())