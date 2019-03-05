import sad
import os
import json
import requests

def init():
    command = "mkdir -p " + sad.INSTALL_PATH
    os.system(command)
    token = raw_input("Write the token here: ")
    setToken(token)
    tokenFile = open(sad.TOKEN_FILE, 'w')
    tokenFile.write(token)
    tokenFile.close()


def setToken(token):
    jsonStructureFile = open(sad.JSON_STRUCTURE_FILE_NAME, 'r')
    data = json.load(jsonStructureFile)

    data["message"]["text"] = "/_setToken " + token
    #data["message"]["id"] = 123456
    #data["message"]["chat"]["id"] = 123456
    jsonData = json.dumps(data)
    res = requests.post(sad.WEB_HOOK_URL, json = data)

init()
