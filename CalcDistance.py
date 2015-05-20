

__author__ = 'kerem'

import cv2
import numpy as np
import os
#from matplotlib import pyplot as plt

image = cv2.imread('dataset/images/image_daisy_0172.png')

fast = cv2.FastFeatureDetector(40)

fastKp = fast.detect(image, None)

img = cv2.drawKeypoints(image, fastKp, outImage=image, color=(0, 0, 255))

#minimum x ve y degerleri bulunur.
(minX, minY) = fastKp[0].pt
(maxX, maxY) = fastKp[len(fastKp)-1].pt


(rowImage, colImage) = image.shape

for i in range(0, len(fastKp)):
    (x, y) = fastKp[i].pt

    if x < minX:
        minX = x
        #print "x minimumdur", minX
    else:
        '''print "degisim yoktur(x)", minX'''

for i in range(0, len(fastKp)):
    (x, y) = fastKp[i].pt

    if y < minY:
        minY = y
        '''print "y minimumdur", minY'''
    else:
        '''print "degisim yoktur(y) ", minY'''

for i in range(0, len(fastKp)):
    (x, y) = fastKp[i].pt

    if x > maxX:
        maxX = x
        '''print "x maximumdur", maxX'''
    else:
        '''print "degisim yoktur(x)", maxX'''

for i in range(0, len(fastKp)):
    (x, y) = fastKp[i].pt

    if y > maxY:
        maxY = y
        '''print "y maximumdur", maxY'''
    else:
        '''print "degisim yoktur(y)", maxY'''


distanceX = maxX - minX
distanceY = maxY - minY

distanceMean = (distanceX + distanceY) / 2

print "Tac Yaprak uzunlugu ya ", distanceX, "ya da ", distanceY, "pixeldir"


#realSizeOfObject = (focalLength * distanceToObject * colImage) / (distanceY * sensorHeigth)


cv2.namedWindow("fast", cv2.WINDOW_NORMAL)
cv2.imshow("fast", img)

cv2.waitKey(0)









