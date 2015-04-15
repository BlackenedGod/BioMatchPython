__author__ = 'altug'

import ParseJSON
import MaskingClass

#******************Test Edilecek Fotonun Tac ve Canagini Indir*************************
jsoninstance = ParseJSON.parseJSON()

jsoninstance.downloadLastImageTac()
jsoninstance.downloadLastImageCanak()
#**************************************************************************************

tacImagePath = "TestImg/picTac.jpg"
canakImagePath = "TestImg/picCanak.jpg"
maskFilePath = "MaskImg/"+"mask_" , jsoninstance.getNowTime()

#******************Tac ve Canak icin maske cikar MaskImg ye kayit et*******************
maskingTacinstance = MaskingClass.maskingClass(maskFilePath, tacImagePath)
maskingCanakinstance = MaskingClass.maskingClass(maskFilePath, canakImagePath)
#**************************************************************************************
