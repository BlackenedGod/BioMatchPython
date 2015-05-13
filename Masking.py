__author__ = 'kerem'

import cv2
import numpy as np


def Masking():

    file_name = "TestImg/3_3.jpg"
    image = cv2.imread(file_name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #Burada grabCut metodu icin gerekli parametreler hazirlaniyor
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    mask = np.zeros(image.shape[:2], np.uint8)

    #grabCut icin thresholding islemi
    (_, new_mask) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

    #grabCut mask parametresi icin siyah - beyaz isaretlemeler icin array dolduruluyor
    mask[new_mask == 0] = 0
    mask[new_mask == 255] = 1

    #grabCut uygulaniyor
    mask, bgd_model, fgd_model = cv2.grabCut(image, mask, None, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_MASK)

    #grabCut mask ciktisi siyah - beyaz olarak ayarlaniyor
    mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    #img degiskenine resim ile maske matrisleri carpilarak yeni olusturulan maske yaziliyor
    img = image*mask[:, :, np.newaxis]

    cv2.imshow("Masked", new_mask)
    cv2.imshow("GrabCut", img)

    #dosya adi degistiriliyor : directory olan TestImg/ ifadesi kesiliyor ve dosya basina mask_ ifadesi ekleniyor
    file_name = "mask_" + file_name[8:]

    #dosya kayit.
    cv2.imwrite(file_name, new_mask)


    cv2.waitKey(0)

Masking()