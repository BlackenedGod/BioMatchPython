__author__ = 'kerem'

import numpy as np
import cv2


class Masking():
    def __init__(self):
        self.file_path = ""
        self.file_name = ""
        self.image = cv2.imread(self.file_name)
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)


    def masking(self):
        (_, new_mask) = cv2.threshold(self.gray, 128, 255, cv2.THRESH_BINARY)
        cv2.imwrite("MaskImg/"+"mask_"+self.file_name, new_mask)



