import sys, json, copy
import bs4, re, collections
import http.client
import urllib.parse
import shapely.wkt

BEACON_HEADERS = {
    'Content-Type': 'application/json',
    'User-Agent': 'OA',
    }

BODY_TEMPLATE = {
    "layerId": None,
    "useSelection": False,
    "ext": {
        "minx": 0,
        "miny": 0,
        "maxx": 40000000,
        "maxy": 40000000
        },
    "wkt": None,
    "spatialRelation": 1,
    "featureLimit": 1
    }

def get_connection(raw_url):
    ''' Return an HTTPConnection and URL path for a starting Beacon URL.
    
        Expects a raw URL similar to:
        https://beacon.schneidercorp.com/api/beaconCore/GetVectorLayer?QPS=xxxx
    '''
    # Safari developer tools sneaks in some zero-width spaces:
    # http://www.fileformat.info/info/unicode/char/200B/index.htm
    url = raw_url.replace('\u200b', '')

    scheme, host, path, _, query, _ = urllib.parse.urlparse(url)
    layer_path = urllib.parse.urlunparse(('', '', path, None, query, None))
    
    if scheme == 'https':
        return http.client.HTTPSConnection(host), layer_path
    elif scheme == 'http':
        return http.client.HTTPConnection(host), layer_path

def get_starting_bbox(conn, layer_path, layer_id, radius_km=200):
    ''' Retrieves a bounding box tuple for a Beacon layer and radius in km.
    
        This is meant to be an overly-large, generous bbox that should
        encompass any reasonable county or city data source.
    '''
    body = copy.deepcopy(BODY_TEMPLATE)
    body['layerId'] = int(layer_id)
    
    conn.request(
        'POST', url=layer_path,
        body=json.dumps(body),
        headers=BEACON_HEADERS
        )
    
    resp = conn.getresponse()
    
    if resp.status not in range(200, 299):
        raise RuntimeError('Bad status in get_starting_bbox')
    
    results = json.load(resp)
    wkt = results.get('d', [{}])[0].get('WktGeometry', None)

    if not wkt:
        raise RuntimeError('Missing WktGeometry in get_starting_bbox')
    
    xmin, ymin, xmax, ymax = shapely.wkt.loads(wkt).buffer(radius_km*1000).bounds

    return xmin, ymin, xmax, ymax

def partition_bbox(xmin, ymin, xmax, ymax):
    '''
    '''
    xmid, ymid = xmin/2 + xmax/2, ymin/2 + ymax/2
    
    return [
        (xmin, ymin, xmid, ymid),
        (xmin, ymid, xmid, ymax),
        (xmid, ymin, xmax, ymid),
        (xmid, ymid, xmax, ymax),
        ]

def recursively_descend(conn, layer_path, layer_id, bbox, limit=0, depth=0):
    '''
    '''
    body = copy.deepcopy(BODY_TEMPLATE)
    body['layerId'], body['featureLimit'] = int(layer_id), limit
    body['ext'] = dict(minx=bbox[0], miny=bbox[1], maxx=bbox[2], maxy=bbox[3])
    
    conn.request(
        'POST', url=layer_path,
        body=json.dumps(body),
        headers=BEACON_HEADERS
        )
    
    resp = conn.getresponse()
    
    if resp.status not in range(200, 299):
        raise RuntimeError('Bad status in recursively_descend')

    features = json.load(resp).get('d', [])
    
    if limit == 0:
        # This is our first time through and we don't actually know how many
        # things there are. Assume that the current count is the limit.
        limit = len(features)

    if len(features) >= limit:
        # There are too many features, recurse!
        # This also happens the first time through before we know anything.
        bbox1, bbox2, bbox3, bbox4 = partition_bbox(*bbox)
        return recursively_descend(conn, layer_path, layer_id, bbox1, limit, depth+1) \
             + recursively_descend(conn, layer_path, layer_id, bbox2, limit, depth+1) \
             + recursively_descend(conn, layer_path, layer_id, bbox3, limit, depth+1) \
             + recursively_descend(conn, layer_path, layer_id, bbox4, limit, depth+1)

    # We are good.
    return features

def feature_properties(feature):
    '''
    '''
    properties = collections.OrderedDict()
    pattern = re.compile(r'^(\w+) = (.*)$', re.M)

    html1 = feature.get('TipHtml', '').replace('\r\n', '\n')
    html2 = feature.get('ResultHtml', '').replace('\r\n', '\n')

    soup1 = bs4.BeautifulSoup(html1, 'html.parser')
    soup2 = bs4.BeautifulSoup(html2, 'html.parser')
    
    for text in soup1.find_all(text=pattern):
        properties.update({k: v for (k, v) in pattern.findall(text)})
    
    for text in soup2.find_all(text=pattern):
        properties.update({k: v for (k, v) in pattern.findall(text)})
    
    return properties

def feature_geometry(feature):
    '''
    '''
    prop = feature_properties(feature)
    geom = dict(type='Point', coordinates=[float(prop['Long']), float(prop['Lat'])])
    
    return geom

if __name__ == '__main__':
    _, raw_url, layer_id = sys.argv
    
    conn, layer_path = get_connection(raw_url)
    bbox = get_starting_bbox(conn, layer_path, layer_id)
    print(bbox)
    
    features = recursively_descend(conn, layer_path, layer_id, bbox)
    with open('out.json', 'w') as file:
        json.dump(features, file, indent=2)
