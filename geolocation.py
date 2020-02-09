from math import  radians
import geopy.distance


def latlong2dis(x1,x2):
    '''Given two coordinates returns the distance 
    between them'''
    x1 = [radians(x) for x in x1]
    x2 = [radians(x) for x in x2]

    
    return geopy.distance.geodesic(x1,x2).km