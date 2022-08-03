import sqlite3 as sq
import pandas as pd
table_name = "stock_database" # table and file name

conn = sq.connect('{}.sqlite'.format(table_name))
df = pd.read_sql('select * from {}'.format(table_name), conn)

print(df)
data = df[df["Ticker"]=="AAN"]
Ticker =  data["Ticker"].unique()[0]
print(Ticker)

conn.close()