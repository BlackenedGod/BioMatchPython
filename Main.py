__author__ = 'altug'

from ParseJSON import parseJSON
import MaskingClass

#******************Test Edilecek Fotonun Tac ve Canagini Indir*************************
jsoninstance = parseJSON()

jsoninstance.downloadLastImageTac()
jsoninstance.downloadLastImageCanak()
#**************************************************************************************

tacImagePath = "TestImg/picTac.jpg"
canakImagePath = "TestImg/picCanak.jpg"
now = str(jsoninstance.getNowTime())

maskFilePath = "MaskImg/"+"mask_"+now

#******************Tac ve Canak icin maske cikar MaskImg ye kayit et*******************
maskingTacinstance = MaskingClass.MaskingClass(maskFilePath, tacImagePath)
maskingCanakinstance = MaskingClass.MaskingClass(maskFilePath, canakImagePath)
#**************************************************************************************
