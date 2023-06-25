# © @WMZ_IND & @Bot_Master

import ttbotapi
import random

PICS = [
 "file:///C:/Users/user/Downloads/343618100_939688137480555_5228557919266828998_n.jpg.html"
]

Client = ttbotapi.Bot(access_token='wko_5FDZB0gOIGBaKizYBYdCIAX2sz4mIR2nxnmOrXo')

@Client.update_handler(chat_type='dialog', bot_command=['start'])
def start (update):
  bot.send_photo(
    photo=random.choice(PICS),
    caption=f"""Hi {update.message.sender.name} 
How Are You..!!"""
  )

print("Bot Started..!!")

Client.run()
