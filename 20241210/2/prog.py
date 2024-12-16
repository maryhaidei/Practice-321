import asyncio
import random

async def merge(C, B, start, middle, finish, event_in1, event_in2, event_out):
    await asyncio.gather(event_in1.wait(), event_in2.wait())  
    i, j = start, middle
    for k in range(start, finish):
        if i < middle and (j >= finish or C[i] <= C[j]):
            B[k] = C[i]
            i += 1
        else:
            B[k] = C[j]
            j += 1
    for k in range(start, finish):
        C[k] = B[k]
    event_out.set()  

async def mtasks(A):
    C=A[:]
    N = len(C)
    B = [0] * N 
    tasks = []  
    events = {}  
    for start in range(N):
        events[(start, start + 1)] = asyncio.Event()
        events[(start, start + 1)].set()  
    width = 1
    while width < N:  
        for start in range(0, N, 2 * width):
            middle = start + width
            finish = min(start + 2 * width, N)
            if middle >= N: 
                continue
            if (start, middle) not in events or (middle, finish) not in events:
                continue
            event_in1 = events[(start, middle)]
            event_in2 = events[(middle, finish)]
            event_out = asyncio.Event()
            task = merge(C, B, start, middle, finish, event_in1, event_in2, event_out)
            tasks.append(task)
            events[(start, finish)] = event_out
        width *= 2  
    return tasks, C

import sys
exec(sys.stdin.read())
