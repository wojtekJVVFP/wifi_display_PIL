from websocket_devices import Ws_devices, devices
import asyncio
import websockets
import json

async def ws_comm(message, device):
    async with websockets.connect(device.return_address()) as websocket:
        await websocket.send(message)
        received = await websocket.recv()
        data_dict = json.loads(received)

        print('dane: ' + data_dict['data'])

