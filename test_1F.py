from floodsystem.stationdata import build_station_list
from floodsystem.station import *


def test_inconsistent_typical_range_stations():
    # Build list of stations
    stations = build_station_list()
    inconsistent=inconsistent_typical_range_stations(stations)
    assert 'North America' in inconsistent