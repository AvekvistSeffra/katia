'''
Aim to build a server that sends out monsters for the clients to slay. 
Will not be hard, just a small text-based fighting game that uses the internet to play. 

Will later extend to chatting with other clients, too. 
'''

import asyncio
import websockets
import logging
from websockets import WebSocketServerProtocol

logging.basicConfig(level=logging.INFO)

class Server:
    clients = set()

    async def register(self, ws: WebSocketServerProtocol) -> None:
        self.clients.add(ws)
        logging.info(f"{ws.remote_address} connects. ")

    async def unregister(self, ws: WebSocketServerProtocol) -> None:
        self.clients.remove(ws)
        logging.info(f"{ws.remote_address} disconnects. ")

    async def send_to_clients(self, message: str, ws: WebSocketServerProtocol) -> None:
        if self.clients:
            await asyncio.wait([client.send(f"Hello, {message}") for client in self.clients])
 #           messages = [f"Hello, {message}" if client is not ws else "" for client in self.clients]
 #           for client in self.clients:
 #               await asyncio.wait([client.send(message) for message in messages])
    
    async def ws_handler(self, ws: WebSocketServerProtocol, uri: str) -> None:
        await self.register(ws)
        try:
            await self.distribute(ws)
        finally:
            await self.unregister(ws)
    
    async def distribute(self, ws: WebSocketServerProtocol) -> None:
        async for message in ws:
#            if message == "/disconnect":
#                await self.unregister(ws)
#                return
            await self.send_to_clients(message, ws)

def main():
    try: 
        server = Server()
        start_server = websockets.serve(server.ws_handler, "localhost", 4000)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(start_server)
        loop.run_forever()
    except KeyboardInterrupt:
        logging.info("Closing server. ")

if __name__ == "__main__":
    main()
