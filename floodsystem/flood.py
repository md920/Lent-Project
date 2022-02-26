try:
    from .utils import sorted_by_key
except ImportError:
    from utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """Returns a list of stations which have a relative water level higher then a tolerence, returns nothing if there is a none type in the relative water level"""
    stations_over_limit = []
    for station in stations:
        try:
            if  station.relative_water_level() > tol:
                stations_over_limit.append((station.name,station.relative_water_level()))
        except:
            pass
    stations_over_limit.sort(key=lambda x: x[1], reverse=True)
    return stations_over_limit