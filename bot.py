import os
import asyncio
from pyrogram import Client, filters
from flask import Flask
from threading import Thread

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

app = Client(
    "MUHyperlinkRemoverBot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(filters.group & filters.text)
async def remove_links(client, message):

    text = message.text.lower()

    if "http" in text or "https" in text or "t.me" in text or "www" in text:

        try:
            await message.delete()

            warn = await message.reply_text(
                "[Message Deleted] Sorry! Messages containing website URLs are not allowed in this group.\n\nAdd @MUHyperlinkRemover_Bot to your group to keep the conversation clean."
            )

            await asyncio.sleep(5)
            await warn.delete()

        except:
            pass


# -------- Web server (Render এর জন্য) --------

web = Flask(__name__)

@web.route("/")
def home():
    return "Bot is running!"

def run():
    web.run(host="0.0.0.0", port=10000)

Thread(target=run).start()

# -------- Start bot --------
app.run()
