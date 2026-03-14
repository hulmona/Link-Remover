from pyrogram import Client, filters
import asyncio

api_id = 38438389
api_hash = "YOUR_API_HASH"
bot_token = "YOUR_BOT_TOKEN"

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

app.run()
