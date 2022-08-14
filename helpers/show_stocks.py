import sqlite3 as sq
import pandas as pd
import numpy as np
table_name = "performance_and_vola" # table and file name

conn = sq.connect('{}.sqlite'.format("database"))
df = pd.read_sql('select * from {}'.format(table_name), conn)
df_infos = pd.read_sql('select * from {}'.format("stock_infos"), conn)

df = pd.merge(df, df_infos[["Ticker", "Name", "Sector"]], on = "Ticker", how = "right")
compare = df[df["Ticker"]=="QLYS"]
print(round(compare[["7d","vola_7d","1m","vola_1m","1y","vola_1y"]]*100,2))

df_stocks = pd.read_sql('select * from {} where Ticker="QLYS"'.format("stock_database"), conn)
df_stocks["Date"] = pd.to_datetime(df_stocks["Date"])
df_stocks[df_stocks["Date"]=="2021-8-12"]["Close"]

df_1d = df_stocks[df_stocks["Date"] >= "2021-08-12"].copy()
df_1d.sort_values(['Ticker', 'Date'], inplace=True, ascending=[True, False])

df_1d["return"] = df_1d.groupby('Ticker')['Close'].apply(lambda x: np.log(x) - np.log(x.shift()))
df_1d["return"] = df_1d.groupby('Ticker')['Close'].apply(lambda x: x/x.shift(-1))
df_1d["return"] = df_1d.groupby('Ticker')['Close'].apply(pd.Series.pct_change)
print(df_1d["return"].sum())

print(df)
data = df[df["Ticker"]=="AAN"]
Ticker = data["Ticker"].unique()[0]
print(Ticker)

conn.close()