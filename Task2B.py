from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold



stations = build_station_list()
update_water_levels(stations)
stations_over_limit = stations_level_over_threshold(stations,0.8)
for station in stations_over_limit:
    print(station)
