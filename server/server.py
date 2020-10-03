import asyncio
import websockets

async def echo(websocket, path):
    name = await websocket.recv()
    message = "Hello, " + name

    print("Found client. ")

    await websocket.send(message)

def main():
    start_server = websockets.serve(echo, "192.168.1.10", 8765)

    try:
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print("Byebye. ")

if __name__ == "__main__":
    main()
