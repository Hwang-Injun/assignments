import websocket
import json
import ast
try:
    import thread
except ImportError:
    import _thread as thread
import time
websocket.WebSocket
def on_message(ws, message):
    message = ast.literal_eval(message.decode('utf-8'))

    if message["type"] == "orderbook":
        a = "ask_price: " + str(message["orderbook_units"][0]["ask_price"])
        b = "bid_price: " + str(message["orderbook_units"][0]["bid_price"])
        c = "ask_size: " + str(message["orderbook_units"][0]["ask_size"])
        d = "bid_size: " + str(message["orderbook_units"][0]["bid_size"])
        print(a,b,c,d)
    elif message["type"] == "trade":
        a = "trade_price: " + str(message["trade_price"])
        b = "trade_volume: " + str(message["trade_volume"])
        c = "ask_bid: " + str(message["ask_bid"])
        print(a,b,c)





def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):


        ws.send('[{"ticket":"UNIQUE_TICKET"},'
                '{"type":"trade","codes":["KRW-BTC"]},'
                '{"type":"orderbook","codes":["KRW-BTC"]}]')

    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://api.upbit.com/websocket/v1",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()