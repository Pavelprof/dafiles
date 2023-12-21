# it does not suit, because it response data of the previous day

from alpha_vantage.timeseries import TimeSeries
import requests

public_api_key = 'CDS03QHDUMLHAUU1'

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=RWJ&interval=1min&apikey={public_api_key}'
r = requests.get(url)
data = r.json()

print(data)




ts = TimeSeries(key=public_api_key)

data1, meta_data = ts.get_quote_endpoint(symbol='RWJ')
last_price = data1['05. price']

print(data1)
print("Last price get_quote_endpoint:", last_price)



data, meta_data = ts.get_intraday(symbol='RWJ', interval='1min', outputsize='compact')
last_time_stamp = max(data.keys())
last_trade_data = data[last_time_stamp]
last_price_data = last_trade_data['4. close']
#
#
# print(" ")
# print(last_time_stamp)
# print(last_trade_data)
# print("Last price get_intraday:", last_price_data)
# print(" ")
# print(data)