import asyncio
import websockets
import socket

debug = True

async def echo(websocket, path):
    name = await websocket.recv()
    message = "Hello, " + name

    print("Found client. ")

    await websocket.send(message)

def main():
    ip = socket.gethostbyname(socket.gethostname())

    if debug:
        port = 8765
    else:
        port = input("Enter a port number: ")

    print("Server starts with address {}:{}".format(ip, port))

    start_server = websockets.serve(echo, ip, port)

    try:
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print("Byebye. ")

if __name__ == "__main__":
    main()
