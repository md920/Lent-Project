from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

"""Test for Task 1B"""
def test_stations_by_distance():
    stations = build_station_list()
    p=[52.2053, 0.1218]
    distance=stations_by_distance(stations,p)
    test_list=[]
    for i in distance:
        x=(i[0].name,i[0].town, i[1])
        test_list.append(x)
        assert test_list[0]==('Cambridge Jesus Lock', 'Cambridge', 0.840237595667494)