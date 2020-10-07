'''
Aim to build a client that sends and receives messages from the server.
The idea is to make an RPG chat game where you face monsters, nothing hard. 
Just a way to practice chatting. 

Will later extend to chatting with other clients, too. 
'''

import asyncio
import websockets

async def produce(message: str, host: str, port: str) -> None:
    async with websockets.connect(f"ws://{host}:{port}") as ws:
        await ws.send(message)
        print(await ws.recv())

def main():
    try:
        asyncio.run(produce(message=input("Enter your name: "), host="localhost", port="4000"))
    except KeyboardInterrupt:
        pass
    except ConnectionRefusedError:
        print("Couldn't connect to server. ")

if __name__ == "__main__":
    main()
