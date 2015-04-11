import json, httplib, urllib
import datetime

tacYaprak = 'TacYaprak'
canakYaprak = 'CanakYaprak'


connection = httplib.HTTPSConnection("api.parse.com", 443)
connection.connect()

connection.request('GET', '/1/classes/Pictures/', json.dumps({
     }), {
       "X-Parse-Application-Id": "HgrrtDO2dnazkQCPY59MR82ERhiamS5b1LTXBit8",
       "X-Parse-REST-API-Key": "hKSwFIi8Y6CrijPpXUABQSrLj5TMVekMwqk2I98I",

     })


result = json.loads(connection.getresponse().read())
dump = json.dumps(result)

print dump

sizeofdata = len(result['results'])

#Tum Tablo Datalari
allresult = result['results']

#En son eklenen kaydi zaman ile bulabilmek icin simdiki zamani al.
nowhour = datetime.datetime.now()

print nowhour

for resultin in allresult:
    print '\n', datetime.datetime.strptime(resultin['createdAt'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S.%f")

connection.request('GET', '/1/classes/Pictures/', json.dumps({
     }), {
       "X-Parse-Application-Id": "HgrrtDO2dnazkQCPY59MR82ERhiamS5b1LTXBit8",
       "X-Parse-REST-API-Key": "hKSwFIi8Y6CrijPpXUABQSrLj5TMVekMwqk2I98I",

     })

#urlInfo = result['results'][0][tacYaprak]['url']

#print urlInfo
#response = urllib.urlretrieve(urlInfo, "TestImg/pic2.jpg")