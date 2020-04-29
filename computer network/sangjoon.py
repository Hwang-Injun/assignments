import requests
import telegram
import pandas as pd
import sys

from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.jobstores.base import JobLookupError

import time

r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=KRW,USD')
print(r.text)
df = r.json()

my_token = '824795624:AAH9CNJNMCe_53IZCNr_MCIFoxNnZdGAXzw'
my = telegram.Bot(token = my_token)
updates = my .getUpdates()
for u in updates:
    print(u.message)

class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.id = 898394881
        self.name = name

    def sendMessage(self, text):
        self.core.sendMessage(chat_id = self.id, text=text)

class CoinTeller(TelegramBot):
    def __init__(self):
        self.token = '824795624:AAH9CNJNMCe_53IZCNr_MCIFoxNnZdGAXzw'
        TelegramBot.__init__(self, '', self.token)

    def start(self):
        self.sendMessage('')


sched = BlockingScheduler()

def send():
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=KRW,USD')
    chii = CoinTeller()
    chii.sendMessage(r.text)

    df = pd.DataFrame({"KRW": [list(r.json().values())[0]],
                       "USD": [list(r.json().values())[1]]})

    data = pd.read_csv("sang.csv")

    data = data.append(df, sort=True)
    data = data.loc[:, 'KRW':'USD']
    data.to_csv("sang.csv")
sched.add_job(send, 'interval', seconds=3)
sched.start()
