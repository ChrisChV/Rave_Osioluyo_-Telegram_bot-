#HEADERS
#TokenFlag False
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
import logging 
import os 
import sys 
import ravegen.Decorators.functionManager as functionManager 
sys.path.insert(0, 'modules')
from create import *
from echo import *
from error import *
from sendMsg import *
from setToken import *
from start import *
from test import *

if __name__ == "__main__":
	TOKEN = "717635382:AAE9Qy-9Vd0wAsUAVnII9y9CLE-8E-s9EAA"
	PORT = os.environ.get('PORT')
	logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
	logger = logging.getLogger(__name__)
	updater = Updater(TOKEN)
	dispatcher = updater.dispatcher
	functionManager.functionManager.generateHandlers(dispatcher)
	updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path="717635382:AAE9Qy-9Vd0wAsUAVnII9y9CLE-8E-s9EAA")
	updater.bot.setWebhook("https://rave-osioluyp-test.herokuapp.com/717635382:AAE9Qy-9Vd0wAsUAVnII9y9CLE-8E-s9EAA")
	updater.idle()
