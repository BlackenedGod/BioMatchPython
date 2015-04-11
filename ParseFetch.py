import json
import httplib
import urllib

tacYaprak = 'TacYaprak'
canakYaprak = 'CanakYaprak'

connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('GET', '/1/classes/Pictures/', json.dumps({
     }), {
       "X-Parse-Application-Id": "HgrrtDO2dnazkQCPY59MR82ERhiamS5b1LTXBit8",
       "X-Parse-REST-API-Key": "hKSwFIi8Y6CrijPpXUABQSrLj5TMVekMwqk2I98I",

     })

result = json.loads(connection.getresponse().read())
dump = json.dumps(result)



print dump

urlInfo = result['results'][0][tacYaprak]['url']

print urlInfo
response = urllib.urlretrieve(urlInfo, "TestImg/pic2.jpg")