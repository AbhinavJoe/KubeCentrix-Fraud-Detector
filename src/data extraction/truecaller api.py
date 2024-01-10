import asyncio
from truecallerpy import search_phonenumber

id = "a1i04--kE1GeYFb-hPQ7gmvIWvjV8hTQdI74aC1IDKiDcogB0zyFezzT0764fYMQ"


async def main():
    result = await search_phonenumber({"1400954437"}, "IN", id)
    contact_name = result['data']['data'][0]['name']
    print(contact_name)
    print(result)

# Event loop to execute the coroutine
asyncio.run(main())
