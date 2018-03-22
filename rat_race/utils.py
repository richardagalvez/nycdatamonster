from geopy.geocoders import Nominatim
geolocator = Nominatim()

def lat_long(address):
    location = geolocator.geocode(address)
    try:
        return location.latitude, location.longitude
    except:
        print('could not find address: ', address)
        return np.nan, np.nan

# notes

# df['violation_description'] = df.violation_description.str.replace("'",'')
# df['dba'] = df.dba.str.replace("'",'')
