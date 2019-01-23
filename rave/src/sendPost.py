import os
import json
import requests
from sad import *


def sendPostToWebHook(WEB_HOOK_URL):
    jsonStructureFile = open(JSON_STRUCTURE_FILE_NAME, 'r')
    data = json.load(jsonStructureFile)

    data["message"]["text"] = "super test"
    jsonData = json.dumps(data)

    res = requests.post(WEB_HOOK_URL, json = data)



    
sendPostToWebHook("https://890e6e98.ngrok.io")
