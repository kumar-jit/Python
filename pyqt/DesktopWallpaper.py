import os
import time
import win32api, win32con, win32gui
from PIL import Image  
import PIL 
import Userinformetion
import random
import threading

try:
    imgaeindex=int(Userinformetion.textInFile("lastImgIndex","GET"))
except:
    imgaeindex=0
i=imgaeindex
def SetWallpaper(path):
    print("setwallpaper call")
    try:
        key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
        win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1+2)
    except Exception as e:
        pass

# def UpdateimageIndex():
#     Userinformetion.textInFile("lastImgIndex","SET",str(i))

def changeDeskWall(pathString,t,checked):
    i=imgaeindex
    try:
        images=os.listdir(pathString)
    except Exception as e:
        pass
    while True: 
        
        try:
            
            name,extesion=os.path.splitext(images[i])
            if extesion in [".JPEG",".jpeg",".PNG",".png",".jpg",".JPG"]:
                path = pathString+ "\\" + images[i]
                t2=threading.Thread(target=SetWallpaper,args=(path,))
                t2.daemon=True
                t2.start()
                # SetWallpaper(path)
                # if setWallpaper(path):
                t1=threading.Thread(target=Userinformetion.textInFile,args=("lastImgIndex","SET",str(i),))
                t1.start()
                # Userinformetion.textInFile("lastImgIndex","SET",str(i))
                time.sleep(t)
                
        except Exception as e:
            pass
        if checked:
            i=random.randint(0,len(images)-1)
        else:
            i +=1
            if i==len(images):
                i=0

    
# def setWallpaper(path):
#     print("setwallpaper call")
#     try:
#         key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
#         win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
#         win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
#         win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1+2)
#     except Exception as e:
#         pass

def Read_last_location():
    # if Userinformetion.New_user():
    #     Userinformetion.New_user_creat()
    path=Userinformetion.textInFile("lastUsePathath","GET")
    return path
    #     path=Userinformetion.New_user_creat()
    #     with open(path,'r')as rf:
    #         lines=rf.readlines()
    #         return lines[0]
    # else:
    #     try:
    #         path=Userinformetion.exists_user_path()
    #         with open(path,'r')as rf:
    #             lines=rf.readlines()
    #             return lines[0]
    #     except Exception as e:
    #         print(e)
def Write_last_location(last_path):
    # path=Userinformetion.exists_user_path()
    # with open(path,'w') as wf:
    #     wf.write(last_path)
    Userinformetion.textInFile("lastUsePathath","SET",last_path)

def GetCurrentDesktopImage():
    gopath=os.path.expandvars(r"%AppData%\Microsoft\Windows\Themes\TranscodedWallpaper")
    #geting the current path
    folder_path=Userinformetion.UserInformetionFolder()
    #creating image file location
    image_location=folder_path+"\desktop.jpg"
    # creating a image object (main image)  
    current_desk_img = Image.open(gopath)
    #saving
    current_desk_img = current_desk_img.save(image_location)
    imagepath= f"{folder_path}\desktop.jpg"
    return imagepath


# changeDeskWall(r"C:\Users\kumar\OneDrive\Pictures\Saved Pictures")