# chapar pão
# fritar hamburger
# montar sanduiche
# fazer milk shake

from time import sleep
import asyncio

class SyncSpongeBob:
    def cook_bread(self):
        sleep(3)

    def cook_hamburger(self):
        sleep(10)

    def mount_sandwich(self):
        sleep(3)

    def make_milkshake(self):
        sleep(5)

    def cook(self):
        self.cook_bread()
        self.cook_hamburger()
        self.mount_sandwich()
        self.make_milkshake()

# sync_spongebob = SyncSpongeBob()
# sync_spongebob.cook()
# time python async_await_sponge_bob.py 
# real	0m21,014s
# user	0m0,008s
# sys	0m0,005s

class AsyncSpongeBob:
    async def cook_bread(self):
        await asyncio.sleep(3)

    async def cook_hamburger(self):
        await asyncio.sleep(10)

    async def mount_sandwich(self):
        await asyncio.sleep(3)

    async def make_milkshake(self):
        await asyncio.sleep(5)

    async def make_sandwich(self):
        await asyncio.gather(
            self.cook_bread(),
            self.cook_hamburger()
        )
        event_loop = asyncio.get_running_loop()
        event_loop.create_task(self.mount_sandwich())
    
    # async def cook(self):
    #     await asyncio.gather(
    #         self.cook_bread(),
    #         self.cook_hamburger(),
    #         self.make_milkshake()
    #     ) # funções executadas ao mesmo tempo

    #     await self.mount_sandwich()

    async def cook(self):
        await asyncio.gather(self.make_sandwich(), self.make_milkshake())

async_spongebob = AsyncSpongeBob()
# asyncio.run(async_spongebob.cook())
# time python async_await_sponge_bob.py 
# real	0m13,072s
# user	0m0,049s
# sys	0m0,014s

asyncio.run(async_spongebob.cook())
# time python async_await_sponge_bob.py 
# real	0m10,062s
# user	0m0,045s
# sys	0m0,012s