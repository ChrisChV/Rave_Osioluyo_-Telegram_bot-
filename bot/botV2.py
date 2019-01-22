#import telegram

#bot = telegram.Bot(token = '717635382:AAE9Qy-9Vd0wAsUAVnII9y9CLE-8E-s9EAA')
#print(bot.get_me())

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

def initServer():

    TOKEN = '717635382:AAE9Qy-9Vd0wAsUAVnII9y9CLE-8E-s9EAA'
    NAME = 'rave-osioluyo'

    PORT = os.environ.get('PORT')

    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)
    caps_handler = CommandHandler('caps', caps, pass_args=True)
    dispatcher.add_handler(caps_handler)


    updater.start_polling()

    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()