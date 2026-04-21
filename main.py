from telethon import TelegramClient
import asyncio
import random
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

commands = ["/lever", "/dice", "/bowling", "/explore"]

# 🔥 3 clients (3 session files)
clients = [
    ("Acc1", TelegramClient("session1", api_id, api_hash,
                            connection_retries=999, retry_delay=5, auto_reconnect=True)),
    ("Acc2", TelegramClient("session2", api_id, api_hash,
                            connection_retries=999, retry_delay=5, auto_reconnect=True)),
    ("Acc3", TelegramClient("session3", api_id, api_hash,
                            connection_retries=999, retry_delay=5, auto_reconnect=True)),
]

async def run_client(name, client):
    try:
        await client.start()  # 🔥 better than connect()

        if not await client.is_user_authorized():
            print(f"❌ {name} session invalid (upload correct session file)")
            return

        print(f"✅ {name} connected")

        while True:
            try:
                for cmd in commands:
                    await client.send_message("YamatoAcn_bot", cmd)
                    print(f"{name} Sent: {cmd}")
                    await asyncio.sleep(random.randint(2,3))  # safer delay

                wait_time = random.randint(116,126)  # safer gap
                print(f"{name} waiting {wait_time} sec\n")
                await asyncio.sleep(wait_time)

            except Exception as e:
                print(f"⚠️ {name} Error:", e)
                await asyncio.sleep(10)

    except Exception as e:
        print(f"❌ {name} startup error:", e)

async def main():
    tasks = []
    for name, client in clients:
        tasks.append(run_client(name, client))

    await asyncio.gather(*tasks)

asyncio.run(main())
