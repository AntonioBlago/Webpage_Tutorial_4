import yfinance as yf
import pandas as pd
import requests as req
import sqlite3 as sq
from io import StringIO
import datetime as dt
import numpy as np

def stocks_update():
        url = "https://www.ishares.com/us/products/239710/ishares-russell-2000-etf/1467271812596.ajax?fileType=csv&fileName=IWM_holdings&dataType=fund"
        data = req.get(url).content

        result = str(data, 'utf-8')
        data = StringIO(result)
        df = pd.DataFrame(data)

        df = df[0][9:] #df = pd.read_csv('temp.csv', delimiter=',^(\(.*,.*\))', skiprows= 9)

        df = df.to_frame()

        df2 = df[0].str.split('","', expand=True).copy()

        df2.columns = df[0][9].split(",")

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


        db = "database"
        table_name = "stock_database" # table and file name
        conn = sq.connect('{}.sqlite'.format(db)) # creates file
        data2.to_sql(table_name, conn, if_exists='replace', index=False) # writes to file
        df2.to_sql("stock_infos",conn, if_exists='replace', index=False) # writes to file)

        conn.close()

def performance_and_risk_calculation():
        conn = sq.connect('{}.sqlite'.format("database"), check_same_thread=False)
        df = pd.read_sql('select * from {}'.format("stock_database"), conn)
        df["Date"] = pd.to_datetime(df["Date"])
        today = dt.date.today()
        last_price_date = pd.Timestamp.date(max(df["Date"]))

        print("Last updated price date is",today - last_price_date, "ago")

        trading_week = 5
        normal_week = 7
        weeks_in_month = 252/5/12 # 252 days are the average amount of trading days in a year with holidays
        trading_month = trading_week*weeks_in_month

        df_performance = df.drop_duplicates("Ticker", keep = "first")[["Ticker"]].copy().reset_index(drop = True)

        trading_days = {"1d":1,"7d":trading_week,"1m":trading_month,"3m":trading_month*3,"6m":trading_month*6,
                        "1y":trading_month*12,"2y":2*trading_month*12,"3y":3*trading_month*12,"5y":5*trading_month*12}

        normal_month = 4.345 * normal_week

        periods = {"1d": 1, "7d": normal_week, "1m": normal_month,
                   "3m": normal_month * 3,
                   "6m": normal_month * 6, "1y": normal_month * 12,
                   "2y": 2 * normal_month * 12, "3y": 3 * normal_month * 12,
                   "5y": 5 * normal_month * 12}

        for key, value in trading_days.items():
                calendar_days = round(periods[key])
                df_1d = df[df["Date"] >= str(last_price_date - dt.timedelta(days=calendar_days))].copy()
                df_1d.sort_values(['Ticker', 'Date'], inplace=True, ascending=[True, True])

                number_of_days_per_ticker = df_1d.groupby('Ticker')['Close'].count().copy().to_frame()

                if key == "1d":
                        tickers_with_enough_days = number_of_days_per_ticker[
                                number_of_days_per_ticker["Close"] == value+1].copy().reset_index()
                else:
                        tickers_with_enough_days = number_of_days_per_ticker[
                                number_of_days_per_ticker["Close"] >= value*0.9].copy().reset_index()

                df_1d = pd.merge(tickers_with_enough_days[["Ticker"]], df_1d, on="Ticker", how="inner")

                df_1d[key] = df_1d.groupby('Ticker')['Close'].apply(lambda x: np.log(x) - np.log(x.shift()))
                df_tmp_vola = df_1d.groupby('Ticker')[key].apply(np.std).copy().to_frame()
                df_tmp_vola[key] = df_tmp_vola[key]* 252 ** 0.5
                df_tmp_vola = df_tmp_vola.rename(columns = {key:"vola_"+key})
                df_tmp = df_1d.groupby('Ticker')[key].sum().copy().to_frame()
                df_performance = pd.merge(df_performance,df_tmp,on="Ticker",how="left")
                df_performance = pd.merge(df_performance, df_tmp_vola, on="Ticker", how="left")
                df_performance = df_performance.fillna(0)

        df_performance.to_sql("performance_and_vola", conn, if_exists='replace', index=False)  # writes to file


if __name__ == '__main__':
        #stocks_update()
        performance_and_risk_calculation()