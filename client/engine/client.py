import asyncio
import websockets
import socket
import sys

debug = True

async def hello(uri, name):
    async with websockets.connect(uri) as websocket:
        await websocket.send(name)
        print(await websocket.recv())
        sys.stdout.flush()

def main():
    if debug:
        ip = socket.gethostbyname(socket.gethostname())
        port = 8765
    else:
        ip = input("Enter an IP Address: ")
        port = input("Enter a port number: ")

    uri = "ws://{}:{}".format(ip, port)

    name = input("Enter your name: ")
    call = hello(uri, name)
    
    try:
        asyncio.get_event_loop().run_until_complete(call)
    except KeyboardInterrupt:
        print("Byebye. ")
        sys.stdout.flush()

if __name__ == "__main__":
    print("Hello, world!")
    sys.stdout.flush()
    main()
