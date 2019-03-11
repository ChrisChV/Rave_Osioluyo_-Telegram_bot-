import os
import psycopg2

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
