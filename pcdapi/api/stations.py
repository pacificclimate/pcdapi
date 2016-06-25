'''module for requesting a list of stations
'''

def stations(sesh):
    '''Provides a list of all seasonal/monthly climo stations with metadata

    Args:
        sesh (sqlalchemy.orm.session.Session): A database Session object

    Returns:
        dictionary: Keyed to each station_id, values containing a dictionary
            with the lat/lon coordinates, name, network,
            native_id, start_date, end_date, and vars_available.

        For example:

        {
            '6656': {
                'name': 'Pine Pass',
                'network_name': 'MoTIe',
                'native_id': '35GJ34',
                'start_date': '2006-01-05 12:00:00',
                'end_date': '2016-01-05 12:00:00',
                'vars_available': ['pr', 'tas', 'tasmin', 'tasmax']
            },
            '6657': {
                [...]
            }
        }
    '''

    # Return some test data

    return {
        '6656': {
            'name': 'Some station 1',
            'network_name': 'MoTIe',
            'native_id': '35GJ34',
            'start_date': '2006-01-05 12:00:00',
            'end_date': '2016-01-05 12:00:00',
            'vars_available': ['pr', 'tas', 'tasmin', 'tasmax']
        },
        '6657': {
            'name': 'Some station 2',
            'network_name': 'EC',
            'native_id': '34GJSD4',
            'start_date': '2006-01-05 12:00:00',
            'end_date': '2016-01-05 12:00:00',
            'vars_available': ['pr', 'tas', 'tasmin', 'tasmax']
        }
    }
