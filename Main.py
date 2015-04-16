__author__ = 'altug'

from ParseJSON import parseJSON
import time
import MaskingClass

#******************Test Edilecek Fotonun Tac ve Canagini Indir*************************
jsoninstance = parseJSON()

jsoninstance.downloadLastImageTac()
time.sleep(1)
jsoninstance.downloadLastImageCanak()
#**************************************************************************************

tacImagePath = "TestImg/picTac.png"
canakImagePath = "TestImg/picCanak.png"
now = str(jsoninstance.getNowTime())

maskFilePathTac = "MaskImg/"+"mask_tac_"+now+".png"
maskFilePathCanak = "MaskImg/"+"mask_canak_"+now+".png"
#******************Tac ve Canak icin maske cikar MaskImg ye kayit et*******************
maskingTacinstance = MaskingClass.maskingClass(maskFilePathTac, tacImagePath)
maskingCanakinstance = MaskingClass.maskingClass(maskFilePathCanak, canakImagePath)
#**************************************************************************************
