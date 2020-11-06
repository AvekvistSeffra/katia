import asyncio
import websockets

async def produce(message: str, host: str, port: str) -> None:
    async with websockets.connect(f"ws://{host}:{port}") as ws:
        await ws.send(message)
        print(await ws.recv())
