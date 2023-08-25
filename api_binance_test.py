import requests

def get_quotes_from_binance(ticker_list):
    base_url = "https://api.binance.com/api/v3/ticker/price"
    quotes = {}

    for ticker in ticker_list:
        response = requests.get(base_url, params={"symbol": ticker+'USDT'})
        data = response.json()
        if 'symbol' in data and 'price' in data:
            quotes[ticker] = float(data['price'])

    return quotes

ticker_list = ["BTC", "ETH", "XRP"]

print(get_quotes_from_binance(ticker_list))