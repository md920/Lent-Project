from floodsystem.stationdata import build_station_list, update_water_levels


def test_update_level():
    """Test update to latest water level"""

    stations = build_station_list()
    for station in stations:
        assert station.latest_level is None

    update_water_levels(stations)
    counter = 0
    for station in stations:
        if station.latest_level is not None:
            counter += 1

    assert counter > 0