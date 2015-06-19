__author__ = 'altug'

import cv2
import numpy as np
class RGBHistogram:
    def __init__(self, bins):
        self.bins = bins

    def describe(self, image, mask=None):
        histogram = cv2.calcHist([image], [0, 1, 2], mask, self.bins, [0, 256, 0, 256, 0, 256])
        histogram = cv2.normalize(histogram, dst=None)

        return histogram.flatten()

instance = RGBHistogram([8, 8, 8])
image = cv2.imread("asd.jpg")
instance.describe(image)

print instance.describe(image)



