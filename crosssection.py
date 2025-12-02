import cv2 as cv
import numpy as np

def crossSection(cnt):
    Ixx = 0
    Iyy = 0
    Ixy = 0
    phi = 0

    M = cv.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    area = cv.contourArea(cnt)
    
    cnt_norm = cnt - [cx, cy]

    for p in cnt_norm:
        x, y = p[0]
        Ixx += (1/12+y*y)
        Iyy += (1/12+x*x)
        Ixy += (-x*y)
    
    secoundMomentOfArea = [(Ixx, Ixy),
                           (Ixy, Iyy)]
    
    if Ixy == 0:
        phi = 0
    elif Ixy != 0 and Iyy == Ixx:
        phi = np.deg2rad(45)
    else:
        phi = 0.5 * np.arctan2(2*Ixy, (Ixx - Iyy))

    return cx, cy, area, secoundMomentOfArea, phi
