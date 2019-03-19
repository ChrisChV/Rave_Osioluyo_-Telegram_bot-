from ravegen import *
from Crypto.Hash import MD5
import Crypto.Random.random as random
import os
import psycopg2
import utils

@Command
def token(bot, update):
    id = str(update.effective_message.chat_id)
    if utils.verifyChatId(id) == False:
        createChatIdRegister(id)
    randomNumber = str(random.getrandbits(1024))
    token = MD5.new(id + randomNumber).hexdigest()
    token = id + ":" + token
    update.effective_message.reply_text(token)


def createChatIdRegister(chatId):
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES(%s)", (chatId,))
    conn.commit()
    cur.close()
    conn.close()


