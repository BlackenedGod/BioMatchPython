__author__ = 'kerem'
from RGBHistogram import RGBHistogram
from MaskingClass import maskingClass

class HistCompare:
    def __init__(self):
        pass

    def Compare(self, image, mask):
        desc = RGBHistogram([8, 8, 8])
        mask = maskingClass()
        desc.describe(image, mask)