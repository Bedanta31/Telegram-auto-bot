from telethon import TelegramClient
import asyncio
import random
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

commands = ["/lever", "/dice", "/bowling", "/explore"]

async def main():
    while True:
        try:
            for cmd in commands:
                await client.send_message("YamatoAcn_bot", cmd)
                print(f"Sent: {cmd}")
                await asyncio.sleep(random.randint(3,6))

            wait_time = random.randint(110,140)
            print(f"Waiting {wait_time} sec...\n")
            await asyncio.sleep(wait_time)

        except Exception as e:
            print("Error:", e)
            await asyncio.sleep(5)

client = TelegramClient("session", api_id, api_hash)

with client:
    client.loop.run_until_complete(main())
