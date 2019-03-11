import sad
import os
import json
import requests
import utils


def init():
    if(utils.verifyRoot() == False):
        print("You must be root")
        return
    if(verifyToken()):
        print("Token is already setted")
        return
    if(install() == False):
        return
    command = "mkdir -p " + sad.INSTALL_PATH
    os.system(command)
    command = "cp " + sad.JSON_STRUCTURE_FILE_NAME + " " + sad.INSTALL_PATH
    os.system(command)
    token = raw_input("Write the token here: ")
    setToken(token)
    tokenFile = open(sad.TOKEN_FILE, 'w')
    tokenFile.write(token)
    tokenFile.close()

def verifyToken():
    return os.path.isfile(sad.TOKEN_FILE)

def install():
    if(os.path.isfile(sad.RC_FILE_PATH) == False):
        print("rc.local file doesn't exist")
        return False
    rcFile = open(sad.RC_FILE_PATH, 'r')
    tempRcFile = open(sad._TEMP_RC_FILE, 'w')
    for line in rcFile:
        line = line.rstrip('\n')
        if line == "exit 0":
            tempRcFile.write("python " + os.getcwd() + sad._DF_ + sad.MAIN_FILE_NAME + " > " + sad.LOG_FILE_PATH + " 2> " + sad.LOG_FILE_PATH + "\n")
        tempRcFile.write(line + "\n")
    rcFile.close()
    tempRcFile.close()
    command = "cp " + sad._TEMP_RC_FILE + " " + sad.RC_FILE_PATH
    os.system(command)
    command = "rm " + sad._TEMP_RC_FILE
    os.system(command)
    return True
    
    
def setToken(token):
    jsonStructureFile = open(sad.JSON_STRUCTURE_FILE_PATH, 'r')
    data = json.load(jsonStructureFile)

    data["message"]["text"] = "/_setToken " + token
    #data["message"]["id"] = 123456
    #data["message"]["chat"]["id"] = 123456
    jsonData = json.dumps(data)
    res = requests.post(sad.WEB_HOOK_URL, json = data)

init()
