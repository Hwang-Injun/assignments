import asyncio
import pathlib
import ssl
import websockets
import websocket


async def hello():
    uri = "wss://api.upbit.com/websocket/v1"
    async with websockets.connect(
        uri, ssl=True
    ) as ws:

        name = input('[{"ticket":"UNIQUE_TICKET"},'
                     '{"type":"trade","codes":["KRW-BTC"]},'
                     '{"type":"orderbook","codes":["KRW-BTC"]}]')

        await ws.send(name)
        print(name)
        greeting = await ws.recv()
        #greeting = websocket.WebSocket
        print(greeting)

asyncio.get_event_loop().run_until_complete(hello())