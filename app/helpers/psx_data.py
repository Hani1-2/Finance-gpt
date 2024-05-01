# from datetime import datetime
import datetime
from psx import stocks, tickers

tickers = tickers()

data = stocks("SILK", start=datetime.date(2024, 2, 1), end=datetime.date.today())

data = stocks(["SILK", "PACE","WTL", "PIBTL", "PIAA", "FFL", "AGL", "FCCL"], start=datetime.date(2024, 3, 1), end=datetime.date.today())
print(type(data),"nature of data")
print(data,"data")
documents = data.to_dict(orient='records')

# to csv
data.to_csv("data.csv")