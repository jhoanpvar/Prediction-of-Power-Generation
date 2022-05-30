from geopy.geocoders import Nominatim

def Find_Region(La,Lo):
    geolocator = Nominatim(user_agent="geoapiExercises")
    Latitude = La
    Longitude = Lo
    location = geolocator.reverse(Latitude + "," + Longitude)
    # Display
    #print(location)
    address = location.raw['address']
    #print(address)
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    code = address.get('country_code')
    zipcode = address.get('postcode')
    #print('City : ',city)
    #print('State : ',state)
    #print('Country : ',country)
    #print('Zip Code : ', zipcode)
    return city
