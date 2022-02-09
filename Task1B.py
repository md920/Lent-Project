from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

stations = build_station_list()
stortedStations = stations_by_distance(stations, (52.2053, 0.1218))
newStats = []
for s in stortedStations:
    newStats.append((s[0].name, s[0].town, s[1]))

print("10 closest stations:")
print(newStats[:10])

print("\n 10 furthest stations:")
print(newStats[-10:])
