import os
import sad

'''def verifyRoot():
    command = "whoami > " + sad._TEMP_ROOT_FILE
    print command
    os.system(command)
    tempFile = open(sad._TEMP_ROOT_FILE, 'w')
    who = tempFile.readline().rstrip('\n')
    tempFile.close()
    command = "rm -f " + sad._TEMP_ROOT_FILE
    os.system(command)
    if(who == "root"):
        return True
    return False
'''

def verifyRoot():
    if os.geteuid() == 0:
        return True
    return False

        
    