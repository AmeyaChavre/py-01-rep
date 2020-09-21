import os

print(os.getcwd())

f = open('C:\\Users\\hp\\Desktop\\test.txt','w+')
f.write("This is the first line.")
f.close()


print(os.listdir())

print(os.listdir('C:\\Users'))



