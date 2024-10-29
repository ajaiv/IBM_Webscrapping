import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# tesla_data = yf.Ticker("TSLA")
# tesla_share = tesla_data.history(period="max")
# # print(tesla_share.head())
#
# tesla_revenue = tesla_data.financials
# # print(tesla_revenue.tail())
#
# gme_data = yf.Ticker("GME")
# gme_share = gme_data.history(period="max")
# # print(gme_share.head())
#
# url = "https://companiesmarketcap.com/inr/gamestop/revenue/#:~:text=According%20to%20GameStop%20's%20latest,were%20of%20%E2%82%B9490.47%20Billion."
# html_data = requests.get(url).text
# soup = BeautifulSoup(html_data,'html.parser')
#
# gme_df = pd.DataFrame(columns=['Year', 'Revenue'])
#
# for row in soup.find("tbody").find_all("tr"):
#     col = row.find_all("td")
#     year = col[0].text
#     revenue = col[1].text
#
#     gme_df = pd.concat([gme_df, pd.DataFrame(
#         {"Year": [year], "Revenue": [revenue]})], ignore_index=True)
#
# print(gme_df.tail())

def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'], label='Closing Price', color='blue')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# tesla = yf.Ticker("TSLA")
# tesla_data = tesla.history(period='max')
# make_graph(tesla_data, 'Tesla Stock Closing Prices')

gme = yf.Ticker("GME")
gme_data = gme.history(period='max')
make_graph(gme_data, 'GameStop Stock Closing Prices')





# # first_day_volume = tesla_share['Volume'].iloc[0]
# # print("Volume on the first day:", first_day_volume)
