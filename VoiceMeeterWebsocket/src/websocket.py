import asyncio
import websockets
from voicemeeterlib.remote import Remote
from websockets import WebSocketServer as WebSocket
import json
import voicemeeter_controller


class WebSocketServer:
    def __init__(self, vm: voicemeeter_controller):
        self.vc = vm

    async def message_handler(self, websocket: WebSocket):
        is_running: bool = True
        while is_running:
            try:
                message = await websocket.recv()
                error = self.vc.interpret_json(message)
                if error:
                    websocket.send(error)
            except websockets.ConnectionClosedOK:
                is_running = False
        await websocket.close()

    async def run(self):
        stop = asyncio.Future()

        async with websockets.serve(self.message_handler, "", 8001):
            await stop  # run forever
