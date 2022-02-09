from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

"""Test for Task 1C"""
def test_stations_within_radius():
    stations=build_station_list()
    centre=[52.2053,0.1218]
    r = 10 #radius
    station_in_radius=stations_within_radius(stations,centre, r)
    assert station_in_radius==['Bin Brook', 'Cambridge Baits Bite', 'Cambridge Byron''s Pool', 'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton', 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']