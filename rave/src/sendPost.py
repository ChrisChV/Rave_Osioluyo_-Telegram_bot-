import os
import json
import requests
from sad import *


def sendPostToWebHook(WEB_HOOK_URL):
    jsonStructureFile = open(JSON_STRUCTURE_FILE_PATH, 'r')
    data = json.load(jsonStructureFile)

    data["message"]["text"] = "/caps test"
    #data["message"]["id"] = 123456
    #data["message"]["chat"]["id"] = 123456
    jsonData = json.dumps(data)


    res = requests.post(WEB_HOOK_URL, json = data)



    
#sendPostToWebHook("https://rave-osioluyp-test.herokuapp.com/717635382:AAE9Qy-9Vd0wAsUAVnII9y9CLE-8E-s9EAA")
