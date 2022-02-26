from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import *

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import *

stations = build_station_list()
update_water_levels(stations)
risky_stations = stations_highest_rel_level(stations,10)
for station in risky_stations:
    print(station.name, station.relative_water_level())
