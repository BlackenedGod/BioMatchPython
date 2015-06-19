__author__ = 'kerem'

import numpy as np
import cv2
from RGBHistogram import RGBHistogram


class maskingClass():
    def __init__(self, file_path, file_name):

        self.file_path = file_path
        self.file_name = file_name
        self.image = cv2.imread(self.file_name)
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.blur = cv2.GaussianBlur(self.gray, (5, 5), 0)
        a = RGBHistogram([8,8,8])
        b = RGBHistogram([8,8,8])
        (_, new_mask) = cv2.threshold(self.blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        arrayA = a.describe(self.image, new_mask)
        arrayB = b.describe(self.image)

        c = np.in1d(arrayA, arrayB)

        print c
        cv2.imwrite(self.file_path, new_mask)

        print 'Basari ile maskelendi -->', self.file_path, '\n'




