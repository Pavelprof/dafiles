import requests
from binance.spot import Spot

client = Spot()

print(client.ticker_price(symbols = ["BTCUSDT", "ETHUSDT", "XRPUSDT"]))



# base_url = "https://api.binance.com/api/v3/ticker/price"
# symbols = ["BTCUSDT", "ETHUSDT", "XRPUSDT"]  # Пример списка пар
#
# for symbol in symbols:
#     response = requests.get(base_url, params={"symbol": symbol})
#     data = response.json()
#     print(f"{symbol}: {data['price']}")