from time import time
import asyncio

""" Bonus: Upgrade the timer decorator for
async functions """

def async_timer(func):
    async def wrapper_function(*args, **kwargs):
        before = time()
        rv = await func(*args, **kwargs)
        after = time()
        print(f"took {after - before} seconds to run.")
        return rv
    return wrapper_function





