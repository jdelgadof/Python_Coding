# Exercise 12-1
import requests

request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()

print("The Chuck Norris joke of the day is: " + '"' + response["value"] + '"')

# Exercise 12-2

query = input("Please give the name of a city to check the weather: ")
APIKey = "3afac1ef1fef39c9fe17b2ebe5cd5f42"
request = f"https://api.openweathermap.org/geo/1.0/direct?q={query}&limit={1}&appid={APIKey}"
response = requests.get(request).json()
# print(response[0])
lat = response[0]["lat"]
lon = response[0]["lon"]
name = response[0]["name"]
code_country = response[0]["country"]
print(f"we find out the city {name} belong to the code country {code_country}")

request = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIKey}"
response2 = requests.get(request).json()
Far = float(response2["main"]["temp"])
cel = Far-273.15
weather = response2["weather"][0]["main"]
print(f"The weather is {weather} with {cel:.2f}C grades")

