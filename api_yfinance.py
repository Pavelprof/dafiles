import yfinance as yf

tkrs = yf.download(["RWJ", "GOOGL"], period="1m")
current_prices_series = tkrs['Adj Close'].iloc[-1]
current_prices_dict = current_prices_series.to_dict()

print(current_prices_dict)
