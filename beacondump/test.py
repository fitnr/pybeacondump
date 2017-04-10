import unittest, unittest.mock
from . import dump

class DumpTest (unittest.TestCase):
    
    def test_dump(self):
        '''
        '''
        with unittest.mock.patch('http.client.HTTPSConnection') as HTTPSConnection:
            conn, path = dump.get_connection('https://beacon.schneidercorp.com/api/beaconCore/GetVectorLayer?QPS=xxxx')

        HTTPSConnection.assert_called_once_with('beacon.schneidercorp.com')
        self.assertIs(conn, HTTPSConnection.return_value)
        self.assertEqual(path, '/api/beaconCore/GetVectorLayer?QPS=xxxx')
        
        conn.getresponse.return_value.status = 200
        conn.getresponse.return_value.read.return_value = '''{"d":[{"Key":"1","Fields":{},"WktGeometry":"MULTIPOINT ((1408409 265912))","TipHtml":"Address = 160 VILLA DR\\r\\n\\u003cbr\\u003e\\r\\nBLDING_SUI =  \\r\\n\\u003cbr\\u003e\\r\\nCITY_LIMIT = TANEY COUNTY\\r\\n\\u003cbr\\u003e\\r\\nCOMMUNITY = HOLLISTER\\r\\n\\u003cbr\\u003e\\r\\ncreated_date = \\r\\n\\u003cbr\\u003e\\r\\ncreated_user = \\r\\n\\u003cbr\\u003e\\r\\nDATAFILE = A053003.ssf\\r\\n\\u003cbr\\u003e\\r\\nEASTING = 1408483.1000000001\\r\\n\\u003cbr\\u003e\\r\\nEmail_Dist = \\r\\n\\u003cbr\\u003e\\r\\nESN = 12_166\\r\\n\\u003cbr\\u003e\\r\\nFEAT_NAME = Address_\\r\\n\\u003cbr\\u003e\\r\\nGPS_DATE = 1054252800000\\r\\n\\u003cbr\\u003e\\r\\nGPS_HEIGHT = 0\\r\\n\\u003cbr\\u003e\\r\\nGPS_TIME = 01:55:53pm\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_date = 1490699094000\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_user = ISGIS\\r\\n\\u003cbr\\u003e\\r\\nLat = 36.561191497240003\\r\\n\\u003cbr\\u003e\\r\\nLong = -93.289987614449998\\r\\n\\u003cbr\\u003e\\r\\nNORTHING = 265915.70400000003\\r\\n\\u003cbr\\u003e\\r\\nNOTES =  \\r\\n\\u003cbr\\u003e\\r\\nNotes_2 = \\r\\n\\u003cbr\\u003e\\r\\nPoints_ID = 1\\r\\n\\u003cbr\\u003e\\r\\nPROPERTY_N = \\r\\n\\u003cbr\\u003e\\r\\nSTATE = MO\\r\\n\\u003cbr\\u003e\\r\\nStatus = \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DI2 =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DIR =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_NAM = VILLA\\r\\n\\u003cbr\\u003e\\r\\nSTREET_NUM = 160\\r\\n\\u003cbr\\u003e\\r\\nSTREET_SUF = DR\\r\\n\\u003cbr\\u003e\\r\\nUNIT_OR_LO = 2\\r\\n\\u003cbr\\u003e\\r\\nZIP_CODE = 65672\\r\\n\\u003cbr\\u003e\\r\\n","ResultHtml":"Address = 160 VILLA DR\\r\\n\\u003cbr\\u003e\\r\\nBLDING_SUI =  \\r\\n\\u003cbr\\u003e\\r\\nCITY_LIMIT = TANEY COUNTY\\r\\n\\u003cbr\\u003e\\r\\nCOMMUNITY = HOLLISTER\\r\\n\\u003cbr\\u003e\\r\\ncreated_date = \\r\\n\\u003cbr\\u003e\\r\\ncreated_user = \\r\\n\\u003cbr\\u003e\\r\\nDATAFILE = A053003.ssf\\r\\n\\u003cbr\\u003e\\r\\nEASTING = 1408483.1000000001\\r\\n\\u003cbr\\u003e\\r\\nEmail_Dist = \\r\\n\\u003cbr\\u003e\\r\\nESN = 12_166\\r\\n\\u003cbr\\u003e\\r\\nFEAT_NAME = Address_\\r\\n\\u003cbr\\u003e\\r\\nGPS_DATE = 1054252800000\\r\\n\\u003cbr\\u003e\\r\\nGPS_HEIGHT = 0\\r\\n\\u003cbr\\u003e\\r\\nGPS_TIME = 01:55:53pm\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_date = 1490699094000\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_user = ISGIS\\r\\n\\u003cbr\\u003e\\r\\nLat = 36.561191497240003\\r\\n\\u003cbr\\u003e\\r\\nLong = -93.289987614449998\\r\\n\\u003cbr\\u003e\\r\\nNORTHING = 265915.70400000003\\r\\n\\u003cbr\\u003e\\r\\nNOTES =  \\r\\n\\u003cbr\\u003e\\r\\nNotes_2 = \\r\\n\\u003cbr\\u003e\\r\\nPoints_ID = 1\\r\\n\\u003cbr\\u003e\\r\\nPROPERTY_N = \\r\\n\\u003cbr\\u003e\\r\\nSTATE = MO\\r\\n\\u003cbr\\u003e\\r\\nStatus = \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DI2 =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DIR =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_NAM = VILLA\\r\\n\\u003cbr\\u003e\\r\\nSTREET_NUM = 160\\r\\n\\u003cbr\\u003e\\r\\nSTREET_SUF = DR\\r\\n\\u003cbr\\u003e\\r\\nUNIT_OR_LO = 2\\r\\n\\u003cbr\\u003e\\r\\nZIP_CODE = 65672\\r\\n\\u003cbr\\u003e\\r\\n","ParentId":null,"ChildIds":null}]}'''

        bbox = dump.get_starting_bbox(conn, path, 13494, 100)
        args, kwargs = conn.request.mock_calls[-1][1:]
        self.assertEqual(args, ('POST', ))
        self.assertEqual(kwargs['url'], path)
        self.assertIn('"layerId": 13494', kwargs['body'])
        self.assertEqual(bbox, (1308409, 165912, 1508409, 365912))
        
if __name__ == '__main__':
    unittest.main()