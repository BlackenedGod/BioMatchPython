import json, httplib, urllib
import datetime
import time
import Image
import cv2
from CalcDistance import CalcDistance
from MaskingClass import maskingClass

class parseJSON:

    def __init__(self):
        #Bu Strinlerin tanimlanmasi ileride degisebilecekleri anlamina gelir JSON objelerinin alanlarinin isimleridir.
        self.tacYaprakString = 'TacYaprak'
        self.canakYaprakString = 'CanakYaprak'
        self.resultsString = 'results'
        self.createdAtString = 'createdAt'
        self.urlString = 'url'
        self.canakURLPath = "TestImg/picCanak"
        self.focalLengthString = "focalLength"
        self.focalLength = ""
        self.sensorSize = ""
        self.objIDString = "objectID"
        self.sensorSizeString = "sensorSize"
        self.tacURLPath = "TestImg/picTac"
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


            urlInfoTac = self.result[self.resultsString][i][self.objIDString][self.tacYaprakString][self.urlString]
            urlInfoCanak = self.result[self.resultsString][i][self.objIDString][self.canakYaprakString][self.urlString]
            dateTimePath = datetime.datetime.strptime(self.result[self.resultsString][i][self.createdAtString], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S.%f")
            urllib.urlretrieve(urlInfoTac, self.tacURLPath+dateTimePath+".png")
            urllib.urlretrieve(urlInfoCanak, self.canakURLPath+dateTimePath+".png")
            maskFilePathTac = "MaskImg/"+"mask_tac_"+str(i)+".png"
            maskFilePathCanak = "MaskImg/"+"mask_canak_"+str(i)+".png"
            focalLength = self.result[self.resultsString][i][self.objIDString][self.focalLengthString]
            sensorSize = self.result[self.resultsString][i][self.objIDString][self.sensorSizeString]
            CalcDistance().calcDistance(focalLength=focalLength, sensorHeigth=sensorSize, distanceToObject=10)
            maskingInstanceTac = maskingClass(maskFilePathTac, self.tacURLPath+dateTimePath+".png")
            maskingInstanceCanak = maskingClass(maskFilePathCanak, self.canakURLPath+dateTimePath+".png")

    def downloadSpecificObject(self, objID):
        length = len(self.JSONObjectresult)
        retval = 0
        for i in range(0, length):
            objectID = self.result[self.resultsString][i][self.objIDString]

            if objectID == objID:
                urlInfoTac = self.result[self.resultsString][i][self.tacYaprakString][self.urlString]
                urlInfoCanak = self.result[self.resultsString][i][self.canakYaprakString][self.urlString]
                dateTimePath = datetime.datetime.strptime(self.result[self.resultsString][i][self.createdAtString], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S.%f")

                maskFilePathTac = "MaskImg/"+"mask_tac_"+str(i)+".png"
                maskFilePathCanak = "MaskImg/"+"mask_canak_"+str(i)+".png"
                focalLength = self.result[self.resultsString][i][self.focalLengthString]
                sensorSize = self.result[self.resultsString][i][self.sensorSizeString]
                CalcDistance().calcDistance(focalLength=focalLength, sensorHeigth=sensorSize, distanceToObject=10)
                maskingClass(maskFilePathTac, self.tacURLPath+dateTimePath+".png")
                maskingClass(maskFilePathCanak, self.canakURLPath+dateTimePath+".png")
                retval = 1

        return retval








#instance = parseJSON()

#instance.downloadLastImageCanak()
#time.sleep(1)
#instance.downloadLastImageTac()

#picTac = cv2.imread("TestImg/picTac.png")
#picCanak = cv2.imread("TestImg/picCanak.png")

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