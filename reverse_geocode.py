################################################################################
#
# Reverse Geocoder
#
################################################################################
import config
from helper import logger

import sys, os
import pandas as pd
import pandas._libs.lib as lib
from geopy.geocoders import Nominatim, Photon, Pelias
from tqdm.auto import tqdm
import tkinter
from tkinter import filedialog


#===============================================================================
# Variables
#-------------------------------------------------------------------------------

MIN_LAT_USA = 25
MAX_LAT_USA = 50
MIN_LON_USA = -125
MAX_LON_USA = -60

locator = Nominatim(user_agent='reverse_geocode')
if config.GEOCODER == 'Photon':
    locator = Photon(user_agent='reverse_geocode')

try:
    config.NAMES_INPUT
except (NameError, AttributeError):
    config.NAMES_INPUT = lib.no_default
try:
    config.HEADER_INPUT
except (NameError, AttributeError):
    config.HEADER_INPUT = 'infer'
try:
    config.USECOLS_INPUT
except (NameError, AttributeError):
    config.USECOLS_INPUT = None
try:
    config.DIRPATH_OUTPUT
except (NameError, AttributeError):
    config.DIRPATH_OUTPUT = None
try:
    config.PREVIOUS_COLUMNS_OUTPUT
except (NameError, AttributeError):
    config.PREVIOUS_COLUMNS_OUTPUT = []
try:
    config.ADDRESS_COLUMNS_OUTPUT
except (NameError, AttributeError):
    config.ADDRESS_COLUMNS_OUTPUT = []


#===============================================================================
# Helper Functions
#-------------------------------------------------------------------------------

def to_coordinate(lat, lon):
    return str(lat)+','+str(lon)


def apply_rgeocode(coordinate_df, file_path, interactive_mode):
    if interactive_mode:
        tqdm.pandas(desc=f'Reverse geocoding... {os.path.basename(file_path)}')
        rgeocoded_list = list(coordinate_df.progress_apply(locator.reverse))
    if not interactive_mode:
        rgeocoded_list = list(map(locator.reverse, coordinate_df))
    return [x.raw for x in rgeocoded_list]


#===============================================================================
# Interactive Modes

#-------------------------------------------------------------------------------
# File Explorer Mode

if config.INTERACTIVE_MODE:
    tkinter.Tk().withdraw()
    file_paths = filedialog.askopenfilenames()
    print(file_paths)


#-------------------------------------------------------------------------------
# CLI Mode

if not config.INTERACTIVE_MODE:
    file_paths = sys.argv[1:]
    print(file_paths)


#===============================================================================
# Reverse Geocode
#-------------------------------------------------------------------------------
if 'file_paths' in locals():
    logger(f'{len(file_paths)}  files to reverse geocode', 'INFO', func=__name__, file=os.path.splitext(os.path.realpath(__file__))[0] + '.log', stdout=True)
    for count, file_path in enumerate(file_paths):
        count += 1
        if file_path.lower().endswith('.csv'):
            logger(f'''
    {count =  } of {len(file_paths)}
    {file_path =  }
            ''', 'INFO', func=__name__, file=os.path.splitext(os.path.realpath(__file__))[0] + '.log', stdout=True)

            try:
                df = pd.read_csv(file_path, index_col=False,
                    delimiter=config.DELIMITER_INPUT,
                    header=config.HEADER_INPUT,
                    names=config.NAMES_INPUT,
                    usecols=config.USECOLS_INPUT
                )
            except Exception as e:
                logger(f'Reading csv file error... {e}', 'ERROR', func=__name__, file=os.path.splitext(os.path.realpath(__file__))[0] + '.log', stdout=True)
            # print(df.info())
            # print(df.head())

            if isinstance(config.LATITUDE, int): # int -> str, column name
                config.LATITUDE = df.columns[config.LATITUDE]
            if isinstance(config.LONGITUDE, int):
                config.LONGITUDE = df.columns[config.LONGITUDE]

            df = df.loc[(df[config.LATITUDE] > MIN_LAT_USA) & (df[config.LATITUDE] < MAX_LAT_USA) & (df[config.LONGITUDE] > MIN_LON_USA) & (df[config.LONGITUDE] < MAX_LON_USA)]
            # print(df.info())
            
            df['coordinate'] = list(map(to_coordinate, df[config.LATITUDE], df[config.LONGITUDE]))
            # print(df['coordinate'])

            data = apply_rgeocode(df['coordinate'], file_path, config.INTERACTIVE_MODE)
            rgeocoded_address_df = pd.json_normalize(data)
            # if config.GEOCODER == 'Nominatim':
                # rgeocoded_address_df.drop(columns=['licence', 'osm_type'], inplace=True)
            # print(rgeocoded_address_df.head())
            # print(rgeocoded_address_df.info())
            rgeocoded_combined_df = pd.concat([df, rgeocoded_address_df],axis=1)
            # print(rgeocoded_combined_df.info())
            # print(rgeocoded_combined_df.head())

            if config.DIRPATH_OUTPUT:
                if not os.path.exists(config.DIRPATH_OUTPUT):
                    os.mkdir(config.DIRPATH_OUTPUT)
                rgeocoded_file_path = os.path.join( config.DIRPATH_OUTPUT, os.path.splitext(os.path.basename(file_path))[0] + '_rgeocoded.csv' )
            elif config.DIRPATH_OUTPUT is None:
                rgeocoded_file_path = os.path.splitext(file_path)[0] + '_rgeocoded.csv'
            print(rgeocoded_file_path)

            if not config.PREVIOUS_COLUMNS_OUTPUT:
                config.PREVIOUS_COLUMNS_OUTPUT = list(df.columns)
            if not config.ADDRESS_COLUMNS_OUTPUT:
                config.ADDRESS_COLUMNS_OUTPUT = list(rgeocoded_address_df.columns)

            combined_columns_output = config.PREVIOUS_COLUMNS_OUTPUT + config.ADDRESS_COLUMNS_OUTPUT

            rgeocoded_combined_df.to_csv(rgeocoded_file_path, index=False,
                sep=config.DELIMITER_OUTPUT,
                columns=combined_columns_output
            )

# from geopy.extra.rate_limiter import RateLimiter

# # locator = Nominatim(user_agent='reverse_geocode')
# # rgeocode = RateLimiter(locator.reverse, min_delay_seconds=0.001)
# # coordinates = '33.616721277742727, -86.709107871930712'
# # location = locator.reverse(coordinates)
# # coordinates = locator.geocode(location.address)
# # print(location.address)
# # print(coordinates.latitude, coordinates.longitude)
