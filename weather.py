import requests
from pprint import pprint

API_Key = 'f8a922011d130a1b3fcf18330d72c7c2'    # openweathermaps api key

city = input("Enter a city: ")          # city variable for input

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city   # request to url

weather_data = requests.get(base_url).json()        # stored response data as json file

pprint(weather_data)                # pprint to increase readability