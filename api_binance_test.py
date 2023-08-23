import requests

def get_quotes_from_binance(ticker_list):
    base_url = "https://api.binance.com/api/v3/ticker/price"
    quotes = {}

    for ticker in ticker_list:
        response = requests.get(base_url, params={"symbol": ticker})
        data = response.json()
        if 'symbol' in data and 'price' in data:
            quotes[data['symbol']] = float(data['price'])

    return quotes

ticker_list = ["BTCUSDT", "ETHUSDT", "XRPUSDT"]

print(get_quotes_from_binance(ticker_list))