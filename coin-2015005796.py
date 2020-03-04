


import requests
import time
import telegram
#
# coin_token = '930380527:AAGwzJNNwMK8NoxvUXblLjQxeNgRdGdgGew'
# coin = telegram.Bot(token=coin_token)
# updates = coin.getUpdates()
# for u in updates:
#     print(u.message)

from telegram.ext import Updater

class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = 883266761
        self.name = name





class injunBot(TelegramBot):
    def __init__(self):
        self.token = '930380527:AAGwzJNNwMK8NoxvUXblLjQxeNgRdGdgGew'
        TelegramBot.__init__(self, 'injun', self.token)
        self.updater.stop()

    def sendMessage(self, text):
        self.core.sendMessage(chat_id = self.id, text=text)



url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,KRW"
response = requests.get(url).json()
current= [0, 0]
def requesting():
    global current
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,KRW"
    response = requests.get(url).json()
    now = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
    print(response)
    up1 = current[0]
    up2 = current[1]
    current = list(response.values())
    up1 = round(current[0] - up1, 2)
    up2 = round(current[1] - up2, 2)
    message = "BitFenix-BTC-USD: "+str(current[0])+", UP: "+str(up1) +"\nBithumb-BTC-KRW: " + str(current[1]) + ", UP: " + str(up2)



    injun = injunBot()
    injun.sendMessage(message)

    with open("test.csv", "a") as csvfile:

        csvfile.write(now)
        csvfile.write(",")
        for value in response.values():
            csvfile.write(str(value))
            csvfile.write(",")
        csvfile.write("\n")
        csvfile.close()




from apscheduler.schedulers.blocking import BlockingScheduler
scheduler = BlockingScheduler()

scheduler.add_job(requesting, 'interval', seconds=60)

try:

    scheduler.start()
except(KeyboardInterrupt, SystemExit):
    pass


