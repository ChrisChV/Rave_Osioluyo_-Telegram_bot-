import sys
import os
import sad
from sendMsg import *



command = "hostname > " + sad.TEMP_HOST_FILE
os.system(command)
tempFile = open(sad.TEMP_HOST_FILE, 'r')
host = tempFile.readline().rstrip('\n')
tempFile.close()
command = "rm -f " + sad.TEMP_HOST_FILE
os.system(command)

initMsg = host + " turn on"
print("TEST")
sendMsg(initMsg)
