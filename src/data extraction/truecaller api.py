from truecallerpy import search_phonenumber

id = "a1i04--kE1GeYFb-hPQ7gmvIWvjV8hTQdI74aC1IDKiDcogB0zyFezzT0764fYMQ"

async def main():
    result = await search_phonenumber({"phone_number"}, "IN", id)
    contact_name = result['data']['data'][0]['name']
    print(contact_name)

# Run the event loop to execute the coroutine
import asyncio  
asyncio.run(main())
