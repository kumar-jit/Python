import os
import ctypes
import time
import win32api, win32con, win32gui
from PIL import Image  
import PIL
import multiprocessing as mp


current_path=""
def setpath():
    current_path=os.getcwd()

    
def UserInformetionFolder():
    path=os.path.join(current_path,'User_info')
    if os.path.exists(path):
        return path + "\\"
    else:
        os.mkdir(path)
        return path + "\\"

def New_user():
    path=UserInformetionFolder()
    path=path+"\info.txt"
    if os.path.exists(path):
        return(False)
        # return path
    else:
        return(True)
        # print("else work")
        # with open(path,'w') as f:
        #     print("file open")
        #     gopath=os.path.expandvars(r"%AppData%\Microsoft\Windows\Libraries\Pictures.library-ms")
        #     string="path,"+gopath
        #     f.write(string)
        #     return path


 
def New_user_creat():
    path=UserInformetionFolder()
    path=path+"\info.txt"
    with open(path,'w') as f:
        string=os.path.expandvars("%AppData%\\Microsoft\Windows\\Libraries\\Pictures")
        text="lastUsePathath,\""+string+"\"\nlastImgIndex,\"0\""
        f.write(text)
        return path



def exists_user_path():
    path=UserInformetionFolder()
    return(path+"\\info.txt")

def damage():
    path=UserInformetionFolder()
    path=os.path.join(path,"info.txt")
    with open(path,'r') as rf:
        text=rf.read()
    if text.find("lastUsePathath,\"")==-1 or text.find("lastImgIndex,\"")==-1:
        return True
    else:
        return False

def textInFile(Type,status,newtext=""):
    if New_user():
        path=New_user_creat()
    else:
        path=exists_user_path()
    if damage():
        print("delete damage path")
        os.remove(path)
        path=New_user_creat()

    oldtext=""
    text=""
    with open(path,"r") as rf:
        text=rf.read()
        try:
            post=text.find(Type)
            fist_index=text.find("\"",post)
            last_index=text.find("\"",fist_index+1)
            oldtext=text[fist_index+1:last_index]
        except:
            pass
    if status=="SET":
        text=text.replace(oldtext,newtext)
        with open(path,"w") as rf:
            rf.write(text)
            return True
    elif status=="GET":
        return oldtext