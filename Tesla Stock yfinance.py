import pandas as pd
import yfinance as yf
ticker = "TSLA" # Define the ticker symbol for Tesla
tesla_data = yf.download(ticker, start="2021-01-01", end="2023-07-07")  # Use yfinance to get the stock data
tesla_data = tesla_data.reset_index()   # Reset the index
tesla_data.to_csv("tesla_stock_data.csv", index=False)  # Save the data to a CSV file
print(tesla_data.head())    # Display the first five rows using the head function