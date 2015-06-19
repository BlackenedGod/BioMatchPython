import glob
import json, httplib, urllib
import datetime
import time
import Image
import cv2
import numpy
from CalcDistance import CalcDistance
from MaskingClass import maskingClass
from RGBHistogram import RGBHistogram


class parseJSON:

    def __init__(self):
        #Bu Strinlerin tanimlanmasi ileride degisebilecekleri anlamina gelir JSON objelerinin alanlarinin isimleridir.
        self.tacYaprakString = "TacYaprak"
        self.canakYaprakString = "CanakYaprak"
        self.resultsString = "results"
        self.createdAtString = "createdAt"
        self.urlString = 'url'
        self.canakURLPath = "TestImg/Canak/picCanak"
        self.focalLengthString = "focalLength"
        self.sensorSize = ""
        self.objIDString = "objectId"
        self.sensorSizeString = "sensorSize"
        self.tacURLPath = "TestImg/Tac/picTac"
        self.dateTimePath = ""

        self.locationParam = urllib.urlencode({"where": json.dumps({
            "location": {
                "$exists" : True
            }
        })})
        try:
            self.connection = httplib.HTTPSConnection("api.parse.com", 443)
            self.connection.connect()

            self.connection.request('GET', '/1/classes/Pictures?%s' % self.locationParam, json.dumps({
            }), {
                "X-Parse-Application-Id": "HgrrtDO2dnazkQCPY59MR82ERhiamS5b1LTXBit8",
                "X-Parse-REST-API-Key": "hKSwFIi8Y6CrijPpXUABQSrLj5TMVekMwqk2I98I",
            })

            self.result = json.loads(self.connection.getresponse().read())
            self.dump = json.dumps(self.result) # Komple String sonucu icin .
            self.JSONObjectresult = self.result[self.resultsString] # Tum JSON objeleri icin .

        except RuntimeError:
            print 'Baglanti Kurulamadi !'

    def printAllResult(self):

        print self.dump

    def getAllJSONResult(self):
        #Tum Tablo Datalari
        return self.JSONObjectresult

    def getNowTime(self):
        #En son eklenen kaydi zaman ile bulabilmek icin simdiki zamani al.
        self.nowhour = datetime.datetime.now()
        return self.nowhour

    def printNowTime(self):
        #En son eklenen kaydi zaman ile bulabilmek icin simdiki zamani al.
        self.nowhour = datetime.datetime.now()
        print self.nowhour

    def downloadLastImageCanak(self):
        #Tum Data Uzunlugunu Al(Kayit Sayisi)
        self.sizeofdata = len(self.result[self.resultsString])
        self.lastdataIndex = self.sizeofdata - 1

        print self.lastdataIndex + 1, 'Kayit Basari ile Bulundu .'
        self.urlInfo = self.result[self.resultsString][self.lastdataIndex][self.canakYaprakString][self.urlString]
        print '\nLast Canak Image Date :', datetime.datetime.strptime(self.result[self.resultsString][self.lastdataIndex][self.createdAtString], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S.%f"), '\n'
        response = urllib.urlretrieve(self.urlInfo, self.canakURLPath)
        if(response != None):
            print 'Canak Yaprak Indirildi .\n'

    def downloadLastImageTac(self):
        #Tum Data Uzunlugunu Al(Kayit Sayisi)
        self.sizeofdata = len(self.result[self.resultsString])
        self.lastdataIndex = self.sizeofdata - 1

        print self.lastdataIndex + 1, 'Kayit Basari ile Bulundu .'
        self.urlInfo = self.result[self.resultsString][self.lastdataIndex][self.tacYaprakString][self.urlString]
        dateTimePath = datetime.datetime.strptime(self.result[self.resultsString][self.lastdataIndex][self.createdAtString], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S.%f")
        print '\nLast Tac Image Date :', dateTimePath, '\n'
        response = urllib.urlretrieve(self.urlInfo, self.tacURLPath)
        if(response != None):
            print 'Tac Yaprak Indirildi .\n'

    def focalLengthSensorSizeInfo(self):
        length = len(self.JSONObjectresult)
        for i in range(0, length):
            self.focalLength = self.result[self.resultsString][i][self.focalLengthString]
            self.sensorSize = self.result[self.resultsString][i][self.sensorSizeString]
            CalcDistance().calcDistance(focalLength=self.focalLength, sensorHeigth=self.sensorSize, distanceToObject=10)

    def downloadAll(self):

        length = len(self.JSONObjectresult)

        for i in range(0, length):


            urlInfoTac = self.result[self.resultsString][i][self.tacYaprakString][self.urlString]
            urlInfoCanak = self.result[self.resultsString][i][self.canakYaprakString][self.urlString]
            dateTimePath = datetime.datetime.strptime(self.result[self.resultsString][i][self.createdAtString], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S.%f")
            urllib.urlretrieve(urlInfoTac, self.tacURLPath+dateTimePath+".jpg")
            urllib.urlretrieve(urlInfoCanak, self.canakURLPath+dateTimePath+".jpg")
            maskFilePathTac = "MaskImg/"+"mask_tac_"+str(i)+".jpg"
            maskFilePathCanak = "MaskImg/"+"mask_canak_"+str(i)+".jpg"
            #focalLength = self.result[self.resultsString][i][self.objIDString][self.focalLengthString]
            #sensorSize = self.result[self.resultsString][i][self.objIDString][self.sensorSizeString]
            #CalcDistance().calcDistance(focalLength=focalLength, sensorHeigth=sensorSize, distanceToObject=10)
            #maskingInstanceTac = maskingClass(maskFilePathTac, self.tacURLPath+dateTimePath+".jpg")
            #maskingInstanceCanak = maskingClass(maskFilePathCanak, self.canakURLPath+dateTimePath+".jpg")

    def downloadSpecificObject(self, objID):

        print 'Istek geldi bulunursa indirilecek.'

        length = len(self.JSONObjectresult)
        retArray = []
        for i in range(0, length):
            objectID = self.result[self.resultsString][i][self.objIDString]
            if objectID == objID:
                urlInfoTac = self.result[self.resultsString][i][self.tacYaprakString][self.urlString]
                urlInfoCanak = self.result[self.resultsString][i][self.canakYaprakString][self.urlString]
                self.dateTimePath = datetime.datetime.strptime(self.result[self.resultsString][i][self.createdAtString], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S.%f")

                responseTac = urllib.urlretrieve(urlInfoTac, self.tacURLPath+"_"+self.dateTimePath+".jpg")
                if(responseTac != None):
                    print 'Tac Yaprak Indirildi .\n'
                responseCanak = urllib.urlretrieve(urlInfoCanak, self.canakURLPath+"_"+self.dateTimePath+".jpg")
                if(responseCanak != None):
                    print 'Canak Yaprak Indirildi .\n'

                #maskTacInstance = maskingClass(self.tacURLPath+"_"+self.dateTimePath+".jpg", self.canakURLPath+"_"+self.dateTimePath+".jpg")
                path1 = self.tacURLPath+"_"+self.dateTimePath+".jpg"
                path2 = self.canakURLPath+"_"+self.dateTimePath+".jpg"
                '''
                retArray.append(path1)
                retArray.append(path2)
                retval = 1'''

                tac_file_path = path1
                canak_file_path = path2

                imageTac = cv2.imread(tac_file_path)
                imageCanak = cv2.imread(canak_file_path)

                imagePathsTac = sorted(glob.glob("TrainImg/Tac/*.jpg"))
                imagePathsCanak = sorted(glob.glob("TrainImg/Canak/*.jpg"))

                grayTac = cv2.cvtColor(imageTac, cv2.COLOR_BGR2GRAY)
                grayCanak = cv2.cvtColor(imageCanak, cv2.COLOR_BGR2GRAY)

                blurTac = cv2.GaussianBlur(grayTac, (5, 5), 0)
                blurCanak = cv2.GaussianBlur(grayCanak, (5, 5), 0)

                time.sleep(2)
                #***************************************TAC***************************
                (_, new_mask) = cv2.threshold(blurTac, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
                a = RGBHistogram([8, 8, 8])
                b = RGBHistogram([8, 8, 8])
                x = RGBHistogram([8, 8, 8])
                y = RGBHistogram([8, 8, 8])

                for imagePathTac, imagePathCanak in zip(imagePathsTac, imagePathsCanak):
                    i = 1
                    counter = i + 1
                    arrayA = a.describe(imagePathTac)
                    arrayB = b.describe(imagePathCanak)

                    arrayC = x.describe(path1)
                    arrayD = y.describe(path2)

                    c = arrayA - arrayC
                    d = arrayB - arrayD

                    print c, d



                maskFilePathTac = "MaskImg/"+"mask_tac_"+str(self.getNowTime())+".jpg"
                print 'Basari ile maskelendi -->', maskFilePathTac, '\n'
                #*********************************************************************

                time.sleep(2)
                (_, new_mask) = cv2.threshold(blurCanak, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)



                maskFilePathCanak = "MaskImg/"+"mask_canak_"+str(self.getNowTime())+".jpg"

                cv2.imwrite(maskFilePathCanak, new_mask)
                cv2.imwrite(maskFilePathTac, new_mask)

                print 'Basari ile maskelendi -->', maskFilePathCanak, '\n'







                #***********************************************************




#instance = parseJSON()

#instance.downloadLastImageCanak()
#time.sleep(1)
#instance.downloadLastImageTac()

#picTac = cv2.imread("TestImg/picTac.jpg")
#picCanak = cv2.imread("TestImg/picCanak.jpg")

#cv2.imshow("Tac Yaprak", picTac)
#cv2.imshow("Canak Yaprak", picCanak)

#cv2.waitKey(0)

























#Tum Kayitlari Gezmek Icin
'''
            counter = 0
        for resultin in self.allresult:
            if(counter == self.lastdataIndex):
                self.urlInfo = resultin[self.canakYaprakString][self.urlString]
                 print '\n', datetime.datetime.strptime(resultin[self.createdAtString], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S.%f")
                response = urllib.urlretrieve(self.urlInfo, self.canakURLPath)
                if(response != None):
                    print 'Canak Yaprak Indirildi .\n'
            else:
                counter += 1
'''