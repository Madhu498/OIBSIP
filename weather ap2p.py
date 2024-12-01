import requests

# Function to fetch weather data from WeatherAPI
def get_weather(location, api_key, units="C"):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": location,
        "aqi": "no"  # Air Quality Index (optional, set to 'yes' if needed)
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Handle HTTP errors
        data = response.json()

        # Parse relevant weather details
        temp = data["current"]["temp_c"] if units == "C" else data["current"]["temp_f"]
        weather = {
            "location": data["location"]["name"],
            "region": data["location"]["region"],
            "country": data["location"]["country"],
            "temperature": temp,
            "humidity": data["current"]["humidity"],
            "condition": data["current"]["condition"]["text"]
        }
        return weather
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP Error: {http_err.response.status_code} - {http_err.response.reason}"
    except requests.exceptions.RequestException as req_err:
        return f"Network Error: {req_err}"
    except KeyError:
        return "Invalid data received. Please check your input or API key."

# Main function to handle user interaction
def main():
    print("Welcome to the Weather App!")
    api_key = input("Enter your WeatherAPI key: ").strip()

    while True:
        print("\nOptions:")
        print("1. View weather in Celsius")
        print("2. View weather in Fahrenheit")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == "3":
            print("Goodbye!")
            break
        elif choice in ["1", "2"]:
            location = input("Enter a city name or ZIP code: ").strip()
            units = "C" if choice == "1" else "F"
            weather = get_weather(location, api_key, units)
            
            if isinstance(weather, dict):
                unit_symbol = "°C" if units == "C" else "°F"
                print(f"\nWeather in {weather['location']}, {weather['region']}, {weather['country']}:")
                print(f"Temperature: {weather['temperature']}{unit_symbol}")
                print(f"Humidity: {weather['humidity']}%")
                print(f"Conditions: {weather['condition']}")
            else:
                print(f"Error: {weather}")
        else:
            print("Invalid choice. Please try again.")

# Run the app
if __name__ == "__main__":
    main()
