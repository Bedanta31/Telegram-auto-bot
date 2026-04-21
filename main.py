from telethon import TelegramClient
import asyncio
import random
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

commands = ["/lever", "/dice", "/bowling", "/explore"]

clients = [
    TelegramClient("session1", api_id, api_hash),
    TelegramClient("session2", api_id, api_hash),
    TelegramClient("session3", api_id, api_hash)
]

async def run_client(client, name):
    await client.connect()

    if not await client.is_user_authorized():
        print(f"❌ {name} session invalid")
        return

    print(f"✅ {name} connected")

    while True:
        try:
            for cmd in commands:
                await client.send_message("YamatoAcn_bot", cmd)
                print(f"{name} Sent: {cmd}")
                await asyncio.sleep(random.randint(3,6))

            wait_time = random.randint(110,140)
            print(f"{name} waiting {wait_time} sec\n")
            await asyncio.sleep(wait_time)

        except Exception as e:
            print(f"{name} Error:", e)
            await asyncio.sleep(5)

async def main():
    tasks = []
    for i, client in enumerate(clients):
        tasks.append(run_client(client, f"Acc{i+1}"))

    await asyncio.gather(*tasks)

asyncio.run(main())
