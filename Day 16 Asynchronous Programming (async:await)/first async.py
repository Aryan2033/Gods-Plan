import asyncio
import time

async def main():

    print("starting")

    await asyncio.sleep(3) #this is a non-blocking sleep, it allows other tasks to run while waiting
    #it does not block the entire program, it only blocks the current task, allowing other tasks to run concurrently
    print("finished")

asyncio.run(main())


