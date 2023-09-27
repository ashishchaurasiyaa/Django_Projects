from django.shortcuts import render
import json
import urllib.request
from decouple import config  # Import the config function from the decouple library

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        # Read the OpenWeatherMap API key from the .env file
        api_key = config('OPENWEATHERMAP_API_KEY')

        # Build the URL with the API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        try:
            source = urllib.request.urlopen(url).read()
            list_of_data = json.loads(source)
            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
                "temp": str(list_of_data['main']['temp']) + 'k',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
            }
            print(data)
        except urllib.error.HTTPError as e:
            # Handle the HTTP error, e.g., log the error message.
            print(f"HTTP Error: {e}")
            data = {}
    else:
        data = {}
    return render(request, "main/index.html", data)
