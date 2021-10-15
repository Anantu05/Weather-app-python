import requests
while True:

	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

	def getweather(city):
		result = requests.get(url.format(city, api_key))
		
		if result:
			json = result.json()
			city = json['name']
			country = json['sys']['country']
			temp_kelvin = json['main']['temp']
			temp_celsius = temp_kelvin-273.15
			temp_celsius = str(round(temp_celsius, 2)) + ' Degrees Celsius'
			weather1 = json['weather'][0]['main']
			desc = json['weather'][0]['description'].capitalize()
			wind = json['wind']['speed']
			wind_dir = json['wind']['deg']
			humidity = json['main']['humidity']
			final = [city, country, temp_celsius, weather1, desc, wind, wind_dir, humidity]
			return final
		else:
			print("Please enter a real city's name... not an imaginary ones' xd")

	def search(city_name):
		data = getweather(city_name)
		if data:
			print(f"{'-'*35}\nCity: {data[0]}, {data[1]}\nTemperature: {data[2]}\nWeather conditions: {data[3]}\nDescription: {data[4]}\n\nAdditional Details:\n\tWind speed: {data[5]}km/h\n\tWind direction: {data[6]} Degrees\n\tHumidity: {data[7]}%\n{'-'*35}")
		else:
			return 'Error', f"Cannot find {city}",'\n'+"Please enter a real city's name... not an imaginary ones' xd"

	city = input(">>> Enter the city's name\n>>> ")
	search(city)