# Reverse Geocoding
Reverse geocoding app. Interactive or programmatic mode.


## Getting Started

### Get Miniconda
Install Miniconda [here](https://docs.conda.io/en/latest/miniconda.html)


### Create Conda Environment

```bash
conda env create -n ENVNAME --file environment.yml
```

### Running the app

#### Interactive mode:
```bash
%USER%/Miniconda3/envs/ENVNAME/python.exe "./reverse_geocode/reverse_geocode.py"
```
Input files using file explorer dialog.

#### Programmatic mode (Interactive=False):
```bash
%USER%/Miniconda3/envs/ENVNAME/python.exe "./reverse_geocode/reverse_geocode.py" arg1 arg2 ...
```
Input files using positional args.

## Config

#### `INTERACTIVE_MODE = [ True | False ]`
```sh
True : File dialog popup
False : No file dialog popup and takes CLI positional arguments
```


#### `GEOCODER = [ 'Nominatim' | 'Photon' ]`
```sh
'Nominatim' :
- database - PostGIS
- data sources - OpenStreetMap, Wikipedia, US Tiger & Postcodes, UK Postcodes
- response - GeoJSON, JSON, HTML, XML

'Photon' : 
- database - Elasticsearch
- data sources - OpenStreetMap
- response - GeoJSON
```

#### `LATITUDE = [ (str) | (int) ]`
#### `LONGITUDE = [ (str) | (int) ]`
```sh
(str) : Column name
(int) : Column position
```

#### `DELIMITER_INPUT = [ (str) ]`
#### `DELIMITER_OUTPUT = [ (str) ]`
```sh
(str) : Delimiting character(s)
```

## Logs
`./reverse_geocode/reverse_geocode.log`