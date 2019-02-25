from ravegen import *
import os
import psycopg2

@RaveGen
@Command
def _setToken(message):
    tokens = message.split(" ")
    tokens[-1] = tokens[0].rstrip("\n")
    token = tokens[0].split(":")
    if verifyChatId(token[0]) == False:
        return "Invalid token"
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("INSERT into tokens  values(%s, %s) ", (token[0], tokens[0]))
    conn.commit()
    cur.close()
    conn.close()
    return "El token ha sido validado correctamente"

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