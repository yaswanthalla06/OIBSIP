import requests
print("<=== WEATHER FORECAST ===>")
city = input("Enter city name: ")
api = "f016c33d52b0f70916f0be79bfaf4673"

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": api,
    "units": "metric"
}

response = requests.get(url,params)
data = response.json()
if response.status_code == 200:
    cityname = city.title()
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    print(f"The current temperature of {cityname} is {temperature}°C and it's {description}")
else:
    print("City not found. Please enter a valid city name.")
