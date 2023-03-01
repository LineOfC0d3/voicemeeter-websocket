import asyncio
import websockets
from voicemeeterlib.remote import Remote
from websockets import server


class WebSocketServer:
    def __init__(self, vm):
        self.vm = vm
        self.mute = False

    async def message_handler(self, websocket):
        while True:
            try:
                message = await websocket.recv()
                print(message)
                await websocket.send(message)
                self.vm.strip[4].label = message
            except websockets.ConnectionClosedOK:
                break

    async def run(self):
        async with websockets.serve(self.message_handler, "", 8001):
            await asyncio.Future()  # run forever
