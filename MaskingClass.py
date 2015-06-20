from datetime import datetime

__author__ = 'kerem'

import numpy as np
import cv2
from RGBHistogram import RGBHistogram
import time

class maskingClass():
    def __init__(self, tac_file_path, canak_file_path):

        self.tac_file_path = tac_file_path
        self.canak_file_path = canak_file_path

        self.imageTac = cv2.imread(self.tac_file_path)
        self.imageCanak = cv2.imread(self.canak_file_path)

        self.grayTac = cv2.cvtColor(self.imageTac, cv2.COLOR_BGR2GRAY)
        self.grayCanak = cv2.cvtColor(self.imageCanak, cv2.COLOR_BGR2GRAY)

        self.blurTac = cv2.GaussianBlur(self.grayTac, (5, 5), 0)
        self.blurCanak = cv2.GaussianBlur(self.grayCanak, (5, 5), 0)

        time.sleep(10)
        #***************************************TAC***************************
        (_, new_mask) = cv2.threshold(self.blurTac, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        a = RGBHistogram([8,8,8])
        b = RGBHistogram([8,8,8])

        arrayA = a.describe(self.imageTac, new_mask)
        arrayB = b.describe(self.imageTac)
        maskFilePathTac = "MaskImg/"+"mask_tac_"+self.getNowTime()+".jpg"
        c = np.in1d(arrayA, arrayB)
        print c
        cv2.imwrite(maskFilePathTac, new_mask)

        print 'Basari ile maskelendi -->', maskFilePathTac, '\n'
        #*********************************************************************

        time.sleep(10)
        (_, new_mask) = cv2.threshold(self.blurCanak, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        a = RGBHistogram([8,8,8])
        b = RGBHistogram([8,8,8])

        arrayA = a.describe(self.imageCanak, new_mask)
        arrayB = b.describe(self.imageCanak)
        maskFilePathCanak = "MaskImg/"+"mask_canak_"+self.getNowTime()+".jpg"
        c = np.in1d(arrayA, arrayB)
        print c
        cv2.imwrite(maskFilePathCanak, new_mask)

        print 'Basari ile maskelendi -->', maskFilePathCanak, '\n'
        #***********************************************************

    def getNowTime(self):
        #En son eklenen kaydi zaman ile bulabilmek icin simdiki zamani al.
        self.nowhour = datetime.datetime.now()
        return self.nowhour
