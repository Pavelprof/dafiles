import requests
from binance.spot import Spot

client = Spot()

base_url = "https://api.binance.com/api/v3/ticker/price"
symbols = ["BTCUSDT", "ETHUSDT", "XRPUSDT"]

for symbol in symbols:
    response = requests.get(base_url, params={"symbol": symbol})
    data = response.json()
    print(f"{symbol}: {data['price']}")