import asyncio

import voicemeeterlib
from websocket import WebSocketServer
from voicemeeter_controller import VoiceMeeterController


async def main():
    # TODO: detect VoiceMeeterVersion
    with voicemeeterlib.api("potato") as vm:
        controller = VoiceMeeterController(vm)
        server = WebSocketServer(controller)
        await server.run()
        print("Server exited")


if __name__ == '__main__':
    asyncio.run(main())
    # vm_kind = "potato"
    # main()
