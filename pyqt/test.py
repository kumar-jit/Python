from PIL import Image  
import PIL  
import os

gopath=os.path.expandvars(r"%AppData%\Microsoft\Windows\Themes\TranscodedWallpaper")
# creating a image object (main image)  
im1 = Image.open(gopath)  
  
# save a image using extension 
im1 = im1.save(r"cd..geesdks.jpg") 