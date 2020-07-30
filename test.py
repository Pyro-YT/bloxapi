import bloxapi
import asyncio

client = bloxapi.Client(None)

async def main():
    user_object = await client.get_user_by_id(1)
    if user_object:
        print('This user exists!')
        print(user_object.name, user_object.Id, user_object.status, user_object.about)

asyncio.run(main())