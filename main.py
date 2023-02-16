import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = ""
account_sid = ""
auth_token = ""
MY_LAT = 41.715137
MY_LONG = 44.827095

weather_params = {
    "lat": 35.386639,
    "lon": -94.424362,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]


will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️.",
        from_='+12316133398',
        to='+995551125832'
    )

print(message.status)

# print(weather_data["hourly"][0]["weather"][0]["id"])