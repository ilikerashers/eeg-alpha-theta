import asyncio
from eeg_result_producer import get_ratio, get_stats
import websockets
import concurrent.futures
# import * from eeg_result_producer

# async def hello(websocket, path):
#     await websocket.send("greeting")
    

#     # send_alpha_theta_ratio(websocket)
#     # while True:
#     # await send_alpha_theta_ratio(websocket=websocket)
#         # await websocket.send(greeting)
#         # print(f"> {greeting}")

# start_server = websockets.serve(hello, "localhost", 8765)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()


async def hello(websocket, path):
    name = await websocket.recv()
    print(f"<<< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f">>> {greeting}")
    print(get_ratio())

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  # run forever


async def multiple_tasks():
  input_coroutines = [main(), get_stats()]
  res = await asyncio.gather(*input_coroutines, return_exceptions=True)
  return res

asyncio.run(multiple_tasks())