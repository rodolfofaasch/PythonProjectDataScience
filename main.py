import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use( 'seaborn')
               
import yfinance as yf

apple = yf.Ticker("AAPL")

stockinfo = apple.info
for key, value in stockinfo.items():
    print(key, ";", value)
