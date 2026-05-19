import asyncio

async def sensor(id):

    print(f"sensor {id} starting")

    await asyncio.sleep(2) #simulate a sensor reading that takes time

    print(f"sensor {id} finished")

async def main():
    await asyncio.gather(
        sensor(1),
        sensor(2),
        sensor(3)
    )

asyncio.run(main())

# output
# sensor 1 starting
# sensor 2 starting
# sensor 3 starting
# sensor 1 finished
# sensor 2 finished
# sensor 3 finished

# Without async:

# 2+2+2 = 6 sec

# With async:

# ≈2 sec

# Massive improvement.