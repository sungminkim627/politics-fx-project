import requests
import csv
import json
import datetime

# using now() to get current time
current_time = datetime.datetime.now()
year = current_time.year
month = current_time.month
day = current_time.day
time = current_time.strftime("%H:%M")

#-----Political Data-----
#PredictIt API URL
URL_predictit = "https://www.predictit.org/api/marketdata/all/"
#API pull
response_political_data = requests.get(URL_predictit)
json_political_data = json.loads(response_political_data.text)
#print(json_political_data)
#Data setup
csv_header = ['Topic ID', 'Topic Name', 'Prediction', 'Last Trade Price', 'Year', 'Month', 'Day', 'Time']

political_data = []

#Get market predictions relating to Repub vs. Democrat and put in list
for x in json_political_data['markets']:
    for y in x['contracts']:
        if y['name'] == 'Republican' or y['name'] == 'Democratic':
            list = [x['id'], x['shortName'], y['name'], y['lastTradePrice'], year, month, day, time]
            political_data.append(list)

#Write data to csv file
with open('marketPrediction.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csv_header)
    writer.writerows(political_data)
