from ravegen import *
import os
import psycopg2

@RaveGen
@Command
def create(message):
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("CREATE TABLE users(chat_id serial PRIMARY KEY);")
    cur.execute("CREATE TABLE tokens(token_id serial PRIMARY KEY, chat_id serial, token varchar(254));")
    #cur.execute("INSERT INTO test(data) VALUES ('test');")
    #cur.execute("DROP TABLE test;")
    #cur.execute("SELECT * from test;")
    #reply = cur.fetchone()[1]
    conn.commit()
    cur.close()
    conn.close()
    #return reply
