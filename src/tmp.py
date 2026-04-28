import requests
import numpy as np
from pathlib import Path
import osmnx as ox
from shapely.geometry import Point

lat, lng = ox.geocode("Restaurant Vækst, Copenhagen")
geometry = Point(lat, lng)
gdf = ox.features_from_point(
    (lat, lng),
    tags={
        'name': 'Vækst'
    },
    dist=50
)
for thing in gdf:
    print(gdf[thing])