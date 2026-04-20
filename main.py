from telethon import TelegramClient
import asyncio
import random
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

commands = ["/lever", "/dice", "/bowling", "/explore"]

client = TelegramClient(
    "session",
    api_id,
    api_hash,
    connection_retries=999,
    retry_delay=5,
    auto_reconnect=True
)

async def main():
    await client.connect()   # 🔥 FORCE CONNECT

    if not await client.is_user_authorized():
        print("❌ Session invalid. Re-login required.")
        return

    print("✅ Connected successfully!")

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
            print("⚠️ Error:", e)
            await asyncio.sleep(5)

with client:
    client.loop.run_until_complete(main())
