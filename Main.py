__author__ = 'altug'

from ParseJSON import parseJSON
import time
import MaskingClass

#******************Test Edilecek Fotonun Tac ve Canagini Indir*************************
jsoninstance = parseJSON()


jsoninstance.downloadLastImageTac()
jsoninstance.downloadLastImageCanak()
#**************************************************************************************

tacImagePath = "TestImg/picTac.png"
canakImagePath = "TestImg/picCanak.png"
now = str(jsoninstance.getNowTime())

maskFilePathTac = "MaskImg/"+"mask_tac_"+now
maskFilePathCanak = "MaskImg/"+"mask_canak_"+now
#******************Tac ve Canak icin maske cikar MaskImg ye kayit et*******************
maskingTacinstance = MaskingClass.MaskingClass(maskFilePathTac, tacImagePath)
maskingCanakinstance = MaskingClass.MaskingClass(maskFilePathCanak, canakImagePath)
#**************************************************************************************
