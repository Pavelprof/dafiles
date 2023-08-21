import requests


def get_moex_quote(ticker):
    base_url = f"https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQTF/securities/{ticker}.json?iss.meta=off&iss.json=extended"

    response = requests.get(base_url)
    data = response.json()

    if len(data) > 1 and 'marketdata' in data[1]:
        marketdata = data[1]['marketdata'][0]
        if 'BID' in marketdata:
            bid_price = marketdata['BID']
            return bid_price
    return None


import requests


def get_quotes_from_moex(ticker_list):
    def get_moex_quote(ticker):
        base_url = f"https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQTF/securities/{ticker}.json?iss.meta=off&iss.json=extended"
        response = requests.get(base_url)
        data = response.json()

        if len(data) > 1 and 'marketdata' in data[1]:
            marketdata = data[1]['marketdata'][0]
            bid_price = marketdata.get('BID')
            last_price = marketdata.get('LAST')

            # Если BID отсутствует или равен None, возвращаем LAST. Иначе возвращаем BID.
            return bid_price if bid_price is not None else last_price
        return None

    quotes = {}
    for ticker in ticker_list:
        quotes[ticker] = get_moex_quote(ticker)

    return quotes


ticker = ["INGO", "TGRN"]
price = get_quotes_from_moex(ticker)

if price is not None:
    print(f"BID Price of {ticker}: {price}")
else:
    print(f"Failed to retrieve BID price for {ticker}")
