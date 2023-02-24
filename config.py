'''Reverse Geocode Config'''

# Interactive mode. False=CLI positional args
# [ True | False ]
#-------------------------------------------------------------------------------
INTERACTIVE_MODE = True


# Geocoder engine.
# [ 'Nominatim' | 'Photon' ]
#-------------------------------------------------------------------------------
GEOCODER = 'Nominatim'


# Input latitude / longitude column name or position.
# [ (str) | (int) ]
#-------------------------------------------------------------------------------
LATITUDE = 'overallLAT'
LONGITUDE = 'overallLON'


# Delimiter to use.
# [ ',' | (str) ]
#-------------------------------------------------------------------------------
DELIMITER_INPUT = ','
DELIMITER_OUTPUT = ','


# Optional. Row number(s) to use as the column names, and the start of the data. HEADER=0 denotes the first line of data rather than the first line of the file.
# [ (int) | (list of int) | None ]
#-------------------------------------------------------------------------------
# HEADER_INPUT = [0,1,2]


# Optional. *Only use if HEADER_INPUT=None. List of column names to use. Duplicates in this list are not allowed.
# [ (list of str) ]
#-------------------------------------------------------------------------------
# NAMES_INPUT = ['A', 'B', 'C']


# Optional. Return a subset of the columns. If list-like, all elements must either be positional or strings that are inferred from the document header row(s) or correspond to NAMES_INPUT.
# [ (list of int) | (list of str) ]
#-------------------------------------------------------------------------------
# USECOLS_INPUT = ['overallLAT', 'overallLON']


# Optional. Output directory path. Default(commented) is in the same directory as input files.
# [ (str) ]
#-------------------------------------------------------------------------------
# DIRPATH_OUTPUT = ''


# Optional. Specify which previous columns to output. Default(commented) is all columns.
# [ (list of str) ]
#-------------------------------------------------------------------------------
# PREVIOUS_COLUMNS_OUTPUT = ['overallLAT']


# Optional. Specify which address columns to output. Default(commented) is all address columns.
# [ (list of str) ]
#-------------------------------------------------------------------------------
ADDRESS_COLUMNS_OUTPUT = [
    # 'place_id',
    # 'licence',
    # 'osm_type',
    # 'osm_id',
    # 'lat',
    # 'lon',
    'display_name',
    # 'boundingbox',
    'address.house_number',
    'address.road',
    # 'address.town',
    # 'address.county',
    'address.state',
    # 'address.ISO3166-2-lvl4',
    'address.postcode',
    # 'address.country',
    # 'address.country_code',
    # 'address.hamlet',
    # 'address.highway',
    # 'address.amenity',
    'address.city',
]
