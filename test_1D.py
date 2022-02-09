from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river


def test_rivers_with_station(): 
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    assert len(rivers) >= 843

def test_stations_by_river():
    stations = build_station_list()
    stats = stations_by_river(stations)
    stats1= stats['River Aire']
    for i in range(len(stats1)):
        stats1[i] = stats1[i].name
    assert 'Bingley' in stats1
