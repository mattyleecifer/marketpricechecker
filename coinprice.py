import requests
from datetime import datetime
coin = input("Coin name:\n")
date = input("Enter date in ISO8601 separated with dashes eg 2022-01-13 (up to 100 days before):\n")

global_url = "https://min-api.cryptocompare.com/data/v2/histoday?fsym=" + coin + "&tsym=AUD&limit=100"
request = requests.get(global_url)
results = request.json()
data = results['Data']['Data']
pricedata = {}

for i in range(0, len(data)):
    timestamp = data[i]["time"]
    dt_object = str(datetime.fromtimestamp(timestamp))
    dt = dt_object.replace(" 10:00:00", "")
    pricedata[dt] = data[i]["low"]

print("The lowprice on " + date + " was: " + str(pricedata[date]))
