Weather App:
  This is a simple command-line weather app that retrieves the current weather information for a specified city using the OpenWeatherMap API.

Dependencies:
  Python 3.x,
  requests library

How to Run:
  Ensure that you have Python 3.x installed on your computer.

Install the requests library using pip:

  pip install requests

Replace the API_Key variable with your own OpenWeatherMap API key. You can obtain an API key by signing up for a free account at OpenWeatherMap.

Run the Weather App by executing the Python script:
  python weather_app.py
  
Enter a city name when prompted and the current weather information for that city will be displayed.

Code Structure:

API_Key: Your OpenWeatherMap API key

city: A variable for storing the user's input (city name)

base_url: The URL for making the API request, including the API key and city name

weather_data: Stores the JSON data returned from the API request

pprint(): Pretty prints the JSON data to increase readability

Usage:
  The script prompts the user to enter a city name, then it sends a request to the OpenWeatherMap API to retrieve the current weather information for that city. The JSON data is then pretty-printed to the console for easy readability.


