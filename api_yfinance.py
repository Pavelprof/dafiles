import yfinance as yf


def get_quotes_from_yfinance(ticker_list):
    tkrs = yf.download(ticker_list, period="1d")
    yf_quotes = {}

    if len(ticker_list) == 1:
        last_valid_price = tkrs['Adj Close'].dropna().iloc[-1] if not tkrs['Adj Close'].dropna().empty else None
        if last_valid_price is not None:
            yf_quotes[ticker_list[0]] = {'price': last_valid_price, 'currency': None}
    else:
        for ticker in ticker_list:
            ticker_data = tkrs.xs(ticker, level=1, axis=1)
            last_valid_price = ticker_data['Adj Close'].dropna().iloc[-1] if not ticker_data[
                'Adj Close'].dropna().empty else None
            if last_valid_price is not None:
                yf_quotes[ticker] = {'price': last_valid_price, 'currency': None}

    return yf_quotes


ticker_list = ['IWC']
quotes = get_quotes_from_yfinance(ticker_list)
print(quotes)

ticker_list = ['IWC', 'RUBUSD=X', 'RWJ']
quotes = get_quotes_from_yfinance(ticker_list)
print(quotes)

