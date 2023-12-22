import yfinance as yf
import time

# start_time = time.time()
#
# tickers = yf.Tickers('msft aapl goog iwc rwj')
#
# last_prices = []
#
# for ticker in tickers.tickers.values():
#     last_price = ticker.get_fast_info.last_price
#     last_prices.append(last_price)
#
# print(last_prices)
#
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"yf.Tickers execution time: {elapsed_time} sec")
#

start_time = time.time()

def get_quotes_from_yf(ticker_list):
    tkrs = yf.download(ticker_list, period="1d")
    yf_quotes = {}

    if len(ticker_list) == 1:
        last_valid_price = tkrs['Adj Close'].dropna().iloc[-1] if not tkrs['Adj Close'].dropna().empty else None
        if last_valid_price is not None:
            yf_quotes[ticker_list[0]] = {'price': last_valid_price, 'currency': None}
    else:
        for ticker in ticker_list:
            print(ticker)
            ticker_data = tkrs.xs(ticker, level=1, axis=1)
            last_valid_price = ticker_data['Adj Close'].dropna().iloc[-1] if not ticker_data[
                'Adj Close'].dropna().empty else None
            if last_valid_price is not None:
                yf_quotes[ticker] = {'price': last_valid_price, 'currency': None}

    return yf_quotes

ticker_list = ["MSFT", "AAPL", "GOOG", "IWC", "RWJ"]
quotes = get_quotes_from_yf(ticker_list)
print(quotes)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"yf.download execution time: {elapsed_time} sec")