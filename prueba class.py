from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Find_Region import *
import cv2
from time import *
import threading
from CapTime import *
from geopy.geocoders import Nominatim

Hora = localtime()
print(f'{Hora[0]}{Hora[1]}{Hora[2]}_{Hora[3]}{Hora[4]}{Hora[5]}')
geolocator = Nominatim(user_agent="geoapiExercises")
Latitude = -25.5
Longitude = -45.5
location = geolocator.reverse(Latitude + "," + Longitude)
# Display
# print(location)
address = location.raw['address']
# print(address)
city = address.get('city', '')
state = address.get('state', '')
country = address.get('country', '')
code = address.get('country_code')
zipcode = address.get('postcode')
print('City : ',city)
print('State : ',state)
print('Country : ',country)
print('Zip Code : ', zipcode)