from os import path
from os import system

def checkfolder(name):
    if(path.exists(name) == False):
        system('mkdir' + name)
        print('Made And Found') 
    else:
        return True
