import pandas as pd
import yfinance as yf

ticker = "GME"

gme_data = yf.download(ticker, start="2021-01-01", end="2023-07-07")

gme_data = gme_data.reset_index()

gme_data.to_csv("gme_stock_data.csv", index=False)

print(gme_data.head())