import requests
import csv
import json
import pytz
import datetime
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

# using now() to get current time
current_time = datetime.datetime.now()
year = current_time.year
month = current_time.month
day = current_time.day
time = current_time.strftime("%H:%M")

est = pytz.timezone('US/Eastern')
utc = pytz.utc

#Data setup
csv_header = ['From FX', 'To FX', 'Open', 'High', 'Low', 'Close', 'Year', 'Month', 'Day', 'Time']
fx_data = []

#Alpha Vantage API key: AXTYII0H82EFJEDA
FX_list = ['EUR', 'GBP', 'CNY', 'CAD', 'KRW']

#-----FX Data-----
#API Pull
for x in FX_list:
    URL = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='+x+'&to_currency=USD&apikey=' + api_key
    response_fx_data = requests.get(URL)
    json_fx_data = response_fx_data.json()
    from_FX = json_fx_data['Realtime Currency Exchange Rate']['1. From_Currency Code']
    to_FX = json_fx_data['Realtime Currency Exchange Rate']['3. To_Currency Code']
    exchange_rate = json_fx_data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    bid_price = json_fx_data['Realtime Currency Exchange Rate']['8. Bid Price']
    ask_price = json_fx_data['Realtime Currency Exchange Rate']['9. Ask Price']
    list = [from_FX, to_FX, exchange_rate, bid_price, ask_price, year, month, day, time]
    fx_data.append(list)

#Write data to csv file
with open('fxData.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csv_header)
    writer.writerows(fx_data)

