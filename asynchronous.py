import asyncio
async def Asyncfun(data,delay):
    print(f"start{data}")
    await asyncio.sleep(delay)
    print(f"start{data}")

async def main():
    await asyncio.gather(Asyncfun("1",4),Asyncfun("2",2))
asyncio.run(main())