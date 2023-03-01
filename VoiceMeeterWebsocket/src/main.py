import asyncio

import voicemeeterlib
from websocket import WebSocketServer


async def main():
    # TODO: detect VoiceMeeterVersion
    with voicemeeterlib.api("potato") as vm:
        server = WebSocketServer(vm)
        await server.run()
        print("Server exited")


if __name__ == '__main__':
    asyncio.run(main())
    # vm_kind = "potato"
    # main()
