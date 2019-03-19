from ravegen import *
import os
import psycopg2
import utils

@RaveGen
@Command
def _setToken(message):
    tokens = message.split(" ")
    tokens[-1] = tokens[0].rstrip("\n")
    token = tokens[0].split(":")
    if utils.verifyChatId(token[0]) == False:
        return "Invalid token"
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("INSERT into tokens(chat_id, token)  values(%s, %s) ", (token[0], tokens[0]))
    conn.commit()
    cur.close()
    conn.close()
    return "El token ha sido validado correctamente"
