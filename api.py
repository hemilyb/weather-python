import requests
from config import API_KEY

api_key = API_KEY

def verify_temperature(city):
  return requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}')