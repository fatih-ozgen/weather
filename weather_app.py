#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import requests


# DOC
# -------------------------------------------------------------
#1 export WEATHER_API_KEY="your_api_key"
#2 virtualenv venv
#3 activate virtual env (source venv/bin/activate)
#4 pip install requests
#5 python3 weather_app.py
#6 enter country name

#option'ları ekle

def get_api_key():
    api_key = os.getenv("WEATHER_API_KEY")

    if not api_key:
        raise ValueError("WEATHER_API_KEY not found!")
    return api_key

def get_capital(country):
    # country = "estonia"
    BASE_URL = f"http://restcountries.eu/rest/v2/name/{country}"
    r = requests.get(BASE_URL).json()
    capital = r[0]["capital"]
    print(f"Capital of {country} is {capital}")

    return capital


def get_weather(capital):
    WEATHER_API_KEY = get_api_key()
    params = {
        "access_key": WEATHER_API_KEY,
        # 'query': 'New York'
        "query": capital,
    }
    api_result = requests.get("http://api.weatherstack.com/current", params)
    api_response = api_result.json()
    ret = u'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature'])
    #ret = api_response
    return ret

def main(country):
    _country = get_capital(country)
    weather = get_weather(capital=_country)

    print(weather)
    return weather

if __name__ == "__main__":
    country = input("Enter a Country:")
    main(country)