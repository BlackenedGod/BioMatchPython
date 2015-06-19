from ParseJSON import parseJSON
import time
import MaskingClass

class Main:

    def __init__(self):
        print "Main Started"

    def jsonStart(self, objectid):
        #******************Test Edilecek Fotonun Tac ve Canagini Indir*************************
        jsoninstance = parseJSON()
        #jsoninstance.downloadAll()
        #jsoninstance.downloadLastImageTac()
        #time.sleep(1)
        #jsoninstance.downloadLastImageCanak()
        if objectid == "":
            if jsoninstance.downloadSpecificObject(objectid) != 1: print 'Kayit Bulunamadi!'
        else:
            jsoninstance.downloadSpecificObject(objectid)
    #**************************************************************************************
        '''tacImagePath = "TestImg/picTac.png"
        canakImagePath = "TestImg/picCanak.png"
        now = str(jsoninstance.getNowTime())

        maskFilePathTac = "MaskImg/"+"mask_tac_"+now+".png"
        maskFilePathCanak = "MaskImg/"+"mask_canak_"+now+".png"
        #******************Tac ve Canak icin maske cikar MaskImg ye kayit et*******************
        #maskingTacinstance = MaskingClass.maskingClass(maskFilePathTac, tacImagePath)
        #maskingCanakinstance = MaskingClass.maskingClass(maskFilePathCanak, canakImagePath)'''
        #**************************************************************************************