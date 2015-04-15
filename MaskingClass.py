__author__ = 'kerem'

import numpy as np
import cv2


class MaskingClass():
    def __init__(self, file_path, file_name):

        self.file_path = file_path
        self.file_name = file_name
        self.image = cv2.imread(self.file_name)
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        (_, new_mask) = cv2.threshold(self.gray, 128, 255, cv2.THRESH_BINARY)
        cv2.imwrite(self.file_path+".jpg", new_mask)
        print self.file_path , '\n', self.file_name
        cv2.imshow("Mask", new_mask)




