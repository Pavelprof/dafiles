import yfinance as yf

rwj = yf.Ticker("RWJ")

current_price = rwj.history(period="1d")["Close"].iloc[0]

print(current_price)