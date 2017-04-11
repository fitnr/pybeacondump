import unittest, unittest.mock, json
from . import dump

Records = dict(
    F1 = '''{"Key":"1","Fields":{},"WktGeometry":"MULTIPOINT ((1408409.02 265911.91))","TipHtml":"Address = 160 VILLA DR\\r\\n\\u003cbr\\u003e\\r\\nBLDING_SUI =  \\r\\n\\u003cbr\\u003e\\r\\nCITY_LIMIT = TANEY COUNTY\\r\\n\\u003cbr\\u003e\\r\\nCOMMUNITY = HOLLISTER\\r\\n\\u003cbr\\u003e\\r\\ncreated_date = \\r\\n\\u003cbr\\u003e\\r\\ncreated_user = \\r\\n\\u003cbr\\u003e\\r\\nDATAFILE = A053003.ssf\\r\\n\\u003cbr\\u003e\\r\\nEASTING = 1408483.1000000001\\r\\n\\u003cbr\\u003e\\r\\nEmail_Dist = \\r\\n\\u003cbr\\u003e\\r\\nESN = 12_166\\r\\n\\u003cbr\\u003e\\r\\nFEAT_NAME = Address_\\r\\n\\u003cbr\\u003e\\r\\nGPS_DATE = 1054252800000\\r\\n\\u003cbr\\u003e\\r\\nGPS_HEIGHT = 0\\r\\n\\u003cbr\\u003e\\r\\nGPS_TIME = 01:55:53pm\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_date = 1490699094000\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_user = ISGIS\\r\\n\\u003cbr\\u003e\\r\\nLat = 36.561191497240003\\r\\n\\u003cbr\\u003e\\r\\nLong = -93.289987614449998\\r\\n\\u003cbr\\u003e\\r\\nNORTHING = 265915.70400000003\\r\\n\\u003cbr\\u003e\\r\\nNOTES =  \\r\\n\\u003cbr\\u003e\\r\\nNotes_2 = \\r\\n\\u003cbr\\u003e\\r\\nPoints_ID = 1\\r\\n\\u003cbr\\u003e\\r\\nPROPERTY_N = \\r\\n\\u003cbr\\u003e\\r\\nSTATE = MO\\r\\n\\u003cbr\\u003e\\r\\nStatus = \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DI2 =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DIR =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_NAM = VILLA\\r\\n\\u003cbr\\u003e\\r\\nSTREET_NUM = 160\\r\\n\\u003cbr\\u003e\\r\\nSTREET_SUF = DR\\r\\n\\u003cbr\\u003e\\r\\nUNIT_OR_LO = 2\\r\\n\\u003cbr\\u003e\\r\\nZIP_CODE = 65672\\r\\n\\u003cbr\\u003e\\r\\n","ResultHtml":"Address = 160 VILLA DR\\r\\n\\u003cbr\\u003e\\r\\nBLDING_SUI =  \\r\\n\\u003cbr\\u003e\\r\\nCITY_LIMIT = TANEY COUNTY\\r\\n\\u003cbr\\u003e\\r\\nCOMMUNITY = HOLLISTER\\r\\n\\u003cbr\\u003e\\r\\ncreated_date = \\r\\n\\u003cbr\\u003e\\r\\ncreated_user = \\r\\n\\u003cbr\\u003e\\r\\nDATAFILE = A053003.ssf\\r\\n\\u003cbr\\u003e\\r\\nEASTING = 1408483.1000000001\\r\\n\\u003cbr\\u003e\\r\\nEmail_Dist = \\r\\n\\u003cbr\\u003e\\r\\nESN = 12_166\\r\\n\\u003cbr\\u003e\\r\\nFEAT_NAME = Address_\\r\\n\\u003cbr\\u003e\\r\\nGPS_DATE = 1054252800000\\r\\n\\u003cbr\\u003e\\r\\nGPS_HEIGHT = 0\\r\\n\\u003cbr\\u003e\\r\\nGPS_TIME = 01:55:53pm\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_date = 1490699094000\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_user = ISGIS\\r\\n\\u003cbr\\u003e\\r\\nLat = 36.561191497240003\\r\\n\\u003cbr\\u003e\\r\\nLong = -93.289987614449998\\r\\n\\u003cbr\\u003e\\r\\nNORTHING = 265915.70400000003\\r\\n\\u003cbr\\u003e\\r\\nNOTES =  \\r\\n\\u003cbr\\u003e\\r\\nNotes_2 = \\r\\n\\u003cbr\\u003e\\r\\nPoints_ID = 1\\r\\n\\u003cbr\\u003e\\r\\nPROPERTY_N = \\r\\n\\u003cbr\\u003e\\r\\nSTATE = MO\\r\\n\\u003cbr\\u003e\\r\\nStatus = \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DI2 =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DIR =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_NAM = VILLA\\r\\n\\u003cbr\\u003e\\r\\nSTREET_NUM = 160\\r\\n\\u003cbr\\u003e\\r\\nSTREET_SUF = DR\\r\\n\\u003cbr\\u003e\\r\\nUNIT_OR_LO = 2\\r\\n\\u003cbr\\u003e\\r\\nZIP_CODE = 65672\\r\\n\\u003cbr\\u003e\\r\\n","ParentId":null,"ChildIds":null}''',
    F2 = '''{"Key":"2","Fields":{},"WktGeometry":"MULTIPOINT ((1408481.6 265803.22))","TipHtml":"Address = 178 VILLA DR\\r\\n\\u003cbr\\u003e\\r\\nBLDING_SUI =  \\r\\n\\u003cbr\\u003e\\r\\nCITY_LIMIT = TANEY COUNTY\\r\\n\\u003cbr\\u003e\\r\\nCOMMUNITY = HOLLISTER\\r\\n\\u003cbr\\u003e\\r\\ncreated_date = \\r\\n\\u003cbr\\u003e\\r\\ncreated_user = \\r\\n\\u003cbr\\u003e\\r\\nDATAFILE = A053003.ssf\\r\\n\\u003cbr\\u003e\\r\\nEASTING = 1408554.861\\r\\n\\u003cbr\\u003e\\r\\nEmail_Dist = \\r\\n\\u003cbr\\u003e\\r\\nESN = 12_166\\r\\n\\u003cbr\\u003e\\r\\nFEAT_NAME = Address_\\r\\n\\u003cbr\\u003e\\r\\nGPS_DATE = 1054252800000\\r\\n\\u003cbr\\u003e\\r\\nGPS_HEIGHT = 0\\r\\n\\u003cbr\\u003e\\r\\nGPS_TIME = 01:56:10pm\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_date = 1490699094000\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_user = ISGIS\\r\\n\\u003cbr\\u003e\\r\\nLat = 36.560894620340001\\r\\n\\u003cbr\\u003e\\r\\nLong = -93.289737463319995\\r\\n\\u003cbr\\u003e\\r\\nNORTHING = 265782.38500000001\\r\\n\\u003cbr\\u003e\\r\\nNOTES =  \\r\\n\\u003cbr\\u003e\\r\\nNotes_2 = \\r\\n\\u003cbr\\u003e\\r\\nPoints_ID = 2\\r\\n\\u003cbr\\u003e\\r\\nPROPERTY_N = \\r\\n\\u003cbr\\u003e\\r\\nSTATE = MO\\r\\n\\u003cbr\\u003e\\r\\nStatus = \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DI2 =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DIR =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_NAM = VILLA\\r\\n\\u003cbr\\u003e\\r\\nSTREET_NUM = 178\\r\\n\\u003cbr\\u003e\\r\\nSTREET_SUF = DR\\r\\n\\u003cbr\\u003e\\r\\nUNIT_OR_LO = 4\\r\\n\\u003cbr\\u003e\\r\\nZIP_CODE = 65672\\r\\n\\u003cbr\\u003e\\r\\n","ResultHtml":"Address = 178 VILLA DR\\r\\n\\u003cbr\\u003e\\r\\nBLDING_SUI =  \\r\\n\\u003cbr\\u003e\\r\\nCITY_LIMIT = TANEY COUNTY\\r\\n\\u003cbr\\u003e\\r\\nCOMMUNITY = HOLLISTER\\r\\n\\u003cbr\\u003e\\r\\ncreated_date = \\r\\n\\u003cbr\\u003e\\r\\ncreated_user = \\r\\n\\u003cbr\\u003e\\r\\nDATAFILE = A053003.ssf\\r\\n\\u003cbr\\u003e\\r\\nEASTING = 1408554.861\\r\\n\\u003cbr\\u003e\\r\\nEmail_Dist = \\r\\n\\u003cbr\\u003e\\r\\nESN = 12_166\\r\\n\\u003cbr\\u003e\\r\\nFEAT_NAME = Address_\\r\\n\\u003cbr\\u003e\\r\\nGPS_DATE = 1054252800000\\r\\n\\u003cbr\\u003e\\r\\nGPS_HEIGHT = 0\\r\\n\\u003cbr\\u003e\\r\\nGPS_TIME = 01:56:10pm\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_date = 1490699094000\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_user = ISGIS\\r\\n\\u003cbr\\u003e\\r\\nLat = 36.560894620340001\\r\\n\\u003cbr\\u003e\\r\\nLong = -93.289737463319995\\r\\n\\u003cbr\\u003e\\r\\nNORTHING = 265782.38500000001\\r\\n\\u003cbr\\u003e\\r\\nNOTES =  \\r\\n\\u003cbr\\u003e\\r\\nNotes_2 = \\r\\n\\u003cbr\\u003e\\r\\nPoints_ID = 2\\r\\n\\u003cbr\\u003e\\r\\nPROPERTY_N = \\r\\n\\u003cbr\\u003e\\r\\nSTATE = MO\\r\\n\\u003cbr\\u003e\\r\\nStatus = \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DI2 =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DIR =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_NAM = VILLA\\r\\n\\u003cbr\\u003e\\r\\nSTREET_NUM = 178\\r\\n\\u003cbr\\u003e\\r\\nSTREET_SUF = DR\\r\\n\\u003cbr\\u003e\\r\\nUNIT_OR_LO = 4\\r\\n\\u003cbr\\u003e\\r\\nZIP_CODE = 65672\\r\\n\\u003cbr\\u003e\\r\\n","ParentId":null,"ChildIds":null}''',
    F3 = '''{"Key":"3","Fields":{},"WktGeometry":"MULTIPOINT ((1408605.34 265645.73))","TipHtml":"Address = 200 VILLA DR\\r\\n\\u003cbr\\u003e\\r\\nBLDING_SUI =  \\r\\n\\u003cbr\\u003e\\r\\nCITY_LIMIT = TANEY COUNTY\\r\\n\\u003cbr\\u003e\\r\\nCOMMUNITY = HOLLISTER\\r\\n\\u003cbr\\u003e\\r\\ncreated_date = \\r\\n\\u003cbr\\u003e\\r\\ncreated_user = \\r\\n\\u003cbr\\u003e\\r\\nDATAFILE = A053003.ssf\\r\\n\\u003cbr\\u003e\\r\\nEASTING = 1408633.564\\r\\n\\u003cbr\\u003e\\r\\nEmail_Dist = \\r\\n\\u003cbr\\u003e\\r\\nESN = 12_166\\r\\n\\u003cbr\\u003e\\r\\nFEAT_NAME = Address_\\r\\n\\u003cbr\\u003e\\r\\nGPS_DATE = 1054252800000\\r\\n\\u003cbr\\u003e\\r\\nGPS_HEIGHT = 0\\r\\n\\u003cbr\\u003e\\r\\nGPS_TIME = 01:56:28pm\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_date = 1490699094000\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_user = ISGIS\\r\\n\\u003cbr\\u003e\\r\\nLat = 36.560464849970003\\r\\n\\u003cbr\\u003e\\r\\nLong = -93.289311785600006\\r\\n\\u003cbr\\u003e\\r\\nNORTHING = 265727.73100000003\\r\\n\\u003cbr\\u003e\\r\\nNOTES =  \\r\\n\\u003cbr\\u003e\\r\\nNotes_2 = \\r\\n\\u003cbr\\u003e\\r\\nPoints_ID = 3\\r\\n\\u003cbr\\u003e\\r\\nPROPERTY_N = \\r\\n\\u003cbr\\u003e\\r\\nSTATE = MO\\r\\n\\u003cbr\\u003e\\r\\nStatus = \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DI2 =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DIR =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_NAM = VILLA\\r\\n\\u003cbr\\u003e\\r\\nSTREET_NUM = 200\\r\\n\\u003cbr\\u003e\\r\\nSTREET_SUF = DR\\r\\n\\u003cbr\\u003e\\r\\nUNIT_OR_LO = 1\\r\\n\\u003cbr\\u003e\\r\\nZIP_CODE = 65672\\r\\n\\u003cbr\\u003e\\r\\n","ResultHtml":"Address = 200 VILLA DR\\r\\n\\u003cbr\\u003e\\r\\nBLDING_SUI =  \\r\\n\\u003cbr\\u003e\\r\\nCITY_LIMIT = TANEY COUNTY\\r\\n\\u003cbr\\u003e\\r\\nCOMMUNITY = HOLLISTER\\r\\n\\u003cbr\\u003e\\r\\ncreated_date = \\r\\n\\u003cbr\\u003e\\r\\ncreated_user = \\r\\n\\u003cbr\\u003e\\r\\nDATAFILE = A053003.ssf\\r\\n\\u003cbr\\u003e\\r\\nEASTING = 1408633.564\\r\\n\\u003cbr\\u003e\\r\\nEmail_Dist = \\r\\n\\u003cbr\\u003e\\r\\nESN = 12_166\\r\\n\\u003cbr\\u003e\\r\\nFEAT_NAME = Address_\\r\\n\\u003cbr\\u003e\\r\\nGPS_DATE = 1054252800000\\r\\n\\u003cbr\\u003e\\r\\nGPS_HEIGHT = 0\\r\\n\\u003cbr\\u003e\\r\\nGPS_TIME = 01:56:28pm\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_date = 1490699094000\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_user = ISGIS\\r\\n\\u003cbr\\u003e\\r\\nLat = 36.560464849970003\\r\\n\\u003cbr\\u003e\\r\\nLong = -93.289311785600006\\r\\n\\u003cbr\\u003e\\r\\nNORTHING = 265727.73100000003\\r\\n\\u003cbr\\u003e\\r\\nNOTES =  \\r\\n\\u003cbr\\u003e\\r\\nNotes_2 = \\r\\n\\u003cbr\\u003e\\r\\nPoints_ID = 3\\r\\n\\u003cbr\\u003e\\r\\nPROPERTY_N = \\r\\n\\u003cbr\\u003e\\r\\nSTATE = MO\\r\\n\\u003cbr\\u003e\\r\\nStatus = \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DI2 =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DIR =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_NAM = VILLA\\r\\n\\u003cbr\\u003e\\r\\nSTREET_NUM = 200\\r\\n\\u003cbr\\u003e\\r\\nSTREET_SUF = DR\\r\\n\\u003cbr\\u003e\\r\\nUNIT_OR_LO = 1\\r\\n\\u003cbr\\u003e\\r\\nZIP_CODE = 65672\\r\\n\\u003cbr\\u003e\\r\\n","ParentId":null,"ChildIds":null}''',
    F4 = '''{"Key":"4","Fields":{},"WktGeometry":"MULTIPOINT ((1408616.28 265851.91))","TipHtml":"Address = 179 VILLA DR\\r\\n\\u003cbr\\u003e\\r\\nBLDING_SUI =  \\r\\n\\u003cbr\\u003e\\r\\nCITY_LIMIT = TANEY COUNTY\\r\\n\\u003cbr\\u003e\\r\\nCOMMUNITY = HOLLISTER\\r\\n\\u003cbr\\u003e\\r\\ncreated_date = \\r\\n\\u003cbr\\u003e\\r\\ncreated_user = \\r\\n\\u003cbr\\u003e\\r\\nDATAFILE = A053003.ssf\\r\\n\\u003cbr\\u003e\\r\\nEASTING = 1408571.247\\r\\n\\u003cbr\\u003e\\r\\nEmail_Dist = \\r\\n\\u003cbr\\u003e\\r\\nESN = 12_166\\r\\n\\u003cbr\\u003e\\r\\nFEAT_NAME = Address_\\r\\n\\u003cbr\\u003e\\r\\nGPS_DATE = 1054252800000\\r\\n\\u003cbr\\u003e\\r\\nGPS_HEIGHT = 0\\r\\n\\u003cbr\\u003e\\r\\nGPS_TIME = 01:56:42pm\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_date = 1490699094000\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_user = ISGIS\\r\\n\\u003cbr\\u003e\\r\\nLat = 36.56103139348\\r\\n\\u003cbr\\u003e\\r\\nLong = -93.289280288819995\\r\\n\\u003cbr\\u003e\\r\\nNORTHING = 265777.30800000002\\r\\n\\u003cbr\\u003e\\r\\nNOTES =  \\r\\n\\u003cbr\\u003e\\r\\nNotes_2 = \\r\\n\\u003cbr\\u003e\\r\\nPoints_ID = 4\\r\\n\\u003cbr\\u003e\\r\\nPROPERTY_N = \\r\\n\\u003cbr\\u003e\\r\\nSTATE = MO\\r\\n\\u003cbr\\u003e\\r\\nStatus = \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DI2 =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DIR =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_NAM = VILLA\\r\\n\\u003cbr\\u003e\\r\\nSTREET_NUM = 179\\r\\n\\u003cbr\\u003e\\r\\nSTREET_SUF = DR\\r\\n\\u003cbr\\u003e\\r\\nUNIT_OR_LO = 2\\r\\n\\u003cbr\\u003e\\r\\nZIP_CODE = 65672\\r\\n\\u003cbr\\u003e\\r\\n","ResultHtml":"Address = 179 VILLA DR\\r\\n\\u003cbr\\u003e\\r\\nBLDING_SUI =  \\r\\n\\u003cbr\\u003e\\r\\nCITY_LIMIT = TANEY COUNTY\\r\\n\\u003cbr\\u003e\\r\\nCOMMUNITY = HOLLISTER\\r\\n\\u003cbr\\u003e\\r\\ncreated_date = \\r\\n\\u003cbr\\u003e\\r\\ncreated_user = \\r\\n\\u003cbr\\u003e\\r\\nDATAFILE = A053003.ssf\\r\\n\\u003cbr\\u003e\\r\\nEASTING = 1408571.247\\r\\n\\u003cbr\\u003e\\r\\nEmail_Dist = \\r\\n\\u003cbr\\u003e\\r\\nESN = 12_166\\r\\n\\u003cbr\\u003e\\r\\nFEAT_NAME = Address_\\r\\n\\u003cbr\\u003e\\r\\nGPS_DATE = 1054252800000\\r\\n\\u003cbr\\u003e\\r\\nGPS_HEIGHT = 0\\r\\n\\u003cbr\\u003e\\r\\nGPS_TIME = 01:56:42pm\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_date = 1490699094000\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_user = ISGIS\\r\\n\\u003cbr\\u003e\\r\\nLat = 36.56103139348\\r\\n\\u003cbr\\u003e\\r\\nLong = -93.289280288819995\\r\\n\\u003cbr\\u003e\\r\\nNORTHING = 265777.30800000002\\r\\n\\u003cbr\\u003e\\r\\nNOTES =  \\r\\n\\u003cbr\\u003e\\r\\nNotes_2 = \\r\\n\\u003cbr\\u003e\\r\\nPoints_ID = 4\\r\\n\\u003cbr\\u003e\\r\\nPROPERTY_N = \\r\\n\\u003cbr\\u003e\\r\\nSTATE = MO\\r\\n\\u003cbr\\u003e\\r\\nStatus = \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DI2 =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DIR =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_NAM = VILLA\\r\\n\\u003cbr\\u003e\\r\\nSTREET_NUM = 179\\r\\n\\u003cbr\\u003e\\r\\nSTREET_SUF = DR\\r\\n\\u003cbr\\u003e\\r\\nUNIT_OR_LO = 2\\r\\n\\u003cbr\\u003e\\r\\nZIP_CODE = 65672\\r\\n\\u003cbr\\u003e\\r\\n","ParentId":null,"ChildIds":null}''',
    )

class TestDump (unittest.TestCase):
    
    def test_get_connection(self):
        '''
        '''
        with unittest.mock.patch('http.client.HTTPSConnection') as HTTPSConnection:
            conn, path = dump.get_connection('https://beacon.schneidercorp.com/api/beaconCore/GetVectorLayer?QPS=xxxx')

        HTTPSConnection.assert_called_once_with('beacon.schneidercorp.com')
        self.assertIs(conn, HTTPSConnection.return_value)
        self.assertEqual(path, '/api/beaconCore/GetVectorLayer?QPS=xxxx')
    
    def test_get_starting_bbox(self):
        '''
        '''
        conn, path = unittest.mock.Mock(), '/api/beaconCore/GetVectorLayer?QPS=xxxx'
        
        conn.getresponse.return_value.status = 200
        conn.getresponse.return_value.read.return_value = '''{"d":[{"Key":"1","Fields":{},"WktGeometry":"MULTIPOINT ((1408409 265912))","TipHtml":"Address = 160 VILLA DR\\r\\n\\u003cbr\\u003e\\r\\nBLDING_SUI =  \\r\\n\\u003cbr\\u003e\\r\\nCITY_LIMIT = TANEY COUNTY\\r\\n\\u003cbr\\u003e\\r\\nCOMMUNITY = HOLLISTER\\r\\n\\u003cbr\\u003e\\r\\ncreated_date = \\r\\n\\u003cbr\\u003e\\r\\ncreated_user = \\r\\n\\u003cbr\\u003e\\r\\nDATAFILE = A053003.ssf\\r\\n\\u003cbr\\u003e\\r\\nEASTING = 1408483.1000000001\\r\\n\\u003cbr\\u003e\\r\\nEmail_Dist = \\r\\n\\u003cbr\\u003e\\r\\nESN = 12_166\\r\\n\\u003cbr\\u003e\\r\\nFEAT_NAME = Address_\\r\\n\\u003cbr\\u003e\\r\\nGPS_DATE = 1054252800000\\r\\n\\u003cbr\\u003e\\r\\nGPS_HEIGHT = 0\\r\\n\\u003cbr\\u003e\\r\\nGPS_TIME = 01:55:53pm\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_date = 1490699094000\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_user = ISGIS\\r\\n\\u003cbr\\u003e\\r\\nLat = 36.561191497240003\\r\\n\\u003cbr\\u003e\\r\\nLong = -93.289987614449998\\r\\n\\u003cbr\\u003e\\r\\nNORTHING = 265915.70400000003\\r\\n\\u003cbr\\u003e\\r\\nNOTES =  \\r\\n\\u003cbr\\u003e\\r\\nNotes_2 = \\r\\n\\u003cbr\\u003e\\r\\nPoints_ID = 1\\r\\n\\u003cbr\\u003e\\r\\nPROPERTY_N = \\r\\n\\u003cbr\\u003e\\r\\nSTATE = MO\\r\\n\\u003cbr\\u003e\\r\\nStatus = \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DI2 =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DIR =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_NAM = VILLA\\r\\n\\u003cbr\\u003e\\r\\nSTREET_NUM = 160\\r\\n\\u003cbr\\u003e\\r\\nSTREET_SUF = DR\\r\\n\\u003cbr\\u003e\\r\\nUNIT_OR_LO = 2\\r\\n\\u003cbr\\u003e\\r\\nZIP_CODE = 65672\\r\\n\\u003cbr\\u003e\\r\\n","ResultHtml":"Address = 160 VILLA DR\\r\\n\\u003cbr\\u003e\\r\\nBLDING_SUI =  \\r\\n\\u003cbr\\u003e\\r\\nCITY_LIMIT = TANEY COUNTY\\r\\n\\u003cbr\\u003e\\r\\nCOMMUNITY = HOLLISTER\\r\\n\\u003cbr\\u003e\\r\\ncreated_date = \\r\\n\\u003cbr\\u003e\\r\\ncreated_user = \\r\\n\\u003cbr\\u003e\\r\\nDATAFILE = A053003.ssf\\r\\n\\u003cbr\\u003e\\r\\nEASTING = 1408483.1000000001\\r\\n\\u003cbr\\u003e\\r\\nEmail_Dist = \\r\\n\\u003cbr\\u003e\\r\\nESN = 12_166\\r\\n\\u003cbr\\u003e\\r\\nFEAT_NAME = Address_\\r\\n\\u003cbr\\u003e\\r\\nGPS_DATE = 1054252800000\\r\\n\\u003cbr\\u003e\\r\\nGPS_HEIGHT = 0\\r\\n\\u003cbr\\u003e\\r\\nGPS_TIME = 01:55:53pm\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_date = 1490699094000\\r\\n\\u003cbr\\u003e\\r\\nlast_edited_user = ISGIS\\r\\n\\u003cbr\\u003e\\r\\nLat = 36.561191497240003\\r\\n\\u003cbr\\u003e\\r\\nLong = -93.289987614449998\\r\\n\\u003cbr\\u003e\\r\\nNORTHING = 265915.70400000003\\r\\n\\u003cbr\\u003e\\r\\nNOTES =  \\r\\n\\u003cbr\\u003e\\r\\nNotes_2 = \\r\\n\\u003cbr\\u003e\\r\\nPoints_ID = 1\\r\\n\\u003cbr\\u003e\\r\\nPROPERTY_N = \\r\\n\\u003cbr\\u003e\\r\\nSTATE = MO\\r\\n\\u003cbr\\u003e\\r\\nStatus = \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DI2 =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_DIR =  \\r\\n\\u003cbr\\u003e\\r\\nSTREET_NAM = VILLA\\r\\n\\u003cbr\\u003e\\r\\nSTREET_NUM = 160\\r\\n\\u003cbr\\u003e\\r\\nSTREET_SUF = DR\\r\\n\\u003cbr\\u003e\\r\\nUNIT_OR_LO = 2\\r\\n\\u003cbr\\u003e\\r\\nZIP_CODE = 65672\\r\\n\\u003cbr\\u003e\\r\\n","ParentId":null,"ChildIds":null}]}'''

        bbox = dump.get_starting_bbox(conn, path, 13494, 100)
        args, kwargs = conn.request.mock_calls[-1][1:]

        self.assertEqual(args, ('POST', ))
        self.assertEqual(kwargs['url'], path)
        self.assertIn('"layerId": 13494', kwargs['body'])
        self.assertEqual(bbox, (1308409, 165912, 1508409, 365912))
    
    def test_partition_bbox(self):
        '''
        '''
        boxes = dump.partition_bbox(0, 1, 2, 3)
        self.assertEqual(boxes, [(0, 1, 1, 2), (0, 2, 1, 3), (1, 1, 2, 2), (1, 2, 2, 3)])
    
    def test_recursively_descend1(self):
        '''
        '''
        conn = unittest.mock.Mock()
        path = '/api/beaconCore/GetVectorLayer?QPS=xxxx'
        bbox = (1308409, 165912, 1508409, 365912)
        bboxes = [bbox] + dump.partition_bbox(*bbox)
        
        conn.getresponse.return_value.status = 200
        responses = [
            # top-level has all four records
            '''{{"d":[{F1},{F2},{F3},{F4}]}}'''.format(**Records),
            
            # first two recursed boxes have no records
            '''{"d":[]}''',
            '''{"d":[]}''',
            
            # third recursed box has three records
            '''{{"d":[{F1},{F2},{F3}]}}'''.format(**Records),
            
            # fourth recursed box has last record
            '''{{"d":[{F4}]}}'''.format(**Records),
            ]
        conn.getresponse.return_value.read.side_effect = lambda: responses.pop(0)

        records = dump.recursively_descend(conn, path, 13494, bbox)
        keys = {f.get('Key') for f in records}

        self.assertEqual(keys, {'1', '2', '3', '4'})
        self.assertEqual(len(records), 4)
        self.assertEqual(len(conn.request.mock_calls), 5)
        
        for (_bbox, (_, args, kwargs)) in zip(bboxes, conn.request.mock_calls):
            body = json.loads(kwargs['body'])

            self.assertEqual(args, ('POST', ))
            self.assertEqual(kwargs['url'], path)
            self.assertEqual(body['layerId'], 13494)
            self.assertIn(body['featureLimit'], (0, 4))
            self.assertEqual(body['ext'], {
                'minx': _bbox[0], 'miny': _bbox[1], 'maxx': _bbox[2], 'maxy': _bbox[3]
                })
    
    def test_recursively_descend2(self):
        '''
        '''
        conn = unittest.mock.Mock()
        path = '/api/beaconCore/GetVectorLayer?QPS=xxxx'
        bbox = (1308409, 165912, 1508409, 365912)
        
        # splice in a level of recursion at the third sub-bbox
        bboxes_ = [bbox] + dump.partition_bbox(*bbox)
        bboxes = bboxes_[:4] + dump.partition_bbox(*bboxes_[3]) + bboxes_[4:]
        
        conn.getresponse.return_value.status = 200
        responses = [
            # top-level has limit three records
            '''{{"d":[{F1},{F2},{F3}]}}'''.format(**Records),
            
            # first two recursed boxes have no records
            '''{"d":[]}''',
            '''{"d":[]}''',
            
            # third recursed box has limit three records
            '''{{"d":[{F1},{F2},{F3}]}}'''.format(**Records),
            
                # first two re-recursed boxes have no records
                '''{"d":[]}''',
                '''{"d":[]}''',
            
                # third re-recursed box has first two records
                '''{{"d":[{F1},{F2}]}}'''.format(**Records),
            
                # fourth re-recursed box has last two records
                '''{{"d":[{F3},{F4}]}}'''.format(**Records),
            
            # fourth recursed box has no records
            '''{"d":[]}''',
            ]
        conn.getresponse.return_value.read.side_effect = lambda: responses.pop(0)

        records = dump.recursively_descend(conn, path, 13494, bbox)
        keys = {f.get('Key') for f in records}

        self.assertEqual(keys, {'1', '2', '3', '4'})
        self.assertEqual(len(records), 4)
        self.assertEqual(len(conn.request.mock_calls), 9)
        
        for (_bbox, (_, args, kwargs)) in zip(bboxes, conn.request.mock_calls):
            body = json.loads(kwargs['body'])

            self.assertEqual(args, ('POST', ))
            self.assertEqual(kwargs['url'], path)
            self.assertEqual(body['layerId'], 13494)
            self.assertIn(body['featureLimit'], (0, 3))
            self.assertEqual(body['ext'], {
                'minx': _bbox[0], 'miny': _bbox[1], 'maxx': _bbox[2], 'maxy': _bbox[3]
                })

    def test_extract_properties(self):
        '''
        '''
        properties = dump.extract_properties(json.loads(Records['F1']))

        self.assertEqual(properties, {
            'Address': '160 VILLA DR', 'BLDING_SUI': ' ', 'CITY_LIMIT': 'TANEY COUNTY',
            'COMMUNITY': 'HOLLISTER', 'created_date': '', 'created_user': '',
            'DATAFILE': 'A053003.ssf', 'EASTING': '1408483.1000000001',
            'Email_Dist': '', 'ESN': '12_166', 'FEAT_NAME': 'Address_',
            'GPS_DATE': '1054252800000', 'GPS_HEIGHT': '0', 'GPS_TIME': '01:55:53pm',
            'last_edited_date': '1490699094000', 'last_edited_user': 'ISGIS',
            'Lat': '36.561191497240003', 'Long': '-93.289987614449998',
            'NORTHING': '265915.70400000003', 'NOTES': ' ', 'Notes_2': '',
            'Points_ID': '1', 'PROPERTY_N': '', 'STATE': 'MO', 'Status': '',
            'STREET_DI2': ' ', 'STREET_DIR': ' ', 'STREET_NAM': 'VILLA',
            'STREET_NUM': '160', 'STREET_SUF': 'DR', 'UNIT_OR_LO': '2',
            'ZIP_CODE': '65672'})

    def test_extract_geometry(self):
        '''
        '''
        geom1 = dump.extract_geometry(json.loads(Records['F1']))
        geom2 = dump.extract_geometry(json.loads(Records['F2']))
        geom3 = dump.extract_geometry(json.loads(Records['F3']))
        geom4 = dump.extract_geometry(json.loads(Records['F4']))

        self.assertEqual(geom1, {'type': 'Point',
            'coordinates': [-93.289987614449998, 36.561191497240003]})
        self.assertEqual(geom2, {'type': 'Point',
            'coordinates': [-93.289737463319995, 36.560894620340001]})
        self.assertEqual(geom3, {'type': 'Point',
            'coordinates': [-93.289311785600006, 36.560464849970003]})
        self.assertEqual(geom4, {'type': 'Point',
            'coordinates': [-93.289280288819995, 36.56103139348]})
        
if __name__ == '__main__':
    unittest.main()