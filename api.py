import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')

def verify_temperature(city):
  return requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}')