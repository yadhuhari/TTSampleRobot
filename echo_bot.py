# © @WMZ_IND & @Bot_Master

import ttbotapi
import logging

ttbotapi.logger.setLevel(logging.DEBUG)

# Note: Make sure to actually replace TOKEN with your own API token.
bot = ttbotapi.Bot(access_token='Bot Token')

# After that declaration, we need to register some so-called decorator handlers.
# Update handlers define filters which a message must pass. If a message passes the filter, 
# the decorated function is called and the incoming message is passed as an argument.

# Let's define a message handler which handles incoming `/start` and `/help` bot_command in dialog chat type.
@bot.update_handler(chat_type='dialog', bot_command=['/start', '/help'])
def send_welcome(update):
    # A function which is decorated by an update handler can have an arbitrary name, 
    # however, it must have only one parameter (the update)
    bot.send_message(text="Howdy, how are you doing?", user_id=update.message.sender.user_id, chat_id=None,
                     link={'type': 'reply', 'mid': update.message.body.mid})

# Let's add another handler
@bot.update_handler(chat_type='dialog', regexp='hi')
def send_hi(update):
    bot.send_message(text=f'Hi 👋, {update.message.sender.name}', user_id=update.message.sender.user_id, chat_id=None)


# This one echoes all incoming text messages back to the sender. It uses a lambda function to test a message. 
# If the lambda returns True, the message is handled by the decorated function. 
# Since we want all messages to be handled by this function, we simply always return True.
@bot.update_handler(func=lambda update: update.message.body.text)
def echo(update):
    bot.send_message(text=update.message.body.text, user_id=update.message.sender.user_id, chat_id=None)


# Using long polling now our bot never stop working
bot.polling()

# Alright, that's it! Our source file now looks fine
