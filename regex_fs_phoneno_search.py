import shutil

file_path = "C:\\Users\\hp\\Desktop\\unzip_me_for_instructions.zip"
 
shutil.unpack_archive("C:\\Users\\hp\\Desktop\\unzip_me_for_instructions.zip","C:\\Users\\hp\\Desktop\\instructions","zip")

with open("C:\\Users\\hp\\Desktop\\instructions\\extracted_content\\Instructions.txt") as f:
    content = f.read()
    print(content)
    
import re 

def search(file,pattern= r'\d{3}-\d{3}-\d{4}'):
    f = open(file,'r')
    text = f.read()
    
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ''
    
import os

file_path = "C:\\Users\\hp\\Desktop\\instructions\\extracted_content"
results = []
for folder , sub_folders , files in os.walk(file_path):
    
    for f in files:
        full_path = folder+'\\'+f
         
        results.append(search(full_path))
        
for r in results:
    if r != '':
        print(r.group())

