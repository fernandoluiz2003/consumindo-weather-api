import requests
import os
import json
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

KEY = os.environ.get('KEY')
base_url = 'http://api.weatherapi.com/v1/forecast.json'
city_name = 'Rio de Janeiro'

request_url = f'{base_url}?key={KEY}&q={city_name}&days=10&aqi=no&alerts=no'

response = requests.get(
    url=request_url,
)

data = response.json()
print(json.dumps(data, indent=4))