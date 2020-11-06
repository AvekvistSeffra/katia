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
    
    async def ws_handler(self, ws: WebSocketServerProtocol, uri: str) -> None:
        await self.register(ws)
        try:
            await self.distribute(ws)
        finally:
            await self.unregister(ws)
    
    async def distribute(self, ws: WebSocketServerProtocol) -> None:
        async for message in ws:
            await self.send_to_clients(message, ws)
