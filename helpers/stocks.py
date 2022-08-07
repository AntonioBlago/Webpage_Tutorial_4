import yfinance as yf
import pandas as pd
import requests as re
import os

url = "https://www.ishares.com/us/products/239710/ishares-russell-2000-etf/1467271812596.ajax?fileType=csv&fileName=IWM_holdings&dataType=fund"
data = re.get(url).content

df = pd.read_csv('temp.csv', delimiter=',^(\(.*,.*\))', skiprows= 9)
df2 = df[df.columns[0]].str.split('","', expand=True)

df2.columns = df.columns[0].split(",")

df2 = df2.dropna(axis=0, subset = ['Market Value'], how = "any")
df2["Ticker"] = df2["Ticker"].str.replace('"','')
tickers = df2["Ticker"].tolist()


data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = tickers,

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "5y",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1d",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'column',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )

data2 = data.unstack(level=-1) 
data2 = data2.reset_index()
data2 = data2.pivot(index = ["level_1","Date"], columns = ["level_0"], values = 0) 
data2 = data2.reset_index()
data2 = data2.rename(columns = {"level_1": "Ticker"}) 

import sqlite3 as sq
db = "database"
table_name = "stock_database" # table and file name
conn = sq.connect('{}.sqlite'.format(db)) # creates file
data2.to_sql(table_name, conn, if_exists='replace', index=False) # writes to file
df2.to_sql("stock_infos",conn, if_exists='replace', index=False) # writes to file)

os.remove("temp.csv")
conn.close() 

