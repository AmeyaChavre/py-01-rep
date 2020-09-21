import os
import send2trash

print(os.listdir("C:\\Users\\acer\\Desktop\\Test Folder"))
send2trash.send2trash("C:\\Users\\acer\\Desktop\\Test Folder\\test.txt")
