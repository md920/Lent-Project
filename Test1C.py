from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

"""Test for Task 1C"""
stations=build_station_list()
centre=[52.2053,0.1218]
r = 1 #radius
station_in_radius=stations_within_radius(stations,centre, r)
assert station_in_radius==['Cambridge Jesus Lock']