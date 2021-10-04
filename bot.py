import os
import requests as re
from bs4 import BeautifulSoup
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", 12345))

API_HASH = os.environ.get("API_HASH", "")

app = Client(
        "webscrap",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
    )
    
    
@app.on_message(filters.command(['start']))
def start(client, message):
            message.reply_text(text =f"Hello **{message.from_user.first_name }** \n\n **I Am Disney Team Web Scraper BOT {DTWSB}™️ ** 😊 \n __Send Me Any Website Link And Get That Web Site Source \n Feel Free To Report Bugs Or Any Other Problems Or Any Feature Adding In @Disneyteamchat ❤__",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👨‍🔧Updates Channel👨‍🔧" ,url="https://t.me/Disneygrou") ],
                 [InlineKeyboardButton("👨‍💻Developer👨‍💻", url="https://t.me/Doreamonfans1") ]          ]        ) )


@app.on_message(filters.regex("^(http|https|www\.)"))
def start(client, message):
    ms = message.reply_text("Proccesing To Web Scrap👷‍♂️ .........", reply_to_message_id = message.message_id)
    msg_id = message.chat.id
    html_url = message.text
    try:
    	page = re.get(html_url)
    	soup = BeautifulSoup(page.txt,'html.parser')
    except Exception as e:
    	ms.edit("```Error : {e}```")
    	return
    f = open(f"{msg_id}.txt" , "w")
    f.write(str(soup.prettify()))
    f.close()

    caption = "Here Is Your Web Source🙃"
    try:
    	app.send_document(message.chat.id ,document = f"{msg_id}.txt",caption = caption)
    except ValueError as ve:
    	ms.edit("```file Size value error")
    	os.remove(f"{msg_id}.txt")
    	return
    ms.delete()
    os.remove(f"{msg_id}.txt")
	
app.run()
