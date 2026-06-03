import requests

def get_weather(city):
    """Fetch current weather using Open-Meteo (free, no API key)"""
    try:
        # Get coordinates for the city
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
        geo_resp = requests.get(geo_url).json()
        
        if not geo_resp.get("results"):
            return f"Sorry, I couldn't find the city {city}."
        
        lat = geo_resp["results"][0]["latitude"]
        lon = geo_resp["results"][0]["longitude"]
        
        # Get weather
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_data = requests.get(weather_url).json()
        
        temp = weather_data["current_weather"]["temperature"]
        wind = weather_data["current_weather"]["windspeed"]
        
        return f"The current temperature in {city} is {temp}°C with wind speed of {wind} km/h."
    except Exception as e:
        return f"Could not fetch weather. Error: {str(e)}"