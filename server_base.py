import asyncio
import websockets
import json

ip = 'ws://localhost'
port_no = ':8765'

async def send1(websocket):
    async for message in websocket:
        #print(message)
        #bytes_message =  bytes(message, 'ascii')
        unpacked_message = json.loads(message)
        a = []
        width = 50
        height = 50
        t = []
        for i in range(0,height):
            t.append(unpacked_message[i*width:(i+1)*width])
        print(t)
        #a.append(unpacked_message[0:150])
        #print(unpacked_message[140:160])
        #print(str(type(message)))
        await websocket.send("world")


async def server_routine():
    async with websockets.serve(send1, "192.168.1.106", 8765, max_size=None):
        await asyncio.Future()  # run forever

async def main():
    R = await asyncio.gather(
        server_routine()
    )

asyncio.run(main())