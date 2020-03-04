import requests
import pandas as pd

r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=KRW,USD')

df = pd.DataFrame({"KRW": [list(r.json().values())[0]],
                   "USD": [list(r.json().values())[1]]})
print(df)
data = pd.read_csv("sang.csv")
print(data)
data = data.append(df, sort=True)
data = data.loc[:,'KRW':'USD']
data.to_csv("sang.csv")