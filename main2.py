import asyncio
import pathlib
import ssl
import websockets


# localhost_pem = pathlib.Path(__file__)
# ssl_context.load_verify_locations(localhost_pem)

async def hello():
    uri = "wss://msging.net/commands:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())