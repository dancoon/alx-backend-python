#!/usr/bin/env python3
"""A coroutine that loops 10 times, each time asynchronously
wait 1 second, then yield a random number between 0 and 10."""

import asyncio
import random


async def async_generator():
    """
    yield a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
