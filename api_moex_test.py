import requests


def get_moex_bid_price(ticker):
    base_url = f"https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQTF/securities/{ticker}.json?iss.meta=off&iss.json=extended"

    response = requests.get(base_url)
    data = response.json()

    if len(data) > 1 and 'marketdata' in data[1]:
        marketdata = data[1]['marketdata'][0]
        if 'BID' in marketdata:
            bid_price = marketdata['BID']
            return bid_price
    return None


ticker = "INGO"
bid_price = get_moex_bid_price(ticker)

if bid_price is not None:
    print(f"BID Price of {ticker}: {bid_price}")
else:
    print(f"Failed to retrieve BID price for {ticker}")
