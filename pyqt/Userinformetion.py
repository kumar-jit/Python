import os
import ctypes
import time
import win32api, win32con, win32gui
from PIL import Image  
import PIL


def UserInformetionFolder():
    current_path=os.getcwd()
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
    path=path=UserInformetionFolder()
    path=path+"\info.txt"
    with open(path,'w') as f:
        string=os.path.expandvars(r"%AppData%\Microsoft\Windows\Libraries\Pictures")
        f.write(string)
        return path
def exists_user_path():
    path=UserInformetionFolder()
    return(path+"\\info.txt")