import os
from tinkoff.invest import Client

TOKEN = os.environ["TIN_API_KEY"]

with Client(TOKEN) as client:
    r = client.market_data.get_last_prices(figi=['BBG004730RP0','BBG004731032','BBG004S68B31',])
    print(r)
    print(type(r))
    print(r.last_prices[0])
    print(type(r.last_prices[0]))
    print(r.last_prices[0].price)
    print(type(r.last_prices[0].price))
    p = r.last_prices[0].price
    price = p.units + p.nano / 1e9
    print(price)
