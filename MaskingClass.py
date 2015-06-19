from datetime import datetime

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

    def getNowTime(self):
        #En son eklenen kaydi zaman ile bulabilmek icin simdiki zamani al.
        self.nowhour = datetime.datetime.now()
        return self.nowhour

    def maskTac(self):
        (_, new_mask) = cv2.threshold(self.blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        a = RGBHistogram([8,8,8])
        b = RGBHistogram([8,8,8])

        arrayA = a.describe(self.image, new_mask)
        arrayB = b.describe(self.image)
        maskFilePathTac = "MaskImg/"+"mask_tac_"+self.getNowTime()+".jpg"
        c = np.in1d(arrayA, arrayB)
        print c
        cv2.imwrite(maskFilePathTac, new_mask)

        print 'Basari ile maskelendi -->', maskFilePathTac, '\n'

    def maskCanak(self):
        (_, new_mask) = cv2.threshold(self.blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        a = RGBHistogram([8,8,8])
        b = RGBHistogram([8,8,8])

        arrayA = a.describe(self.image, new_mask)
        arrayB = b.describe(self.image)
        maskFilePathCanak = "MaskImg/"+"mask_canak_"+self.getNowTime()+".jpg"
        c = np.in1d(arrayA, arrayB)
        print c
        cv2.imwrite(maskFilePathCanak, new_mask)

        print 'Basari ile maskelendi -->', maskFilePathCanak, '\n'