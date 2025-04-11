import json

def get_current_weather(location):
    weather = {
        "temperature": "70",
        "unit": "F",
        "forecast": "sunny"
    }
    return json.dumps(weather)

def get_location():
    return "Colombo, Sri Lanka"