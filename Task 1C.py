from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

stations = build_station_list()
stats_within_10 = stations_within_radius(stations, (52.2053, 0.1218), 10)
names = []
for s in stats_within_10:
    names.append(s.name)
print(sorted(names))