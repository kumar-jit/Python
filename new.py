import ctypes
import time
import os

os.chdir(r"C:\Users\kumar\OneDrive\Pictures\Saved Pictures")
images=os.listdir()

for i in range(len(images)):
    print(i)
    name,extesion=os.path.splitext(images[i])
    print(name," " ,extesion)
    if extesion in [".JPEG",".jpeg",".PNG",".png",".jpg",".JPG"]:
        path="C:\\Users\\kumar\\OneDrive\\Pictures\\Saved Pictures\\"+images[i]
        print(ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0))
        time.sleep(10)
    

