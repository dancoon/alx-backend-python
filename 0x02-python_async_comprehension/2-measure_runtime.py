#!/usr/bin/env python3
"""Measure the total execution time of
a function"""
from time import perf_counter
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times in parallel using asyncio.gather
    Returns: elapsed time in seconds
    """
    start = perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )
    elapsed = perf_counter() - start
    return elapsed
