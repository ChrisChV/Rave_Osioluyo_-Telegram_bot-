from ravegen import *
import os
import psycopg2

@RaveGen
@Command
def _sendMsg(message):
    tokens = message.split(" ")
    token = tokens[0]
    tokens = tokens[1:]
    print token
    reply = ' '.join(tokens)
    print reply
    id = token.split(":")
    if verifyChatId(id[0]) and verifyToken(token):
        return reply
    return "Invalid Token"
    

def verifyToken(token):
    tokens = token.split(":")
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("SELECT * from tokens where chat_id = %s and token = %s", (tokens[0], token))
    user = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if user == None:
        return False
    return True

def verifyChatId(chatId):
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("SELECT * from users where chat_id = %s", (chatId,))
    user = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if user == None:
        return False
    return True