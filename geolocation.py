from math import sin, cos, sqrt, atan2, radians


## Approximate radius of the earth in km
R = 6373.0

def latlong2dis(x1,x2):
    '''Given two coordinates returns the distance 
    between them'''
    lat1,lon1 = x1
    lat2,lon2 = x2

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a),sqrt(1-a))

    distance = R * c

    return distance
