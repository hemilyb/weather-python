from api import verify_temperature
from datetime import datetime, timezone

def kelvin_to_celsius(temp_kelvin):
   temp_celsius = temp_kelvin - 273.15
   return temp_celsius

def weather_info(data, index):
   temp = kelvin_to_celsius(data['list'][index]['main']['temp'])

   timestamp = data['list'][index]['dt']
   date_time = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime('%d-%m')

   return temp, date_time

def weather(city):
   response = verify_temperature(city)
   data = response.json()

   temps_list = []
   dates_list = []

   for index in range(0, 33, 8): # (start, stop, step)
      temp, date_time = weather_info(data, index)
      temps_list.append(temp)
      dates_list.append(date_time)
      
   temps = [int(temp) for temp in temps_list]
   dates = dates_list
   print(temps, dates)
   return temps, dates