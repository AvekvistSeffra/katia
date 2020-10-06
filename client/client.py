import asyncio
import websockets
import socket

debug = True

async def hello(uri, name):
    async with websockets.connect(uri) as websocket:
        await websocket.send(name)
        print(await websocket.recv())

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

if __name__ == "__main__":
    main()
