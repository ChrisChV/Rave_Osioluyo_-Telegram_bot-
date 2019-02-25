import sad
import os
import json
import requests


def sendMsg(message):
    tokenFile = open(sad.TOKEN_FILE, 'r')
    token = tokenFile.readline()
    tokenFile.close()
    jsonStructureFile = open(sad.JSON_STRUCTURE_FILE_NAME, 'r')
    data = json.load(jsonStructureFile)

    data["message"]["text"] = "/_sendMsg " + token + " " + message
    #data["message"]["id"] = 123456
    #data["message"]["chat"]["id"] = 123456
    jsonData = json.dumps(data)
    res = requests.post(sad.WEB_HOOK_URL, json = data)