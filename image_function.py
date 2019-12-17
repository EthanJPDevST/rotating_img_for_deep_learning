## Made by EthanJ

import os
from PIL import Image
import piexif

Path = os.path.dirname(os.path.realpath(__file__))

def Rotate90deg(file):
    #img=cv2.imread(file)
    img=Image.open(file)
    
    print("Rotating 90 degrees Clockwise - filename  :: "+ file)
    img=img.transpose(Image.ROTATE_180)
    return img
    
def noMeta(file):
    print("gutting exif data from {}".format(file))
    piexif.remove(file)

def removeExifData():
    for root, dir, files in os.walk(Path):
        for file in files:
            if file.lower().endswith(".jpg") or file.lower().endswith(".jpg"):
                noMeta(os.path.join(root, file))

def rotating_image():
    for root, dir, files in os.walk(Path):
        for file in files:
            if file.lower().endswith(".jpg") or file.lower().endswith(".jpg"):
                img = Rotate90deg(os.path.join(root, file))
                img.save(file)

print("1. Delete EXIF Data from JPG Files")
print("2. Rotate 90 degrees Clockwise")
print(" Made by EthanJ_Dev")

menu_no= input("Enter menu number: ")

if(int(menu_no)==1):
    removeExifData()
elif(int(menu_no)==2):
    rotating_image()
else:
    print("Wrong_INPUT... Ending program...")