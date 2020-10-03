import asyncio
import websockets

async def hello(uri, name):
    async with websockets.connect(uri) as websocket:
        await websocket.send(name)
        print(await websocket.recv())

def main(uri):
    name = input("Enter your name: ")
    call = hello(uri, name)
    
    try:
        asyncio.get_event_loop().run_until_complete(call)
    except KeyboardInterrupt:
        print("Byebye. ")

if __name__ == "__main__":
    main("ws://192.168.1.10:8765")
