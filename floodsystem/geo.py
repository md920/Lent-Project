# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from os import stat

def stations_by_distance(stations,p):
    distance=[]
    for station in stations:
        distance.append((stat, haversine(station.coord, p),))
    result = sorted_by_key(distance, 1)
    return result