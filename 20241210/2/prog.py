import random
import asyncio

async def merge(source, target, start, mid, end, event_left, event_right, event_result):
    await event_left.wait()
    if mid < end:
        await event_right.wait()

    left_idx, right_idx, target_idx = start, mid, start
    while left_idx < mid and right_idx < end:
        if source[left_idx] <= source[right_idx]:
            target[target_idx] = source[left_idx]
            left_idx += 1
        else:
            target[target_idx] = source[right_idx]
            right_idx += 1
        target_idx += 1
    while left_idx < mid:
        target[target_idx] = source[left_idx]
        left_idx += 1
        target_idx += 1
    while right_idx < end:
        target[target_idx] = source[right_idx]
        right_idx += 1
        target_idx += 1

    event_result.set()


async def mtasks(array):
    size = len(array)
    temp_array = [0] * size
    tasks = []
    events = [asyncio.Event() for _ in range(size)]
    for event in events:
        event.set()

    segment_length = 1
    source, result = array.copy(), temp_array

    while segment_length < size:
        next_events = [asyncio.Event() for _ in range((size + 2 * segment_length - 1) // (2 * segment_length))]

        for i in range(0, size, 2 * segment_length):
            start = i
            mid = min(i + segment_length, size)
            end = min(i + 2 * segment_length, size)
            task = merge(
                source, result, start, mid, end,
                events[i // segment_length],
                events[min(i + segment_length, size) // segment_length] if min(i + segment_length, size) < size else asyncio.Event(),
                next_events[i // (2 * segment_length)]
            )
            tasks.append(asyncio.create_task(task))
        events = next_events
        source, result = result, source
        segment_length *= 2

    return tasks, source


import sys

exec(sys.stdin.read())
