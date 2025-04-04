import requests

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Condition: {data['weather'][0]['description'].title()}")
    else:
        print("Error:", data.get("message", "Unable to fetch weather."))

def main():
    api_key = "YOUR_API_KEY"  # Replace this with your OpenWeatherMap API key
    city = input("Enter city name: ")
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
