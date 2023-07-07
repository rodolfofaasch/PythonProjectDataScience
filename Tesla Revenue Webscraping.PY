import pandas as pd
import requests


api_key = "YOUR_API_KEY"  
symbol = "TSLA"
function = "INCOME_STATEMENT"


url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}"
response = requests.get(url)
data = response.json()


revenue_data = data['annualReports']

df = pd.DataFrame(revenue_data)
df = df[['fiscalDateEnding', 'totalRevenue']]


last_five_rows = df.tail(5)
print(last_five_rows)