from geopy.geocoders import Nominatim

nominatim = Nominatim (user_agent = 'user')
location = nominatim.geocode("Moscow, Russia")
print(location.address)
print((location.latitude, location.longitude))
