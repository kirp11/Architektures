
import requests
import json


api_key = '3e9ddc48-02d2-453f-ba1f-f0d071500b95'


class MyAPI:
    def __init__(self, city_name):
        self.city_name = city_name
        self.lat = None
        self.lon = None
        self.temp = None
        self.hum = None
        self.press = None
        self.wind = None
        self.get_weather(api_key)

    def get_coord(self):

        with open('russian-cities.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        for i in data:
            if i["name"] == self.city_name:
                self.lat = i['coords']['lat']
                self.lon = i['coords']['lon']
                return


    def get_weather(self, api_key):
        self.get_coord()

        headers = {
            'X-Yandex-Weather-Key': api_key
        }

        response = requests.get(f'https://api.weather.yandex.ru/v2/forecast?lat={self.lat}&lon={self.lon}', headers=headers)
        if response.status_code == 200:
            city_data = response.json()
            self.temp = city_data['fact']['temp']
            self.hum = city_data['fact']["humidity"]
            self.press = city_data['fact']["pressure_mm"]
            self.wind = city_data['fact']["wind_speed"]
        else:
            raise Exception(f"Fail retrieve weather data: {response.status_code} {response.text}")

# api = MyAPI()
# api.get_coord('Яхрома')
# api.get_weather(api_key, 56.28333, 37.48333)