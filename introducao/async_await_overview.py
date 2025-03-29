import asyncio

async def sum(a, b):
    return a + b

def print_sum(a, b):
    result = sum(a, b)
    print(f'resultado igual a {result}')

# result = sum(2, 3)
# sys:1: RuntimeWarning: coroutine 'sum' was never awaited
# print(result)

# EVENT LOOP
# coro = sum(2, 3)
# event_loop = asyncio.new_event_loop()
# result = event_loop.run_until_complete(coro)
# print(result) # 5

# print_sum(2, 3)
# resultado igual a <coroutine object sum>
# RuntimeWarning: Enable tracemalloc to get the object allocation traceback

async def print_sum_async(a, b):
    result = await sum(a, b)
    print(f'resultado igual a {result}')

# EVENT LOOP
event_loop = asyncio.new_event_loop()
event_loop.run_until_complete(print_sum_async(2, 3)) # resultado igual a 5