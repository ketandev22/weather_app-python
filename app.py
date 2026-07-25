import requests

api_key = "7b2fcfff1aff11030697c5bb641d512a"

city = input("Enter City Name- ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")

if weather_data.json()['cod']=='404':      #checking status code
    print("Invalid City Input\nTry Again!")
else:
    temp = weather_data.json()['main']['temp']

    feels_temp = weather_data.json()['main']['feels_like']

    sky = weather_data.json()['weather'][0]['main']
    desc = weather_data.json()['weather'][0]['description']

    wind_speed = weather_data.json()['wind']['speed']

    humidity = weather_data.json()['main']['humidity']

    print(f"Temperature - {temp}°C\nTemperature feels like - {feels_temp}°C\nSky - {sky}\tstatus - {desc}\nWind speed - {wind_speed} m/s\nHumidity - {humidity} %")

