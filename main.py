import ttbotapi
import random

bot = ttbotapi.Bot(access_token='wko_5FDZB0gOIGBaKizYBYdCIAX2sz4mIR2nxnmOrXo')

@bot.update_handler(chat_type='dialog', bot_command=['start'])
def start (update):
  bot.send_photo(
    photo=random.choice(PICS),
    caption=f"""Hi {update.message.sender.name} 
How Are You..!!"""
  )
