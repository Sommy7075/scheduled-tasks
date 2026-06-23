import requests
from twilio.rest import Client
import os



end_point = "https://api.openweathermap.org/data/2.5/forecast"
api_key=  os.environ.get("OWM_API_KEY")

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

params = {
"lat": 6.524379,
"lon": 3.379206,
"appid": api_key,
"cnt": 4,
}
response = requests.get(end_point, params=params)
response.raise_for_status()
data =response.json()

will_rain = False
for forecast in data['list'][:4]:
    condition_code = forecast['weather'][0]['id']
    #print(f"Weather ID: {condition_code}")

    if condition_code < 700:
        will_rain =True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='MGd920423229bebc1d1bafa8cebd7c58f1',
        body='its going to rain today ☂️',
        to='+2349021957075'
    )

    print(message.status)







