import os
import ctypes
import time

def changeDeskWall(pathString):
    os.chdir(pathString)
    images=os.listdir()
    for i in range(len(images)):
        #t=self.timelist[self.indexNumberofCombobox]*60
        try:
            name,extesion=os.path.splitext(images[i])
            if extesion in [".JPEG",".jpeg",".PNG",".png",".jpg",".JPG"]:
                absolutepath = pathString+ "\\" + images[i]
                ctypes.windll.user32.SystemParametersInfoW(20, 0, absolutepath , 0)
                time.sleep(5)
        except Exception as e:
            print(e)


def GetCurrentDesktopImage():
    gopath=os.path.expandvars(r"%AppData%\Microsoft\Windows\Themes\CachedFiles")
    os.chdir(gopath)
    listofImage=os.listdir()
    imagepath= f"{gopath}\{listofImage[0]}"
    return imagepath