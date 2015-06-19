import httplib
import json

__author__ = 'altug'

class GetTrainingPhotos:

    def __init__(self, objId):
        try:
            self.connection = httplib.HTTPSConnection("api.parse.com", 80)
            self.connection.connect()

            self.connection.request('POST', '/1/classes/Results?%s' % self.locationParam, json.dumps({
            "result": "1234"
            }), {
                "X-Parse-Application-Id": "HgrrtDO2dnazkQCPY59MR82ERhiamS5b1LTXBit8",
                "X-Parse-REST-API-Key": "hKSwFIi8Y6CrijPpXUABQSrLj5TMVekMwqk2I98I",
                "Content-Type": "application/json"
            })
        except:
            print 'RESULT BASAMADIM !!!!!!'