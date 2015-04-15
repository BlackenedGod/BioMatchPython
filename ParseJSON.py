import json, httplib, urllib
import datetime
import Image
import cv2

class parseJSON:

    def __init__(self):
        #Bu Strinlerin tanimlanmasi ileride degisebilecekleri anlamina gelir JSON objelerinin alanlarinin isimleridir.
        self.tacYaprakString = 'TacYaprak'
        self.canakYaprakString = 'CanakYaprak'
        self.resultsString = 'results'
        self.createdAtString = 'createdAt'
        self.urlString = 'url'
        self.canakURLPath = "TestImg/picCanak.jpg"
        self.tacURLPath = "TestImg/picTac.jpg"
        try:
            self.connection = httplib.HTTPSConnection("api.parse.com", 443)
            self.connection.connect()

            self.connection.request('GET', '/1/classes/Pictures/', json.dumps({
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
        print '\nLast Tac Image Date :', datetime.datetime.strptime(self.result[self.resultsString][self.lastdataIndex][self.createdAtString], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S.%f"), '\n'
        response = urllib.urlretrieve(self.urlInfo, self.tacURLPath)
        if(response != None):
            print 'Tac Yaprak Indirildi .\n'


instance = parseJSON()

instance.downloadLastImageCanak()
instance.downloadLastImageTac()

picTac = cv2.imread("TestImg/picTac.jpg")
picCanak = cv2.imread("TestImg/picCanak.jpg")

cv2.imshow("Tac Yaprak", picTac)
cv2.imshow("Canak Yaprak", picCanak)

cv2.waitKey(0)

























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