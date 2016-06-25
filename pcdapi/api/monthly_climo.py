'''module for requesting monthly station climatologies
'''

from dateutil.parser import parse
from geojson import Feature, Point, FeatureCollection

def monthly_climo(sesh, date, variable):
    '''Provides monthly climatological values for all stations by date

    The `monthly_climo` call is intended to provide easy client side 
    mapping of monthly climatological values

    Args:
        d (string): ISO 8601 formatted datestring
        variable: Variable name ('pr', 'tas', etc)

    Returns:
        geojson.FeatureCollection: Each feature containing coordinate location
            of the station and the properties station_id, value, and units.

        For example:

        {
            'type': 'FeatureCollection',
            'features': [
                {
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [ 51.52, -110.54 ]
                    },
                    'properties': {
                        'id': '6656',
                        'value': 4.5,
                        'units': 'mm'
                    }
                }, {
                    [...]
                }
            ]
        }
    '''

    d = parse(date)

    # Return some test data

    fc = FeatureCollection([
        Feature(geometry=Point((51.52, -110.54)),
                properties={'id': 6656, 'value': 4.5, 'units': 'mm'}),
        Feature(geometry=Point((51.78, -109.37)),
                properties={'id': 6657, 'value': 4.5, 'units': 'mm'})
    ])

    return fc
