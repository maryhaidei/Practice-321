import asyncio
from collections import deque
async def writer(queue, delay, stop_event, name):
    count = 0
    await asyncio.sleep(delay)  
    while not stop_event.is_set():
        await queue.put(f"{count}_{name}")
        count += 1
        await asyncio.sleep(delay)

async def stacker(queue, stack, stop_event):
    while not stop_event.is_set() or not queue.empty():
        if not queue.empty():
            item = await queue.get()
            stack.append(item)
        else:
            await asyncio.sleep(0.01)


async def reader(stack, count, delay, stop_event):
    await asyncio.sleep(delay)  
    for _ in range(count):
        while not stack: 
            await asyncio.sleep(0.01)
        print(stack.pop())
        await asyncio.sleep(delay)
    stop_event.set() 

async def main():
    delay1, delay2, delay3, count = map(int, input().split(','))
    queue = asyncio.Queue()
    stack = deque()
    stop_event = asyncio.Event()
    await asyncio.gather(
        writer(queue, delay1, stop_event, name=delay1),
        writer(queue, delay2, stop_event, name=delay2),
        stacker(queue, stack, stop_event),
        reader(stack, count, delay3, stop_event)
    )
asyncio.run(main())

