import requests
import csv
import json
import pytz
from datetime import datetime, timezone

est = pytz.timezone('US/Eastern')
utc = pytz.utc

csv_header = ['From FX', 'To FX', 'Open', 'High', 'Low', 'Close', 'Year', 'Month', 'Day', 'Time']
fx_data = []

with open('x.json', 'r') as openfile:
    json_fx_data = json.load(openfile)
from_FX = json_fx_data['Meta Data']['2. From Symbol']
to_FX = json_fx_data['Meta Data']['3. To Symbol']
# tz = json_fx_data['Meta Data']['7. Time Zone']
keys = json_fx_data['Time Series FX (30min)'].keys()
for i in keys:
    # Creating datetime object and changing timezone (UTC->EST)
    data_time = datetime.strptime(i, '%Y-%m-%d %H:%M:%S')
    data_time = utc.localize(data_time)
    data_time = data_time.astimezone(est)
    # Initializing item elements
    year = data_time.year
    month = data_time.month
    day = data_time.day
    time = data_time.strftime("%H:%M")
    open = json_fx_data['Time Series FX (30min)'][i]['1. open']
    high = json_fx_data['Time Series FX (30min)'][i]['2. high']
    low = json_fx_data['Time Series FX (30min)'][i]['3. low']
    close = json_fx_data['Time Series FX (30min)'][i]['4. close']
    list = [from_FX, to_FX, open, high, low, close, year, month, day, time]
    fx_data.append(list)

#Write data to csv file
with open('fxData.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csv_header)
    writer.writerows(fx_data)
