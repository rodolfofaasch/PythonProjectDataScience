import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def make_graph(data, title):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Close'])
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title(title)
    plt.grid(True)
    plt.show()

# Define the ticker symbol for GameStop
ticker = "GME"

# Use yfinance to get the stock data
gme_data = yf.download(ticker, start="2021-01-01", end="2023-07-07")

# Reset the index
gme_data = gme_data.reset_index()

# Call the make_graph function to plot the data
make_graph(gme_data, "GameStop Stock Price")