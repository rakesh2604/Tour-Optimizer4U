from math import radians, sin, cos, sqrt, atan2
from collections import namedtuple

Place = namedtuple("Place", ["name", "lat", "lon"])

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    return 2 * R * atan2(sqrt(a), sqrt(1 - a))

def compute_distance_matrix(places):
    n = len(places)
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist[i][j] = haversine(places[i].lat, places[i].lon, places[j].lat, places[j].lon)
    return dist
