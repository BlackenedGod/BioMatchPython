__author__ = 'kerem'

import json, httplib, urllib
import datetime
import time
import Image
import cv2
from CalcDistance import CalcDistance
from MaskingClass import maskingClass

class GetTrainingPhotos:

    def __init__(self):
        #Bu Strinlerin tanimlanmasi ileride degisebilecekleri anlamina gelir JSON objelerinin alanlarinin isimleridir.
        self.tacYaprakString = "TacYaprak"
        self.canakYaprakString = "CanakYaprak"
        self.resultsString = "results"
        self.createdAtString = "createdAt"
        self.urlString = "url"
        self.canakURLPath = "TestImg/picCanak.jpg"
        self.focalLengthString = "focalLength"
        self.sensorSize = ""
        self.objIDString = "objectId"
        self.sensorSizeString = "SensorSize"
        self.tacURLPath = "TestImg/picTac.jpg"
        self.specyName = "specy"
        self.locationParam = urllib.urlencode({"where": json.dumps({
            "location": {
                "$exists" : True
            }
        })})
        try:
            self.connection = httplib.HTTPSConnection("api.parse.com", 443)
            self.connection.connect()

            self.connection.request('GET', '/1/classes/Train?%s' % self.locationParam, json.dumps({
            }), {
                "X-Parse-Application-Id": "HgrrtDO2dnazkQCPY59MR82ERhiamS5b1LTXBit8",
                "X-Parse-REST-API-Key": "hKSwFIi8Y6CrijPpXUABQSrLj5TMVekMwqk2I98I",
            })

            self.result = json.loads(self.connection.getresponse().read())
            self.dump = json.dumps(self.result) # Komple String sonucu icin .
            self.JSONObjectresult = self.result[self.resultsString] # Tum JSON objeleri icin .
            #print self.dump
        except RuntimeError:
            print 'Baglanti Kurulamadi !'


    def downloadAll(self):

        length = len(self.JSONObjectresult)
        for i in range(0, length):
            urlInfoTac = self.result[self.resultsString][i][self.canakYaprakString][self.urlString]
            urlInfoCanak = self.result[self.resultsString][i][self.canakYaprakString][self.urlString]
            specyName = self.result[self.resultsString][i][self.specyName]
            print specyName
            dateTimePath = datetime.datetime.strptime(self.result[self.resultsString][i][self.createdAtString], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S.%f")
            urllib.urlretrieve(urlInfoTac, self.tacURLPath+dateTimePath+".jpg")
            urllib.urlretrieve(urlInfoCanak, self.canakURLPath+dateTimePath+".jpg")
            maskFilePathTac = "MaskImg/"+"mask_tac_"+str(i)+".jpg"
            maskFilePathCanak = "MaskImg/"+"mask_canak_"+str(i)+".jpg"
