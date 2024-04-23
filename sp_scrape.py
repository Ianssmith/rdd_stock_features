import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

#scraping list of S&P 500 tickers from wikipedia
wikiurl = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
page = requests.get(wikiurl)
html = page.text
soup = bs(html, 'html.parser')
#print(soup.prettify())
table_rows = soup.find_all('tr')
l = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    l.append(row)
symdf = pd.DataFrame(l, columns=["symbol", "name", "sector","subsector","hq","dateadded","cik","founded"])
#remove extra rows
symdf.iloc[503]
df = symdf[1:503]
df['symbol'] = df['symbol'].str.replace('\n', '')
df['founded'] = df['founded'].str.replace('\n', '')
df.head()

df.to_csv("./data/sp.csv", index=False)