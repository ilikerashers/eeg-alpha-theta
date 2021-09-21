import asyncio
from eeg_result_producer import get_ratio, get_stats
import websockets
import concurrent.futures
from time import monotonic
from concurrent.futures import ThreadPoolExecutor
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
        
# async def async_processing():
#     async with websockets.connect('ws:localhost:8765') as websocket:
#         while True:
#             try:
#                 message = await websocket.recv()
#                 print(message)

#             except websockets.exceptions.ConnectionClosed:
#                 print('ConnectionClosed')
#                 is_alive = False
#                 break
        
# async def async_stat_generator():
    

tasks = [
  main(),
  #  async_processing(),
  get_stats(),
]



# start_time = monotonic()
#     # you can choose max_workers number higher and check if app works faster
#     # e.g choose 16 as max number of workers
# with ThreadPoolExecutor(max_workers=2) as pool:
#     results = pool.map(get_stats)



asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))


# async def multiple_tasks():
#   input_coroutines = [get_stats(), main(),]
#   res = await asyncio.gather(*input_coroutines, return_exceptions=True)
#   return res

# asyncio.run(multiple_tasks())