import os
import ctypes
import time
import win32api, win32con, win32gui
from PIL import Image  
import PIL 


def changeDeskWall(pathString,t):
    os.chdir(pathString)
    images=os.listdir()
    i=0
    while True: 
        
        try:
            
            name,extesion=os.path.splitext(images[i])
            if extesion in [".JPEG",".jpeg",".PNG",".png",".jpg",".JPG"]:
                path = pathString+ "\\" + images[i]
                setWallpaper(path)
                time.sleep(t)
                
        except Exception as e:
            continue
        i +=1
        if i==len(images):
            i=0

def setWallpaper(path):
    try:
        key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
        win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1+2)
    except Exception as e:
        print(e)



def GetFolderPathWallpaper():
    current_path=os.getcwd()
    path=os.path.join(current_path,'Cwallpaper')
    if os.path.exists(path):
        return path + "\\"
    else:
        os.mkdir(path)
        return path + "\\"

def GetCurrentDesktopImage():
    gopath=os.path.expandvars(r"%AppData%\Microsoft\Windows\Themes\TranscodedWallpaper")
    #geting the current path
    folder_path=GetFolderPathWallpaper()
    #creating image file location
    image_location=folder_path+"\desktop.jpg"
    # creating a image object (main image)  
    current_desk_img = Image.open(gopath)
    #saving
    current_desk_img = current_desk_img.save(image_location)
    imagepath= f"{folder_path}\desktop.jpg"
    return imagepath


# changeDeskWall(r"C:\Users\kumar\OneDrive\Pictures\Saved Pictures")