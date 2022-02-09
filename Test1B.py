from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():

     # Build list of stations
    stations = build_station_list()
    p=[52.2053, 0.1218]
    distance=stations_by_distance(stations,p)
    test_list=[]
    for i in range (len(distance)):
        x=(distance[i][0].name, distance[i][0].town, distance[i][1])
        test_list.append(x)

    assert test_list[0]==('Cambridge Jesus Lock', 'Cambridge', 0.8402364350834995)