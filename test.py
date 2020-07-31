import bloxapi
import asyncio

client = bloxapi.Client(None)

async def main():
    group = await client.get_group(1)
    print(group.owner.name)

asyncio.run(main())